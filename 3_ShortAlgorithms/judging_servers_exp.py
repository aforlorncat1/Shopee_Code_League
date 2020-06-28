'''
Clarification: the statement effectively means that buying any server gets a free additional server (buy-1,free-1). The purchased servers do not have to be adjacent to each other.

Logic:
1. The initial server purchase will always be the lowest costing one.
2. Save all selected servers into a selected_server_price_list
3. Sort all available servers into a sorted list.
(Currently the algorithm does not account for duplicate server prices, use enumerate to find the indexes of all duplicates)
4. Select the current lowest priced server and save it to selected_server_price_list.
5. Look at the adjacent servers to the selected one and pick the more expensive option to be included into the free_server_list.
6. Check if the number of servers in the selected_server_price_list and free_server_list equal to or exceed the required number of servers, N.
7. Print out the sum if yes, continue iterating if no. 


'''
import numpy as np
num_test_cases = int(input())
# S = number of available servers
# N = number of servers required
for t in range(num_test_cases):
    S,N = list(map(int,input().split()))
    price_array = list(map(int,input().split()))
    if N == 1:
        selected_server_price_list = []
        selected_server_price_list.append(min(price_array))
        print('Case {}: {}'.format(t+1, selected_server_price_list[0]))
    else:
        selected_server_price_list = []
        free_server_list = []
        sorted_price_list = sorted(price_array)

        for i in range(len(sorted_price_list)):
            current_min = sorted_price_list[i]
            selected_server_price_list.append(current_min) # add current cheapest server to the selected server list.
            # Then, find the adjacent servers to the selected server above and choose the more expensive one to be added to the free server list. 
            min_index = price_array.index(current_min) 
            free_server_list.append(max(price_array[min_index+1],price_array[min_index-1])) 
            # Break condition: if the number of servers in both lists exceed or equal to the number of required servers, N. 
            current_servers = len(selected_server_price_list) + len(free_server_list)
            if current_servers >= N:      
                print('Case {}: {}'.format(t+1, sum(selected_server_price_list)))   
                break 
  
            

