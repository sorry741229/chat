#讀取檔案
def read_file(filename): 
	lines = []
	with open (filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#轉換格式
def convert(lines): #轉換
	new = []
	person = None
	for line in lines:
		if line == 'Martin':
			person = 'Martin' # 這邊要注意等於用法跟上面等於不同
			continue
		elif line == 'Jie':
			person = 'Jie'    # 這邊要注意等於用法跟上面等於不同
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename , 'w') as f:
		for line in lines:
			f.write(line + '\n')



#主要function
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)


main()