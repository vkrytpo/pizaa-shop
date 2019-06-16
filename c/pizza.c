#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>


int order_count = 0;

  struct pizza
{
   char * size;
   float price;
   char * topping[4];
   char * delivery;
   char * name;
   char * phone;
   char * address;
};

struct pizza order[100] = {};


bool isvalueinarray(int val, int *arr, int size){
    int i;
    for (i=0; i < size; i++) {
        if (arr[i] == val)
            return true;
    }
    return false;
}

char get_pizza_size(){
  char pizza_size;
  printf("Enter Your Pizza Size: ");
  scanf("%s",&pizza_size);
  return pizza_size;
}

char do_you_want_more_topping(){
  char more_topping;
  printf("Enter your choice: ");
  scanf("%s",&more_topping);
  return more_topping;
}

int get_new_topping(){

  int top_in = 0;
  printf("Enter topping: ");
  scanf("%d",&top_in);

  return top_in;
}

bool check_new_topping(int val, int *arr, int size){
    int i;
    for (i=0; i < size; i++) {
        if (arr[i] == val)
            return true;
    }
    return false;
}

char * topping_name_by_id(int id){
  char * topping_name;
  switch(id){
    case 1:
    topping_name = "Bacon";
    break;
    case 2:
    topping_name = "Olives";
    break;
    case 3:
    topping_name = "Mushrooms";
    break;
    case 4:
    topping_name = "Pineapple";
    break;
    case 5:
    topping_name = "Salami";
    break;
    case 6:
    topping_name = "Anchovies";
    break;
    default:
    topping_name = "Cheese";
    break;

  }
  return topping_name;

}

void add_topping_to_order(int *arr, int order_count){
    int i;
    order[order_count].topping[0] = "Cheese";
    for (i=0; i < 4; i++) {
      if(arr[i] != 0){
        char * name = topping_name_by_id(arr[i]);
        order[order_count].topping[i] = name;
      }
    }
   
}

