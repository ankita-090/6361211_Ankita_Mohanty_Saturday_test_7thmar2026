from time import sleep
from selenium.webdriver import Chrome , ChromeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ********** QUESTION 1 **************
# Write a script to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Books
# Add first book to cart
# Click Shopping Cart
# Verify the product is present in the cart.
#
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
sleep(3)
driver.find_element(By.LINK_TEXT,"Books").click()
sleep(2)
driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[1]").click()
sleep(2)
driver.find_element(By.LINK_TEXT,"Shopping cart").click()
sleep(2)
product=driver.find_element(By.XPATH,"//td[@class='product']/a")
print("Product is present in cart" if product.is_displayed() else "Product not found")
driver.quit()
#
# ********** QUESTION 2 **************
# Write a Selenium script to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Electronics
# Use XPath contains() to locate the Cell Phones category
# Click it.
#
driver=Chrome()
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
sleep(3)
driver.find_element(By.LINK_TEXT,"Electronics").click()
sleep(3)
driver.find_element(By.XPATH,"//div[@class='sub-category-item']//a[contains(text(),'Cell phones')]").click()
sleep(2)
driver.quit()
#
# ********** QUESTION 3 **************
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/dynamic_loading/1
# Click Start
# Wait until the Hello World text appears
# Print the text.
#
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver=Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.find_element(By.XPATH,"//button").click()
text=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"finish")))
print(text.text)
driver.quit()
#
# ********** QUESTION 4 **************
# Write a script to:
# Open https://the-internet.herokuapp.com/dynamic_controls
# Click Remove
# Wait until Add button becomes clickable
# Click Add
#
driver=Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='Remove']").click()
wait=WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Add']"))).click()
driver.quit()
#
# ********** QUESTION 5 **************
# Write a Selenium script to:
# Open https://demoqa.com/select-menu
# Select "Group 2, option 1" from the Select Value dropdown
# Verify the selected value.
#
driver=Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
sleep(3)
driver.find_element(By.ID,"withOptGroup").click()
sleep(2)
driver.find_element(By.XPATH,"//div[text()='Group 2, option 1']").click()
sleep(2)
value=driver.find_element(By.XPATH,"//div[@id='withOptGroup']//div[contains(@class,'singleValue')]").text
print(value)
driver.quit()
#
# ********** QUESTION 6 **************
# Write a Selenium script to:
# Open https://demoqa.com/select-menu
# Scroll to Standard multi select
# Select Volvo, Saab, and Opel
# Print all selected options.
#
driver = Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
sleep(3)
multi = driver.find_element(By.ID, "cars")
driver.execute_script("arguments[0].scrollIntoView(true);", multi)
sleep(2)
select = Select(multi)
select.select_by_visible_text("Volvo")
sleep(1)
select.select_by_visible_text("Saab")
sleep(1)
select.select_by_visible_text("Opel")
sleep(2)
values = select.all_selected_options
print("Selected options:")
for v in values:
    print(v.text)
driver.quit()
#
# ********** QUESTION 7 **************
# Write a Selenium script to:
# Open https://demoqa.com/menu/
# Hover over Main Item 2
# Hover over SUB SUB LIST
# Click Sub Sub Item 1
#
driver = Chrome()
driver.get("https://demoqa.com/menu/")
driver.maximize_window()
sleep(3)
actions = ActionChains(driver)
main_item = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
actions.move_to_element(main_item).perform()
sleep(2)
sub_sub_list = driver.find_element(By.XPATH, "//a[contains(text(),'SUB SUB LIST')]")
actions.move_to_element(sub_sub_list).perform()
sleep(2)
sub_sub_item1 = driver.find_element(By.XPATH, "//a[text()='Sub Sub Item 1']")
sub_sub_item1.click()
sleep(2)
driver.quit()
#
# ********** QUESTION 8 **************
# Write a Selenium script to:
# Open https://demoqa.com/droppable
# Drag Drag me element
# Drop it on Drop here
# Verify text changes to Dropped!
#
driver = Chrome()
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
sleep(3)
actions = ActionChains(driver)
drag = driver.find_element(By.ID, "draggable")
drop = driver.find_element(By.ID, "droppable")
actions.drag_and_drop(drag, drop).perform()
sleep(2)
result = driver.find_element(By.ID, "droppable").text
print("Result:", result)
if result == "Dropped!":
    print("Drag and Drop successful")
