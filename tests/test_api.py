import requests
import time
import pytest
import urllib

from selenium import webdriver


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
        self.DRIVER_CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'
        self.DRIVER_MOZILLA_PATH = 'C:/Program Files/Mozilla Firefox/geckodriver.exe'
        self.DRIVER_EDGE_PATH = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe'

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
    @pytest.mark.parametrize("rs, raider, operativeOrAlien, fog",[
        (1,True, True, True), (2 ,True, True, True),
        (1, True, True, False), (2, True, True, False),#(1, True, False, True),(1, False, True, True),
        #(1, True, False, False), (1, False, True, False), (1, False, False, True),
        #(1, False, False, False)
        ])
    def test_rbModes(self, rs, raider, operativeOrAlien, fog):
        #driver = webdriver.Firefox(executable_path = self.DRIVER_MOZILLA_PATH)
        #driver = webdriver.Chrome(executable_path = self.DRIVER_CHROME_PATH)
        driver = webdriver.Edge(executable_path= self.DRIVER_EDGE_PATH)
        driver.get(self.domain)
        try:
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
        finally:
            driver.close()

    @pytest.mark.parametrize("words, href",[
        ('известной','https://en.wikipedia.org/wiki/Rebelstar'), ('Играть', 'https://rebelstar.ru/#two'),
        ('Описание', 'https://rebelstar.ru/#three'),('Tomoko','https://www.artstation.com/tdblacksun'),
        ('Howler','https://howlerjs.com/'), ('EasyStar', 'https://easystarjs.com/'),
        ('html5up.net','https://html5up.net/')
        ])
    def test_href(self, words, href):
        driver = webdriver.Edge(executable_path= self.DRIVER_EDGE_PATH)
        driver.get(self.domain)
        try:
            firstHref = driver.find_element_by_link_text(words).get_attribute('href')
            driver.get(firstHref)
            
            assert driver.current_url == href

            time.sleep(2)
        finally:
            driver.quit()