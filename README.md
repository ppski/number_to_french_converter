# Number to French Converter
This is a simple number to French (fr_FR) converter for French numbers up to 999,999. It takes a list of numerical numbers as input and returns a list of the corresponding written numbers in French.

The output respects the [1990 spelling rule changes](https://en.wikipedia.org/wiki/Reforms_of_French_orthography#Rectifications_of_1990).

## Getting Started

### Dependencies
* Python 3.x


### Installing

```bash
git clone https://github.com/ppski/number_to_french_converter.git
cd number_to_french_converter
```


## Running the Application

The application can be run using the following command:

```bash
python3 converter.py
```

To change the dataset, modify the `dataset` variable in the `converter.py` file.

The output will be printed out in the terminal.

## Acknowledgments

The base code was generated using [ChatGPT4](https://chat.openai.com/?model=gpt-4) with the default system prompt on March 14, 2024. The following prompt was used to generate the code:

```
You are a Python developper with perfect written French. Your task is to write (not explain) a Python program that takes a list of numbers (integers) and returns a list of French numbers (strings) written according to the 1990 spelling rule changes. Your program must support numbers up to 999,999.

Test your algorithm with this `input` and `expected_output`:

`input = [252, 2045, 200000, 180000, 130, 1110, 74, 77, 95, 99, 71, 81, 91, 82, 80, 70, 80, 90, 21]`

`expected_output = ["deux-cent-cinquante-deux", "deux-mille-quarante-cinq", "deux-cent-milles", "cent-quatre-vingt-milles", "cent-trente", "mille-cent-dix", "soixante-quatorze", "soixante-dix-sept", "quatre-vingt-quinze", "quatre-vingt-dix-neuf", "soixante-et-onze", "quatre-vingt-un", "quatre-vingt-onze",  "quatre-vingt-deux", "quatre-vingts", "soixante-dix", "quatre-vingts",  "quatre-vingt-dix", "vingt-et-un"]`

```

