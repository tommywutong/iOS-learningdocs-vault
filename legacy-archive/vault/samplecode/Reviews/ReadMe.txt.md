---
title: Reviews
apple_id: DTS40010057
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2011-07-21'
source_url: https://developer.apple.com/library/archive/samplecode/Reviews/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:22:12.225918Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Reviews](Reviews.md)


[Next](Reviews-AppDelegate.h.md)[Previous](Reviews.md)

# ReadMe.txt

```swift
### Reviews ###

================================================================================
DESCRIPTION:

This is a simple CoreData NSDocument-based app which demonstrates the following:

- Using an "AccessibilityImageDescriptions.strings" file to add accessibility descriptions to named images without using code.
- Setting up an NSCollectionView using a nib-based NSCollectionViewItem.
- Using NSSplitView delegate method to easily keep one pane a constant size.
- Writing and using custom NSValueTransformers.
- Using an application delegate to open a custom untitled document on launch.
- Adding a second window and window controller to a single document via "View" menu -> Show Edit Window menu item.

Since this application was written to demo the ease in which an "AccessibilityImageDescriptions.strings"
file can be added to a project to greatly increase the accessibility of an app - a sample document is included with the project.

On launch, the app will look for a document with the name 'DemoReviewDoc.review' on the Desktop. If it is present, that file will be opened on launch - otherwise an untitled document will be used.

To test viewing descriptions of the images in this app, you can run Voice Over from System Preferences, or test them by running the UIElementInspector sample code project.


===========================================================================
BUILD REQUIREMENTS:

Xcode 3.2, Mac OS X 10.6 Snow Leopard or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X 10.6 Snow Leopard or later

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.1
- Project updated for Xcode 4.
Version 1.0
- First release


===========================================================================
Copyright (C) 2010-2011, Apple Inc.
```

[Next](Reviews-AppDelegate.h.md)[Previous](Reviews.md)

