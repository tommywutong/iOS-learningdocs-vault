---
title: CoreTextRTF
apple_id: DTS40007772
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: null
published: '2011-08-22'
source_url: https://developer.apple.com/library/archive/samplecode/CoreTextRTF/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:05:06.465888Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CoreTextRTF](CoreTextRTF.md)


[Next](main.m.md)[Previous](CoreTextRTF.md)

# ReadMe.txt

```
CoreTextRTF
===========

This sample illustrates how to use CoreText to draw rtf content in a Cocoa application.  

The main functionality demonstrated in this application is encapsulated in the -drawRect: and -createColumns methods in the file CoreTextView.m.  That is where all of the CoreText drawing and layout takes place.  

Interested readers will also want to look at the -readFromURL:ofType:error: method in the MyDocument.m file where the rtf file data is read into memory.  In this sample, that operation is very simple and only requires three lines of code.


Using the Sample
Build and run this sample in Xcode 3.2 or later and run the resulting application.  

When the application starts up choose the "Open..." command from the "File" menu and open the enclosed "CoreTextRTF Test Document.rtf" document.  The contents of the file will be displayed in a window.  Clicking on that window will cycle through displaying the rtf content in one, two, or three columns.

===========================================================================
BUILD REQUIREMENTS

Xcode 3.2, Mac OS X 10.6 Snow Leopard or later.

===========================================================================
RUNTIME REQUIREMENTS

Mac OS X 10.6 Snow Leopard or later.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS

Version 1.1
- Project updated for Xcode 4.
Version 1.0
- Initial Version

===========================================================================
Copyright (C) 2007-2011 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](CoreTextRTF.md)

