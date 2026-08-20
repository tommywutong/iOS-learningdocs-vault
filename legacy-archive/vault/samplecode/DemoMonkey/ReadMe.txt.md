---
title: DemoMonkey
apple_id: DTS40008848
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2010-08-31'
source_url: https://developer.apple.com/library/archive/samplecode/DemoMonkey/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:06:24.409817Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoMonkey](DemoMonkey.md)


[Next](main.m.md)[Previous](DemoMonkey.md)

# ReadMe.txt

```
### DemoMonkey ###

===========================================================================
DESCRIPTION:

This example shows how to use pasteboard and services APIs for Mac OS X v10.6 and later.

The example is a document-based application which serves as a "typing assistant". Each document contains a collection of text snippets which you can insert in turn into another application using a service.  When creating a document, you can import text snippets also using a service.

The application uses the pasteboard to support copy and paste and drag and drop. Drag and drop is illustrated using a subclass of NSArrayController in conjunction with Cocoa bindings.

===========================================================================
BUILD REQUIREMENTS:

Xcode 3.2 or later, Mac OS X v10.6 or later.

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X v10.6 or later.

===========================================================================
PACKAGING LIST:

MyDocument.{h,m}
Document object to manage a collection of text snippets; the snippets may be displayed in one or two windows:
 * A window managed by a DisplayController window controller which is solely for display purposes;
 * Optionally, a window managed by an EditController window controller, which is used for editing the snippets.

DisplayController.{h,m}
A window controller to display the titles of the text snippets.

EditController.{h,m}
A window controller to manage editing the text snippets.

AppDelegate.{h,m}
Application delegate class to act as the Services provider.  Services requests are routed to the current main document. The delegate also manages the application's preferences.

DMKArrayController.{h,m}
An array controller subclass to manage a collection of text snippets, including support for drag and drop.

Step.{h,m}
A model object to represent a text snippet.
The class conforms to the NSCoding, NSPasteboardReading, and NSPasteboardWriting protocols so that instances can be used with archives and written to and read from a pasteboard.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.1
- Removed extraneous comments and log statements. Updated implementation of initializer methods.

Version 1.0
- First version.

===========================================================================
Copyright (C) 2009-2010 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](DemoMonkey.md)