else:
    print("Drag and Drop failed")
sleep(2)
driver.quit()
#
# ********** QUESTION 9 **************
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/javascript_alerts
# Click JS Confirm
# Accept the alert
# Verify result text shows You clicked: Ok
#
driver = Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
sleep(3)
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
sleep(2)
result = driver.find_element(By.ID, "result").text
print("Result:", result)
if result == "You clicked: Ok":
    print("Test Passed")
else:
    print("Test Failed")
sleep(2)
driver.quit()
#
# ********** QUESTION 10 **************
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/upload
# Upload a file from local system
# Click Upload
# Verify uploaded file name.
#
driver = Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
sleep(3)
file_path = r"C:\Users\Ankita\OneDrive\Documents\pagetsx.txt"
driver.find_element(By.ID, "file-upload").send_keys(file_path)
sleep(2)
driver.find_element(By.ID, "file-submit").click()
sleep(2)
uploaded_file = driver.find_element(By.ID, "uploaded-files").text
print("Uploaded file:", uploaded_file)
if uploaded_file == "testfile.txt":
    print("File upload successful")
else:
    print("File upload failed")
sleep(2)
driver.quit()
#
# ********** QUESTION 11 **************
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/download
# Download any file
# Verify the file is downloaded in the Downloads folder using Python.
#
import os
driver = Chrome()
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
sleep(3)
file_element = driver.find_element(By.XPATH, "//div[@class='example']/a[1]")
file_name = file_element.text
file_element.click()
print("Downloading:", file_name)
sleep(5)
download_path = r"D:\Downloads"
file_path = os.path.join(download_path, file_name)
if os.path.exists(file_path):
    print("Download successful:", file_name)
else:
    print("Download failed")
driver.quit()
#
# ********** QUESTION 12 **************
# Write a script to:
# Open https://demowebshop.tricentis.com
# Add any two products from Books
# Navigate to Shopping Cart
# Verify total number of products added is 2.
#
driver = Chrome()
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
sleep(3)
driver.find_element(By.LINK_TEXT, "Books").click()
sleep(3)
driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[1]").click()
sleep(2)
driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[2]").click()
sleep(2)
driver.find_element(By.LINK_TEXT, "Shopping cart").click()
sleep(3)
products = driver.find_elements(By.XPATH, "//table[@class='cart']//tr[contains(@class,'cart-item-row')]")
count = len(products)
print("Total products in cart:", count)
if count == 2:
    print("Test Passed")
else:
    print("Test Failed")
sleep(2)
driver.quit()
#
# ********** QUESTION 13 **************
# Write a Selenium script that:
# Open https://demowebshop.tricentis.com
# Navigate to Books
# Add all books priced below $20 to cart
#
driver = Chrome()
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
sleep(3)
driver.find_element(By.LINK_TEXT, "Books").click()
sleep(3)
books = driver.find_elements(By.XPATH, "//div[@class='product-item']")
count = 0
for i in range(len(books)):
    books = driver.find_elements(By.XPATH, "//div[@class='product-item']")
    book = books[i]
    try:
        price_text = book.find_element(By.CLASS_NAME, "actual-price").text
        price = float(price_text.replace("$", ""))
        if price < 20:
            add_btn = book.find_element(By.XPATH, ".//input[contains(@value,'Add to cart')]")
            add_btn.click()
            count += 1
            print("Added book with price:", price)
            sleep(2)
    except:
        print("Skipped a book (no button or issue)")
        continue
print("Total books added:", count)
sleep(2)
driver.quit()
#
# Write the steps to read the data from excel
#
import xlrd
wb = xlrd.open_workbook("sel_test.xlsx")
sheet = wb.sheet_by_index(0)
for i in range(sheet.nrows):
    print(sheet.row_values(i))
#
# Write the syntax for the xpath to locate the elements using
# 	*	attributes
driver.find_element(By.XPATH,"//tag[@attribute='value']")
# 	*	text
driver.find_element(By.XPATH,"//tag[text()='value']")
# 	*	group indexing
driver.find_element(By.XPATH,"(//tag[@attribute='value'])[1]")
# 	*	contains
driver.find_element(By.XPATH,"//tag[contains(@attribute,'value')]")
