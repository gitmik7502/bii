# Bii

This is my newest I made called 'Bii'.
its a command-line copy-ish of the Wii's OS.
Enough text lets begin:

### setup:  
#### Requirements:
1. [python 3+](https://www.python.org/downloads/) installed to root    
2. requests
3. win32file    
4. folder OS in root
5. 2 usb's (i am using a 15GB and a 32GB drive)
#### Steps:

1. Download and extract the files in the zip file		
2. copy the OS folder in your C:\ drive		
3. make a run.bat file on your desktop and paste the code in it (run.bat in the repo)
4. open cmd and type 'pip install win32file, requests' 
5. plug in one usb if the letter is d:\ skip th next steps
6. press Win + R and type 'diskmgmt.msc' and press ok 
![image](https://user-images.githubusercontent.com/108491891/231522349-e678c524-c987-4754-8dd5-ac2f4521ab43.png)
you will see this 
![image](https://user-images.githubusercontent.com/108491891/231523334-702b49d4-0e03-45b0-b92d-a40a53f627bf.png)
my usb is called 'example drive (E:)'
right-click your drive and click format
![image](https://user-images.githubusercontent.com/108491891/231529666-f56fb833-b2b4-479c-8d7b-d957828bab85.png)
then change the drive name to 'GAME' its does not have to be 'GAME' it can be anything 
![image](https://user-images.githubusercontent.com/108491891/231530574-fcf9e775-bd14-4644-956a-c21e1b941ebd.png)
click 'OK'
![image](https://user-images.githubusercontent.com/108491891/231531469-8ff27d76-7b32-4221-b85b-966d936b0c4a.png)
and again click 'OK'
![image](https://user-images.githubusercontent.com/108491891/231531663-2f649f4e-d437-4cde-9b55-0392f8da5f7b.png)
### then change the letter to 'D:\'
![image](https://user-images.githubusercontent.com/108491891/231532143-e3eba9b1-492e-4bf5-8ac7-365645b54270.png)
firstly, right-click the drive
![image](https://user-images.githubusercontent.com/108491891/231534639-ad6d1ff4-5a5a-49cd-834e-131985ff744e.png)
then click the 'Change Letter And Paths'
![image](https://user-images.githubusercontent.com/108491891/231534695-55ad91e8-945f-480a-af2e-627c0069b896.png)
Click 'Change'
![image](https://user-images.githubusercontent.com/108491891/231534857-19502e19-a7bc-40e0-a8c0-7a4ead19d4ed.png)
click the dropdown menu and select 'D:'
![image](https://user-images.githubusercontent.com/108491891/231534925-ecb1da3a-6a6c-474c-b549-a8d1795e07b8.png)
click 'OK'
![image](https://user-images.githubusercontent.com/108491891/231534996-c749ae6b-db94-4f23-9385-6e3fdbdb5ac2.png)
and again click 'OK'
![image](https://user-images.githubusercontent.com/108491891/231535062-86a3c6c1-ee90-4315-aa51-52412e95e7cb.png)
DONE! now if you are a python programer just make a file called disc.pyw and paste the template (temp_disc.pyw) if not make the file but paste the game (game_disc.pyw)
![image](https://user-images.githubusercontent.com/108491891/231535110-d6a6ce50-246f-4cf1-9f01-361ee373c3aa.png)
next lets format the next USB
![image](https://user-images.githubusercontent.com/108491891/231537046-0fc6c441-262f-4389-86ce-0dc67e57d4af.png)
First lets split the drive to 2 formats
1. Delete the volume
![image](https://user-images.githubusercontent.com/108491891/231539472-fa6a8f6d-102b-4ceb-9279-e03a72ad6ba8.png)
click 'OK'
![image](https://user-images.githubusercontent.com/108491891/231539612-fb688518-508a-4385-b9ae-157056035fef.png)
make it a new simple volume
![image](https://user-images.githubusercontent.com/108491891/231542231-80313d7f-d566-4987-b796-6c735a9b262f.png)
![image](https://user-images.githubusercontent.com/108491891/231542683-5610ad07-0c9f-4e5b-af8e-8a1d79e2034c.png)
i have a 32GB drive so i will half them (160000MB)
![image](https://user-images.githubusercontent.com/108491891/231544197-2e0993aa-6a7f-445a-a2b4-5c6ff2da5c84.png)
assign the letter to be 'E:'
![image](https://user-images.githubusercontent.com/108491891/231544690-15b87084-ea76-4eeb-a64b-71fa3b5993e5.png)
call it USB
![image](https://user-images.githubusercontent.com/108491891/231546625-ae6c1828-a82a-4389-9799-5ec234233bd2.png)
Now lets do the same again
make it a new simple volume again
![image](https://user-images.githubusercontent.com/108491891/231542231-80313d7f-d566-4987-b796-6c735a9b262f.png)
![image](https://user-images.githubusercontent.com/108491891/231542683-5610ad07-0c9f-4e5b-af8e-8a1d79e2034c.png)
just press next
asaign the letter to 'F:'
![image](https://user-images.githubusercontent.com/108491891/231549053-d59ea33d-e588-42fc-89cd-e55c627a6d22.png)
call it SD
![image](https://user-images.githubusercontent.com/108491891/231549275-a77d9baa-1015-4cd8-afc6-2514de0b0079.png)
open run.bat and your done


if you want to run your own shop server read customgit.md.
