---
title: PMPrinterTest
apple_id: DTS10003404
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2009-02-13'
source_url: https://developer.apple.com/library/archive/samplecode/PMPrinterTest/Listings/Readme_txt.html
archived_at: '2026-07-18T03:18:36.084848Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PMPrinterTest](PMPrinterTest.md)


[Next](main.m.md)[Previous](PMPrinterTest.md)

# Readme.txt

```
PMPrinterTest demonstrates how you can use the PMPrinter APIs to obtain the list of connected printers and obtain information such as the user and CUPS queue names, the printer model and the printer URI as well as current printer state. This sample requires Xcode 3.1 and Mac OS X 10.5 to build, but should run on Mac OS X 10.4 as well.

In this sample, we use PMServerCreatePrinterList() to obtain a list of known printers. For each printer in the list we obtain the name, id, location, URI, state, model and if the printer is the default, is a favorite and is remote. Once this information is gathered for each printer, it is displayed in an NSTableView for perusal. To refresh the list (such as after adding a printer or sending a print job) there is a Refresh command in the application menu (or you can use Command-R).

PMPrinterTestController.h/m
Implements a controller object to to do the work described above. The method that does all the work is the -makeList method, and is called on -awakeFromNib (in order to get the initial list) and when the Refresh command is sent.
```

[Next](main.m.md)[Previous](PMPrinterTest.md)

