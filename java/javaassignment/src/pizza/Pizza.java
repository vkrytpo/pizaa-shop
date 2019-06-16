package pizza;

import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Pizza {
	
	
	
	String regex = "^\\+?[0-9. ()-]{10,25}$";
	String regex1="^[#.0-9a-zA-Z\\s,-]+$";
    private String size;
	
	private int cost;
	
	private List<String> pizzatoppings;
	
	private String name;
	private String phone;
	private String address;
	Scanner sc = new Scanner(System.in);

	public String getSize() {
		return size;
	}

	public List<String> getPizzatoppings() {
		return pizzatoppings;
	}

	public void setPizzatoppings(List<String> pizzatoppings) {
		this.pizzatoppings = pizzatoppings;
	}

	public void setSize(String size) {
		this.size = size;
	}

	
	

	public int getCost() {
		return cost;
	}

	public void setCost(int cost) {
		this.cost = cost;
	}

	public String nameValidation() {
		while(true)
		{
		 System.out.println("Enter name:"); 
		    name = sc.nextLine(); 
		  
		       if (!name.matches("[a-zA-Z_]+")) {
		         System.out.println("Name is invalid. Please use valid name.");
		         continue;
		       }
		       else
		         {
		    	    break;
		          }
		      
		}
		
		 return name;       
		// TODO Auto-generated method stub
		
	}

	public String phoneNumberValidation() {
	     while(true)
		   {  
		    System.out.println("Enter Phone:"); 
		    phone = sc.nextLine();
		   
		   Pattern pattern = Pattern.compile(regex);
	        Matcher matcher = pattern.matcher(phone);
		    if(matcher.matches())
		  
		      {  break;
		        
		       }
		       else
		       {
		    	 System.out.println("Phone number is invalid. Please use 10 digit Phone Number.");
		         continue;
		       }
		       
		   }
	     return phone;
		// TODO Auto-generated method stub
		
	}

	public String addressValidation() {
		  while(true)
		   {  
		    System.out.println("Enter your address: "); 
		    address = sc.nextLine();
		   
		   Pattern pattern = Pattern.compile(regex1);
	        Matcher matcher = pattern.matcher(address);
		    if(matcher.matches())
		  
		      { 
		    	break;
		        
		       }
		       else
		       {
		    	 System.out.println("Address is invalid.");
		         continue;
		       }
		       
		   }
		  return address;
		// TODO Auto-generated method stub
		
	}
	
	

}
