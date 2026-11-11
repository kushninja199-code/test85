'''
question
Use the NewsAPI and the requests module to fetch the daily news related to different topics. I
Go to: https://newsapi.org/ and explore the various options to build you application
'''
import requests
apikey="e8cd22dca4141b27fa308863de5d1338"
category=input(str("Enter the catogory you want to get news about (e.g., business, general, entertainment, health, science, sports, technology): "))
language=input(str("Enter the language you want to get news in : "))
country=input(str("enter the country you want to get news about : "))
print(f"Fetching news for category: {category}, language: {language}, country: {country[0:2]}...")
URL = f"https://gnews.io/api/v4/top-headlines?category={category}&lang={language[0:2]}&country={country[0:2]}&max=10&apikey={apikey}"
response = requests.get(URL)
data = response.json()
articles = data.get("articles",[])  # Returns [] if the key is missing, allowing your loops or data processing to continue running smoothly without errors.  
print(f"Latest news about {category}:")
for article in articles[:5]:
    print(f"- {article['title']}")
    print(f"- {article['description']}")