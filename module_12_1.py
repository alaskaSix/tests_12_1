import runner as r
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = r.Runner('Ирина')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = r.Runner('Максим')
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = r.Runner("Ольга")
        runner_4 = r.Runner("Андрей")
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


if __name__ == "__main__":
    unittest.main()




'''Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

Пункты задачи:
Скачайте исходный код для тестов.
Создайте класс RunnerTest и соответствующие описанию методы.
Запустите RunnerTest и убедитесь в правильности результатов.'''