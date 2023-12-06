from datetime import datetime

import csv


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
dictionary and return the dictionary.

Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
                to use as the keys in the dictionary.
Return: a compound dictionary that contains
        the contents of the CSV file.
"""

    data = {}
    count = 0
    with open(filename, 'r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
              if index == 0:
                
              
                continue
                
  
              data[row[key_column_index]] = row

              
            
      
    return data

            
    



def main():
    try:
      current_date_and_time = datetime.now()
      num =0
      sub = 0
      product_dict = read_dictionary("products.csv", 0)
      print(product_dict)
      print("Savvy Mall")
      with open("request.csv", 'r') as file:
          data = []
          reader = csv.reader(file)
          print("Your order list")
          for index, row in enumerate (reader):
            if index == 0:
              continue
            data.append(row)
              
          for dic in product_dict:
            for lis in data:
              
            
                
              if lis[0]==product_dict[dic][0] :
                
                print()
                pname = product_dict[dic][1]
                
                qty = lis[1]
                price = product_dict[dic][2]
                if current_date_and_time.strftime("%H:%m %a")== "11:00 a.m":

                  price *= 0.1
                num += int(qty) 
                sub += int(qty ) * float(price)
                print(f"{pname}: {qty}unit @ {price} per unit")
                
          # if any(data[0]) not in any(product_dict[dic][0]) :
          # #   raise KeyError("Product not found")
          uni = [inner_list[0] for inner_list in data]
          # print(uni)
          # for item in uni:
          #   if item not in 
          # if all(uni) in any(product_dict.keys()):
          #   print("true")
          # else:
          #   print("false")
          #if alloop
          
          sales_t = sub * 0.06
          Total = sub + sales_t
          print("")
          print(f"Total number of ordered items: {num}")
          print(f"Subtotal: ${sub}")
          
          print(f"Sales tax: ${sales_t:.2f}")
          print("")
          print(f"Total: ${Total}")
          print("Thank you for patronizing Savvy mall ")

          print(f"{current_date_and_time:%A %b %d %I:%M:%S %p %Y}")
    except FileNotFoundError as file_err:
      print(file_err)
    except KeyError as key_err:
      print(type(key_err).__name__, key_err)
    except Exception as err:
      print(type(err).__name__, err)



if __name__ == "__main__":
  main()
