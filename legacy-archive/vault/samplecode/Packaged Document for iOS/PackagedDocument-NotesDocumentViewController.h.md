---
title: Packaged Document for iOS
apple_id: DTS40014139
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Foundation
published: '2016-02-04'
source_url: https://developer.apple.com/library/archive/samplecode/sc2281/Listings/PackagedDocument_NotesDocumentViewController_h.html
archived_at: '2026-07-26T19:54:13.737655Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for iOS](Packaged%20Document%20for%20iOS.md)


[Next](ReadMe.md.md)[Previous](PackagedDocument-AppDelegate.h.md)

# PackagedDocument/NotesDocumentViewController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The view controller used for editing "NotesDocument".
 */

@import UIKit;

@protocol NotesDocumentDelegate;

@interface NotesDocumentViewController : UITableViewController

@property (nonatomic, assign) id <NotesDocumentDelegate> delegate;

- (void)setDocumentURL:(NSURL *)url createNewFile:(BOOL)createNewFile;

@end

#pragma mark -

// used to notify when a document was renamed, so we can update our parent's table
@protocol NotesDocumentDelegate <NSObject>

@optional
- (void)directoryDidChange;

@end
```

[Next](ReadMe.md.md)[Previous](PackagedDocument-AppDelegate.h.md)

