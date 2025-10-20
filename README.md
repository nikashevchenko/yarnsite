# Yarn World
***The main idea*** is to create a specialized and user-friendly online yarn catalog that meets the needs of both beginners and experienced crafters.
The website is not just a store, but also an informational resource where the process of choosing yarn is as transparent and efficient as possible.
There will be a page listing all yarns, with a search bar allowing users to filter by brand name or yarn type (e.g., wool, cotton, etc.).
#### Users will also be able to sort results by:
* lowest price,
* highest price,
* popularity,
* newest arrivals.
#### Each yarn will have its own detailed page containing:
* price,
* description,
* stock status (availability),
* a table of characteristics,
* product photos,
* an example of the yarn used in a finished item, showing how it looks in real use.
### API Description

All endpoints exchange data in JSON format.
For each endpoint, a brief description of its purpose is provided, along with the Request Method, Request Body/Parameters (if applicable), and the Response Status and Response Body (if applicable).
[Rest API](https://docs.google.com/spreadsheets/d/1m7OdmJv0rojxWQyFBp6YMk7nsoO9Mqy50FzeB4d1zZ8/edit?usp=sharing) 
### Data Base 
![image](https://github.com/nikashevchenko/yarnsite/blob/5ad251a202913eda6e15b1a364b58ab8d52d2f07/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-10-07%20205011.png)
 

  

## How to start the project

To start this project locally, follow these steps.

1.  **Clone the repository:**
```bash
git clone https://github.com/nikashevchenko/yarnsite.git
cd yarnsite
```

2.  **Create and activate a virtual environment:**
* For **Windows**:
```bash
        python -m venv venv
        venv\Scripts\activate
        ```
* For **macOS and Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
```bash
python manage.py migrate
```

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

The project is available in your browser at: [http://127.0.0.1:8000/].
