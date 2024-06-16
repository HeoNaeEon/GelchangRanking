import dc_api
import asyncio

num = int(input("Searching Num : "))
id = input("id : ")
lst = []
lst2 = [] 
lst3 = []
lst4 = []

async def run():
  k=0
  l=1
  api = dc_api.API()
  async for index in api.board(board_id=id, num=num, start_page=1, document_id_upper_limit=None, document_id_lower_limit=None):
   lst.append(index.author)
  for value in lst:
   if value not in lst2:
    lst2.append(value)
  for i in lst2:
   lst3.append(i + " | " + str(lst.count(i)))
  for j in lst3:
   lst4.append(j.split(" | "))
  sorted_list = sorted(lst4,key=lambda x:-int(x[1]))
  while k < len(sorted_list):
   print(str(l) +  ". " + "User : " + sorted_list[k][0] + " | " + "Total Doc : " + sorted_list[k][1])
   if sorted_list[k][1] != sorted_list[k+1][1]:
    l=l+1
   k=k+1
  await api.close()
try: 
 asyncio.run(run())
except:
 pass
   
