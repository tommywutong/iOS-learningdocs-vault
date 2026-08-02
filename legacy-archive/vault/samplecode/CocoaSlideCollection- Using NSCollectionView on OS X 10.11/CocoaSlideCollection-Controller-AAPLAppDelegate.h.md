---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_Controller_AAPLAppDelegate_h.html
archived_at: '2026-07-18T03:03:42.948839Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-Model-AAPLTag.h.md)[Previous](CocoaSlideCollection-Controller-AAPLBrowserWindowController.m.md)

# CocoaSlideCollection/Controller/AAPLAppDelegate.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the application delegate declaration.
*/

#import <Cocoa/Cocoa.h>

/*
    The application delegate opens a browser window for
    "/Library/Desktop Pictures" on launch, and handles requests to open
    additional browser windows.
*/

@interface AAPLAppDelegate : NSObject <NSApplicationDelegate>
{
    NSMutableSet *browserWindowControllers;
}

// CocoaSlideCollection's "File" -> "Browse Folder..." (Cmd+O) menu item sends this.
- (IBAction)openBrowserWindow:(id)sender;

@end
```

[Next](CocoaSlideCollection-Model-AAPLTag.h.md)[Previous](CocoaSlideCollection-Controller-AAPLBrowserWindowController.m.md)

