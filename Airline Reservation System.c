#include<stdio.h>
#include<string.h>
#include<windows.h>
#include<conio.h>

void option1(char m[], char n[], int p[])
{
    int i,x=100; // x= available seat
    printf("\tFlight\t\t\tPrice\t\tSeating Capacity\tAvailable Seats\n");

    for(i=1; i<=3; i++)
    {
        printf("%d. %s To %s\t\t%d\t\t       %d\t\t\t20\n",i,m,n,p[i],x);
        x=x-10;
    }
}

void option2(char m[], char n[], int p[])
{
    int i,x=100;
    printf("\tFlight\t\t\t\tPrice\t\tSeating Capacity\tAvailable Seats\n");

    for(i=4; i<=6; i++)
    {
        printf("%d. %s To %s\t\t\t%d\t\t       %d\t\t\t14\n",i,m,n,p[i],x);
        x=x-20;
    }
}



struct ticket
{
    int flight;
    int price;
    char time[15];
};

int main()
{

    printf("\t\t\t\tWelcome To Bangladesh Airline Reservation System\n\n");
    struct ticket book;
    int price,con,con_pay,trip,a, x, y, i, total,c,X;
    long con_number,con_payment;
    int p[10]= {0,3500,4000,4500,1000,1500,2500};
    char user[10], pass[10], admin_user[10]="Elon Musk", admin_pass[10]="elonmusk",repeat,m[50],n[50],ch1,con_name1[50],con_name2[50];
    char date[15],date2[15];
    printf("\nEnter username: ");// user id
    scanf("%[^\n]",user);
    printf("Enter Password: ");
    for(i=0; i<10; i++) //pass only show (*)
    {
        ch1=getch();//take input that don't show
        pass[i]=ch1;

        if(ch1!=13) // ascii value of enter = 13
            printf("*");
        if(ch1 == 13)
            break;
    }
    pass[i]='\0';
    if (strcmp(user, admin_user)==0 || strcmp(pass, admin_pass)==0) // confirmation
    {
        printf("\nPlease wait");
        for(i=1; i<=5; i++)
        {
            printf(". ");
            Sleep(500);
        }

        printf("\n\nChoose if one way trip or roundtrip: ");
        printf("\n1. One way trip \n2. Roundtrip\n");
        scanf("%d", &trip);
        printf("\nWhich class you prefer?\n");
        printf("\n1. Business Class\n2. Economic Class\n");
        scanf("%d", &c);
        printf("\n");
        printf("Departure Airport: ");
        scanf("%*c%s",m);
        printf("Arrival Airport: ");
        scanf("%s",n);
        printf("\n");
        printf("\nEnter Departure Date(DD/MM/YYYY)\n");
        scanf("%s",&date);

        switch (trip)
        {
        case 1: // one way trip
        {
            if (c==1)//business
            {
                printf("\n%s\n",date);
                option1(m,n,p);// n= arrival , m= landing , p = price
                printf("\nPlease select which flight you will book: ");
                scanf("%d", &book.flight);
                if(book.flight==1||book.flight==2||book.flight==3)
                {
                    printf("\nHow many tickets will you get?:");
                    scanf("%d", &x);
                    book.price=x*p[book.flight];// flight price er sathe x er gun
                }
                else
                {
                    printf("Invalid\n");

                }



            }
            else if (c==2)//economic
            {

                printf("\n%s\n",date);
                option2(m,n,p);
                printf("\nPlease select which flight you will book: ");
                scanf("%d", &book.flight);
                if(book.flight==4||book.flight==5||book.flight==6)
                {
                    printf("\nHow many tickets will you get?:");
                    scanf("%d", &x);
                    book.price=x*p[book.flight];
                }
                else
                {
                    printf("Invalid\n");
                }


            }

            else
                printf("\nInvalid\n");
            break;
        }

        case 2: // round trip
        {
            if (c==1) // business
            {
                printf("\n%s\n",date);
                printf("\nEnter Return Date(DD/MM/YYYY)\n");
                scanf("%s", &date2);
                option1(m,n,p);
                printf("\nPlease select which flight you will book: ");
                scanf("%d", &book.flight);
                if(book.flight==1||book.flight==2||book.flight==3)
                {
                    printf("\nHow many tickets will you get?:");
                    scanf("%d", &x);
                    book.price=2*x*p[book.flight];
                }
                else
                {
                    printf("Invalid\n");
                }

            }

            else if (c==2) // economic
            {
                printf("\n%s\n",date);
                printf("\nEnter Return Date(DD/MM/YYYY)\n");
                scanf("%s", &date2);
                option2(m,n,p);
                printf("\nPlease select which flight you will book: ");
                scanf("%d", &book.flight);
                if(book.flight==4||book.flight==5||book.flight==6)
                {
                    printf("\nHow many tickets will you get?:");
                    scanf("%d", &x);
                    book.price=2*x*p[book.flight];
                }
                else
                {
                    printf("Invalid\n");
                }

            }

            else
                printf("\nInvalid");
            break;
        }
        default:
            break;
        }

        printf("\n");
        if(book.flight==1||book.flight==2||book.flight==3||book.flight==4||book.flight==5||book.flight==6){

            printf("\n******************************Ticket Details********************************\n");
            printf("Name: %s\n",admin_user);
            printf("Flight No: %d\t\t",book.flight);
            printf("Departure Date: %s\t\t",date);
            if(trip==2)
            {
                printf("Return Date:%s",date2);
            }
            printf("\n");
            printf("From: %s\t",m);
            printf("\tTo: %s",n);
            if(c==1)
            {
                printf("\nClass: Business\t");
            }
            else
            {
                printf("\nClass: Economic\t");
            }
            printf("\tPassengers: %d\t\t", x);
            printf("\nPrice: %d\n", book.price);
            printf("\n****************************************************************************\n");
            printf("\n");
            printf("Do you want to book the ticket?\n");
            printf("1.YES\n2.NO\n");
            scanf("%d%*c",&con);
            printf("\n");
            if(con==1)
            {
                printf("Enter your first name: ");
                scanf("%[^\n]",con_name1);
                printf("\n");
                printf("Enter your last name: ");
                scanf("%s",con_name2);
                printf("\n");
                printf("Enter your contact number: ");
                scanf("%ld",&con_number);
                printf("\n");
                printf("Which method you want to use for payment: \n");
                printf("1.Bkash\n2.Rocket\n3.Visa Card\n4.Master Crad\n5.Nagad\n6.Nexus Card\n7.DDBL\n");
                scanf("%d",&con_pay);
                printf("\n");
                if(con_pay==1||con_pay==2||con_pay==5)
                {
                    printf("Enter your number: ");
                    scanf("%ld",&con_payment);
                }
                else
                {
                    printf("Enter your card number: ");
                    scanf("%ld",&con_payment);
                }
                printf("\n");
                printf("Are you sure for the payment?\n");
                printf("1.Yes\n2.No\n");
                scanf("%d",&X);
                printf("\n");
                if(X==1)
                {
                    printf("Your Payment Has Been Done\n");
                    printf("*****Your ticket has been successfully reserved*****\n");
                }
                else
                {
                    printf("Thank You\n");
                }




            }
            else
            {
                printf("Thank You\n");
            }


        }

    else
        {
            printf("Something is wrong\nTry Again\n");

        }

    }
   else
        {
            printf("\nInvalid login\nTry Again\n");

        }




return 0;
}


