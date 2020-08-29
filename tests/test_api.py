import requests
import time
import pytest
import urllib

#Декоратор, измеряющий время
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        assert  end - start <= 0.5
        return result
    return wrapper


class TestRebelStar:

    def setup_class(self):
        self.domain = 'https://rebelstar.ru/'
        self.timeout = 3.0 # В секундах

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

