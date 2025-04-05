import unittest
from Proxy import *


class Hi:
    def __init__(self):
        self.number = 0

    def f1(self):
        pass

    def f2(self):
        pass


class Test(unittest.TestCase):
    def test_sample_1(self):
        str_proxy = Proxy("test_string")
        self.assertTrue(isinstance(str_proxy, Proxy), '\nنام کلاس مورد نظر باید Proxy باشد.')
        t = Hi()
        proxy = Proxy(t)
        proxy.number = 6
        self.assertEqual(6, proxy.number, '\nکلاس Proxy باید قابلیت تغییر مقدار یک ویژگی از کلاس‌های دیگر را داشته باشد.')

    def test_sample_2(self):
        proxy = Proxy("Test String")
        proxy.upper()
        self.assertEqual("upper", proxy.last_invoked_method(), '\nآخرین متد معتبری که فراخوانی شده، upper است.')
        try:
            proxy.no_such_method()
            self.assertFalse(True)
        except Exception as e:
            self.assertEqual("No Such Method", str(e), '\nتابع مورد نظر جزو توابع تعریف شده نیست؛ پس باید استثنایی با پیغام No Such Method پرتاب شود.')

        self.assertEqual(1, proxy.count_of_calls("upper"), '\nمتد upper تاکنون ۱ بار روی شئ مورد نظر فراخوانی شده است.')
        self.assertEqual(0, proxy.count_of_calls("capitalize"), '\nمتد ‌capitalize تاکنون روی شئ مورد نظر فراخوانی نشده است.')

    def test_sample_3(self):
        proxy = Proxy(Hi())
        proxy.f1()
        self.assertTrue(proxy.was_called("f1"), '\nمتد f1 روی شئ مورد نظر فراخوانی شده است.')
        self.assertFalse(proxy.was_called("f2"), '\nمتد f2 روی شئ مورد نظر فراخوانی نشده است.')
        proxy.f2()
        self.assertTrue(proxy.was_called("f2"), '\nمتد f2 روی شئ مورد نظر فراخوانی شده است.')
        self.assertFalse(proxy.was_called("not valid"), '\nمتد not valid روی شئ مورد نظر فراخوانی نشده است.')

    def test_sample_4(self):
        t = Hi()
        proxy = Proxy(t)

        try:
            proxy.last_invoked_method()
        except Exception as e:
            self.assertEqual("No Method Is Invoked", str(e), '\nتا به حال متد معتبری فراخوانی نشده، پس باید استثنایی با پیغام No Method Is Invoked پرتاب شود.')

        proxy.f1()
        proxy.f2()
        self.assertEqual("f2", proxy.last_invoked_method(), '\nآخرین متد معتبری که فراخوانی شده، f2 است.')