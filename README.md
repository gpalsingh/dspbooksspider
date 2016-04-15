PBooksSpider
Scrapy spider to download all books related to DSP books on http://serv.yanchick.org/Books/

[![Codacy Badge](https://api.codacy.com/project/badge/grade/6e6bd089c57a4d35872f5affa3b45f23)](https://www.codacy.com/app/gurkirpal204/dspbooksspider)
[![Code Climate](https://codeclimate.com/github/gpalsingh/dspbooksspider/badges/gpa.svg)](https://codeclimate.com/github/gpalsingh/dspbooksspider)
[![Test Coverage](https://codeclimate.com/github/gpalsingh/dspbooksspider/badges/coverage.svg)](https://codeclimate.com/github/gpalsingh/dspbooksspider/coverage)
[![Issue Count](https://codeclimate.com/github/gpalsingh/dspbooksspider/badges/issue_count.svg)](https://codeclimate.com/github/gpalsingh/dspbooksspider)

# Getting the spider
*Note*: You need to have `Python2.7`, `pip` and `git` pre-installed.

1. Clone the github repo to get the spider.

    ```sh
    $ git clone https://github.com/gpalsingh/dspbooksspider.git
    ```

2. Install the dependencies.

    ```sh
    $ pip install scrapy appdirs colorama
    ```

# Running the spider
1. Move to the directory in which the `README.md` file lies.
2. Use the `getbooks` shell scipt.
    ```sh
    $ ./getbooks
    ```

    or
                                            
    Run the spider manually.
    ```sh
    $ scrapy crawl dspbooks
    ```

# Getting the saved data
On running the spider, it will make a link to the location where
the downloaded data is placed by the name `saved_books`. The exact location
is system dependent. To get the absolute path to the files run the 
`wherefiles` script.

```sh
$ ./wherefiles
```
