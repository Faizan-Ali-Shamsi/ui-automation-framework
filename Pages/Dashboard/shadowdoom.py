from Base.base import boi
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class shadow(boi):

    shadow_button = (By.ID, "create-basic-shadow")
    shadowdom_host_button = (By.XPATH, "//div[@id='shadow-host-element']")
    shadowdom_button = (By.CSS_SELECTOR, "button")

    def shadowdom(self):
        self.click(self.shadow_button)

        host = self.wait.until(
            EC.presence_of_element_located(self.shadowdom_host_button))
        assert host.is_displayed(), "Shadow host element should be visible"

        shadow_root = host.shadow_root
        shadow_button = shadow_root.find_element(*self.shadowdom_button)
        assert shadow_button.is_displayed(), "Shadow DOM button should be visible"

        element = self.d.find_element(By.TAG_NAME, "body")
        element.send_keys(Keys.PAGE_DOWN)

        self.MoveToElement(shadow_button)
        shadow_button.click()
