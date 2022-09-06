
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


public class TextToJson {
    public static void main(String[] args) {
        
        String line = null;
        
        try {
            
            BufferedReader bufferedReader = new BufferedReader(new FileReader("src\\sample.txt"));
            BufferedWriter out=new BufferedWriter(new FileWriter("src/output.txt" , false));
            
            boolean tag=false;
            
            String type,sub,obj;
            type=sub=obj="";
            String uri = "http://example.com/";
            
            out.write("[");
            out.newLine();
            
            long i=1;
            
            while ((line = bufferedReader.readLine()) != null) 
            {
               
                if(line.contentEquals("A0:"))
                {
                    while(!"V:".equals(line = bufferedReader.readLine()))
                    {
                        if(!"\"".equals(line)){
                            sub +=line+" ";
                        }
                        
                    }
                    
                    sub = sub.trim();
                    
                    while(!"A1:".equals(line = bufferedReader.readLine()))
                    {
                        if(!"\"".equals(line)){
                            type += "-"+line;
                        }
                    }
                    type=type.replaceFirst("-", "");
                    //type = type.trim();
                    
                    while(!"".equals(line = bufferedReader.readLine()))
                    {
                        if(!"\"".equals(line)){
                            obj +=line+" ";
                        }
                    }
                    
                    obj = obj.trim();
                    
                    if(tag){
                        out.write(",");
                        out.newLine();
                        
                    }
                    else{
                        tag=true;
                    }
                    
                    out.write("{");
                    out.newLine();
                    out.write("    \"@id\": \""+uri+""+i+"\",");
                    out.newLine();
                    out.write("    \"@type\": \""+type+"\",");
                    out.newLine();
                    out.write("    \"subject\": \""+sub+"\",");
                    out.newLine();
                    out.write("    \"object\": \""+obj+"\",");
                    out.newLine();
                    out.write("    \"@context\": {");
                    out.newLine();
                    out.write("        \""+type+"\": \""+uri+"type#"+type+"\",");
                    //out.write("        \""+type+"\": \""+uri+"type/"+i+"\",");
                    out.newLine();
                    out.write("        \"subject\": \""+uri+"subject\",");
                    out.newLine();
                    out.write("        \"object\": \""+uri+"object\"");
                    out.newLine();
                    out.write("    }");
                    out.newLine();
                    out.write("}");
                    
                    type=sub=obj="";
                    i++;
                }
                else if(line.isEmpty())
                {   
                    type=sub=obj="";
                }
                
            }
            
            out.newLine();
            out.write("]");
            bufferedReader.close();
            out.close();
            
        } catch (FileNotFoundException ex) {
            System.out.println("Unable to open file");
        } catch (IOException ex) {
            System.out.println("Error reading file");
        }
    }
 
}
