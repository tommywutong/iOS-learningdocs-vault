---
title: 'SimpleCocoaBrowser: Using NSBrowser class'
apple_id: DTS40008872
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-04-29'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleCocoaBrowser/Listings/SimpleBrowser_FileSystemNode_m.html
archived_at: '2026-07-18T03:23:57.370815Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleCocoaBrowser: Using NSBrowser class](SimpleCocoaBrowser-%20Using%20NSBrowser%20class.md)


[Next](SimpleBrowser-FileSystemNode.h.md)[Previous](SimpleBrowser-AppController.m.md)

# SimpleBrowser/FileSystemNode.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An abstract wrapper node around the file system.
 */

#import "FileSystemNode.h"

@interface FileSystemNode ()

@property (strong) NSURL *URL;
@property (assign) BOOL childrenDirty;
@property (strong) NSMutableDictionary *internalChildren;

@end


#pragma mark -

@implementation FileSystemNode

@dynamic displayName, children, isDirectory, icon, labelColor;

- (instancetype)init {

    NSAssert(NO, @"Invalid use of init; use initWithURL to create FileSystemNode");
    return [self init];
}

- (id)initWithURL:(NSURL *)url {
    self = [super init];
    if (self != nil) {
        _URL = url;
    }
    return self;
}

- (NSString *)description {
    return [NSString stringWithFormat:@"%@ - %@", super.description, self.URL];
}

- (NSString *)displayName {
    NSString *displayName = @"";
    NSError *error = nil;

    BOOL success = [self.URL getResourceValue:&displayName forKey:NSURLLocalizedNameKey error:&error];

    // if we got a no value for the localized name, we will try the non-localized name
    if (success && displayName.length > 0) {
        [self.URL getResourceValue:&displayName forKey:NSURLNameKey error:&error];
    }
    else {
        // can't find resource value for the display name, use the localizedDescription as last resort
        return error.localizedDescription;
    }

    return displayName;
}

- (NSImage *)icon {
    return [[NSWorkspace sharedWorkspace] iconForFile:[self.URL path]];
}

- (BOOL)isDirectory {
    id value = nil;
    [self.URL getResourceValue:&value forKey:NSURLIsDirectoryKey error:nil];
    return [value boolValue];
}

- (BOOL)isPackage {
    id value = nil;
    [self.URL getResourceValue:&value forKey:NSURLIsPackageKey error:nil];
    return [value boolValue];
}

- (NSColor *)labelColor {
    id value = nil;
    [self.URL getResourceValue:&value forKey:NSURLLabelColorKey error:nil];
    return value;
}

- (NSArray *)children {
    if (self.internalChildren == nil || self.childrenDirty) {
        // This logic keeps the same pointers around, if possible.
        NSMutableDictionary *newChildren = [NSMutableDictionary new];

        NSString *parentPath = [self.URL path];
        NSArray *contentsAtPath = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:parentPath error:nil];

        if (contentsAtPath) {   // We don't deal with the error
            for (NSString *filename in contentsAtPath) {
                // Use the filename as a key and see if it was around and reuse it, if possible
                if (self.internalChildren != nil) {
                    FileSystemNode *oldChild = [self.internalChildren objectForKey:filename];
                    if (oldChild != nil) {
                    [newChildren setObject:oldChild forKey:filename];
                    continue;
                    }
                }
                // We didn't find it, add a new one
                NSString *fullPath = [parentPath stringByAppendingPathComponent:filename];
                NSURL *childURL = [NSURL fileURLWithPath:fullPath];
                if (childURL != nil) {
                    // Wrap the child url with our node
                    FileSystemNode *node = [[FileSystemNode alloc] initWithURL:childURL];
                    [newChildren setObject:node forKey:filename];
                }
            }
        }

        self.internalChildren = newChildren;
        self.childrenDirty = NO;
    }

    NSArray *result = [self.internalChildren allValues];

    // Sort the children by the display name and return it
    result = [result sortedArrayUsingComparator:^(id obj1, id obj2) {
        NSString *objName = [obj1 displayName];
        NSString *obj2Name = [obj2 displayName];
        NSComparisonResult sortedResult = [objName compare:obj2Name options:NSNumericSearch | NSCaseInsensitiveSearch | NSWidthInsensitiveSearch | NSForcedOrderingSearch range:NSMakeRange(0, [objName length]) locale:[NSLocale currentLocale]];
        return sortedResult;
    }];
    return result;
}

- (void)invalidateChildren {
    _childrenDirty = YES;
    for (FileSystemNode *child in [self.internalChildren allValues]) {
        [child invalidateChildren];
    }
}

@end
```

[Next](SimpleBrowser-FileSystemNode.h.md)[Previous](SimpleBrowser-AppController.m.md)

