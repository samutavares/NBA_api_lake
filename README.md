# NBA API Lake

Welcome to the NBA API Lake project. This repository is structured to provide a multi-layered data architecture for NBA data, enabling efficient storage, processing, and visualization. The data is sourced from the [Ball Don't Lie API](https://docs.balldontlie.io/#get-all-games).

## Architecture

The project is organized into four distinct layers, each serving a different purpose in the data lifecycle:

### Raw Layer
Contains raw JSON data as retrieved from the Ball Don't Lie API. This is the unprocessed data that serves as the base for all further transformations.

### Bronze Layer
Utilizes DuckDB to store the raw data with minimal transformations. This layer serves as the initial stage of structured storage.

### Silver Layer
Incorporates cleaned and processed data within DuckDB. Data at this stage is ready for more complex analysis and transformations.

### Gold Layer
Features aggregated data optimized for dashboarding and analytics. This layer is the final form of the data, tailored for visualization tools like Superset and Power BI.

## Project Roadmap

As an initial project, the following improvements are slated for future development:

1. Create an upsert mechanism to handle data updates efficiently.
2. Implement checkpointing for reliable data ingestion and processing.
3. Develop a Python-based data ingestion process for the Silver layer.
4. Establish connectivity with data visualization tools such as Superset and Power BI.

## Prerequisites

Before you can use this repository, you will need:

- API access: Obtain your API key from [Ball Don't Lie API](https://docs.balldontlie.io/#get-all-games).
- Python environment: Set up a Python environment with the necessary libraries.

## Installation

1. Clone the repository:
