from Base.base import boi
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Dynamic(boi):

    DelayedElements_path = (By.ID, "trigger-delayed")
    DelayedElements_confirmation = (
        By.XPATH, "//p[text()= '✓ Element appeared after 5 second delay!']")

    AJAXDataLoading_path = (By.ID, "load-ajax-data")
    AJAXDataLoading_confirmation1 = (
        By.XPATH, "//h4[text()= 'Dynamic Item 1']")

    def DelayedElements(self):
        self.click(self.DelayedElements_path)
        delayed = self.wait.until(EC.visibility_of_element_located(
            (self.DelayedElements_confirmation)))

        assert delayed.is_displayed()

    def AJAXDataLoading(self):
        self.click(self.AJAXDataLoading_path)
        element = self.wait.until(EC.visibility_of_element_located(
            (self.AJAXDataLoading_confirmation1)))
        self.MoveToElement(element)

        names = [
            (By.XPATH, f"//h4[text()='Dynamic Item {j}']") for j in range(2, 6)]

        for locator in names:
            confirm = self.wait.until(
                EC.visibility_of_element_located(locator))
            assert confirm.is_displayed(
            ), f"Dynamic element was not displayed, got {confirm.text}"
            self.MoveToElement(confirm)

    InfiniteScroll_path = (
        By.XPATH, "//p[text()='Automatically loads more content as you scroll down.']/following-sibling::*[1]")

    def InfiniteScroll(self):
        element0 = self.wait.until(
            EC.visibility_of_element_located((self.InfiniteScroll_path)))
        self.MoveToElement(element0)

        for item_no in [10, 20, 30, 40, 50]:
            element = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, f"//h4[text()='Item {item_no}']")
            ))
            assert element.is_displayed(
            ), f"Infinite scroll item {item_no} should appear"
            self.MoveToElement(element)

    HiddenDynamicElements_path = (
        By.XPATH, "//h4[text()='Hidden Elements']/following-sibling::*[2]")
    HiddenDynamicElements_found = (By.ID, "hidden-element")

    def HiddenDynamicElements(self):
        element = self.wait.until(EC.visibility_of_element_located(
            self.HiddenDynamicElements_path))
        self.MoveToElement(element)
        element.click()
        element1 = self.wait.until(EC.visibility_of_element_located(
            self.HiddenDynamicElements_found))

        assert element1.is_displayed(), "Hidden element should appear!"

        self.MoveToElement(element1)

    DynamicContentGeneration_button = (By.ID, "generate-content")
    DynamicContentGeneration_confirmation = (
        By.XPATH, "//p[contains(@class, 'text-blue-800')]")

    def DynamicContentGeneration(self):
        element = self.wait.until(EC.visibility_of_element_located(
            self.DynamicContentGeneration_button))
        self.MoveToElement(element)
        element.click()

        element1 = self.wait.until(EC.visibility_of_element_located(
            self.DynamicContentGeneration_confirmation))

        assert element1.is_displayed(), "Generated content should appear!"

        self.MoveToElement(element1)
