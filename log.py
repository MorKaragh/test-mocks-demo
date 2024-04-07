import logging
import sys

# Создание объекта логгера
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Создание объекта форматирования
class SingleLineFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)

    def format(self, record):
        record.message = record.getMessage()
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        s = self._fmt % record.__dict__
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            if s[-1:] != "\n":
                s = s + "\n"
            try:
                s = s + record.exc_text
            except UnicodeError:
                s = s + record.exc_text.decode(sys.getfilesystemencoding(), 'replace')
        return s

formatter = SingleLineFormatter('%(asctime)s - %(levelname)s - %(message)s')

# Создание объекта обработчика для записи в stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

# Добавление обработчика в логгер
logger.addHandler(stdout_handler)

# Пример использования логгера
try:
    result = 10 / 0
except Exception as e:
    logger.exception(e)
