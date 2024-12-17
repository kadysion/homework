package oodj;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class SupplierList {
    private static final String supplierFile = "src/oodj/supplier.txt"; // File location relative to the project directory

    // Get a list of all suppliers from the file
    public static ArrayList<String[]> getSupplierList() {
        try {
            ReadFile read = new ReadFile(supplierFile);
            return read.getRecords(); // Returns all supplier records
        } catch (IOException ex) {
            Logger.getLogger(SupplierList.class.getName()).log(Level.SEVERE, "Error reading supplier file", ex);
            return new ArrayList<>(); // Return empty list if there's an error
        }
    }

 

    // Inner class to read the supplier file
    private static class ReadFile {
        private BufferedReader reader;

        public ReadFile(String fileName) throws IOException {
            reader = new BufferedReader(new FileReader(fileName));
        }

        public ArrayList<String[]> getRecords() throws IOException {
            ArrayList<String[]> records = new ArrayList<>();
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                records.add(parts);
            }
            reader.close();
            return records;
        }
    }
}
