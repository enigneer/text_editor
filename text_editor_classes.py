class TextEditor(object):   # KLASA GENERUJĄCA TABLICĘ ELEMENTÓW (WYRAZÓW, LICZB) Z WPROWADZONEGO TEKSU

    def __init__(self, text, option):
        self.text = text
        self.option = option

    def __str__(self):
        description = "\nTextEditor tworzy listę wyrazów i liczb na podstawie wprowadzonego przez użytkownika tekstu.\n"
        return description

    def elements_in_text(self):

        word = ""
        words = [1]
        i = 0
        # WRONG_SIGNS = [" ", ".", ",", ":", ";"]

        # generowanie listy wyrazów i liczb z wprowadzonego tekstu (razem z wyrazami "pustymi")
        for sign in self.text:
            if sign != " " and sign != "." and sign != "," and sign != ":"\
                           and sign != ";" and sign != "(" and sign != ")":
                word += sign
                words[i] = word
            else:
                word = ""
                words.append("")
                i += 1

        # generowanie listy wyrazów i liczb bez pustych pól
        final_elements = [word for word in words if word != ""]

        option = self.option    # zmienna pomocnicza

        while True:
            if option == '1':
                return final_elements   # funkcja zwraza listę wyrazów i liczb
            elif option == '2':
                final_numbers = [int(num) for num in final_elements if num.isnumeric()]
                return final_numbers   # funkcja zwraza listę wyrazów
            elif option == '3':
                final_words = [word for word in final_elements if not word.isnumeric()]
                return final_words   # funkcja zwraza listę wyrazów
            elif option.upper() == "EXIT":
                break
            else:
                print("Nie ma takiej opcji. Podaj inną opcję. Do wyboru opcja 1, 2 lub 3.\n")
                option = (input("Twoja nowa opcja to:\n"))


class ElementsEditor(object):  # KLASA EDYTUJĄCA LISTĘ WYRAZÓW

    def __init__(self, elements_list):
        self.elements_list = elements_list

    def __str__(self):
        description = "\nWordsEditor pozwala edytować listę wyrazów oraz uzyskiwać informację na temat tej listy.\n"
        return description

    def finding_firs(self, element):   # Funkcja zwracająca indeks pierwszego wsytąpienia szukanego wyrazu w liście
        element_index = self.elements_list.index(element)
        return element_index

    def count_of_element(self, element):  # Funkcja zwracająca liczbę wsytąpień szukanego wyrazu w liście
        element_count = self.elements_list.count(element)
        return element_count

    def sorting_words(self, alphabet):
        sorted_words_list = self.elements_list
        if alphabet == "yes":
            sorted_words_list.sort(reverse=False)
        elif alphabet == "no":
            sorted_words_list.sort(reverse=True)
        else:
            print("Something goes wrong with sorting list..")
        return sorted_words_list

    def sorting_numbers(self, increase):
        sorted_num_list = self.elements_list
        if increase == "yes":
            sorted_num_list.sort(reverse=False)
        elif increase == "no":
            sorted_num_list.sort(reverse=True)
        else:
            print("Something goes wrong with sorting list..")
        return sorted_num_list
