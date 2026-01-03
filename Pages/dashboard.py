from Base.base import boi
from selenium.webdriver.common.by import By


class board(boi):

    DragAndDrop_path = (By.XPATH, "//a[@href='/drag-and-drop/']/button")
    DynamicElement_path = (By.XPATH, "//a[@href='/dynamic-elements/']/button")
    IFRAME_path = (By.XPATH, "//a[@href='/iframe-windows/']/child::button")
    KeyboardMouse_path = (
        By.XPATH, "//button[text()='Start Practice']/parent::a[@href='/keyboard-mouse-events/']")
    shadowdom_path = (By.XPATH, "//a[@href='/shadow-dom/']/child::button")

    def drangNdrop_practise(self):
        self.click(self.DragAndDrop_path)

    def DynamicElement(self):
        self.click(self.DynamicElement_path)

    def IFRAMEnWINDOWS(self):
        self.click(self.IFRAME_path)

    def KeyboardMouse(self):
        self.click(self.KeyboardMouse_path)

    def ShadowDom(self):
        self.click(self.shadowdom_path)
