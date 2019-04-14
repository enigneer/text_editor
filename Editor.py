import text_editor_classes as te

print('''
---------------------------------------------------------------------------------
---------------------------  T E X T    E D I T O R  ----------------------------
---------------------------------------------------------------------------------
    
WITAJ W EDYTORZE TEKSTU. ŻEBY WPROWADZIĆ TEKST DO EDYCJI MOŻESZ WPISAĆ GO RĘCZNIE
LUB ZASTOSOWAĆ SKRÓT KLAWISZY "CTRL+C" I "CTRL+V" I ZATWIERDZIĆ KLAWISZEM ENTER.
    
JEŻELI CHCESZ OPUŚCIĆ PROGRAM WPISZ: "EXIT" I ZATWIERDZIĆ KLAWISZEM ENTER.
''')

# <<<<<<< KOD PROGRAMU >>>>>>>>

sentence = input("Podaj zdanie lub ciąg wyrazów oddzielonych 'spacjami': ")

while sentence.upper() != "EXIT":

    print("\nTwoj tekst: \n")
    print(">>>", sentence, "\n")

    print("W jaki sposób chcesz przefiltrować swój teskt?")
    print('''
    1. Wygeneruj listę elementów, z których składa się tekst (wyrazy i liczby) ---> wpisz '1'
    2. Wygeneruj listę liczb, które pojawiają się w tekście ----------------------> wpisz '2'
    3. Wygeneruj listę wyrazów, z których składa się tekst -----------------------> wpisz '3'
    4. Zakończ program -----------------------------------------------------------> wpisz 'EXIT'
    ''')

    opcja = input("\nTwój wybór to numer: ")

    single_elements = te.TextEditor(sentence, opcja)
    list_of_elements = single_elements.elements_in_text()

    if opcja == 1 or opcja == '1':
        print("\nOto twoja przefiltrowana lista (wyrazy i liczby): \n")
        print(">>>", list_of_elements)
    if opcja == 2 or opcja == '2':
        print("\nOto twoja przefiltrowana lista (liczby): \n")
        print(">>>", list_of_elements)
    if opcja == 3 or opcja == '3':
        print("\nOto twoja przefiltrowana lista (wyrazy): \n")
        print(">>>", list_of_elements)
    if opcja.upper() == "EXIT":
        print("\nKoniec działania programu.\n")
        break

    elements = te.ElementsEditor(list_of_elements)

    if opcja == 1 or opcja == '1':
        print('''
        1. Wyszukaj element (wynikiem jest numer pierwszej pozycji na której wystąpił) ---> wpisz '1'
        2. Ile razy w tekście występuje szukany element ----------------------------------> wpisz '2'
        3. Cofnij ------------------------------------------------------------------------> wpisz 'BACK'
        ''')

        opcja_1 = input("\nTwój wybór to numer: ")

        if opcja_1 == 1 or opcja_1 == '1':
            element = input("\nCzego szukasz?: ")
            element_position = elements.finding_firs(element)
            print("\nElement '{}', którego szukasz wystąpił na pozycji nr {}".format(element, element_position))
        elif opcja_1 == 2 or opcja_1 == '2':
            element = input("\nIlość sztuk jakiego elementu Cie intersuje?: ")
            element_count = elements.count_of_element(element)
            print("\nElement '{}', którego szukasz wystąpił w tekście {} razy".format(element, element_count))
        elif opcja_1.upper() == "BACK":
            pass
        else:
            print("Something goes wrong...")

    if opcja == 2 or opcja == '2':
        print('''
        1. Wyszukaj element (wynikiem jest numer pierwszej pozycji na której wystąpił) ---> wpisz '1'
        2. Ile razy w tekście występuje szukany element ----------------------------------> wpisz '2'
        3. Posortuj liczby rosnąco -------------------------------------------------------> wpisz '3'
        4. Posortuj liczby malejąco ------------------------------------------------------> wpisz '4'
        5. Cofnij ------------------------------------------------------------------------> wpisz 'BACK'
            ''')

        opcja_2 = input("\nTwój wybór to numer: ")

        if opcja_2 == 1 or opcja_2 == '1':
            number = int(input("\nCzego szukasz?: "))
            number_position = elements.finding_firs(number)
            print("\nElement '{}', którego szukasz wystąpił na pozycji nr {}".format(number, number_position))
        elif opcja_2 == 2 or opcja_2 == '2':
            number = int(input("\nIlość sztuk jakiego elementu Cie intersuje?: "))
            number_count = elements.count_of_element(number)
            print("\nElement '{}', którego szukasz wystąpił w tekście {} razy".format(number, number_count))
        elif opcja_2 == 3 or opcja_2 == '3':
            increase_list = elements.sorting_numbers("yes")
            print("\nLista numerów posorotwanych rosnąco:\n")
            print(">>>", increase_list)
        elif opcja_2 == 4 or opcja_2 == '4':
            decrease_list = elements.sorting_numbers("no")
            print("\nLista numerów posorotwanych rosnąco:\n")
            print(">>>", decrease_list)
        elif opcja_2.upper() == "BACK":
            pass
        else:
            print("Something goes wrong...")

    if opcja == 3 or opcja == '3':
        print('''
        1. Wyszukaj element (wynikiem jest numer pierwszej pozycji na której wystąpił) ---> wpisz '1'
        2. Ile razy w tekście występuje szukany element ----------------------------------> wpisz '2'
        3. Posortuj wyrazy alfabetycznie -------------------------------------------------> wpisz '3'
        4. Posortuj wyrazy anty-alfabetycznie --------------------------------------------> wpisz '4'
        5. Cofnij ------------------------------------------------------------------------> wpisz 'BACK'
            ''')

        opcja_3 = input("\nTwój wybór to numer: ")

        if opcja_3 == 1 or opcja_3 == '1':
            word = input("\nCzego szukasz?: ")
            word_position = elements.finding_firs(word)
            print("\nElement '{}', którego szukasz wystąpił na pozycji nr {}".format(word, word_position))
        elif opcja_3 == 2 or opcja_3 == '2':
            word = input("\nIlość sztuk jakiego elementu Cie intersuje?: ")
            word_count = elements.count_of_element(word)
            print("\nElement '{}', którego szukasz wystąpił w tekście {} razy".format(word, word_count))
        elif opcja_3 == 3 or opcja_3 == '3':
            alphabetic_list = elements.sorting_words("yes")
            print("\nLista wyrazów posorotwanych alfabetycznie:\n")
            print(">>>", alphabetic_list)
        elif opcja_3 == 4 or opcja_3 == '4':
            unalphabetic_list = elements.sorting_words("no")
            print("\nLista wyrazów posorotwanych anty-alfabetycznie:\n")
            print(">>>", unalphabetic_list)
        elif opcja_3.upper() == "BACK":
            pass
        else:
            print("Something goes wrong...")

    input("Wciśnij 'ENTER' żeby kontynuować.")


