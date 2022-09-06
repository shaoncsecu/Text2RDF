'''
Extracting triples from the output of UDPipe
'''
import io

# Constants for the column indices
COL_COUNT = 10
ID, FORM, LEMMA, UPOSTAG, XPOSTAG, FEATS, HEAD, DEPREL, DEPS, MISC = range(COL_COUNT)
COL_NAMES = u"ID,FORM,LEMMA,UPOSTAG,XPOSTAG,FEATS,HEAD,DEPREL,DEPS,MISC".split(u",")
DUMMY_HEAD = {'0': ['0', '', '', '', '', '', '', '', '', '']}



def get_file_content(file_path):
    """ Parse data from CoNLL-U format file """

    data = []
    with io.open(file_path, 'r', encoding='utf-8') as f:
        sent_id = ''
        tmp_cont = DUMMY_HEAD.copy()# tmp_cont is a dict object

        for line in f:
            line = line.strip()

            if len(line) == 0:
                if len(tmp_cont) > 1:
                    data.append((sent_id, tmp_cont))
                    tmp_cont = DUMMY_HEAD.copy()

            elif line[0].isdigit():
                data_line = line.split('\t')

                if len(data_line) != COL_COUNT:
                    print('Missing data: %s' % line)
                    continue

                tmp_cont[data_line[ID]] = data_line

            else:
                data_line = line.split()
                if len(data_line) == 4 and data_line[1] == 'sent_id':
                    sent_id = data_line[-1]

        if len(tmp_cont) > 1:
            data.append((sent_id, tmp_cont))

    return data

def get_triplets(file_path):
    """Extract triplets from conllu data (returned as list)"""

    data = get_file_content(file_path)
    triplets_out = []

    for sent in data:
        sent_id = sent[0]
        triplet = (sent_id, ["","",""])

        # iterate through the content-dict
        for k,v in sent[1].items():
            # v is list of conll data for word k
            if v[DEPREL] == 'nsubj':
                head_idx = v[HEAD]
                # check if head of this token is the root token
                if sent[1][head_idx][DEPREL] == 'root':
                    triplet[1][0] = (v[LEMMA], v[ID])
            elif v[DEPREL] == 'obj':
                head_idx = v[HEAD]
                # check if head of this token is the root token
                if sent[1][head_idx][DEPREL] == 'root':
                    triplet[1][2] = (v[LEMMA], v[ID])
            elif v[DEPREL] == 'root':
                triplet[1][1] = (v[LEMMA], v[ID])

        # if triplet has all three elements
        if "" not in triplet[1]:
            triplets_out.append(triplet)

    return triplets_out


if __name__ == '__main__':
    triplets = get_triplets('./UDpipe_parse_output/parsed_out.txt')

    with open('triples_from_UDPipe.txt', 'w') as fo:
        for trip in triplets:
            print(trip[0], file=fo)
            print(trip[1], file=fo)

    print('Done')
