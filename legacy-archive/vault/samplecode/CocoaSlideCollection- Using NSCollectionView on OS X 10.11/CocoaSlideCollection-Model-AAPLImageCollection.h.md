---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_Model_AAPLImageCollection_h.html
archived_at: '2026-07-18T03:03:43.470619Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-Model-AAPLFileTreeWatcherThread.m.md)[Previous](CocoaSlideCollection-Model-AAPLFileTreeWatcherThread.h.md)

# CocoaSlideCollection/Model/AAPLImageCollection.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "ImageCollection" class declaration.
*/

#import <Cocoa/Cocoa.h>

@class AAPLImageFile;
@class AAPLTag;
@class AAPLFileTreeWatcherThread;

// An AAPLImageCollection encapsulates a list of AAPLImageFile objects, together with a rootURL that identifies the folder (if any) where we found them.  It also has a list of associated Tags, each of which can return the list of ImageFiles to which it's applied.
@interface AAPLImageCollection : NSObject
{
    NSURL *rootURL;                         // URL of folder in which we found our imageFiles
    AAPLFileTreeWatcherThread *fileTreeWatcherThread;   // thread that watches the folder for changes
    NSOperationQueue *fileTreeScanQueue;    // operation queue for asynchronous scans of the folder's contents

    NSMutableArray *imageFiles;             // a flat, ordered list of the collection's ImageFiles
    NSMutableDictionary *imageFilesByURL;   // an NSURL -> AAPLImageFile lookup table
    NSMutableArray *untaggedImageFiles;     // a flat, ordered list of the ImageFiles that aren't referenced by any AAPLTag

    NSMutableArray *tags;                   // a flat, alphabetical list of the collection's Tags
    NSMutableDictionary *tagsByName;        // an NSString -> AAPLTag lookup table
}
- (id)initWithRootURL:(NSURL *)newRootURL;


#pragma mark Properties

@property(readonly) NSURL *rootURL;
@property(readonly) NSArray *imageFiles;    // KVO observable


#pragma mark Querying the List of ImageFiles

- (AAPLImageFile *)imageFileForURL:(NSURL *)imageFileURL;


#pragma mark Modifying the List of ImageFiles

- (void)addImageFile:(AAPLImageFile *)imageFile;
- (void)insertImageFile:(AAPLImageFile *)imageFile atIndex:(NSUInteger)index;
- (void)removeImageFile:(AAPLImageFile *)imageFile;
- (void)removeImageFileAtIndex:(NSUInteger)index;
- (void)moveImageFileFromIndex:(NSUInteger)fromIndex toIndex:(NSUInteger)toIndex;


#pragma mark Modifying the List of Tags

@property(readonly) NSArray<AAPLTag *> *tags;
- (AAPLTag *)tagWithName:(NSString *)name;
- (AAPLTag *)addTagWithName:(NSString *)name;

@property(readonly) NSArray<AAPLImageFile *> *untaggedImageFiles;


#pragma mark Finding Image Files

- (void)startOrRestartFileTreeScan;
- (void)stopFileTreeScan;

- (void)stopWatchingFolder;

@end

extern NSString *imageFilesKey;
```

[Next](CocoaSlideCollection-Model-AAPLFileTreeWatcherThread.m.md)[Previous](CocoaSlideCollection-Model-AAPLFileTreeWatcherThread.h.md)

