from Base.base import boi
from selenium.webdriver.common.by import By


class page(boi):

    try_without_account_path = By.XPATH, ("//a[@href='/dashboard/']/*[1]")

    def start(self):
        self.click(self.try_without_account_path)
