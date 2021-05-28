import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket(browser):

    browser.get(link)

    time.sleep(10)

    text = browser.find_element_by_class_name("btn-add-to-basket").text

    browser.find_element_by_class_name("btn-add-to-basket").click()

    assert text is not None
