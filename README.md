# dr-reward-template

Template for AWS DeepRacer reward function to facilitate unit
testing and CI.

## Install Requirements and Run Unit Tests

## 1) Install Python requirements

```
pip3 install -r requirements.txt
```

## 2) Run unit tests

```
python3 test_reward.py
```

## 3) Run lint

```
pylint reward.py test_reward.py
```

## Optional: Python Virtual Environment Setup


### 1) One-time setup

```
python3 -m venv dr_venv
```

### 2) Each time before running python commands

Activate the python environment

```
source dr_venv/bin/activate
```


## Optional: GitLab CI Setup

`.gitlab-ci.yml` is already set up to run the lint and unit tests
