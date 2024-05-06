# euro-yen_exchange_calculator
This script provides a straightforward solution for converting between Euro (EURO) and Japanese Yen (JPY) using real-time exchange rates sourced from the European Central Bank (ECB) website. It also offers the option to display the current exchange rate.

Simply execute the script, and it will guide you through the conversion process.
  
  
How to use:    
  Ensure you have Python installed on your system. This script relies on internet connectivity as well as the module 'requests' to fetch the latest exchange rates from the ECB website.

  To install the module 'requests' simply enter 'pip install requests' into your console.

  To use my program, there are two options that you can choose from:
  
  Option 1: Separate Files:  
    Exchange Rate Function File (import_exchange_rate.py):  
      This file contains the function responsible for pulling the exchange rate from the ECB website.
      Ensure that import_exchange_rate.py is placed in the same directory as the main script file.  
    Main Script File (euro_yen_calculator.py):  
      This file imports the function (as well as the link of the website), from import_exchange_rate.py,  that pulls the exchange rate from the ECB website.
      Run euro_yen_converter.py to execute the conversion script.
      Follow the prompts to convert between Euro and Yen and to view the current exchange rate.

  Option 2: Merged Files  
    Single Script File (euro_yen_converter_merged.py):  
      This file contains both the function for requesting the exchange rate and the currency conversion.
      Run euro_yen_converter_merged.py directly to execute the script.
      Follow the prompts to convert between Euro and Yen and to view the current exchange rate.

  
If you have any questions, suggestions, or recommendations, please feel free to reach out.
Happy converting!




