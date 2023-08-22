# %%
import openai
from selenium import webdriver

# Set up your OpenAI API key
openai_api_key = ''
openai.api_key = openai_api_key

def generate_response(user_input, content):
    prompt = f"You: {user_input}\nURL: {url}\nContent from webpage: {content}\nGPT-3 Chatbot:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100  # Adjust as needed
    )
    return response.choices[0].text

# Set up the Selenium driver (update the path to your ChromeDriver accordingly)
driver = webdriver.Chrome(executable_path="chromedriver.exe")

# Open a new tab
driver.execute_script("window.open('about:blank', '_blank');")
driver.switch_to.window(driver.window_handles[1])

# Navigate to the webpage you want to scrape in the new tab
url = 'https://example.com'
driver.get(url)

print("GPT-3 Chatbot: Hello! How can I assist you today?")

# Loop to keep the chatbot running
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("GPT-3 Chatbot: Goodbye!")
        break

    # Extract the content you want (customize this part as needed)
    content = driver.find_element_by_tag_name('body').text

    # Generate the response using the user input and content
    response = generate_response(user_input, content)
    print("GPT-3 Chatbot:" + response)

# Close the driver
driver.quit()



