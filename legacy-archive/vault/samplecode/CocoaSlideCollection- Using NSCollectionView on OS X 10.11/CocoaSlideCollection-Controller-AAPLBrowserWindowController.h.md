---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_Controller_AAPLBrowserWindowController_h.html
archived_at: '2026-07-18T03:03:43.065190Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-Controller-AAPLBrowserWindowController.m.md)[Previous](CocoaSlideCollection-Controller-AAPLAppDelegate.m.md)

# CocoaSlideCollection/Controller/AAPLBrowserWindowController.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the browser window controller declaration.
*/

#import <Cocoa/Cocoa.h>

@class AAPLImageCollection;

typedef enum {
    SlideLayoutKindCircular = 0,
    SlideLayoutKindLoop = 1,
    SlideLayoutKindScatter = 2,
    SlideLayoutKindWrapped = 3
} SlideLayoutKind;

/*
    Each browser window is managed by a AAPLBrowserWindowController, which
    serves as its CollectionView's dataSource and delegate.  (The
    CollectionView's dataSource and delegate outlets are wired up in
    BrowserWindow.xib, so there is no need to set these properties in code.)
*/
@interface AAPLBrowserWindowController : NSWindowController <NSCollectionViewDataSource, NSCollectionViewDelegate, NSCollectionViewDelegateFlowLayout>
{
    // Model
    NSURL *rootURL;                                         // URL of the folder whose image files the browser is displaying
    AAPLImageCollection *imageCollection;                   // the ImageFiles we found in the folder, which we can access as a flat list or grouped by AAPLTag

    // Views
    IBOutlet NSCollectionView *__weak imageCollectionView;  // a CollectionView that displays items ("slides") representing the image files
    IBOutlet NSTextField *__weak statusTextField;           // a TextField that shows informative status

    // UI State
    SlideLayoutKind layoutKind;                             // what kind of layout to use, per the above SlideLayoutKind enumeration
    BOOL groupByTag;                                        // YES if our imageCollectionView should show its items grouped by tag, with header and footer views (usable with Wrapped layout only)
    BOOL autoUpdateResponseSuspended;                       // YES when we want to suppress our usual automatic KVO response to assets coming and going
    NSSet<NSIndexPath *> *indexPathsOfItemsBeingDragged;    // when our imageCollectionView is the source for a drag operation, this array of NSIndexPaths identifies the items that are being dragged within or out of it
}

// Initializes a browser window that's pointed at the given folder URL.
- (id)initWithRootURL:(NSURL *)newRootURL;


#pragma mark Outlets

@property(weak) IBOutlet NSCollectionView *imageCollectionView;
@property(weak) IBOutlet NSTextField *statusTextField;


#pragma mark Actions

- (IBAction)refresh:(id)sender;


#pragma mark Properties

@property SlideLayoutKind layoutKind;
@property BOOL groupByTag;

@end
```

[Next](CocoaSlideCollection-Controller-AAPLBrowserWindowController.m.md)[Previous](CocoaSlideCollection-Controller-AAPLAppDelegate.m.md)

