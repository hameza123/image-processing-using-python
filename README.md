# image-processing-using-python

1. Make sure you have Streamlit installed. If not, you can install it via pip:
   ```
   pip install streamlit
   ```

2. Copy the code into a Python file, e.g., `image_processing_app.py`.

3. Navigate to the directory containing the Python file in your terminal or command prompt.

4. Run the Streamlit app by executing the following command:
   ```
   streamlit run image_processing_app.py
   ```

5. The app should open in your default web browser, allowing you to upload images and perform basic image processing tasks interactively.

Feel free to customize and expand upon this code to add more features and functionalities as needed for your image processing application.


To convert the Streamlit app script to an executable file, you can use tools like PyInstaller or cx_Freeze. Here, I'll guide you through 
using PyInstaller, which is a popular choice for creating standalone executables from Python scripts.

Here are the steps:

1. **Install PyInstaller**:
   If you haven't installed PyInstaller yet, you can do so via pip:
   ```
   pip install pyinstaller
   ```

2. **Navigate to Your Project Directory**:
   Open a terminal or command prompt, and navigate to the directory containing your Streamlit app script (`image_processing_app.py` in this case).

3. **Run PyInstaller**:
   Use PyInstaller to convert your script into an executable. The basic command syntax is:
   ```
   pyinstaller --onefile image_processing_app.py
   ```
   This command tells PyInstaller to create a single executable file (`--onefile`) from your Streamlit app script (`image_processing_app.py`).

4. **Locate the Executable**:
   After PyInstaller finishes, you can find the standalone executable file in the `dist` directory within your project directory.

5. **Run the Executable**:
   You can now run the executable file (`image_processing_app.exe` on Windows, or `image_processing_app` on Linux/Mac) directly. Double-click the file,
   and your Streamlit app should launch as a standalone application.

That's it! You've successfully converted your Streamlit app script to an executable file using PyInstaller. You can distribute this executable to others
who may want to use your image processing application without needing Python or Streamlit installed.
