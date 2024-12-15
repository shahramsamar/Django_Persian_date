# Django Persian Date

A utility library for handling Persian (Jalali) dates in Django projects. This library allows you to work seamlessly with Persian dates, offering conversion, formatting, and localization capabilities.

## Features

- Convert Gregorian dates to Persian dates.
- Format Persian dates with custom templates.
- Support for Django's date handling utilities.
- Lightweight and easy to integrate into existing Django projects.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shahramsamar/Django_Persian_date.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Django_Persian_date
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Add the library to your Django project:
   ```python
   from persian_date import convert_to_persian, format_persian_date
   ```

2. Convert a Gregorian date to a Persian date:
   ```python
   from datetime import datetime
   
   gregorian_date = datetime.now()
   persian_date = convert_to_persian(gregorian_date)
   print(persian_date)
   ```

3. Format a Persian date:
   ```python
   formatted_date = format_persian_date(persian_date, "%Y/%m/%d")
   print(formatted_date)
   ```

## Examples

### Example 1: Simple Conversion
```python
from datetime import datetime
from persian_date import convert_to_persian

gregorian_date = datetime(2024, 12, 15)
persian_date = convert_to_persian(gregorian_date)
print(f"Persian Date: {persian_date}")
```

### Example 2: Formatting Persian Dates
```python
from persian_date import format_persian_date

persian_date = (1402, 9, 24)  # Example Persian date
template = "%A, %d %B %Y"
formatted_date = format_persian_date(persian_date, template)
print(f"Formatted Persian Date: {formatted_date}")
```

## Requirements

- Python 3.7+
- Django 3.2+

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

- **Author**: Shahramsamar
- **Email**: [shahramsamar2010@gmail.com](mailto:shahramsamar2010@gmail.com)
- **GitHub**: [Shahramsamar](https://github.com/shahramsamar)

 
