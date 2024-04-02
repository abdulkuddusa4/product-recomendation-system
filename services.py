from functools import reduce
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

csv_data = """
category,name,Regular Price,price,model,stutus,Product code,Key_Features
mobile,Apple iPhone 14 Pro Max 128GB Deep Purple (Singapore),221759,172000,iPhone 14 Pro Max, In Stock,26830,"{""Model"": ""iPhone 14 Pro Max"", ""Display"": ""6.7\"" Super Retina XDR Always-On display"", ""Processor"": ""A16 Bionic chip"", ""Storage"": ""128GB"", ""Camera"": {""Rear"": {""Main"": ""48MP"", ""Wide"": ""12MP"", ""Ultra-Wide"": ""12MP""}, ""Front"": ""12MP""}, ""Features"": [""Dynamic Island"", ""Face ID"", ""eSIM Support""]}"
mobile,Apple iPhone 14 Pro Max 256GB Space Black (Singapore),185699,241600,iPhone 14 Pro Max, In Stock,26528,"{""Model"": ""iPhone 14 Pro Max"", ""Display"": ""6.7\"" Super Retina XDR Always-On display"", ""Processor"": ""A16 Bionic chip"", ""Storage"": ""256GB"", ""Camera"": ""48MP + 12MP + 12MP Rear, 12MP Front"", ""Features"": ""Dynamic Island, Face ID, eSIM Support""}"
mobile,Samsung Galaxy A04e Smartphone (3/32GB),14399,16389,Galaxy A04e,In Stock,30067,"{""Model"": ""Galaxy A04e"", ""Display"": ""6.5-inch HD+ Infinity-V Display"", ""Processor"": ""Mediatek MT6765 Helio P35 (12nm)"", ""Camera"": ""Dual 13+2 MP Rear, 5MP Front"", ""Features"": ""5000mAh Li-Ion Battery""}"
mobile,OPPO A17k Smartphone (3/64GB),"13499","15389",A17k,In Stock,26871,"{""MPN"": ""CPH2471"", ""Model"": ""A17k"", ""Display"": ""6.56\"" HD+ Eye-care Display"", ""Processor"": ""Mediatek MT6765 Helio G35 (12 nm)"", ""Camera"": ""Single 8MP on Rear, 5MP Front"", ""Features"": ""Side-mounted Fingerprint, IPX4""}"
mobile,Samsung Galaxy A03 Core Smartphone (2/32GB),12299,13528,Galaxy A03 Core,In Stock,26129,"{""Model"": ""Galaxy A03 Core"", ""Display"": ""6.5\"" 720 x 1600 (HD+)"", ""Processor"": ""Octa-core (1.6GHz, 1.2GHz)"", ""Camera"": ""8MP Rear, 5MP Front"", ""Features"": ""5000mAh Li-Ion Battery""}"
mobile,Vivo Y02t Smartphone (4/64GB),14999,16499,Y02t,In Stock,29634,"{""Model"": ""Y02t"", ""Display"": ""6.51\"" HD+ Eye Protection Screen"", ""Processor"": ""Mediatek MT6765 Helio P35 (12nm)"", ""Camera"": ""Single 8MP on Rear, 5MP Front"", ""Features"": ""5000mAh Battery, 4GB Extended RAM""}"
mobile,Samsung Galaxy A04 Smartphone (3/32GB),15499,17599,Galaxy A04,In Stock,26133,"{""Model"": ""Galaxy A04"", ""Display"": ""6.5\"" 720 x 1600 (HD+)"", ""Processor"": ""Octa-core (4x2.3 GHz 4x1.8 GHz)"", ""Camera"": ""50MP + 2MP Rear, 5MP Front"", ""Features"": ""5000mAh Li-Ion Battery""}"
mobile,"Vivo Y16 Smartphone (4/64GB)
",16199,18699,Y16,In Stock,26971,"{""Model"": ""Y16"", ""Display"": ""6.51\"" HD+ Halo FullView Screen"", ""Processor"": ""Mediatek MT6765 Helio P35 (12nm)"", ""Camera"": ""Dual 13+2 MP on Rear, 5MP Front"", ""Features"": ""4GB Extended RAM, Side Fingerprint, 5000mAh Battery""}"
mobile,"OPPO A17 Smartphone (4/64GB)
",16099,18699,A17,In Stock,26867,"{""MPN"": ""CPH2477"", ""Model"": ""A17"", ""Display"": ""6.56\"" HD+ Eye-care Display"", ""Processor"": ""Mediatek MT6765 Helio G35 (12 nm)"", ""Camera"": ""Dual 50+2MP on Rear, 5MP Front"", ""Features"": ""Side-mounted Fingerprint, IPX4""}"
mobile,Samsung Galaxy A03s Smartphone (4/64GB),17399,19799,Galaxy A03s,In Stock,26136,"{""Model"": ""Galaxy A03s"", ""Display"": ""6.5\"" 720 x 1600 (HD+)"", ""Processor"": ""Octa-core (4x2.3 GHz 4x1.8 GHz)"", ""Camera"": ""13MP + 2MP + 2MP Rear, 5MP Front"", ""Features"": ""5000mAh Li-Ion Battery""}"
mobile,OPPO A57 Smartphone (4/64GB),18990,20889,A57,In Stock,26942,"{""MPN"": ""CPH2387"", ""Model"": ""A57"", ""Display"": ""6.56\"" HD+ Eye Care Display"", ""Processor"": ""Mediatek MT6765G Helio G35 (12 nm)"", ""Camera"": ""Dual 13+2 MP on Rear, 8MP Front"", ""Features"": ""Side Fingerprint, 33W SUPERVOOC""}"
mobile,"Samsung Galaxy F13 Smartphone (4/64GB)
",22399,25739,Galaxy F13,In Stock,26146,"{""Model"": ""Galaxy F13"", ""Display"": ""6.6\"" FHD+ PLS LCD Touchscreen"", ""Processor"": ""Octa-Core 2GHz, Exynos 850 (8nm)"", ""Camera"": ""Triple 50+5+2 MP on Rear, 8MP Selfie"", ""Features"": ""6000mAh Battery, Side Mounted Fingerprint""}"
mobile,"Vivo Y33s Smartphone (8/128GB)
",23999,26399,Y33s,In Stock,27508,"{""Model"": ""Y33s"", ""Display"": ""6.58\"" FHD+ in-cell Display"", ""Processor"": ""Mediatek MT6769V/CU Helio G80 (12 nm)"", ""Camera"": ""Triple 50+2+2 MP on Rear, 16MP Front"", ""Features"": ""4GB Extended RAM, Side Fingerprint""}"
mobile,Samsung Galaxy A14 Smartphone (4/64GB),22999,26399,Galaxy A14,In Stock,30071,"{""Model"": ""Galaxy A14"", ""Display"": ""6.6-inch FHD+ (1080 x 2408)"", ""Processor"": ""Mediatek MT6769 Helio G80 (12 nm)"", ""Camera"": ""Triple 50+5+2MP Rear, 13MP Front"", ""Features"": ""5000mAh Li-Ion Battery""}"
mobile,Vivo Y36 Smartphone (8/128GB),26999,29699,Y36,In Stock,29684,"{""Model"": ""Y36"", ""Display"": ""6.64\"" FHD+ 90 Hz Display"", ""Processor"": ""Qualcomm SM6225 Snapdragon 680 4G (6 nm)"", ""Camera"": ""Dual 50+2 MP on Rear, 16MP Front"", ""Features"": ""44W Fast Charging, Side Fingerprint, 4GB Extended RAM""}"
mobile,Vivo V23e Smartphone (8/128GB),27990,30789,V23e,In Stock,27712,"{""Model"": ""V23e"", ""Display"": ""6.44\"" FHD+ AMOLED Display"", ""Processor"": ""Mediatek Helio G96 (12 nm)"", ""Camera"": ""Triple 64+8+2 MP on Rear, 50MP Front"", ""Features"": ""In-display Fingerprint, 44W FlashCharge""}"
mobile,"Samsung Galaxy F13 Smartphone (6/128GB)
",26999,31899,Galaxy F13,In Stock,26147,"{""Model"": ""Galaxy F13"", ""Display"": ""6.6\"" FHD+ PLS LCD Touchscreen"", ""Processor"": ""Octa-Core 2GHz, Exynos 850 (8nm)"", ""Camera"": ""Triple 50+5+2 MP on Rear, 8MP Selfie"", ""Features"": ""6000mAh Battery, Side Mounted Fingerprint""}"
mobile,Apple iPhone 14 Pro 128GB Deep Purple (Dual SIM),115000,132500,iPhone 14 Pro,In Stock,26482,"{""Model"": ""iPhone 14 Pro"", ""Display"": ""6.1\"" Super Retina XDR Always-On display"", ""Processor"": ""A16 Bionic chip"", ""Storage"": ""128GB"", ""Camera"": ""48MP + 12MP + 12MP Rear, 12MP Front"", ""Features"": ""Dynamic Island, Face ID, Dual SIM""}"
mobile,Realme 9 Pro 5G Smartphone (8/128GB),29999,33000,realme 9 Pro 5G,In Stock,27784,"{""Model"": ""realme 9 Pro 5G"", ""Display"": ""6.6\"" FHD+ 120Hz Ultra Smooth Display"", ""Processor"": ""Qualcomm SM6375 Snapdragon 695 5G (6 nm)"", ""Camera"": ""Triple 64+8+2 MP on Rear, 16MP Front"", ""Features"": ""Side Fingerprint, 33W Dart Charge""}"
mobile,Vivo V25e Smartphone (8/128GB),31999,35199,V25e,In Stock,27713,"{""Model"": ""V25e"", ""Display"": ""6.44\"" FHD+ 90Hz AMOLED Display"", ""Processor"": ""Mediatek MT8781 Helio G99 (6nm)"", ""Camera"": ""Triple 64+2+2 MP on Rear, 32MP Front"", ""Features"": ""In-display Fingerprint, 44W FlashCharge""}"
mobile,Samsung Galaxy A23 LTE Smartphone (6/128GB),31299,35749,Galaxy A23 LTE,In Stock,26148,"{""Model"": ""Galaxy A23 LTE"", ""Display"": ""6.6\"" FHD+ PLS TFT LCD 90Hz, V-Cut Display"", ""Processor"": ""Qualcomm SM6225 Snapdragon 680 4G (6 nm)"", ""Camera"": ""Quad 50+5+2+2 MP on Rear, 8MP Selfie"", ""Features"": ""Side Mounted Fingerprint, 25W Fast Charging""}"
mobile,OPPO Reno8 T Smartphone (8/128GB),32990,36289,Reno8 T,In Stock,27313,"{""Model"": ""Reno8 T"", ""Display"": ""6.43\"" FHD+ 90Hz AMOLED Eye-Care Display"", ""Processor"": ""Mediatek MT8781 Helio G99 (6nm)"", ""Camera"": ""Triple 100+2+2 MP on Rear, 32MP Front"", ""Features"": ""In-Display Fingerprint, 33W SUPERVOOC""}"
mobile,OPPO F21 Pro 5G Smartphone (8/128GB),34900,38390,F21 Pro 5G,In Stock,27312,"{""Model"": ""F21 Pro 5G"", ""Display"": ""6.43\"" FHD+ Punch-hole AMOLED Screen"", ""Processor"": ""Qualcomm SM6375 Snapdragon 695 5G (6 nm)"", ""Camera"": ""Triple 64+2+2 MP on Rear, 16MP Front"", ""Features"": ""IPX4, In-Display Fingerprint, 33W SUPERVOOC""}"
mobile,Realme GT Master Edition Smartphone (8/128GB),34990,38489,GT Master Edition,In Stock,27788,"{""Model"": ""GT Master Edition"", ""Display"": ""6.43\"" FHD+ 120Hz Super AMOLED Display"", ""Processor"": ""Qualcomm SM7325 Snapdragon 778G 5G (6 nm)"", ""Camera"": ""Triple 64+8+2 MP on Rear, 32MP Front"", ""Features"": ""In-display Fingerprint, 65W SuperDart Charge""}"
mobile,Samsung Galaxy F23 5G Smartphone (6/128GB),33999,38499,Galaxy F23 5G,In Stock,26150,"{""Model"": ""Galaxy F23 5G"", ""Display"": ""6.6\"" FHD+ TFT LCD 120Hz, Infinity-U Display"", ""Processor"": ""Qualcomm SM7225 Snapdragon 750G 5G (8 nm)"", ""Camera"": ""Triple 50+8+2 MP on Rear, 8MP Selfie"", ""Features"": ""Power Cool Tech, Side Fingerprint, 25W Fast Charging""}"
tv,"Starex 17NB 17"" Wide LED Television",5200,5720,17NB,In Stock,18083,"{""Model"": ""17NB"", ""Design"": ""Slim Design TV Body"", ""Size"": ""17 inch (Wide) Display"", ""Resolution"": ""1920 x 1080 LED"", ""Warranty"": ""1 Year""}"
tv,"Starex 19"" NB Wide Led TV Monitor",7800,8580,Starex 19 NB,In Stock,11232,"{""Model"": ""Starex 19 NB"", ""Design"": ""Slim Design TV Body"", ""Size"": ""19 inch (Wide) Display"", ""Resolution"": ""1920 x 1080 LED"", ""Warranty"": ""1 Year""}"
tv,"Smart SEL-24L22KS 24"" HD Basic LED Television",11000,12100,SEL-24L22KS,In Stock,24887,"{""Model"": ""SEL-24L22KS"", ""Resolution"": ""HD (1360x768) Resolution"", ""Ports"": {""HDMI"": 2, ""USB"": 1, ""VGA"": 1, ""Audio Out"": 1}, ""DisplayLanguage"": ""Multiple"", ""PictureModes"": [""Bright"", ""Standard"", ""Soft"", ""User""]}"
tv,"Starex 32"" Wide Led Tv Monitor",12000,13200,Starex 32 Wide,In Stock,11235,"{""Model"": ""Starex 32 Wide"", ""Features"": ""Dynamic Contrast Ratio, 32-Inch Display with HD Resolution, Hi Quality Built In Speaker"", ""Warranty"": ""1 Year""}"
tv,"Smart SEL-32L22KS 32"" HD Basic LED Television",14000,15400,SEL-32L22KS,In Stock,24884,"{""Model"": ""SEL-32L22KS"", ""Resolution"": ""HD (1360x768) Resolution"", ""Ports"": {""HDMI"": 2, ""USB"": 1, ""Audio Out"": 1}, ""Material"": ""Plastic Fiber"", ""PictureModes"": [""Dynamic"", ""Standard"", ""Soft"", ""User""]}"
tv,Haier H32D2M 32 Inch Miracast HD Non-Smart LED Television,15500,17050,H32D2M,In Stock,22450,"{""Model"": ""H32D2M"", ""Display"": ""32 inch HD(1366 x 768) LED Display"", ""Input"": {""HDMI"": 3, ""USB"": 1, ""Audio Ports"": 1}, ""ResponseTime"": ""20ms"", ""Features"": ""Miracast Screen Mirroring""}"
tv,"Samsung 32N4010 32"" Basic HD LED Television",16200,18150,32N4010,In Stock,22099,"{""Model"": ""32N4010"", ""Display"": ""32-inch HD (1366 x 768)"", ""Audio"": {""Speaker"": ""2CH Speaker"", ""Wattage"": ""20W (RMS)""}, ""Ports"": {""HDMI"": 2, ""USB"": 1}, ""Features"": ""Wide Colour Enhancer""}"
tv,JVCO J9TS 32 Inch HD Android Voice Control Smart LED Television,17500,19000,J9TS,In Stock,27460,"{""Model"": ""J9TS"", ""Resolution"": ""HD (1360x768)"", ""RAM"": ""2 GB"", ""ROM"": ""16 GB"", ""OperatingSystem"": ""Android 10"", ""Features"": ""Google Assistance""}"
tv,"LG 32LK510B 32"" HD LED Television",19700,22000,32LK510B,In Stock,20341,"{""Model"": ""32LK510B"", ""Display"": ""32\"" HD (1366 x 768) @50Hz LED-Backlit Display"", ""Features"": ""Dynamic Color & Virtual Surround Sound, Immersive home entertainment, Sophisticated inside and out""}"
tv,Haier H32K66G 32 Inch Bezel Less HD Android Smart LED Television,21000,23100,H32K66G,In Stock,26992,"{""Model"": ""H32K66G"", ""Display"": ""32\"" HD(1366 x 768) LED Display"", ""Features"": {""Remote"": ""Voice Control Remote"", ""Input"": {""HDMI"": 3, ""USB"": 2}, ""Voice Assistant"": ""Google Voice Assistant"", ""Audio"": ""Dolby Digital Decoding""}}"
tv,OnePlus 32 Y1 Y Series 32-Inch HD Smart Android LED Television,22000,25850,Y1,In Stock,24004,"{""Model"": ""Y1"", ""DisplaySize"": ""32 inches"", ""Resolution"": ""1366 × 768 pixel"", ""RAM"": ""1GB"", ""ROM"": ""8GB"", ""Audio"": ""Dolby Digital Dolby Audio""}"
tv,SINGER S32 SLE32E3AGOTV 32 Inch HD Android Google Television,22000,24000,S32 SLE32E3AGOTV,In Stock,27434,"{""MPN"": ""SRTV-SLE32E3AGOTV"", ""Model"": ""S32 SLE32E3AGOTV"", ""Resolution"": ""HD (1366 x 768)"", ""OperatingSystem"": ""Latest Official Android 11 OS"", ""Features"": {""Chromecast"": ""Built-in"", ""Audio"": ""Dolby Digital Sound""}}"
tv,Xiaomi Mi A2 L32M7-EAUKR 32-Inch Smart Android HD LED TV with Netflix Global Version,23500,26180,Mi A2 L32M7-EAUKR,In Stock,25332,"{""MPN"": ""L32M7-EAUKR"", ""Model"": ""Mi A2 L32M7-EAUKR"", ""Resolution"": ""32\"" HD (1,366 x 768)"", ""Processor"": {""CPU"": ""CA55 × 4"", ""GPU"": ""Mali G31 MP2""}, ""RAM"": ""1.5GB"", ""Storage"": ""8GB"", ""AudioSupport"": [""Dolby Audio"", ""DTS-X"", ""DTS"", ""Virtual:X Sound""]}"
tv,"Haier H43K6FG 43"" FHD Android Bezel-Less Smart LED Television",31000,34100,H43K6FG,In Stock,22452,"{""Model"": ""H43K6FG"", ""Display"": ""43\"" Full HD (1920 x 1080) Display"", ""Features"": {""Remote"": ""Voice Control Remote"", ""Ports"": {""HDMI"": 3, ""USB"": 2}, ""OperatingSystem"": ""Android 11""}}"
tv,"Smart SEL-43S22KKS 43"" FHD Voice Control Android LED Television",30900,34100,SEL-43S22KKS,In Stock,24879,"{""Model"": ""SEL-43S22KKS"", ""Resolution"": ""FHD (1920X1080) Resolution"", ""Ports"": {""HDMI"": 2, ""USB"": 2, ""Audio Out"": 1}, ""RAM"": ""1GB"", ""ROM"": ""8GB"", ""SupportedApps"": [""PlayStore"", ""App Store"", ""Netflix"", ""YouTube"", ""Facebook"", ""Toffee""]}"
tv,OnePlus 43 Y1 Y Series 43-Inch HD Smart Android LED Television,29900,34870,Y1G,In Stock,24032,"{""Model"": ""Y1G"", ""DisplaySize"": ""43 inches"", ""Resolution"": ""1920 × 1080 pixel"", ""RAM"": ""1GB"", ""ROM"": ""8GB"", ""Audio"": ""Dolby Digital Dolby Audio""}"
tv,SINGER Primax S50-SLE50U5000GOTV 50 Inch 4K Android Google Television,58000,64990,Primax S50-SLE50U5000GOTV,In Stock,31151,"{""Model"": ""Primax S50-SLE50U5000GOTV"", ""Resolution"": ""4K (3840 X 2160)"", ""RAM"": ""2GB"", ""ROM"": ""16GB"", ""Features"": {""Chromecast"": ""Built-in"", ""Audio"": ""Dolby Audio (2x10W Speaker)""}}"
tv,SINGER E43 SLE43A5000GOTV 43 Inch Full HD Android Smart LED Television,34000,37490,SRTV-SLE43A5000GOTV,In Stock,27423,"{""MPN"": ""SRTV-SLE43A5000GOTV"", ""Model"": ""E43 SLE43A5000GOTV"", ""Resolution"": ""Full HD (1920x1080)"", ""RAM"": ""1.5GB"", ""ROM"": ""8GB"", ""Features"": {""Chromecast"": ""Built-in"", ""Audio"": ""Dolby Audio (2x10W Speaker)""}}"
tv,SINGER Primax S43-SLE43U5000GOTV 43 Inch 4K Android Google Television,42000,46000,Primax S43-SLE43U5000GOTV,In Stock,31144,"{""Model"": ""Primax S43-SLE43U5000GOTV"", ""Resolution"": ""4K (3840 X 2160)"", ""RAM"": ""2GB"", ""ROM"": ""16GB"", ""Features"": {""Chromecast"": ""Built-in"", ""Audio"": ""Dolby Audio (2x10W Speaker)""}}"
tv,SINGER Primax S55-SLE55U5000GOTV 55 Inch 4K Android Google Television,70000,79990,Primax S55-SLE55U5000GOTV,In Stock,31154,"{""Model"": ""Primax S55-SLE55U5000GOTV"", ""Resolution"": ""4K (3840 X 2160)"", ""RAM"": ""2GB"", ""ROM"": ""16GB"", ""Features"": {""Chromecast"": ""Built-in"", ""Audio"": ""Dolby Audio (2x10W Speaker)""}"
tv,Haier H43K66UG 43 Inch Bezel Less 4K Android Smart LED Television,36000,39600,H43K66UG,In Stock,27005,"{""Model"": ""H43K66UG"", ""Display"": ""43\"" 4K HDR UHD (3840 x 2160)"", ""Features"": {""Remote"": ""Voice Control Remote"", ""Input"": {""HDMI"": 4, ""USB"": 2}, ""Chromecast"": ""Google Chromecast"", ""Audio"": ""Dolby Digital Decoding""}}"
tv,Samsung 43T5400 43-Inch Full HD Smart Led Television,36300,39600,43T5400,In Stock,25454,"{""Model"": ""43T5400"", ""Display"": ""43\"" HD (1920 x 1080p)"", ""Processor"": ""Quad-Core"", ""Technology"": ""Ultra Pix Color Technology"", ""Ports"": {""HDMI"": 3, ""USB"": 1}}"
tv,ROWA 43S52 43 Inch Full HD Android Smart LED Television,31500,40150,43S52,In Stock,27359,"{""Model"": ""43S52"", ""Resolution"": ""Full HD (1920x1080)"", ""RAM"": ""1GB"", ""ROM"": ""8GB"", ""OperatingSystem"": ""Android 11"", ""Features"": ""Chromecast Built-in""}"
tv,JVCO DK5L 50 Inch 4K Single Glass Android Voice Control Smart LED Television,37000,40700,DK5L,In Stock,27465,"{""Model"": ""DK5L"", ""Resolution"": ""4K (3840 x 2160)"", ""RAM"": ""2 GB"", ""ROM"": ""16 GB"", ""OperatingSystem"": ""Android 10"", ""Features"": ""Google Assistance""}"

"""

