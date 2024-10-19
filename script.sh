#!/bin/bash

# Функция возвращает размер переданного файла или директории ($1).
get_entity_size() {
  if [ ! -e "$1" ]; then
    echo "Ожидается путь к файлу или директории первым аргументом!"
    return 1
  fi

  du --bytes --summarize "$1" | cut -f1
}

# Функция выводит список файлов и директорий вместе с их размерами в текущей директории.
print_entities() {
  for FILE in *; do
    FILE_SIZE="$(get_entity_size "$FILE")"
    printf "%15d | %s\n" "$FILE_SIZE" "$FILE"
  done
}

# Функция выводит список файлов и директорий вместе с их размерами в текущей директории.
# Вывод отсортирован по уменьшению размера.
print_sorted_by_size_entities() {
  print_entities | sort -g -r
}

printf " %s | %s\n" "Размер (байты)" "Имя файла"
echo "-------------------------------"
print_sorted_by_size_entities
