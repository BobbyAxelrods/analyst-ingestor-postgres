# Data Ingestion Tool for Visualization

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This tool is designed specifically for analysts who need to ingest data for manipulating visualization purposes. It provides a safe and convenient way to work with data without granting access to other schemas, thereby mitigating the risk of accidentally deleting important data. Moreover, it eliminates the need to use tools, which can potentially expose other schemas to unintended changes.

## Features

- **Data Ingestion:** The tool enables analysts to ingest data specifically dedicated to visualization tasks, ensuring a focused and streamlined workflow.

- **Schema Isolation:** Analysts are granted access only to the necessary schema(s) for data ingestion, preventing any accidental modifications or deletions to other important data.

- **Enhanced Security:** By avoiding the use of general-purpose database tools like DBeaver, the risk of inadvertently affecting unrelated schemas or data is significantly reduced.

- **Simplified Workflow:** With a dedicated tool for data ingestion, analysts can efficiently perform their visualization tasks without the need for additional tools or unnecessary access permissions.

## Prerequisites

Before running the tool, make sure you have the following:

- Python 3.x installed
- Required packages: SQLAlchemy, pandas, streamlit

## Getting Started

To get started with the Data Ingestion Tool for Visualization, follow the steps below:

1. Clone the repository to your local machine.

   ```shell
   git clone https://github.com/your-username/data-ingestion-tool.git

Feel free to copy and use this code in your project's README file.
