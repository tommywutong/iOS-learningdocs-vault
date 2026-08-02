---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_Model_AAPLImageFile_h.html
archived_at: '2026-07-18T03:03:43.634308Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-Model-AAPLImageCollection.m.md)[Previous](CocoaSlideCollection-Model-AAPLTag.h.md)

# CocoaSlideCollection/Model/AAPLImageFile.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "ImageFile" class declaration.
*/

#import <Foundation/Foundation.h>

// This is our Model representation of an image file.  It provides access to the file's properties and its contained image, including pixel dimensions and a thumbnail preview.
@interface AAPLImageFile : NSObject
{
    CGImageSourceRef imageSource;           // NULL until metadata is loaded
    NSDictionary *imageProperties;          // nil until metadata is loaded
}

- (id)initWithURL:(NSURL *)newURL;


#pragma mark File Properties

@property(copy) NSURL *url;
@property(copy) NSString *fileType;
@property unsigned long long fileSize;
@property(copy) NSDate *dateLastUpdated;
@property(copy) NSArray *tagNames;

@property(readonly) NSString *filename;
@property(readonly) NSString *filenameWithoutExtension;
@property(readonly) NSString *localizedTypeDescription;
@property(readonly) NSString *dimensionsDescription;


#pragma mark Image Properties

@property(readonly) NSInteger pixelsWide;
@property(readonly) NSInteger pixelsHigh;

@property(strong) NSImage *previewImage;


#pragma mark Loading

// These are triggered automatically the first time relevant properties are requested, but can be invoked explicitly to force loading earlier.
- (BOOL)loadMetadata;

- (void)requestPreviewImage;

@end
```

[Next](CocoaSlideCollection-Model-AAPLImageCollection.m.md)[Previous](CocoaSlideCollection-Model-AAPLTag.h.md)

