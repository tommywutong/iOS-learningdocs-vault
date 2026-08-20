---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_Model_AAPLTag_m.html
archived_at: '2026-07-18T03:03:43.828764Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-AAPLFooterView.h.md)[Previous](CocoaSlideCollection-Model-AAPLImageFile.m.md)

# CocoaSlideCollection/Model/AAPLTag.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "Tag" class implementation.
*/

#import "AAPLTag.h"
#import "AAPLImageFile.h"

@implementation AAPLTag

- (id)initWithName:(NSString *)newName {
    self = [super init];
    if (self) {
        name = [newName copy];
        imageFiles = [[NSMutableArray alloc] init];
    }
    return self;
}

@synthesize name;
@synthesize imageFiles;

- (void)insertImageFile:(AAPLImageFile *)imageFile {
    NSUInteger insertionIndex = [imageFiles indexOfObject:imageFile inSortedRange:NSMakeRange(0, [imageFiles count]) options:NSBinarySearchingInsertionIndex usingComparator:^NSComparisonResult(AAPLImageFile *imageFile1, AAPLImageFile *imageFile2) {
        return [imageFile1.filenameWithoutExtension caseInsensitiveCompare:imageFile2.filenameWithoutExtension];
    }];
    if (insertionIndex == NSNotFound) {
        NSLog(@"** Couldn't determine insertionIndex for imageFiles array");
    } else {
        [imageFiles insertObject:imageFile atIndex:insertionIndex];
    }
}

- (NSString *)description {
    return [NSString stringWithFormat:@"{Tag: %@}", self.name];
}

@end
```

[Next](CocoaSlideCollection-View-AAPLFooterView.h.md)[Previous](CocoaSlideCollection-Model-AAPLImageFile.m.md)

