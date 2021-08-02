q=["1. In which game are the terms 'checkmate' and 'stalemate' used?","2. A student obtains which of these educational degrees or  certificates first?","3. Which of these units of measurement cannot be used to measure any of the ingredients of a banana shake - banana, milk and sugar?","4. Which of these is a first-person shooter game?","5. How will your mother's brother's wife be related to you?","6. In comic book, which teenager was bitten by a radioactive spider and hence he gains superhuman strength, speed and the ability to cling the walls?","7. Who was born as Mool Shankar in Tankara, Gujarat, worked towards reviving Vedic ideologies and was the founder of the Arya Samaj?","8. Who among the following finds prey with the help of a special sound?","9. The Palk Strait seperates which of these countries from mainland India?","10. Whose birthday is celebrated as National Milk Day in India?","11. Who administered the oath of office to Pandit Jawaharlal Nehru as the first Prime Minister of Independent India?","12. Which was the first planet that was found with the art of a telescope?","13. Which cricketer has been involved in the most run - outs in Test and ODI Cricket?","14. Mustang Jaguar and Chrysler are all brands of what? "," 15. In a class of 30 students with a 1:1 gender ratio, how many 1 girl - 1 boy pairs can be made on a given day if 3 girls are on leave?","16. Which son of Karna survived the Kurukshetra War and took part in Yudhisthira's Ashwamedha Yaga? "]
s=["A: Chess                       B: Carrom\nC: Ludo                        D: Snake & Ladders","A: PhD Degree                  B: Master's Degree\nC: Graduation Degree           D: Mastric Certificate","A: Dozen                       B: Meter\nC: Gram                        D: Millilitre","A: Candy Crush Saga            B: Minecraft\nC: Call of Duty                D: Subway Surfers","A: Chachi                      B: Mami\nC: Bua                         D: Mausi","A: Peter Parker                B: Bruce Wayne\nC: Tony Stark                  D: Steve Rogers","A: Chaitanya Mahaprabhu        B: Dayanand Saraswati\nC: Raja Ram Mohan Roy          D: Ramkrishna Paramahamsa","A: Bat                         B: Owl\nC: Kite                        D: Dawk","A: Pakistan                    B: Bangladesh\nC: Sri Lanka                   D: Indonesia","A: Louis Pasteur               B: Arun Krishna\nC: Vergese Kurien              D: M. S. Swaminathan","A: Lord Wavell                 B: Lord Louis Mountbatten\nC: Chakravarti Rajagopalachari D: Rajendra Prasad","A: Uranus                      B: Naptune\nC: Saturn                      D: Mars","A: Inzaman - ul - Haq          B: Rahul Dravid\nC: Sachin Tendulakar           D: Steve Waugh","A: Motorcycle                  B: Bicycle\nC: Watches                     D: Cars","A: 15                          B: 13\nC: 12                          D: 30","A: Vrishaketu                  B: Satyasena\nC: Vrishasena                  D: Vrinanta"]
f=["A: Chess                       B: Carrom","A: PhD Degree                  D: Mastric Certificate","A: Dozen                       B: Meter","A: Candy Crush Saga            C: Call of Duty","A: Chachi                      B: Mami","A: Peter Parker                B: Bruce Wayne","A: Chaitanya Mahaprabhu        B: Dayanand Saraswati","A: Bat                         B: Owl","C: Sri Lanka                   D: Indonesia","C: Vergese Kurien              D: M. S. Swaminathan","A: Lord Wavell                 B: Lord Louis Mountbatten","A: Uranus                      B: Naptune","C: Sachin Tendulakar           D: Steve Waugh","C: Watches                     D: Cars","C: 12                          D: 30","A: Vrishaketu                  B: Satyasena"]
a=["A","D","B","C","B","A","B","A","C","C","B","A","D","D","C","A"]
r=[1000,2000,3000,5000,"10,000","20,000","40,000","80,000","1,60,000","3,20,000","6,40,000","12,50,000","25,00,000","50,00,000","1 Crore"," 7 Crore"]
t=0
sto=00
user=input('Enter you name : ')
print('                   **WELCOME TO KBC*         \n                   Kaun Banega Karorpati           \n\n\n*You have only one life line - 50:50 (use ×2)\nTo Quit the game - X or x\n')
for i in range(len(q)):
    if i==10:
        sto=r[i-1]
        print('Congratulation! You are playing well keep playing like this. Now you got a cheque of Rs',r[i-1])
        print ()
    print(q[i])
    print(s[i])
    p=input('Enter your option: ')
    if p=='X' or p=='x':
        print("\n        You have quit the Game.\n")
        if i>=11:
            print("You won the cheque of Rs",sto, "\nWe KBC team wish that  you'll use these amounts in fulfilling your dream 😃😇 ")   
        break
    if p=='50:50' or p=='5050':
        if t<2:
            t+=1
            print(f[i])
            p1=input('Enter your option: ')
            if p1==a[i]:
                print('Congratulation! You won Rs',r[i])
                print ()
                continue
            else:
                print("Ohh! You lost the game!")
                break
        else:
            print('You have already used it.\n')
            p=input('Enter your option: ')
    elif p==a[i]:
        print('Congratulation! You won Rs',r[i])
        print ()
        continue 
    else:
        print("ohh! You lost the game!")
        break
if i==(len(q)-1):
    print (" You are the Crorepati of this Game. We KBC team wish that  you'll use these amounts in fulfilling your dream 😃😇 ")


