from mcolour import change_style_text

poem = """Вечоріло
Гуділи мухи
Світив ліхтарик
Кипіла вода в чайнику
Венера спалахнула на небі
Дерева шуміли
Хмари розійшлися
Листя зеленіло"""

if __name__ == "__main__":
    styled_poem = change_style_text(poem, text_style='3', text_color='30', background_color='45')
    print(styled_poem)
