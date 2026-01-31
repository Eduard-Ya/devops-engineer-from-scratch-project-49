echo "=== Установка пакета ==="
echo "pip install -e ."
sleep 2
echo ""
echo "=== Запуск brain-even (победа) ==="
echo "brain-even"
sleep 1
echo "Welcome to the Brain Games!"
echo "May I have your name? TestUser"
echo "Hello, TestUser!"
echo "Answer 'yes' if the number is even, otherwise answer 'no'."
sleep 1
echo "Question: 15"
echo "Your answer: no"
echo "Correct!"
sleep 1
echo "Question: 42"
echo "Your answer: yes"
echo "Correct!"
sleep 1
echo "Question: 77"
echo "Your answer: no"
echo "Correct!"
echo "Congratulations, TestUser!"
echo ""
sleep 2
echo "=== Запуск brain-even (поражение) ==="
echo "brain-even"
sleep 1
echo "Welcome to the Brain Games!"
echo "May I have your name? FailUser"
echo "Hello, FailUser!"
echo "Answer 'yes' if the number is even, otherwise answer 'no'."
sleep 1
echo "Question: 24"
echo "Your answer: yes"
echo "Correct!"
sleep 1
echo "Question: 57"
echo "Your answer: yes"
echo "'yes' is wrong answer ;(. Correct answer was 'no'."
echo "Let's try again, FailUser!"
