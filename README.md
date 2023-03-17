# foggs-journey

### Local Setup

1. Create a virtual environment

   ```bash
   python3 -m venv <ENV_NAME>
   ```

2. Install all the dependencies

   ```bash
   pip3 install -r requirements.txt
   ```

3. Run `preprocess.py` to generate all the csv files.

   ```bash
   python3 preprocess.py
   ```

4. Finally, Run `app.py` to execute your streamlit application.

   ```bash
   streamlit run app.py
   ```
