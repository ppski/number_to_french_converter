class FrenchNumberConverter:
    def __init__(self, numbers: list[str]):
        # fmt: off
        self.units = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]

        # fmt: off
        self.teens = ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
        
        # fmt: off
        # Set empty strings for indexing
        self.tens = ["", "", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]

        self.written_list = [self.number_to_french(n) for n in numbers]

    def number_to_french(self, n: int) -> str:
        """
        Breakdown the number into smaller parts and convert to French.
        """
        if not isinstance(n, int):
            try:
                n = int(n)
            except ValueError:
                return f"{n} is not an integer or cannot be converted to an integer. Cannot convert to written French."
        if n < 100:
            return self._convert_below_100(n)
        if n == 100:
            return "cent"
        if n < 200:
            return f"cent-{self.number_to_french(n - 100)}"
        if n < 2000:
            return self._convert_below_2000(n)
        if n < 1000000:
            return self._convert_above_2000(n)
        return f"{n} is out of range."

    def _convert_below_100(self, n: int) -> str:
        """
        Convert numbers 0-99 (inclusive).
        """
        if n < 10:
            # 0-10
            return self.units[n]
        if n % 10 == 1:
            # numbers ending in 1
            if n == 11:
                return self.teens[n // 10]
            if n == 71:
                return "soixante-et-onze"
            if n == 81:
                return "quatre-vingt-un"
            if n == 91:
                return "quatre-vingt-onze"
            return self.tens[n // 10] + "-et-un"
        if n < 20:
            # 10-19
            return self.teens[n - 10]
        if n < 70:
            # 20-69
            if n % 10 == 0:
                return self.tens[n // 10]
            return f"{self.tens[n // 10]}-{self.units[n % 10]}"
        if n < 80:
            # 72 - 79
            return f"soixante-{self.teens[n - 70]}"
        if n < 100:
            if n == 80:
                return "quatre-vingts"
            if n == 90:
                return "quatre-vingt-dix"
            if n < 91:
                # 82 - 90
                return f"quatre-vingt-{self.units[n % 10]}"
            # 91 - 99
            return f"quatre-vingt-{self.teens[n - 90]}"

    def _convert_below_2000(self, n: int) -> str:
        """
        Convert numbers 200-1999 (inclusive).
        """
        if n < 1000:
            # 200 - 999
            if n % 100 == 0:
                return f"{self.units[n // 100]}-cents"
            return f"{self.units[n // 100]}-cent-{self.number_to_french(n % 100)}"
        if n == 1000:
            return "mille"
        if n < 2000:
            # 1001 - 1999
            return f"mille-{self.number_to_french(n - 1000)}"

    def _convert_above_2000(self, n: int) -> str:
        """
        Convert numbers 2000-999999 (inclusive).
        """
        if n % 1000 == 0:
            prefix = self.number_to_french(n // 1000)
            if prefix.endswith(("cents", "milles", "vingts")):
                prefix = prefix[:-1]
            return f"{prefix}-milles"

        return f"{self.number_to_french(n // 1000)}-mille-{self.number_to_french(n % 1000)}"


if __name__ == "__main__":
    # fmt: off
    dataset = [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]

    convertor = FrenchNumberConverter(dataset).written_list
    print(convertor)
