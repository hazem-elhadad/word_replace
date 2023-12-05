# Word and Table Replacement Service

This service is designed to perform text replacement in Microsoft Word documents and replace entire tables with specified content.

## Features

- Replace specific words in a Word document.
- Replace entire tables with custom content.

## Prerequisites

Before running the service, make sure you have the following installed on your system:

- Python installed
- Microsoft Word (or Microsoft Office) installed
- Windows operating system (the provided batch file is for Windows)

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/omarnazih/word-replace-service.git
    ```

2. Navigate to the project directory:

    ```bash
    cd word-replace-service
    ```

3. Create a virtual environment:

    ```bash
    python -m venv .venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source .venv/bin/activate
        ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Word Replacement & Table Replacement

1. Make sure to place the Word documents in the `MODIFIED_FILES` directory.

2. Open a command prompt and run the following command:

    ```bash
    
    ```

    This batch file will initiate the word replacement process.

3. After the process is complete, you can find the modified Word document in the `output` directory.

## Configuration

- Word Replacement: 
  
- Table Replacement:

## Notes

- Ensure that Microsoft Word is installed on your system.
- The replaced Word documents will be saved in the `output` directory.

## Troubleshooting

If you encounter any issues or errors during the replacement process, please check the following:

- Ensure that Microsoft Word is installed on your system.
- Verify that the input Word document is in the `MODIFIED_FILES` directory.

If the issue persists, feel free to open an issue on this repository, providing details about the problem you are facing.

Happy replacing!
