package pizza;
import pizza.Pizza;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class assignmentpizza {
	
public static void main(String[] args) 	{
			
	Pizza pizza = new Pizza();
	Scanner sc = new Scanner(System.in);
	String customerName="";
	String CustomerPhone="";
	String CustomerAddress = "";
	int delCharge=8;
	int toppingsCount,size;
	int price=0;
	int price_before_delivary =0;
	int beforeOrderPrice=0;
	int num;
	int numberOfPizza;
	System.out.println("\n******************* PIZZA SHOP ***********************************\n");
	System.out.println("How many pizza do you want to order?\n");
	numberOfPizza = sc.nextInt();
	List<String> ToppingsList = new ArrayList<>(Arrays.asList("Bacon", "Olives","Ham","Mushrooms","Pineapple","Salami","Anchovies"));
	List<Pizza> PizzasSelected = new ArrayList<>();
	for(int i=0;i<numberOfPizza;i++){
		Pizza pizza1 = new Pizza();
		toppingsCount = 0;
	
		//beforeOrderPrice=0;
		System.out.println("\nSelect Pizza Size:");
		System.out.println("Enter 1 for Small | 2 for Meduim | 3 for Large\n");
		size = sc.nextInt();
	
		if(size == 1){
			price += 5;
			pizza1.setSize("Small ($5)");
		}else if(size == 2){
			price += 8;
			pizza1.setSize("Medium ($8)");
		}else if(size==3){
			price += 12;
			pizza1.setSize("Large ($12)");
		}
		
	   
		List<String> pizzatoppings = new ArrayList<>();
		 num=1;
		 System.out.println("TOPPINGS: 1 for Bacon | 2 for Olives | 3 for Ham | 4 for  Mushrooms | 5 for Pineapple | 6 for Salami  | 7 for Anchovies | 0 for exit \n");
	
		while(toppingsCount<4 && num>=1 && num<=7){
			
			System.out.println("Select 1 to 7 for toppings or Enter 0 to exit");
			num = sc.nextInt();
			
		
				
				if(num>=1 && num<=7) {
					price++;
					pizzatoppings.add(ToppingsList.get(num-1));
					toppingsCount++;
				}else {
					break;
				}
				
				
				
			
			
			
		}
		
		pizza1.setPizzatoppings(pizzatoppings);
		pizza1.setCost(price - beforeOrderPrice);
		beforeOrderPrice = price;
	    PizzasSelected.add(pizza1);
		
	}
	
	System.out.println("Select Delivary Type :");
	System.out.println("1 for Collect | 2 for Delivery\n");
	int type = sc.nextInt();
	sc.nextLine();

	if(type == 1) {
	
		customerName=pizza.nameValidation();	
		CustomerPhone=pizza.phoneNumberValidation();
	}
	else 
	{
		customerName=pizza.nameValidation();
		CustomerPhone=pizza.phoneNumberValidation();
		CustomerAddress=pizza.addressValidation();	
		price_before_delivary = price;
		if(price<30) {
			price += delCharge;
		}
	}
	
	System.out.println("\n*********************** Order Details ******************************");
	for(Pizza pizz : PizzasSelected) {
		System.out.println("\nPizza Size : "+pizz.getSize());
		
		System.out.println("Topping: ");
		for(String s : pizz.getPizzatoppings()) {
			System.out.println("\t"+s);
		}
		//System.out.println("Pizza plus Toppings price: "+pizz.getCost());
	}
	System.out.println("\nName : "+ customerName );
	System.out.println("Phone Number : "+CustomerPhone);
	
	if(type != 1) {
		System.out.println("Address : " +CustomerAddress);
		if(price_before_delivary<30) {
			System.out.println("Delivery Charge : $"+ delCharge );
		}
	    
	}
		System.out.println("TOTAL PRICE: $"+price);
		System.out.println("\n*******************************************************************\n\n");
		
	
}


}
