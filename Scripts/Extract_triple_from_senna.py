# -*- coding: utf-8 -*-
'''
Object to extract triplets from Senna
'''

'''
Calling extractor:
(see also above example)

Create a SennaTripleExtractor object (which doesn't need any argument) by calling
name_of_extract_object = SennaTripleExtractor()

From the extractor object, call the method 'get_triplets', the input arguments being a) path to input file and b) path to / name of output file
name_of_extract_object.get_triplets(IN_FILE, OUT_FILE)

IN_FILE must be in the form of Senna parser output
OUT_FILE will have be the triplets of the following form:

A0:
[words in the subject argument, each printed on one line]
V:
[words in the verb, each printed on one line]
A1:
[words in the object argument, each printed on one line]
'''

class SennaTripleExtractor:
    """Extractor for extracting triples from Senna output"""

    def __init__(self):
        pass

    def get_content(self, file_path):
        """ Parse data from Senna output file """

        print('Processing input file...')
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            sent_id = -1# starting count
            tmp_cont = []

            for line in f:
                line = line.strip()

                if len(line) == 0:
                    if len(tmp_cont) > 0:
                        sent_id += 1
                        data.append((sent_id, tmp_cont))
                        tmp_cont = []

                else:
                    data_line = line.split()
                    tmp_cont.append(data_line)
    #
            if len(tmp_cont) > 0:
                sent_id += 1
                data.append((sent_id, tmp_cont))

        return data


    def get_triplets(self, input_file_path, output_file_path):
        """ Get triplets from Senna output file """

        data = self.get_content(input_file_path)

        triplets = []

        print('Extracting triplets...')
        for sent in data:# where each sent is a tuple of the form (sent_id, list of data-per-line-lists)
            sent_id = sent[0]
            #print('Working on Sent no:', sent_id)

            A0 = []
            A1 = []
            V = []
            A0_1 = []
            A1_1 = []
            V_1 = []
            A0_2 = []
            A1_2 = []
            V_2 = []
            A0_3 = []
            A1_3 = []
            V_3 = []

            for line_list in sent[1]:# where each line_list is the data on one line in input file:
                #print(line_list)
                if len(line_list) >= 6:
                    if line_list[5].endswith('A0') and line_list[1] not in {'PRP', 'WDT', 'PRP$'}:
                        A0.append(line_list[0])
                    elif line_list[5].endswith('A1') and line_list[1] not in {'PRP', 'WDT', 'PRP$'}:
                        A1.append(line_list[0])
                    elif line_list[5].endswith('V') and line_list[1] in {'VB','VBD','VBG','VBN','VBP','VBZ', 'IN'}:
                        V.append(line_list[0])

                if len(line_list) >= 7:
                    if line_list[6].endswith('A0') and line_list[1] not in {'PRP', 'WDT', 'PRP$', 'WP'}:
                        A0_1.append(line_list[0])
                    elif line_list[6].endswith('A1') and line_list[1] not in {'PRP', 'WDT', 'PRP$', 'WP'}:
                        A1_1.append(line_list[0])
                    elif line_list[6].endswith('V') and line_list[1] in {'VB','VBD','VBG','VBN','VBP','VBZ', 'IN'}:
                        V_1.append(line_list[0])

                if len(line_list) >= 8:
                    if line_list[7].endswith('A0') and line_list[1] not in {'PRP', 'WDT', 'PRP$', 'WP'}:
                        A0_2.append(line_list[0])
                    elif line_list[7].endswith('A1') and line_list[1] not in {'PRP', 'WDT', 'PRP$', 'WP'}:
                        A1_2.append(line_list[0])
                    elif line_list[7].endswith('V') and line_list[1] in {'VB','VBD','VBG','VBN','VBP','VBZ', 'IN'}:
                        V_2.append(line_list[0])

                if len(line_list) >= 9:
                    if line_list[8].endswith('A0') and line_list[1] not in {'PRP', 'WDT', 'PRP$', 'WP'}:
                        A0_3.append(line_list[0])
                    elif line_list[8].endswith('A1') and line_list[1] not in {'PRP', 'WDT', 'PRP$', 'WP'}:
                        A1_3.append(line_list[0])
                    elif line_list[8].endswith('V') and line_list[1] in {'VB','VBD','VBG','VBN','VBP','VBZ', 'IN'}:
                        V_3.append(line_list[0])

            # triplets found as 4-tuples (including sent_id)
            # if triplet has all four components, keep it
            '''
            filtering constraints: max length for subjects and objects: 8 words.
            max length for verbs: 3 words.
            '''

            if 9 > len(A0) > 0 and 4 > len(V) > 0 and 9 > len(A1) > 0:
                triplets.append((sent_id, A0, V, A1))
            if 9 > len(A0_1) > 0 and 4 > len(V_1) > 0 and 9 > len(A1_1) > 0:
                triplets.append((sent_id, A0_1, V_1, A1_1))
            if 9 > len(A0_2) > 0 and 4 > len(V_2) > 0 and 9 > len(A1_2) > 0:
                triplets.append((sent_id, A0_2, V_2, A1_2))
            if 9 > len(A0_3) > 0 and 4 > len(V_3) > 0 and 9 > len(A1_3) > 0:
                triplets.append((sent_id, A0_3, V_3, A1_3))

        print('Outputting triplets ...')

        with open(output_file_path, 'w', encoding='utf-8') as fo:
            for trip in triplets:
                print('Sentence:', trip[0], file=fo)
                print('A0:', file = fo)
                for word in trip[1]:
                    print(word, file=fo)
                print('V:', file = fo)
                for word in trip[2]:
                    print(word, file=fo)
                print('A1:', file = fo)
                for word in trip[3]:
                    print(word, file=fo)
                print("", file=fo)

        print('Done')
        return

if __name__ == '__main__':

    my_extractor = SennaTripleExtractor()
    my_extractor.get_triplets('./senna_parsed.txt', './testOut.txt')


