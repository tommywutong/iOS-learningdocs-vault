---
title: Cocoa Printing using Core Printing
apple_id: DTS10003958
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2012-08-14'
source_url: https://developer.apple.com/library/archive/samplecode/PMPrinterPrintWithFile/Introduction/Intro.html
archived_at: '2026-07-18T03:18:35.645101Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Cocoa Printing using Core Printing

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2012-08-14 Updated for OS X v10.8. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojvhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X v10.8, Xcode 4.4 |
| __Runtime Requirements:__ | OS X v10.8 |

"PMPrinterPrintWithFile" shows how to use the PMPrinterPrintWithFile function to submit existing content to the printing system.

One of the parameters for PMPrinterPrintWithFile is a mime type, depending on this mime type the print system may or may not do post processing on the file you are sending. For example, if you want to generate all the PostScript data for your print job you need submit a fully formed PostScript job using the PMPrinterPrintWithFile function and use the mime type application/vnd.cups-postscript. If the same file is submitted using the mime type application/postscript, the printing system uses the page format and print settings you provide in other parameters, in addition to the printer PPD file to insert the appropriate PostScript data into the print stream. This is done automatically by the pstops filter that runs as part of printing.

Use PMPrinterGetMimeTypes() to check whether a mime type is supported by the printer you are targeting.

Mime Type Examples

–application/postscript // We insert the PS for the PMPrintSettings into the PostScript stream. –application/vnd.cups-postscript // Raw postscript/finished postscript. We don't insert anything –application/pdf // PDF document –image/gif, image/jpeg, image/tiff // Images –text/plain, text/rtf, text/html // Text –application/vnd.cups-raw //Raw printer commands and escape codes, mainly for the printer venders –and more...

[Next](ReadMe.txt.md)