col_description = {
    'category': "It's a string describing category of the prodcut",
    'name': "It's a string representing product name",
    'Regular Price': "It's number describing the Actual price of the product",
    'price': "It's a number describing the discount price of the product ",
    'model': "It's a string describing the model of the product",
    'status': "it's a string describing if the product is available in stock.",
    "Product code": "It's a unique integer describing product code",
    "Key_Features": "It's a json string describing various key featuers of the product."
                    "Each key in the json describes a key feature."
}

query_prompt = """
Warning: Your response format must follow the following format.
```
{{
  "query": [
      "query_string1",
       "query_string2",
       ...
    ]
}}
```
for example:
```
{{
  "query": [
    "MY_DF[MY_DF['col1'] == 'xyz']",
    "MY_DF[MY_DF['col2'] == 'xyz']"
    ]
}}
```
NOTE: do not use this example. It is just to explain the logic to you.

if the user's question is not related to the topics of the dataframe or You
do not understand the user's query, Just put null instead of any query.

example:
```

{{
  "query": null
}}
```


I have  created a pandas dataframe object MY_DF
It has the following column:
{column_description}

Each row of the object contains info about a particular question.

Now your are an assistant.
Your job is to understand the user question and generate a list of tabular queries that can
be run on the MY_DF object.

Plz Note that, You may want to make the queries first column different in each query.

for example:
  if a user asks about a product "A".

the word "A" may exists on more than one column (colx, coly, colz etc).
So you may need to make more than one query to make sure that you query iterate over all
possible column to get the best result for user.

You may also want to make a query what matches string very losely.

for example:
  1. "mobile phone" should be match with "mobile" or "phone" or "mobilephone"
  2. "SINGER Primax S55-SLE55U5000GOTV 55 Inch 4K Android Google Television" 
      should be match with "singer" or "televition" or "55 inch Android" tv 
      because they all are substring of it.
remember the dataframe object is "MY_DF"



WARNING:  
1. You have to make a valid pandas tabular query.
2,   Do not make a query on a column that does'nt exists.
3. You're response must follow the given format.

"""

