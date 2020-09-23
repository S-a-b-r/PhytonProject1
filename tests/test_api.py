import requests
import time
import pytest
import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Декоратор, измеряющий время
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        assert  end - start <= 1
        return result
    return wrapper


class TestRebelStar:

    def setup_class(self):
        self.domain = 'https://rebelstar.ru/'
        self.timeout = 3.0 # В секундах
        DRIVER_PATH_CHROME = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'
        DRIVER_PATH_MOZILLA = 'C:/Program Files/Mozilla Firefox/geckodriver.exe'
        DRIVER_PATH_EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe'
        self.firefox = webdriver.Firefox(executable_path = DRIVER_PATH_MOZILLA)
        #self.chrome = webdriver.Chrome(executable_path = DRIVER_PATH_CHROME)
        self.edge = webdriver.Edge(executable_path= DRIVER_PATH_EDGE)

    def teardown_class(self):
        self.firefox.close()
        #self.chrome.close()
        self.edge.close()

    @benchmark
    def callUrl(self, part = None, params = None):
        try:
            url = self.domain
            if part:
                url += part
            if params:
                url += '?' + urllib.parse.urlencode(params)
            return requests.get(url, timeout = self.timeout)
        except ValueError:
            return False

    def test_domain(self):
        result = self.callUrl()
        assert result.status_code == 200
    
     # Позитивные проверки
    @pytest.mark.parametrize("raider, operative, fog",[
        (True, True, True),
        (True, True, False),(True, False, True),(False, True, True),
        (True, False, False), (False, True, False), (False, False, True),
        (False, False, False)
        ])
    

    def test_method(self, raider, operative, fog):
        part = 'RS1/index.html'
        result = self.callUrl(part, dict(raider = raider, operative = operative, fog = fog))
        assert result.status_code == 200

    #Далее крашнутые тесты
    def test_crush_method(self, raider, operative, fog):
        part = 'Rs1/index.html'
        result = self.callUrl(part, dict(raider = raider, operative = operative, fog = fog))
        assert result.status_code == 200

    def test_crush_method_1(self, raider, operative, fog):
        part = 'RS1/index.html'
        result = self.callUrl(part, dict(raider = raide, operative = operativ, fog = fog))
        assert result.status_code == 200
    
    def test_crush_method_2(self, raider, operative, fog):
        part = 'RS1/index.html'
        result = self.callUrl(part, dict(raider = raider, operative = operative, fog = fog))
        assert result.status_code == 404


    #rs - номер игры(1 часть или 2 часть игры)
    @pytest.mark.parametrize(" driverName, rs, raider, operativeOrAlien, fog",[
        ('edge', 1, True, True, True),
        ('edge', 1,  True, True, False),  ('edge',1, True, False, True),  ('edge',1, False, True, True),
        ('edge', 1,  True, False, False), ('edge',1, False, True, False), ('edge',1, False, False, True),
        ('edge', 1,  False, False, False),
        ('edge', 1, True, True, True),
        ('edge', 2,  True, True, False),  ('edge',2, True, False, True),  ('edge',2, False, True, True),
        ('edge', 2,  True, False, False), ('edge',2, False, True, False), ('edge',2, False, False, True),
        ('edge', 2,  False, False, False),
        ('firefox', 1, True, True, True),
        ('firefox', 1,  True, True, False),  ('firefox',1, True, False, True),  ('firefox',1, False, True, True),
        ('firefox', 1,  True, False, False), ('firefox',1, False, True, False), ('firefox',1, False, False, True),
        ('firefox', 1,  False, False, False),
        ('firefox', 1, True, True, True),
        ('firefox', 2,  True, True, False),  ('firefox',2, True, False, True),  ('firefox',2, False, True, True),
        ('firefox', 2,  True, False, False), ('firefox',2, False, True, False), ('firefox',2, False, False, True),
        ('firefox', 2,  False, False, False)
        ])
    def test_rbModes(self, driverName, rs, raider, operativeOrAlien, fog):
        driver = self.__getattribute__(driverName)

        driver.get(self.domain)

        assert "Rebel Star" in driver.title
        #Включаем чекбоксы
        if raider:
            driver.execute_script("document.getElementById('rs%s-ai1').checked = true" % (rs) )
        if operativeOrAlien:
            driver.execute_script("document.getElementById('rs%s-ai2').checked = true" % (rs) )
        if fog:
            driver.execute_script("document.getElementById('rs%s-fog').checked = true" % (rs))

        #Перейти к игре
        button = driver.find_element_by_id('imgRS%s' % (rs))
        button.click()

        urlParse = urllib.parse.urlparse(driver.current_url)
        if rs == 1:
            query = urllib.parse.urlencode(dict(raider = raider, operative = operativeOrAlien, fog = fog)).lower()
        else:
            query = urllib.parse.urlencode(dict(raider = raider, alien = operativeOrAlien, fog = fog)).lower()

        assert urlParse.query == query


    @pytest.mark.parametrize("driverName, words, href",[
        ('edge','известной','https://en.wikipedia.org/wiki/Rebelstar'), ('edge','Играть', 'https://rebelstar.ru/#two'),
        ('edge','Описание', 'https://rebelstar.ru/#three'),             ('edge','Tomoko','https://www.artstation.com/tdblacksun'),
        ('edge','Howler','https://howlerjs.com/'),                      ('edge','EasyStar', 'https://easystarjs.com/'),
        ('edge','html5up.net','https://html5up.net/'),
        ('firefox','известной','https://en.wikipedia.org/wiki/Rebelstar'), ('firefox','Играть', 'https://rebelstar.ru/#two'),
        ('firefox','Описание', 'https://rebelstar.ru/#three'),             ('firefox','Tomoko','https://www.artstation.com/tdblacksun'),
        ('firefox','Howler','https://howlerjs.com/'),                      ('firefox','EasyStar', 'https://easystarjs.com/'),
        ('firefox','html5up.net','https://html5up.net/'),
        ])
    def test_href(self,driverName, words, href):
        driver = self.__getattribute__(driverName)
        driver.get(self.domain)
        firstHref = driver.find_element_by_link_text(words).get_attribute('href')
        driver.get(firstHref)
        
        assert driver.current_url == href