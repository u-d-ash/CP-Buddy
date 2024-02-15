import os
import sys
import subprocess
from playwright.sync_api import sync_playwright
from atwebscrape import atwebscrape
from cfwebscrape import cfwebscrape
from contestac import contest_activity
from contestmode import contestmode
from practicemode import practicemode
from problemac import problem_activity
import requests
from bs4 import BeautifulSoup