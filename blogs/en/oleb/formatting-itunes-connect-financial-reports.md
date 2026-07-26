---
title: Formatting iTunes Connect Financial Reports
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2009/09/formatting-itunes-connect-financial-reports/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:7f7639a410bd3a63'
translated: false
---

> 原文：[Formatting iTunes Connect Financial Reports](https://oleb.net/blog/2009/09/formatting-itunes-connect-financial-reports/)　·　Ole Begemann

# Formatting iTunes Connect Financial Reports

**Update 2009-09-23:** There is an updated version of the script available. Please [see the corresponding blog post](https://oleb.net/blog/2009/09/updated-itunes-connect-financial-reports-to-html-script/) and [get the newest version of the code from GitHub](https://github.com/ole/itunesconnect-financialreports).

The monthly financial reports Apple provides to iPhone developers in iTunes Connect are plain tab-separated text files. To print those reports for our tax accountants or the taxman, we must apply a little formatting. Since importing text files into a spreadsheet involves some manual work (some columns have to be marked as numeric or text) and I do not need to do further calculations with the data at the moment, I wrote a Ruby script that converts Apple’s text files into printable HTML tables. To use the script, download all financial reports from iTunes Connect into a folder and run the script as follows:

```
./financialreport_to_html.rb *.txt
```

The script will create a .html file with the same name for every file you specify on the command line. You can use the `-o` option to force it to overwrite existing files.

The script uses a settings file in [YAML](http://www.yaml.org/) format to configure things like column headings, column types and which columns to exclude from the formatted page (there’s a lot of columns to fit on one page). Have a look at `financialreport_to_html_settings.yaml` to see the available options.

The HTML template code, complete with CSS, is directly embedded in the script file. I opted for a simple table that looks good when printed but it should be easy for you to adapt the styling to your needs. The only thing you still have to do manually is to set your printer to landscape format as the page orientation cannot be specified in CSS.

The result looks like this:

![Output from financialreport_to_html.rb](https://oleb.net/media/financialreport_to_html-output-screenshot.png)

<sub>Output from `financialreport_to_html.rb`.</sub>

~~Download the script: financialreport_to_html.zip~~ [Get the newest version from GitHub](https://github.com/ole/itunesconnect-financialreports). You can do whatever you want with it. I hope you find it useful.
