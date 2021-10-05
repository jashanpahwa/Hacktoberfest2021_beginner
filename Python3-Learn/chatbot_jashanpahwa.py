import re

def words(input1):
      global t,a,b,bk,c,crn,dc,no,tr,sma,s,n
      t,a,b,bk,c,crn,dc,no,tr,sma,s,n=0,0,0,0,0,0,0,0,0,0,0,0
      if (re.search("transfer",input1)):
	      tr=1
      if(re.search("account",input1)):
   	    a=1
      if(re.search("balance",input1)):
	       b=1	    
      if(re.search("bank",input1)):
	      bk=1       
      if(re.search("code",input1)):
   	    c=1	    
      if(re.search("crn",input1)):
	       crn=1
      if(re.search("debit card ",input1)):
    	    dc=1
      if(re.search("number",input1)):
    	    no=1
      if(re.search("name",input1)):
   	    n=1	
   	    
      if(re.search("transaction",input1)):
	       t=1	    
      if(re.search("send money abroad",input1)):
  	    sma=1
      if(re.search("send",input1)):
  	     s=1
while(1):
         input1=input()
         words(input1)
         if(n==1&a==1):
         	print('Bank account name is xxxxxxx')
         if(tr==1&s==1):
         	print('Transfer your money safely in following steps ')
         if(b==1&bk==1):
         	print('Bank balance in account is Rs. XXXXXXX')
         if(a==1&no==1):
         	print('Bank account number is xxxxxxxxxxxxxxxx')
         if (t==1):
         	print('These are your last 10 transaction')
         if(dc==1&no==1):
         	print('Your Debit Card number is xxxx xxxx xxxx ')
         if(c==1):
         	print('Bank IFSC Code is xxxxxxxxxxxxx')
         if(crn==1):
         	print('Your CRN no. is xxxxx')
         if(sma==1):
         	print('Sending money abroad is easier now \n Follow these steps\n1.---------------\n2.---------------\n3.---------------\n')
         j= input("Press 1 to use again and 0 to terminate")
         j= int(j)
         if (j==1):
           continue
         else:
            break


	

	    
		    	    
		    	    	    
		    	    	    	    
		    	    	    	    	    
		    	    	    	    	    	    
		    	    	    	    	    	    	    
		    	    	    	    	    	    	    	    
		    	    	    	    	    	    	    	    	    
		    	    	    	    	    	    	    	    	    	    
		    	    	    	    	    	    	    	    	    	    	    	    