import java.io.*;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class JsonObjectToTxt {

    public static void main(String[] args) {
        
        JSONObject obj;
        String line = null;

        try {
            
            BufferedReader bufferedReader = new BufferedReader(new FileReader("src\\sample.json"));
            BufferedWriter out=new BufferedWriter(new FileWriter("src/output.txt" , false));
            
            long i=0;
            long limit = 1000;         //Taking a subset of the input
            
            while ((line = bufferedReader.readLine()) != null && ++i<=limit) 
            {
                obj = (JSONObject) new JSONParser().parse(line);
                
                //System.out.println((String) obj.get("content"));
                
                out.write((String) obj.get("content"));
                out.newLine();
                //out.write("#");                 //Just a end marker
                out.newLine();
            }
            
            bufferedReader.close();
            out.close();
            
        } catch (FileNotFoundException ex) {
            System.out.println("Unable to open file");
        } catch (IOException ex) {
            System.out.println("Error reading file");
        } catch (ParseException e) {
            System.out.println("Parser Exception");
        }
    }
}
