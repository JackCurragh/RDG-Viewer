# RDG-Viewer
<b>Ribosome Decision Graph Viewer in the Browser</b>

- <b>[RDG-Viewer - Colab Notebook</b>](https://colab.research.google.com/drive/1f5iSgy5DAXeq27Lx1fCyngm4IjinkgC5?usp=sharing)

This Google Colaboratory notebook serves as a tool for generating Ribosome Decision Graph (RDG) visualizations within a web browser. The RDG concept, introduced alongside this notebook ([BioRxiv](https://doi.org/10.1101/2023.11.10.566564)), enables accurate representation of translation complexity commonly seen in eukaryotic RNA, and this interactive tool empowers users to explore and visualize these RDGs programmatically.

## Table of Contents

- [RDG-Viewer](#RDG-Viewer)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Dependencies](#dependencies)
  - [Usage](#usage)
  - [License](#license)

## Overview

The RDG-Viewer enables users to generate RDG plots through various methods, providing flexibility and control over the visualization process. Users can:

- Generate RDG plots by specifying translon coordinates from annotations.
- Construct graphs by providing the transcript nucleotide sequence along with customizable parameters.
- Obtain transcript sequences using "gget" based on gene names and subsequently generate RDG plots.

## Dependencies

Dependencies are installed at the beginning of the notebook. They include:
- Python 3
- sqlitedict
- matplotlib
- networkx
- gget
- RDG

## Usage

Explain how to use the notebook. Include step-by-step instructions if necessary. For example:

1. Open the notebook in Google Colab.
2. Click on "Runtime" in the menu, then "Run all" to execute all cells.
3. Follow the prompts, alter parameters or modify the code as necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
