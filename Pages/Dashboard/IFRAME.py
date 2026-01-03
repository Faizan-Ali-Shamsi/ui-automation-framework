from Base.base import boi
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class iFramesWindows(boi):

    iframe_path = (By.ID, "basic-iframe")
    iframe_basic_button = (By.ID, "iframe-button")
    iframe_form = (By.XPATH, "//button[text()='Form']")
    iframe_form_input = (By.ID, "iframe-name")
    iframe_form_email = (By.ID, "iframe-email")
    iframe_form_comment = (By.ID, "iframe-comment")
    iframe_form_comment_button = (By.ID, "iframe-submit")
    iframe_nested = (By.XPATH, "//button[text()='Nested']")
    iframe_nested_path = (By.ID, "inner-iframe")
    iframe_nested_button = (By.ID, "nested-button")
    iframe_nested_nested_button = (By.XPATH, "//button[@id='iframe-button']")
    iframe_main_button = (By.ID, "send-iframe-message")

    windows_1st = (By.ID, "open-basic-popup")
    windows_input = (By.ID, "popup-input")
    windows_select_dropdown = (By.ID, "popup-select")
    windows_check_box = (By.XPATH, "//input[@id='popup-checkbox']")
    windows_main_button = (By.ID, "send-message")
    windows_resize = (By.ID, "resize-window")
    windows_move = (By.ID, "move-window")
    windows_2st = (By.ID, "open-small-popup")

    alert = (By.ID, "trigger-alert")
    confirm = (By.ID, "trigger-confirm")
    prompt = (By.ID, "trigger-prompt")

    CustomModals_button = (By.ID, "open-modal")
    CustomModalDialog_button = (By.ID, "modal-action")

    def WindowWork(self):
        self.d.switch_to.window(self.d.window_handles[-1])

        input_el = self.wait.until(
            EC.visibility_of_element_located(self.windows_input))
        assert input_el.is_displayed(), "Popup input should be visible"
        input_el.send_keys("afnkauen")

        dropdown_el = self.wait.until(
            EC.visibility_of_element_located(self.windows_select_dropdown))
        Select(dropdown_el).select_by_visible_text("Option 2")

        checkbox = self.wait.until(
            EC.element_to_be_clickable(self.windows_check_box))
        assert checkbox.is_displayed(), "Popup checkbox should be visible"
        self.click(self.windows_check_box)

        self.wait.until(
            EC.element_to_be_clickable(self.windows_main_button))
        self.click(self.windows_main_button)

        self.wait.until(
            EC.element_to_be_clickable(self.windows_resize))
        self.click(self.windows_resize)

        self.wait.until(
            EC.element_to_be_clickable(self.windows_move))
        self.click(self.windows_move)

    def iframe(self):
        # ---------Basic---------
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(self.iframe_path))
        basic_btn = self.wait.until(
            EC.element_to_be_clickable(self.iframe_basic_button))
        assert basic_btn.is_displayed(), "Basic iframe button should be visible"
        self.click(self.iframe_basic_button)
        self.d.switch_to.default_content()

        # ---------Form---------
        self.wait.until(
            EC.element_to_be_clickable(self.iframe_form))
        self.click(self.iframe_form)

        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(self.iframe_path))
        name_input = self.wait.until(
            EC.visibility_of_element_located(self.iframe_form_input))
        name_input.send_keys("nigga")
        assert name_input.get_attribute("value") == "nigga"

        email_input = self.d.find_element(*self.iframe_form_email)
        email_input.send_keys("nigga@gmail.com")
        assert email_input.get_attribute("value") == "nigga@gmail.com"

        comment_input = self.d.find_element(*self.iframe_form_comment)
        comment_input.send_keys("nigga123")
        assert comment_input.get_attribute("value") == "nigga123"

        submit_btn = self.d.find_element(*self.iframe_form_comment_button)
        self.MoveToElement(submit_btn)
        self.click(self.iframe_form_comment_button)

        try:
            alert = self.wait.until(EC.alert_is_present())
            assert alert is not None, "Alert should appear after form submit"
            alert.accept()
        except:
            pass

        self.d.switch_to.default_content()

        # ---------Nested---------
        self.click(self.iframe_nested)
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(self.iframe_path))
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(
            self.iframe_nested_path))

        iframe_body = self.d.find_element(By.TAG_NAME, "body")
        iframe_body.click()
        iframe_body.send_keys(Keys.PAGE_DOWN, Keys.PAGE_DOWN)

        inner_btn = self.wait.until(
            EC.element_to_be_clickable(self.iframe_nested_nested_button))
        assert inner_btn.is_displayed(), "Nested inner button should be visible"
        inner_btn.click()

        self.d.switch_to.parent_frame()
        self.wait.until(
            EC.element_to_be_clickable(self.iframe_nested_button))
        self.click(self.iframe_nested_button)
        self.d.switch_to.default_content()
        self.wait.until(
            EC.element_to_be_clickable(self.iframe_main_button))
        self.click(self.iframe_main_button)

        # ---------Windows---------
        self.click(self.windows_1st)
        self.WindowWork()
        self.d.close()
        self.d.switch_to.window(self.d.window_handles[0])

        self.click(self.windows_2st)
        self.WindowWork()
        self.d.close()
        self.d.switch_to.window(self.d.window_handles[0])

        # ---------Browser Dialogs---------
        for dialog_locator in [self.alert, self.confirm, self.prompt]:
            self.click(dialog_locator)
            dialog_alert = self.wait.until(EC.alert_is_present())
            assert dialog_alert is not None, f"Alert for {dialog_locator} should appear"
            dialog_alert.accept()

        # ---------Custom Modals---------
        self.click(self.CustomModals_button)
        custom_btn = self.wait.until(
            EC.element_to_be_clickable(self.CustomModalDialog_button))
        assert custom_btn.is_displayed(), "Custom modal button should be visible"
        self.click(self.CustomModalDialog_button)
        alert4 = self.wait.until(EC.alert_is_present())
        assert alert4 is not None, "Custom modal alert should appear"
        alert4.accept()
