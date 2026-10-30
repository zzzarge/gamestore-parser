from cleaner import run_cleaner
from scraper import run_scraper

def main():
    print('Сбор данных')
    run_scraper()
    print('Очистка')
    run_cleaner()

if __name__ == '__main__':
    main()