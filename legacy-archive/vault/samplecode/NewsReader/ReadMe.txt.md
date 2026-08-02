---
title: NewsReader
apple_id: DTS10003985
resource_type: Sample Code
platform: macOS
topic: null
technology: PublicationSubscription
published: '2007-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/NewsReader/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:17:02.305405Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NewsReader](NewsReader.md)


[Next](English.lproj-EnclosureTemplate.html.md)[Previous](NewsReader.md)

# ReadMe.txt

```
NewsReader


Objective

The NewsReader example shows how to use the PubSub API to create a simple RSS reader application. It also demonstrates the use of Cocoa bindings to populate some of the columns in its table view, the use of value transformers, the implementation of an NSOutlineView datasource and an NSTableView datasource, and the implementation of a WebView delegate.


Files of Interest

MainMenu.nib - This interface file contains object and array controllers connected to the back end, that in turn provide information for UI elements including text fields and tables. Investigate how the bindings tab in the Inspector changes for the different controllers and UI elements.

EntryTemplate_NoLink.html and EntryTemplate.html - These files are used to build the HTML that is displayed in a WebView when a single entry is selected in a table view. See also: EntryController class files.

EntryController and EntryListController class files - These files assist in obtaining entry-specific information using the PubSub API, and providing it for display in the UI. EntryController is a WebView delegate. EntryListController is an NSTableView datasource.

FeedListController class files - These files assist in obtaining feed-specific information using the PubSub API, and providing it for display in the UI. FeedListController is an NSOutlineView datasource.

NewsReaderApp class files - These files carry out general UI tasks in the NewsReader application, including feed and entry selection, and menu commands such as Subscribe and Unsubscribe. NewsReaderApp is an NSApplication delegate, and a PSClient delegate.
```

[Next](English.lproj-EnclosureTemplate.html.md)[Previous](NewsReader.md)

