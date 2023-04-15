import pysd

model = pysd.read_vensim("src/vensim/models/population.mdl")

# Modify the value of the INITIAL TIME parameter
model.set_components({'INITIAL TIME': 2004})

stocks = model.run(progress=True, output_file="src/vensim/data/population.csv", params={
    "Average lifetime": 60,
    "Birth rate": 0.01,
}, final_time=2010)

print(stocks)
