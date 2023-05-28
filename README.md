# qCaster

Schedule future casts on Farcaster

<!-- Badge row 1 - status -->

[![GitHub contributors](https://img.shields.io/github/contributors/wbnns/qcaster)](https://github.com/wbnns/qcaster/graphs/contributors)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/w/wbnns/qcaster)](https://github.com/wbnns/qcaster/graphs/contributors)
[![GitHub Stars](https://img.shields.io/github/stars/wbnns/qcaster.svg)](https://github.com/wbnns/qcaster/stargazers)
![GitHub repo size](https://img.shields.io/github/repo-size/wbnns/qcaster)
[![GitHub](https://img.shields.io/github/license/wbnns/qcaster?color=blue)](https://github.com/wbnns/qcaster/blob/main/LICENSE)

<!-- Badge row 2 - links and profiles -->

[![Website wbnns.com](https://img.shields.io/website-up-down-green-red/https/wbnns.com.svg)](https://wbnns.com/)
[![Log](https://img.shields.io/badge/blog-up-green)](https://log.wbnns.com/)
[![Twitter wbnns](https://img.shields.io/twitter/follow/wbnns?style=social)](https://twitter.com/wbnns)

<!-- Badge row 3 - detailed status -->

[![GitHub pull requests by-label](https://img.shields.io/github/issues-pr-raw/wbnns/qcaster)](https://github.com/wbnns/qcaster/pulls)
[![GitHub Issues](https://img.shields.io/github/issues-raw/wbnns/qcaster.svg)](https://github.com/wbnns/qcaster/issues)

## Description

This application uses the Tweepy and Requests libraries to interact with the Twitter and Farcaster APIs, respectively. It also includes a simple Bootstrap frontend interface for managing scheduled tweets.

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- SQLite

### Installation

1. Clone this repository:
```
The README.md is a crucial file in any project and typically contains the following sections:

    Project Title: A descriptive title for your project.

    Description: A brief explanation of what the project does.

    Getting Started/Installation: A step-by-step guide on how to set up the project locally. This could include steps to clone the repository, installing dependencies, setting up the database, and any other steps required to get the project running.

    Usage: Some examples of how to use the project. For a web application, this might be instructions on how to run the server and access it in a browser.

    Contributing: Guidelines for people who want to contribute to your project.

    License: The license your project uses.

Here's a sample README.md for your Flask application:

markdown

# Twitter-Farcaster Tweet Scheduler

This is a Flask application that allows scheduling of tweets and farcaster posts.

## Description

This application uses the Tweepy and Requests libraries to interact with the Twitter and Farcaster APIs, respectively. It also includes a simple Bootstrap frontend interface for managing scheduled tweets.

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- SQLite

### Installation

1. Clone this repository:
```
git clone https://github.com/wbnns/qcaster.git
cd qcaster
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Copy the `.env.example` file to `.env` and update the variables with your credentials:
```
cp .env.example .env
```
4. Run the application:
```
flask run
```
## Usage

Once the application is running, you can access the interface at http://localhost:5000. From there, you can add, update, and delete scheduled tweets.

## Contributing

Pull requests are welcome. Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
