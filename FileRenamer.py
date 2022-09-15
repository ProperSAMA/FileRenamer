import os

file_dir = os.chdir('F:\py_test\\file')
file_list = os.listdir()
ignore_count = 0
rename_count = 0
error_count = 0

print('')
print('=== 操作开始 ===')

for file in file_list:
    file_split = file.split('_')
    if len(file_split) == 4:
        new_name = file_split[3]
        try:
            os.rename(file, new_name)
            rename_count += 1
        except FileExistsError:
            print(f'无法重命名{file}: 目标文件名“{new_name}”已存在')
            error_count += 1
    else:
        ignore_count += 1

print('=== 操作结束 ===')
print(f'本次共重命名{rename_count}个文件,忽略了{ignore_count}个文件')
print(f'{error_count}个文件出现异常')
print('')