## Short Info
Replace numerals with corresponding numbers in the given text.
Available on [PyPI](https://pypi.org/project/numberize/).
Consider checking out [Wiki](https://github.com/DanATW/numberize/wiki) for more info.
## Supported languages
* Ukrainian
* Russian
* English
## Requirements
* python 3.6+
* NLTK Data

## How to install it?
```pip install numberize```

## How to install requirements?
After installing this package

```python -m nltk.downloader punkt```

## How to use it?
```
import numberize
numberizer = numberize.Numberizer(lang='ru')    #or 'uk', 'en'
new_text = numberizer.replace_numerals(old_text)
   ```
