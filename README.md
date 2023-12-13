<br/>

<h1 align="center">
  <a href="https://github.com/adilsameer/AWS-ETC-reward-collector-python">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" alt="Logo" width="80" height="80">
  </a>

  <br/>
  AWS ETC Reward Collector 
</h1>

<p align="center">
  This program automatically collects AWS ETC daily rewards. With these reward points, you can get free AWS Exam vouchers.
  <br/>
  <br/>
  <a href="https://github.com/adilsameer/AWS-ETC-reward-collector-python"><strong>Explore the docs »</strong></a>
  <br/>
  <br/>
  <a href="https://github.com/adilsameer/AWS-ETC-reward-collector-python">View Demo</a>
  .
  <a href="https://github.com/adilsameer/AWS-ETC-reward-collector-python/issues">Report Bug</a>
  .
  <a href="https://github.com/adilsameer/AWS-ETC-reward-collector-python/issues">Request Feature</a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/downloads/adilsameer/AWS-ETC-reward-collector-python/total" alt="Downloads">
  <img src="https://img.shields.io/github/contributors/adilsameer/AWS-ETC-reward-collector-python?color=dark-green" alt="Contributors">
  <img src="https://img.shields.io/github/forks/adilsameer/AWS-ETC-reward-collector-python?style=social" alt="Forks">
  <img src="https://img.shields.io/github/stars/adilsameer/AWS-ETC-reward-collector-python?style=social" alt="Stargazers">
  <img src="https://img.shields.io/github/issues/adilsameer/AWS-ETC-reward-collector-python" alt="Issues">
  <img src="https://img.shields.io/github/license/adilsameer/AWS-ETC-reward-collector-python" alt="License">
</p>

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](images/screenshot.png)

This project features a Python program that automatically collects daily rewards from the AWS Emerging Talent Community (ETC).

## Built With

Programming Language: Python
Modules Used:
🔵random
🔵selenium (and its components: webdriver, By, Keys)
🔵time
🔵datetime

## Getting Started

You can use this code by following below steps 

**Server Installation:**
### Prerequisites

**Replit Account:**
- Sign up for a Replit account at [https://replit.com/](https://replit.com/).
  
**UptimeRobot Account:**
- Create an account on [https://uptimerobot.com/](https://uptimerobot.com/).

### Installation

**Fork the Project:**

- Fork the project to your Replit account by visiting [this link](https://github.com/adilsameer/AWS-ETC-reward-collector-python).
   
**Update Credentials:**

- Open the forked project on Replit.
- Replace the values of `USER_EMAIL` and `USER_PASSWORD` in the code with your AWS ETC credentials.
- Optionally, set up environment variables for more secure credential storage.
  
**Set Up UptimeRobot Monitor:**

- Go to [UptimeRobot](https://uptimerobot.com/).
- Create a new monitor.
- Set the URL to your Replit project's address.
- Choose the monitor type as HTTP.
- Click "Create" to activate the monitor.
  
**Run the Code:**

- Run the code on Replit.
- The script will work 24/7, and UptimeRobot will keep it active.

**Local Installation:**

### Prerequisites:

**Python and Interpreter:**

- Install Python on your local machine.
- Ensure you have a Python interpreter installed.

### Installation:

**Download the Project:**

- Download the project from [GitHub](https://github.com/adilsameer/AWS-ETC-reward-collector-python).
  
**Update Credentials:**

- Open the downloaded project.
- Replace the values of `USER_EMAIL` and `USER_PASSWORD` in the code with your AWS ETC credentials.
- Optionally, set up environment variables for more secure credential storage.
  
**Run the Code:**

- Run the code on any Python interpreter on your local machine.
- The script will run, collect rewards, and close the browser.

By following these steps, users can deploy and use your Python project either on Replit or locally on their machines.

## Usage

- The program will automatically log in to the AWS ETC website and claim your daily reward.
- You can monitor the collected points and redeem them for rewards.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/adilsameer/AWS-ETC-reward-collector-python/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/adilsameer/AWS-ETC-reward-collector-python/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

- If you have suggestions for adding or removing features, feel free to [open an issue](https://github.com/adilsameer/AWS-ETC-reward-collector-python/issues/new) to discuss it or directly create a pull request after you edit the *README.md* file with necessary changes.
- Please make sure you check your spelling and grammar.
- Create individual PR for each suggestion.
- Please also read through the [Code Of Conduct](https://github.com/adilsameer/AWS-ETC-reward-collector-python/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. **Fork the Project:**
   - Visit the project's GitHub repository at [https://github.com/adilsameer/AWS-ETC-reward-collector-python](https://github.com/adilsameer/AWS-ETC-reward-collector-python).
   - Click the "Fork" button in the top-right corner of the page.
   - This will create a copy (fork) of the project under your GitHub account.

2. **Clone the Forked Project:**
   - Go to your GitHub profile and find the forked repository (`https://github.com/your-username/AWS-ETC-reward-collector-python`).
   - Copy the repository URL.
   - Open your terminal or command prompt and run the following command:
     ```bash
     git clone https://github.com/your-username/AWS-ETC-reward-collector-python.git
     ```

3. **Create a Feature Branch:**
   - Change to the project directory:
     ```bash
     cd AWS-ETC-reward-collector-python
     ```
   - Create a new branch for your feature:
     ```bash
     git checkout -b feature/YourFeatureName
     ```

4. **Make Changes:**
   - Make the necessary changes to the code using your preferred code editor.

5. **Commit Changes:**
   - Once you've made your changes, stage them for commit:
     ```bash
     git add .
     ```
   - Commit the changes with a meaningful message:
     ```bash
     git commit -m 'Add some YourFeatureName'
     ```

6. **Push to the Branch:**
   - Push your changes to your forked repository:
     ```bash
     git push origin feature/YourFeatureName
     ```

7. **Open a Pull Request:**
   - Visit your forked repository on GitHub.
   - You should see a banner with a suggestion to create a pull request. Click on it.
   - Alternatively, navigate to the "Pull Requests" tab and click on the "New Pull Request" button.
   - Set the base repository to `adilsameer/AWS-ETC-reward-collector-python` and the base branch to `main`.
   - Set the head repository to `your-username/AWS-ETC-reward-collector-python` and the compare branch to `feature/YourFeatureName`.
   - Click "Create Pull Request."

Congratulations! You've successfully created a pull request for the AWS ETC Reward Collector project. The project maintainers will review your changes, and if everything looks good, your feature will be merged into the main branch.


## Authors

* **Adil Sameer** - *Student of CSE* - [Adil Sameer](https://github.com/adilsameer) - *Built this project*

## Acknowledgements

* [adilsameer](https://github.com/adilsameer)

### Disclaimer

This code is provided for educational and experimental purposes only. The creator does not promote misuse of this code, and any misuse is the sole responsibility of the user.

