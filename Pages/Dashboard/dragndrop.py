from Base.base import boi
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class drag(boi):

    progress = (
        By.XPATH, "(//div[@class='flex items-center justify-between'])[7]/child::span")

    def dropping(self):

        target = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='drop-zone']")))

        for itemno in range(1, 5):
            item = self.d.find_element(
                By.XPATH, f"//div[@id='item-{itemno}']/*[1]")
            self.AC.drag_and_drop(item, target).perform()

        status = self.wait.until(
            EC.visibility_of_element_located(self.progress))

        assert "4 / 4" in status.text, f"Expected 4/4, got {status.text}"
