values=('A','2','3','4','5','6','7','8','9','10','J','Q','K') # A=ACE K=king Q=Queen J=Jack
suites=('D','S','C','H')     # D=Diamonds C=Clubs H=Hearts S=Spades
royal_flush=('10','J','Q','K','A')
special_cards=('A','J','Q','K')
cards_value_dic={'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13} 
cards=input('enter the cards value with their suite: ').split()[:5] #example_input_format=2D AH JS QC KH or 4D 8S AC KH 10C

values_lst=[]
value_name_lst=[] # List for values , for example: 2,4,10,K,Q,J,A
suites_lst=[] # List for suites , for example:S,D,H,C
num_same_items=[] #stores the count of items which have same values
forward=0 
values_str=''
index=0
counter=0

if len(cards)!=5:
    print('The number of the cards must be 5!')
else:

 for i in cards:
    count=0
    for j in i:
        if  j.isnumeric() or j.upper() in special_cards :
            values_str+=j.upper()
        else:
            count+=1    
            
        if count==1:
            values_lst.append(cards_value_dic.get(values_str,'!'))
            
            value_name_lst.append(values_str)
            suites_lst.append(j.upper())
            values_str=''    


 for i in value_name_lst:
    if i not in values:
        print('invalid value for values!')
        break

 else:
  for i in suites_lst:
     if i not in suites_lst:
         print('invalid value for suites!')
         break
  else:
   values_lst.sort()
         





   for i in values_lst:
    if values_lst.count(i)>1:
        num_same_items.append(values_lst.count(i))
        for j in range(values_lst.count(i)):
            values_lst.remove(i)
           

   if len(num_same_items)==1:
    if num_same_items[0]==2:
        print('One pair')
    elif num_same_items[0]==3:
        print('Three of a kind')
    elif num_same_items[0]==4:
        print('Four of a kind')
   elif len(num_same_items)==2:
    if num_same_items[0]==2 and num_same_items[1]==2:
        print('Two pairs')
    elif (num_same_items[0]==3 and num_same_items[1]==2) or (num_same_items[0]==2 and num_same_items[1]==3):
        print('Full house')
   else:


    for i in value_name_lst:
       
       
       if i not in royal_flush:
           
           
           break
       else:
           continue
    else:
        
        for i in suites_lst:
            if suites_lst.count(i)==5:
               


               forward+=1
               break
            else:
                break
         
    if forward==1:


        print('Royal Flush')
    else:
        

        for i in values_lst:
            counter+=1
            if counter!=len(values_lst):


                if values_lst[index+1]==values_lst[index]+1:
                    index+=1
                    
                else:
                    for i in suites_lst:
                        if suites_lst.count(i)==5:
                            print('Flush')
                            break
                        else:
                            print(f'High card={max(values_lst)}')
                            break
                    break    

                    
        else:
            for i in suites_lst:
                if suites_lst.count(i)==5:
                    print('Straight Flush')
                    break
                else:
                    print('Straight')
                    break    


                
