from pathlib import Path

root_path = Path(__file__).parents[2]
data_path = root_path / 'data/training/file.txt'
text = data_path.read_text()

print(text)