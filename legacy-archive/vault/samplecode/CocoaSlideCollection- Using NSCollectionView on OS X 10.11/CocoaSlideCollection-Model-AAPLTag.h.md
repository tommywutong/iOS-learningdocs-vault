---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_Model_AAPLTag_h.html
archived_at: '2026-07-18T03:03:43.784017Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-Model-AAPLImageFile.h.md)[Previous](CocoaSlideCollection-Controller-AAPLAppDelegate.h.md)

# CocoaSlideCollection/Model/AAPLTag.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "Tag" class declaration.
*/

#import <Foundation/Foundation.h>

@class AAPLImageFile;

// An AAPLTag is a label string that can be applied to ImageFiles.  An AAPLImageCollection has a list of Tags, each of which has associated ImageFiles.
@interface AAPLTag : NSObject
{
    NSString *name;                 // the tag string (e.g. "Vacation")
    NSMutableArray *imageFiles;     // the ImageFiles that have this tag, ordered for display using our desired sort
}
- initWithName:(NSString *)newName;

@property(readonly) NSString *name;

@property(readonly) NSArray<AAPLImageFile *> *imageFiles;

- (void)insertImageFile:(AAPLImageFile *)imageFile;

@end
```

[Next](CocoaSlideCollection-Model-AAPLImageFile.h.md)[Previous](CocoaSlideCollection-Controller-AAPLAppDelegate.h.md)