int main()
{
 

char pizza_size;

NEW_ORDER:
printf("\nSelect pizza size:\n");
printf("\t s = Small | m = Medium | l = Large\n");

GET_PIZZA_SIZE:
pizza_size = get_pizza_size();


switch(pizza_size) {
      case 's' :
         printf("You have selected small size pizza.\n");
         order[order_count].size = "Small";
         order[order_count].price = 5.0;
         order[order_count].topping[0] = "Cheese";
         break;
      case 'm' :
         printf("You have selected medium size pizza.\n");
         order[order_count].size = "Medium";
         order[order_count].price = 8.0;
         order[order_count].topping[0] = "Cheese";
         break;
      case 'l' :
         printf("You have selected large size pizza.\n");
         order[order_count].size = "Large";
         order[order_count].price = 12.0;
         order[order_count].topping[0] = "Cheese";
         break;
      default :
         printf("\nPlease Enter Valid Character: only s/m/l allowed.\n" );
         //order_count = 0;
         goto GET_PIZZA_SIZE;

   }

char yn;
printf("\nBy default Your Pizza order comes with topping cheese default. You can add more toppings.You will be charged extra $1 for each toppings. \n");
printf("Select Toppings:\n");
printf("\t Enter 1 for Bacon | 2 for Olives | 3 for Mushrooms | 4 for Pineapple | 5 for Salami | 6 for Anchovies\n");

printf("\nDo you want to add more toppings?\n");
printf("\t Enter y for Yes | n for No\n");


int topping_count = 0;
int top_list[4] = {0,0,0,0};
WANT_MORE_TOPPINGS:
yn = do_you_want_more_topping();
int topping_id = 0;
switch(yn) {
      case 'y' :
      //printf("\ntopcount: %d\n",topping_count);
      if(topping_count  >= 4){
        printf("You have selected more than four toppings:\n");
        add_topping_to_order(top_list,order_count);
        break;
      }
      
      topping_id = get_new_topping();
      //printf("selected topping is: %d",topping_id);
      if(topping_id < 0 || topping_id == 0 || topping_id > 6){
        printf("Topping out of range!!");
        printf("\nDo you want to add more toppings?\n");
        printf("\t y = Yes | n = No\n");
        goto WANT_MORE_TOPPINGS;

      }
      else
      { 
          char * tname;
        tname = topping_name_by_id(topping_id);
        printf("You selected: %s\n",tname);
        bool is_selected = check_new_topping(topping_id,top_list,4);
        if(!is_selected){
          top_list[topping_count] = topping_id;
          topping_count = topping_count +1;
          //printf("\nNot selected\n");
          printf("\nDo you want to add more toppings?\n");
          printf("\t y = Yes | n = No\n");
          goto WANT_MORE_TOPPINGS;
        }
        else{
          printf("\nThis topping already selected.\n");
          printf("\nDo you want to add more toppings?\n");
          printf("\t y = Yes | n = No\n");
          goto WANT_MORE_TOPPINGS;
        }
      }

      
         break;
      case 'n' :
        //printf("\nYou have selected No.\n\n");
        //printf("Order Count: %d",order_count);
        add_topping_to_order(top_list,order_count);
         break;
      default :
         printf("Please Enter Valid Character: Only y/n allowed.\n" );
         goto WANT_MORE_TOPPINGS;

   }

   ASK_ANOTHER_ORDER:

   printf("\nDo you like to order another pizza?\n");
    printf("\t y = yes | n = no\n");
    char another_order;
    printf("Enter your choice: ");
    scanf("%s",&another_order);

    switch(another_order){
      case 'y' :
      order_count = order_count+1;
      goto NEW_ORDER;
      break;

      case 'n' :
      //delivery_type = "delivered";
      //ASK_ANOTHER_ORDER
      break;

      default:
      printf("Please enter valid value. y/n allowed.\n");
      goto ASK_ANOTHER_ORDER;
      break;
    }


DELIVARY_TYPE:
   printf("\nYou want your order to be collected or delivered?\n");
    printf("\t c = collected | d = delivered\n");
    char delivery_type_id;
    char * delivery_type;
    printf("Enter your choice: ");
    scanf("%s",&delivery_type_id);
    char your_name[100];
    char your_phone[100];
    char your_address[100];

    switch(delivery_type_id){
      case 'c' :
        delivery_type = "collected";
        printf("\nEnter Your Name: ");
        scanf("%s",your_name);
        // scanf(?"%[^\n]%*c",your_name);
        // fgets (your_name, 100, stdin);
        // scanf("%[^\n]s",your_name);
        printf("Enter Your Phone: ");
        scanf("%s",your_phone);
        break;

      case 'd':
        delivery_type = "delivered";
        printf("\nEnter Your Name: ");
        scanf("%s",your_name);
        printf("Enter Your Phone: ");
        scanf("%s",your_phone);
        printf("Enter Your Address: ");
        scanf("%s",your_address);
        break;

      default:
        printf("Please enter valid value. c/d allowed.\n");
        goto DELIVARY_TYPE;
        break;
    }

int i, j , k;
printf("\n\n\nYour Order Details:\n");
printf("\n|*********************************************************************************|\n");
printf("|*********************************************************************************|\n\n\n");
for ( i = 0; i < order_count+1; i++ ) {
  printf("Pizza%d:",i+1);
  printf("\tSize: %s\n", order[i].size );
  printf("\tPrice: $%f\n", order[i].price );
   printf("\tToppings: \n");
          int top_length;
          //char * topp[5];
          //char topping[100] = {'\0'};
          for(k=0;k<4;k++){
            char * topp = order[i].topping[k];
            //printf("toppingOut : %s\n",topp );
            if(topp != NULL){
              top_length = strlen(topp);
              //printf("top:%s len: %d\n",topp,top_length);
              if(top_length > 0){
                printf("\t\t%s\n",topp);
              }
            }
          }
      }
      printf("Delivary type: %s\n", delivery_type );
      printf("Name: %s\n", your_name );
      printf("Phone: %s\n", your_phone );
      if(delivery_type_id == 'd'){
        printf("Address: %s\n", your_address );
      }
   
//printf("From outside for loop\n");
float total_cost = 0;
for(i=0;i<order_count+1;i++){
  float pizza_cost = order[i].price;
  int topping_count = 0;
  int top_length = 0;

  for(k=0;k<4;k++){
            char * topp = order[i].topping[k];
            //printf("toppingOut : %s\n",topp );
            if(topp != NULL){
              top_length = strlen(topp);
              //printf("top:%s len: %d\n",topp,top_length);
              if(top_length > 0){
                topping_count++;
              }

            }
            
          }


  //int topping_count = length(order[i].topping);
  //printf("Topping Count: %d\n",topping_count);
  float topping_cost = topping_count;
  total_cost = total_cost + pizza_cost + topping_cost;
}
//total_cost = total_cost + topping_count;
printf("\nTotal cost: $%f\n\n",total_cost);
if(delivery_type_id == 'd' && total_cost <30){
  printf("Total cost less than $30 so additional $8 delivery fee will be added.\n");
  printf("\nTotal cost including delivery fee: $%f\n\n",total_cost+8);

}

printf("\n\n|*********************************************************************************|\n");
printf("|*********************************************************************************|\n\n");
exit(0);
return 0;
}