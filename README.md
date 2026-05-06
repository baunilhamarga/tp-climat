# tp-climat

TD/TP work for the ST4 course **Énergie et Climat** on the decarbonization of an electricity generation fleet.

The project uses hourly French electricity data for 2024 to study consumption, production, net demand, generation fleet sizing, and storage-related questions. The data files were originally sourced from the CentraleSupélec Edunao platform and made available by the course professors.

## Repository Structure

- `Template.ipynb`: cleaned notebook version of the original Python template.
- `Exercise 1.ipynb`: consumption analysis.
- `Exercise 2.ipynb`: production analysis and net demand construction.
- `Exercise 3.ipynb`: simplified dispatchable fleet optimization.
- `Exercise 4.ipynb`: storage-related analysis.
- `edunao-files/`: source data and course/lab PDFs.
- `figures/`: exported PDF figures used in the report.
- `main.tex`: LaTeX source for the report.
- `requirements.txt`: pinned Python environment exported from the local `climat` environment.

## Python Environment

The notebooks use common data-science packages only, mainly:

- `pandas` for tabular and time-series data processing
- `numpy` for numerical operations
- `matplotlib.pyplot` and `matplotlib.dates` for plotting

To recreate the Python environment:

```bash
python -m venv climat
source climat/bin/activate
pip install -r requirements.txt
```

To use the environment as a Jupyter kernel:

```bash
python -m ipykernel install --user --name climat --display-name climat
```

## Report

The report is compiled from `main.tex`.

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

## Figures

Notebook figures are exported as PDFs in `figures/` so they can be included directly in the LaTeX report. The current naming convention is:

```text
figures/exercise_<exercise>-<question>.pdf
```

with descriptive suffixes when more than one plot is needed for the same question.
