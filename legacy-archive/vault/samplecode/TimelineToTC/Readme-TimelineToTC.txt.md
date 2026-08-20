---
title: TimelineToTC
apple_id: DTS10004351
resource_type: Sample Code
platform: macOS
topic: Apple Applications
technology: null
published: '2007-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/TimelineToTC/Listings/Readme_TimelineToTC_txt.html
archived_at: '2026-07-18T03:26:57.584264Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TimelineToTC](TimelineToTC.md)


[Next](Document%20Revision%20History.md)[Previous](MyDocument.m.md)

# Readme-TimelineToTC.txt

```
TimelineToTC

Requires: Mac OS X 10.4.9  Final Cut Pro 5.1.2 or later. Xcode 2.1 or later.

The TimelineToTC sample application demonstrates the parsing of a
Final Cut Pro originated XML file, outputting the attributes of
individual clips in an edit list. Individual technologies/methods
illustrated include:

- Parsing and searching of an XML data stream using NSXML and XQuery. 
- Generating properly formatted time-code strings from component values
  (e.g. frame-base, format, frame-count). 

To use the application, first acquire an XML file from Final Cut Pro.
Next, launch TimelineToTC, opening the aforementioned XML file.  Assuming
that the application was successful in parsing the XML data, you will
be presented with a document window containing a list of sequences found,
a description of the currently selected sequence, and a list of optional
attributes to be added to the edit list ultimately exported.

To generate an edit list, select the desired sequence, confirm the desired
attributes to be written out, and click on the "Export Edit List" button.
Once processing has been completed, you will be prompted for a name and 
location to write the completed edit list file.
```

[Next](Document%20Revision%20History.md)[Previous](MyDocument.m.md)

