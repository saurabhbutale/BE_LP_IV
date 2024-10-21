import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class EmailHeaderAnalyzer {
    public static void main(String[] args) {
        // Path to the email file
        String emailFilePath = "sample.eml";
        // Analyze the email header
        analyzeEmailHeader(emailFilePath);
    }

    private static void analyzeEmailHeader(String filePath) {
        String fromAddress = "";
        String toAddress = "";
        String date = "";
        String subject = "";
        String mailedBy = "";
        String signedBy = "";

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                line = line.trim(); // Trim leading and trailing whitespace

                // Stop reading if we reach the end of the header section (empty line)
                if (line.isEmpty()) {
                    break;
                }

                if (line.toLowerCase().startsWith("from:")) {
                    fromAddress = line;
                } else if (line.toLowerCase().startsWith("to:")) {
                    toAddress = line;
                } else if (line.toLowerCase().startsWith("date:")) {
                    date = line;
                } else if (line.toLowerCase().startsWith("subject:")) {
                    subject = line;
                } else if (line.toLowerCase().contains("mailed-by:")) {
                    mailedBy = line;
                } else if (line.toLowerCase().contains("signed by:")) {
                    signedBy = line;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Display the analyzed data
        System.out.println("Email Header Analysis:");
        System.out.println("----------------------");
        System.out.println("From: " + fromAddress);
        System.out.println("To: " + toAddress);
        System.out.println("Date: " + date);
        System.out.println("Subject: " + subject);
        System.out.println("Mailed-By: " + mailedBy);
        System.out.println("Signed By: " + signedBy);
    }
}
