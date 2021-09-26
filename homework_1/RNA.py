def nucleic_acid_checker(x: str) -> bool:
    """ Принимает строку. Проверяет последовательность нуклеиновой кислоты. Пропускает РНК и ДНК,
    не пропускает иные последовательности. Возвращает логическое значение, предназначена для работы в цикле """

    check_unit = {*x}
    dna_check = {"A", "T", "G", "C", "a", "t", "g", "c"}
    rna_check = {"A", "U", "G", "C", "a", "u", "g", "c"}
    if check_unit <= dna_check:
        print("\n", "Принято успешно", sep="")
        return True
    elif check_unit <= rna_check:
        print("\n", "Принято успешно", sep="")
        return True
    else:
        print("\n", "Ваша последовательность не соотвествует формату. Пожалуйста, введите \n"
                    "последовательность ДНК (из букв A,T,C,G) или последовательность РНК (из букв A,U,C,G) \n", sep="")
        return False


def nucleic_acid_type(x: str) -> str:
    """ Принимает строку. Определяет тип нуклеиновой кислоты. Работает только с последовательностями
      нуклеиновых кислот. Возвращает тип нуклеиновой кислоты: DNA или RNA. Уточняет тип нулкеиновой кислоты
      (DNA или RNA), если его невозможно определить."""

    check_unit = {*x}
    dna_check_big = {"T"}
    rna_check_big = {"U"}
    dna_check_small = {"t"}
    rna_check_small = {"u"}
    if dna_check_big <= check_unit or dna_check_small <= check_unit:
        return "DNA"
    elif rna_check_big <= check_unit or rna_check_small <= check_unit:
        return "RNA"
    else:
        print("\n", "Указанная последовательность не может быть однозначно определена. Пожалуйста, укажите тип \n"
                    "нуклеиновой кислоты (DNA или RNA):  ", sep="", end="")
        while True:
            verify = input()
            if verify == "RNA" or verify == "DNA":
                return verify
            print("Вы неправильно ввели данные. Напишите либо DNA, либо RNA")


def case_sensitive(x: str, func) -> str:
    """ Принимает строку и рабочую функцию. Учитывает регистр буквы: пропускает буквы верхнего регистра и
     временно преобразует буквы нижнего регистра. Возвращает преобразованную рабочей функцией строку.
      Рабочие функции: reverse, transcribe_nucl, complement """

    x = list(x)
    for i in range(len(x)):
        if "a" <= x[i] <= "u":
            x[i] = x[i].upper()
            x[i] = func(x[i])
            x[i] = x[i].lower()
        else:
            x[i] = func(x[i])
    x = "".join(x)
    return x


def reverse(x: str) -> str:
    """Принимает строку. Возвращает Инвертированную последовательность"""

    x = x[::-1]
    return x


def transcribe_nucl(letter: str) -> str:
    """ Принимает букву ДНК в верхнем регистре. Возвращает транскрибированную букву РНК"""

    letters = {"A": "U", "T": "A", "G": "C", "C": "G"}
    letter = letters[letter]
    return letter


def complement_dna_nucl(letter: str) -> str:
    """Принимает букву ДНК в верхнем регистре и возвращает комплементарную букву ДНК"""

    letters = {"A": "T", "T": "A", "G": "C", "C": "G"}
    letter = letters[letter]
    return letter


def complement_rna_nucl(letter: str) -> str:
    """Принимает букву РНК в верхнем регистре и возвращает комплементарную букву РНК """

    letters = {"A": "U", "U": "A", "G": "C", "C": "G"}
    letter = letters[letter]
    return letter


def complement(x: str) -> str:
    """Принимает последовательность ДНК или РНК. Определяет тип нуклеиновой кислоты и применяет к ней
    соотвествующую функцию. Возращает тип нуклеиновой кислоты и  комплементарную последовательность
    (ДНК -> ДНК и РНК -> РНК). Зависит от complement_dna, complement_rna, case_sensitive и nucleic_acid_type"""

    if nucleic_acid_type(x) == "DNA":
        return f" ДНК: {case_sensitive(x, complement_dna_nucl)}"
    else:  # type == "RNA"
        return f" РНК: {case_sensitive(x, complement_rna_nucl)}"


def command_navigator(intsruction: str, item: str) -> bool:
    """Принимает командную инструкцию и объект, с которым будет работать. Передаёт объект в функцию,
    соотвествующую команде. Печатает итог работы функции, соответствующей командной инструкции. Предназначена
    для работы в цикле через логическую переменную flag (возвращает логический тип)
    Зависит от reverse, transcribe_nucl, complement, case_sensitive, nucleic_acid_type"""

    if intsruction == "reverse":
        print("\n", "Ваша инвертированная последовательность: ", reverse(item), "\n", sep="")
        return False
    elif intsruction == "transcribe":
        if nucleic_acid_type(item) == "DNA":
            print("\n", "Ваша транскрибированная последовательность: ", case_sensitive(item, transcribe_nucl), "\n",
                  sep="")
            return False
        else:
            print("\n", "Ваша последовательность не является ДНК, поэтому её нельзя транскрибировать."
                        " Пожалуйста, введите другую последовательность \n", sep="")
            return True
    elif intsruction == "complement":
        print("\n", "Ваша комплементарная последовательность", complement(item), "\n", sep="")
        return False
    elif intsruction == "reverse complement":
        print("\n", "Ваша обратная комплементарная последовательность", complement(reverse(item)), "\n", sep="")
        return False


def nucleic_acid_utility():
    """Программа работает с последовательностями нуклеиновых кислот ДНК и РНК. Возможности:
    инвертирование последовательности (reverse), траснкрибирование ДНК в РНК (transcribe),
    построение комплементарной последовательности: ДНК для ДНК и РНК для РНК (complement),
    построение обратной комплементарной последовательности (reverse complement). Работает
    в интерактивном режиме, для выхода ввести команду exit (работает только из основного меню)"""

    commands = {"reverse", "transcribe", "complement", "reverse complement", "exit"}
    print("Добро пожаловать!")
    while True:
        print()
        command = input("Список команд программы: \n"
                        "reverse, transcribe \n"
                        "complement, reverse complement \n"
                        "exit \n\n"
                        "Введите команду: ")
        if command in commands:
            if command == "exit":
                print("\n", "Приходите к нам ещё!", sep="")
                break
            flag = True
            while flag:
                print()
                nucleic_acid = input(f"Ваша команда - {command}. Введите последовательность нуклеиновой кислоты."
                                     " Для смены команды \n(в том числе для выхода из программы по команде exit)"
                                     " введите 'change command':  ")
                if nucleic_acid == "change command":
                    break
                if nucleic_acid_checker(nucleic_acid) is False:  # function checks whether it is DNA or RNA
                    continue
                else:
                    flag = command_navigator(command, nucleic_acid)  # applies command from input to sequence
                    # from anoter input
        else:
            print("\n", "Такая команда не поддерживается. Пожалуйста, введите команду из списка: \n ", sep="")
            continue


nucleic_acid_utility()
