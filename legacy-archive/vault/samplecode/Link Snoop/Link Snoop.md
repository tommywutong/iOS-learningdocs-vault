---
title: Link Snoop
apple_id: DTS10003593
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/LinkSnoop/Introduction/Intro.html
archived_at: '2026-07-18T03:13:31.869231Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# Link Snoop

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2005-06-01 Shows how to use PDFKit to scan for and highlight link annotations in PDFs. |
| __Build Requirements:__ | Mac OS X Tiger |
| __Runtime Requirements:__ | Mac OS X Tiger |

A simple application using the new Quartz framework, PDFKit in Mac OS X Tiger. When a user to open a PDF with the application it scans it for Link annotations that have a URL associated with them. URL link annotations are displayed in an NSTableView. As well, the PDF is displayed with these annotations highlighted.
It shows simple use of PDFKit including creating a PDFDocument and associating it with a PDFView.
It shows how to subclass PDFView and override the drawing method in order to render a box around Link annotations.
It demonstrates bounds-testing of text on a PDFPage (using PDFSelection's).
It also demonstrates simple creaton of PDFDestination's.

[Next](main.m.md)

