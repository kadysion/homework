
package oodj;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class PurchaseOrder {
    private String poID;         // Purchase Order ID
    private String itemID;       // Item ID
    private int quantity;        // Quantity Ordered
    private double unitPrice;    // Unit Price
    private double totalPrice;   // Total Price (calculated)
    private String date;         // Purchase Order Date
    private String status;       // Status (Created/Approved/Rejected)

    // Constructor
    public PurchaseOrder(String poID, String itemID, int quantity, double unitPrice, String date, String status) {
        this.poID = poID;
        this.itemID = itemID;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
        this.totalPrice = quantity * unitPrice; // Calculate total price
        this.date = date;
        this.status = status;
    }

    // Save purchase order to a file
    public void saveToFile(String fileName) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(fileName, true))) {
            bw.write(poID + "," + itemID + "," + quantity + "," + unitPrice + "," + totalPrice + "," + date + "," + status);
            bw.newLine();
            System.out.println("Purchase Order saved successfully.");
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
    }
}



