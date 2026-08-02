---
title: Using NSPageController
apple_id: DTS40012298
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-02-21'
source_url: https://developer.apple.com/library/archive/samplecode/FileCards/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:08:30.282550Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using NSPageController](Using%20NSPageController.md)


[Next](FileCards-AppDelegate.h.md)[Previous](Using%20NSPageController.md)

# ReadMe.txt

```
### FileCards ###

===========================================================================
DESCRIPTION:

Demonstrates the use of NSPageController.

Summary:
"File Cards" are displayed for the contents of the user's Documents folder.
You can swipe, click the arrow buttons or click on the entry in the table to switch between cards.

AppDelegate:
Implements the NSPageControllerDelegate methods.
There are 3 interesting advanced techniques shown in this file:

1. How to programmatically change the pageController.selectedIndex.
2. The use of more than 1 identifier so that we can have 2 card styles.
3. Use of an optional NSPageControllerDelegate to control the layout of the card inside its parent view.

FileObject:
Simple wrapper around NSURL to make binding to file properties in IB easier.

CardBackgroundView:
Draws the rounded edge background of the file cards.

===========================================================================
BUILD REQUIREMENTS:

Xcode 5.0, OS X 10.9

===========================================================================
RUNTIME REQUIREMENTS:

OS X 10.8 or later

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

1.0 - First version.
1.1 - First public version.

===========================================================================
Copyright (C) 2012-2014 Apple Inc. All rights reserved.
```

[Next](FileCards-AppDelegate.h.md)[Previous](Using%20NSPageController.md)

