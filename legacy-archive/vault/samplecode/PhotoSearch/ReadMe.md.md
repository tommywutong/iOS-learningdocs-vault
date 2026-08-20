---
title: PhotoSearch
apple_id: DTS10003994
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoSearch/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:18:54.955297Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoSearch](PhotoSearch.md)


[Next](AppDelegate.h.md)[Previous](SearchQuery.h.md)

# ReadMe.md

```
# PhotoSearch

AppKit Sample application for the WWDC 2007 session:
"Beyond Buttons and Sliders - Advanced Controls in Cocoa"

## Sample Requirements

The supplied Xcode project builds with Mac OS X 10.11 SDK or later, and runs on 10.9 or later.

This sample is also designed to be App Sandboxed, and with Sandboxing, it means this app should also be code signed.

## About the Sample

This sample application uses Spotlight to perform a search for images on your computer. The search location or search scope can also be customized by the user.  The results are displayed in a view-based table view. The NSPredicateEditor (introduced in OS X 10.6) is used to create a search rule. The NSPathControl (also introduced in OS X 10.6) is used to display a selected path.

PhotoSearch is App Sandboxed which offers strong defense against damage from malicious code.  In doing so, it allows you to retain access to file-system resources by employing a security mechanism, "known as security-scoped bookmarks", that preserves user intent between app launches.  Hence, the search location or scope becomes a security-scoped bookmark.

* MainWindowController.h/.m: The main controller that glues the user interface to the data model.
* SearchItem.h/.m: The data model representation for a search result.
* SearchQuery.h/.m: The data model representation for a search query, which contains an array of SearchItem children.
* CaseInsensitivePredicateTemplate.h/.m: A custom predicate template used by the NSPredicateEditor to have a case insensitive Spotlight search.


Copyright (C) 2007-2015 Apple Inc. All rights reserved.
```

[Next](AppDelegate.h.md)[Previous](SearchQuery.h.md)

