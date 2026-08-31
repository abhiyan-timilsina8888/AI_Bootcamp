AI Bootcamp

Author: Abhiyan Timilsina

## Setup

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The notebooks in `pandas/` use the bundled data files. `SampleSuperstore.xls` is a legacy Excel workbook and requires `xlrd`, which is included in `requirements.txt`.

Run the CSV explorer with:

```bash
streamlit run "pandas projects/08_sreamlit.py"
```
