# SmartDietSearch
## How to run the code:

This code is a FastAPI-based application that reads a CSV file ("Final_Data.csv"), 
processes the data based on user input, and returns a JSON response. Here are the steps to run the application:

1. Clone the repository on your local machine.
2. Install the necessary packages and dependencies. You can do this by running the following command in the terminal: pip install -r requirements.txt
3. Make sure the CSV file "Final_Data.csv" is in the same directory as the code file.
4. Start the server by running the following command: uvicorn main:app --reload in your terminal.
5. The application should now be running on your local machine at http://127.0.0.1:8000.
6. You can test the API endpoint by sending a POST request to http://127.0.0.1:8000/getInformation. The request body should contain a JSON object with the following keys:
7. SearchedString (string): The string to search for.
8. Type (string): The type of search to perform ("GoogleTrends" or "Nutrients").
9. The response will be a JSON object containing the results of the search.
