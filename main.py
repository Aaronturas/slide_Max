def sliding_max(lst, w):
  ptr1= 0
  ptr2 = w
  print(w)
  

  while ptr1 < len(lst):
    slide = lst[ptr1:ptr2]
    max = 0
    ptr1+=1
    ptr2+=1
    
    for i in slide:
      if max < i:
        max = i
    print(max)

    

sliding_max([1,2,3,1,4,5], 3)