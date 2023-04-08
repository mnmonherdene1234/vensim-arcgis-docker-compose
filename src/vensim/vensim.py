import pysd

model = pysd.read_vensim("src/vensim/models/teacup.mdl")
stocks = model.run(progress=True, output_file="src/vensim/data/teacup.csv")
print(stocks)