service_prompt_v_0_1 = """
Your are a helpfull assistant who will help a people find their needs.

The user asked the following question:
``` {user_query} ```

We retrieved the following data from database enclosed in ``` ```based on the user_query:
``` {data} ```

if the data is empty, generate the response based on the context.
else describe the data retrieved from database to the user.

  Note:
    1. plz make your answer good looking.
    2. use good listing and indentation.
    3. use line break if a line is too long if more than 15 word.
"""

fallback_prompt = """
We couldn't find any data from database.
so, generate response based on the chat_history or context.
"""

CONDENSE_QUESTION_PROMPT_TEMPLATE = """
Given the following conversation and a follow up question, rephrase the follow up question 
to be a standalone question, in its original language.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""


def formatted_column_description(pdf_obj, description):
    st = ""
    for i, col in enumerate(pdf_obj.columns.to_list(), 1):
        try:
            st += f"  {i}. `{col}`({description[col]}).\n"
        except KeyError as e:
            st += f"  {i}. `{col}`.\n"
    return st


import pandas as pd
from io import StringIO
import json, openai


# Sample CSV-formatted string
# csv_data = """Name,Age,Location
# John,25,New York
# Alice,30,Los Angeles
# Bob,22,Chicago
# """

# Create a file-like object from the CSV data
csv_stringio = StringIO(csv_data)

