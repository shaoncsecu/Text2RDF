
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class JsonArrayToText {
    public static void main(String[] args) {

        JSONParser parser = new JSONParser();

        try {     
            JSONArray a = (JSONArray) parser.parse(new FileReader("src\\sample.json"));

            for (Object o : a) {
                JSONObject person = (JSONObject) o;

                String content = (String) person.get("content");
                System.out.println(content);
                /*
                String city = (String) person.get("city");
                System.out.println(city);

                String job = (String) person.get("job");
                System.out.println(job);

                JSONArray cars = (JSONArray) person.get("cars");

                for (Object c : cars) {
                    System.out.println(c + "");
                }
*/
            }
        } catch (FileNotFoundException e) {
            System.out.println("File Not Found "+e.getMessage());
        } catch (IOException e) {
            System.out.println("File Not Found "+e.getMessage());
        } catch (ParseException ex) {
            Logger.getLogger(JsonArrayToText.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
