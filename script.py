#!/usr/bin/env python3
import os
import subprocess

# Функция возвращает размер записи файловой системы по имени.
def get_entry_size(entry_name):
    try:
        command = ['du','--bytes', '--summarize', entry_name]
        du_output = subprocess.check_output(command)
        size = int(du_output.split()[0].decode('utf-8'))
    except:
        return 0

    return size

# Функция возвращает список записей файловой системы вместе с их размерами.
def get_current_directory_entries_with_size():
    entries = []

    entries_names = os.listdir()
    for entry_name in entries_names:
        entries.append({
            'name': entry_name,
            'size': get_entry_size(entry_name),
        })

    return entries

# Функция принимает список записей и сортирует их по уменьшению размера.
def sort_downsizing(entries):
    def key_size(entry):
        return entry['size']
    entries.sort(key = key_size, reverse = True)

# Главная функция выводит список записей файловой системы.
def main():
    entries = get_current_directory_entries_with_size()
    sort_downsizing(entries)

    print("Размер (байты) | Имя файла")
    for entry in entries:
        print("%14s | %s" % (entry['size'], entry['name']))

if __name__ == "__main__":
    main()
