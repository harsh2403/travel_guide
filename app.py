from flask import Flask, render_template, request
import openai
import os


app = Flask(__name__)

# Set up the OpenAI API key
openai.api_key = "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"



@app.template_filter()
def get_length_and_text(s):
    return len(s), s

# Define the main route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        num_days = request.form['num_days']
        num_days = int(num_days)  # Convert num_days to an integer
        # Use OpenAI's GPT-3 to generate an itinerary for the specified location and number of days
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Create an itinerary for {num_days} days in {location} with atleast 100 words for each day",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        itinerary = response.choices[0].text
        #print(f"itinerary: {itinerary}")
        return render_template('index.html', itinerary=itinerary, num_days=num_days)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
