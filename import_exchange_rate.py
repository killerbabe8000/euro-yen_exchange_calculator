import requests

link1 = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-jpy.en.html"

def get_exchange_rate(link1):



    # ECB-Kurs

    response = requests.get(link1)

    if response.status_code == 200:
        if "rateLatestInverse" in response.text:
            phrase_start1 = response.text.find("rateLatestInverse")
            phrase_end1 = response.text.find(";", phrase_start1)
            extracted_text = response.text[phrase_start1:phrase_end1].strip()
            clean_extracted_text = extracted_text.replace("rateLatestInverse=", "").replace("'", "")
            exchange_value = float(clean_extracted_text)
            if "dateLatestInverse" in response.text:
                phrase_start2 = response.text.find("dateLatestInverse")
                phrase_end2 = response.text.find(";", phrase_start2)
                extracted_date = response.text[phrase_start2:phrase_end2].strip()
                clean_extracted_date = extracted_date.replace("dateLatestInverse=", "").replace("'", "")
                return exchange_value, clean_extracted_date
        else:
            print("Could not acquire currency exchange-rate from the website.")
    else:
        print(f"Website is not working. Errorcode: {response.status_code}")
        


exchange_value = get_exchange_rate(link1) 
