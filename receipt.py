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
                count += 1
  
              data[row[key_column_index]] = row
            count += 1
    return data

            
    



def main():
    try:
      num =0
      sub = 0
      product_dict = read_dictionary("products.csv", 0)
      print("Savvy Mall")
      with open("request.csv", 'r') as file:
          data = []
          reader = csv.reader(file)
          print("Your order list")
          for row in reader:
              data.append(row)
              
          for dic in product_dict:
            for lis in data:
              if dic == lis[0]:
                pname = product_dict[dic][1]
                qty = lis[1]
                price = product_dict[dic][2]
                num += int(qty) 
                sub += int(qty ) * float(price)
                print(f"{pname}: {qty}unit @ {price} per unit")
          sales_t = sub * 0.06
          Total = sub + sales_t
          print("")
          print(f"Total number of ordered items: {num}")
          print(f"Subtotal: ${sub}")
          
          print(f"Sales tax: ${sales_t:.2f}")
          print("")
          print(f"Total: ${Total}")
          print("Thank you for patronizing Savvy mall ")
          current_date_and_time = datetime.now()
          print(f"{current_date_and_time:%A %I:%M %p}")
    except FileNotFoundError as file_err:
      print("File not found.")
    except KeyError as key_err:
      print(type(key_err).__name__, key_err)
    except Exception as err:
      print(type(err).__name__, err)



if __name__ == "__main__":
  main()
