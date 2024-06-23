# resume-agent
ATS(or)Hacker Rank

## Project Structure
```
VishwamAI/
├── data/               # Directory for datasets
├── models/             # Directory for storing trained models
├── scripts/            # Directory for scripts (e.g., training, preprocessing, model conversion, auto-update)
├── notebooks/          # Directory for Jupyter notebooks
├── logs/               # Directory for training logs and metrics
├── docs/               # Directory for documentation
├── config/             # Directory for configuration files
├── utils/              # Directory for utility scripts and functions
├── setup.sh            # Script for setting up the environment
├── requirements.txt    # File for specifying required dependencies
└── README.md           # Project overview and instructions
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/VishwamAI/resume-agent.git
   cd resume-agent
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the LinkedIn Authentication Script
1. Run the Flask application:
   ```bash
   python scripts/linkedin_auth.py
   ```

2. Navigate to `http://localhost:5000` in your web browser to initiate the LinkedIn OAuth flow.

3. Verify that the access token is obtained and displayed.

### Running Tests
1. Run the unit tests:
   ```bash
   python -m unittest discover -s scripts -p "test_*.py"
   ```

## GitHub Actions Workflow
This project uses GitHub Actions for continuous integration. The workflow is defined in the `.github/workflows/ci.yml` file and includes the following steps:
- Checkout code
- Set up Python
- Install dependencies
- Run tests

The workflow is triggered on push and pull request events for the `main` and `feature/linkedin-auth` branches.

## Notes
- The LinkedIn authentication script is a placeholder and outlines the OAuth 2.0 process.
- Further development is needed to use the access token to fetch LinkedIn profile data and analyze resumes in ATS or HackerRank format.