# Read the data into a Pandas DataFrame
MY_DF = pd.read_csv(csv_stringio)


def get_agent_response(user_query=None):
    print("function called........")
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = [
            # {
            #     "role": "system",
            #     "content": query_prompt.format(
            #         column_description=formatted_column_description(MY_DF, col_description)
            #     )
            # },
        ]
    if user_query is None:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                         {
                             "role": "system",
                             "content": "You are product salesman."
                         }
                     ] + st.session_state.get('chat_history'),
            max_tokens=50
        )
        response = completion.choices[0].message.content
        # st.session_state.get('chat_history').append({
        #     "role": "assistant",
        #     "content": response
        # })
        return response

    if not (
            (chat_history := st.session_state.get('chat_history'))
            and chat_history[-1]['role'] == "user"
            and chat_history[-1]['content'] == user_query
    ):
        st.session_state.get('chat_history').append(
            {
                "role": "user",
                "content": user_query
            }
        )

    # GENERATING THE PANDAS QUERY
    # print(st.session_state.get('chat_history'))
    # condense_qa_prompt = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": CONDENSE_QUESTION_PROMPT_TEMPLATE.format(
    #                 chat_history=st.session_state.get('chat_history'),
    #                 question=user_query
    #             )
    #         }
    #     ]
    # ).choices[0].message.content
    # print("condense qa: ", condense_qa_prompt)
    #
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": query_prompt.format(
                    column_description=formatted_column_description(MY_DF, col_description))
            },
            {
                "role": "user",
                "content": user_query  # user_query
            }
        ]  # + st.session_state.get('chat_history'),
        # I phone stream=True,
    )
    json_response = completion.choices[0].message.content
    print("json: ", json_response)
    # print(st.session_state.get('chat_history'))
    # return
    try:
        queries = json.loads(json_response)['query']
    except json.JSONDecodeError:
        return json_response
    if queries:
        datasets = []
        for query in queries:
            try:
                datasets.append(eval(query))
            except Exception as e:
                print(f"warning: error running query: {query}"
                      f"throws: {e}")
        if not datasets:
            data = None
        elif len(datasets) == 1:
            data = datasets[0]
        else:
            data = reduce(
                lambda a, b: pd.concat([a, b]),
                datasets
            )
            if isinstance(data, MY_DF.__class__):
                data.reset_index(drop=True, inplace=True)
    else:
        data = None
    print(data)
    print(st.session_state.get('chat_history'))
    completion = openai.ChatCompletion.create(

        model="gpt-3.5-turbo",
        messages=[
                     {
                         "role": "system",
                         "content": service_prompt_v_0_1.format(user_query=user_query, data=data)
                     }
                 ] + st.session_state['chat_history']
        # stream=True,
    )
    response = completion.choices[0].message.content
    st.session_state.get('chat_history').append(
        {
            "role": "assistant",
            "content": response
        }
    )
    return response
