from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class boi:
    def __init__(self, d):
        self.d = d
        self.AC = ActionChains(d)
        self.wait = WebDriverWait(d, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.AC.move_to_element(element).click().perform()

    def coockies(self):

        coockies_cancle_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Accept All']")))

        if coockies_cancle_button:
            coockies_cancle_button.click()

    def MoveToElement(self, element):
        self.AC.move_to_element(element).perform()
