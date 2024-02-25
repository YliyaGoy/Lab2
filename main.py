class TuringMachine:
    def __init__(self, tape, initial_state, transition_function, final_states):
        self.tape = tape  # Лента
        self.head = 0  # Позиция головки
        self.state = initial_state  # Текущее состояние
        self.transition_function = transition_function  # Функция перехода
        self.final_states = final_states  # Окончательные состояния

    def move(self, direction):
        if direction == 'L':
            self.head -= 1  # Двигаемся влево
        elif direction == 'R':
            self.head += 1  # Двигаемся вправо

    def run(self):
        while self.state not in self.final_states:  # Пока текущее состояние не является окончательным
            if self.head == len(self.tape):  # Если головка достигла конца ленты
                self.tape.append('')  # Добавляем пустой символ в конец ленты
            elif self.head == -1:  # Если головка ушла за левый край ленты
                self.tape.insert(0, '')  # Вставляем пустой символ в начало ленты
                self.head = 0  # Устанавливаем головку в начало

            current_symbol = self.tape[self.head]  # Текущий символ под головкой
            if (self.state, current_symbol) in self.transition_function:  # Если существует правило перехода для текущего состояния и символа
                new_state, new_symbol, move_direction = self.transition_function[(self.state, current_symbol)]  # Получаем новое состояние и символ, а также направление движения
                self.tape[self.head] = new_symbol  # Записываем новый символ на ленту
                self.state = new_state  # Устанавливаем новое состояние
                self.move(move_direction)  # Двигаемся в заданном направлении
            else:
                break  # Если нет правила перехода, то завершаем выполнение

# Определение функции перехода для удвоения символов '1'
transition_function = {
    ('q0', '1'): ('q0', '1', 'R'),  # Если находим '1' в состоянии q0, то заменяем его на '1' и идем вправо
    ('q0', ''): ('q1', '1', 'L'),  # Если достигли пустого символа в состоянии q0, то переходим в состояние q1 и идем влево
    ('q1', '1'): ('q1', '1', 'L'),  # Если находим '1' в состоянии q1, то оставляем его без изменений и идем влево
    ('q1', ''): ('q2', '1', 'R'),  # Если достигли пустого символа в состоянии q1, то переходим в q2, ставим '1' и идем вправо
}

# Инициализация ленты, начального состояния, функции перехода и окончательных состояний
tape = ['1', '1', '1']  # Начальное состояние ленты
initial_state = 'q0'  # Начальное состояние
final_states = {'q2'}  # Окончательное состояние
tm = TuringMachine(tape, initial_state, transition_function, final_states)  # Создание машины Тьюринга

# Запуск машины Тьюринга
tm.run()

# Вывод результата
print("Результат удвоения символов '1':", tm.tape)