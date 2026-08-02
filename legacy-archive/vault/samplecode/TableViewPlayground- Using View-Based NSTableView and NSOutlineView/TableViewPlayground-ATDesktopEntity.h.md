---
title: 'TableViewPlayground: Using View-Based NSTableView and NSOutlineView'
apple_id: DTS40010727
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-04-14'
source_url: https://developer.apple.com/library/archive/samplecode/TableViewPlayground/Listings/TableViewPlayground_ATDesktopEntity_h.html
archived_at: '2026-07-18T03:26:13.803595Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TableViewPlayground: Using View-Based NSTableView and NSOutlineView](TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md)


[Next](TableViewPlayground-ATTableCellView.m.md)[Previous](TableViewPlayground-ATDesktopEntity.m.md)

# TableViewPlayground/ATDesktopEntity.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A sample model object. A base abstract class (ATDesktopEntity) implements caching of a file URL. One concrete subclass implements the ability to have an array of children (ATDesktopFolderEntity). Another (ATDesktopImageEntity) represents an image suitable for the desktop wallpaper.
 */

@import Cocoa;

// KVO key path for thumbnail.
extern NSString *const ATEntityPropertyNamedThumbnailImage;

// Base abstract class that wraps a file system URL 
@interface ATDesktopEntity : NSObject <NSPasteboardWriting, NSPasteboardReading>

- (instancetype)initWithFileURL:(NSURL *)fileURL NS_DESIGNATED_INITIALIZER;

@property (strong) NSString *title;
@property (strong) NSURL *fileURL;

+ (ATDesktopEntity *)entityForURL:(NSURL *)url;

@end


#pragma mark -

// Concrete subclass of ATDesktopEntity that loads children from a folder
@interface ATDesktopFolderEntity : ATDesktopEntity

@property(strong) NSMutableArray *children;

@end


#pragma mark -

// Concrete subclass of ATDesktopEntity that adds support for loading an image at the given URL and stores a fillColor property
@interface ATDesktopImageEntity : ATDesktopEntity

@property (strong) NSColor *fillColor;
@property (copy) NSString *fillColorName;

// Access to the image. This property can be observed to find out when it changes and is fully loaded.
@property (strong) NSImage *image;
@property (readonly, strong, nonatomic) NSImage *thumbnailImage;

// Asynchronously loads the image (if not already loaded). A KVO notification is sent out when the image is loaded.
- (void)loadImage;

// A nil image isn't loaded (or couldn't be loaded).
// An image that is in the process of loading has imageLoading set to YES.
@property (readonly) BOOL imageLoading;

@end
```

[Next](TableViewPlayground-ATTableCellView.m.md)[Previous](TableViewPlayground-ATDesktopEntity.m.md)

