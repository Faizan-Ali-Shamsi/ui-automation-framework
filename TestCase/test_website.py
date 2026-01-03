from Pages.main_page import page
from Pages.dashboard import board
from Pages.Dashboard.dragndrop import drag
from Pages.Dashboard.DynamicElement import Dynamic
from Pages.Dashboard.IFRAME import iFramesWindows
from Pages.Dashboard.KeyboardANDMouse import keyboardandmouse
from Pages.Dashboard.shadowdoom import shadow
import pytest


class Test:
    def start(self, setup):
        main_page = page(setup)
        main_page.coockies()
        main_page.start()

    @pytest.mark.skip(reason="no need")
    def test_booard(self, setup):
        self.start(setup)
        board_page = board(setup)
        board_page.drangNdrop_practise()

        Practise = drag(setup)
        Practise.dropping()

    def test_DyynamicElement(self, setup):
        self.start(setup)
        board_page = board(setup)
        board_page.DynamicElement()

        dynamic = Dynamic(setup)
        dynamic.DelayedElements()
        dynamic.AJAXDataLoading()
        dynamic.InfiniteScroll()
        dynamic.HiddenDynamicElements()
        dynamic.DynamicContentGeneration()

    @pytest.mark.skip(reason="no need")
    def test_IFRAMEnWINDOWSS(self, setup):
        self.start(setup)
        board_page = board(setup)
        board_page.IFRAMEnWINDOWS()

        frame = iFramesWindows(setup)
        frame.iframe()

    @pytest.mark.skip(reason="no need")
    def test_KeyyboardMouse(self, setup):
        self.start(setup)
        board_page = board(setup)
        board_page.KeyboardMouse()

        ki = keyboardandmouse(setup)
        ki.keymo()

    @pytest.mark.skip(reason="no need")
    def test_ShadowDomm(self, setup):
        self.start(setup)
        board_page = board(setup)
        board_page.ShadowDom()

        shia = shadow(setup)
        shia.shadowdom()
