from Base.base import boi
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class keyboardandmouse(boi):

    prefilled = (By.ID, "start-clear-scenario")
    prefilled_input = (By.XPATH, "//input[@id='search-field']")

    confirmationflow = (By.ID, "start-dialog-scenario")
    delete_confirmation = (By.XPATH, "//span[text()='Delete']/parent::button")

    double_click = (By.XPATH, "//div[@id='editable-text']")

    hover = (By.XPATH, "//div[@id='hover-card']")

    def keymo(self):

        # 1. Clear Pre-filled Field

        self.click(self.prefilled)
        input_field = self.d.find_element(*self.prefilled_input)
        input_field.send_keys(Keys.CONTROL, "a")
        input_field.send_keys(Keys.BACKSPACE)
        input_field.send_keys(Keys.BACKSPACE)
        assert input_field.is_displayed(), "Prefilled input should be visible"
        assert input_field.get_attribute(
            "value") == "", "Prefilled input should be cleared"

        # 2. Dialog Confirmation Flow

        self.click(self.confirmationflow)
        delete_btn = self.d.find_element(*self.delete_confirmation)
        assert delete_btn.is_displayed(), "Delete confirmation button should be visible"
        delete_btn.send_keys(Keys.ENTER)

        self.d.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

        # 3. Double-click to Edit

        self.click(self.double_click)
        editable_element = self.d.find_element(*self.double_click)
        self.AC.double_click(editable_element).perform()
        assert editable_element.is_displayed(), "Editable text element should be visible"

        # 4. Hover Interaction

        hover_card = self.d.find_element(*self.hover)
        self.AC.move_to_element(hover_card).pause(2.5).perform()
        assert hover_card.is_displayed(), "Hover card should be visible"
