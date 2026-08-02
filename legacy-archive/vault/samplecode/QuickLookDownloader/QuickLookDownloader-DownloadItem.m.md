---
title: QuickLookDownloader
apple_id: DTS40009082
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: QuickLook
published: '2017-10-26'
source_url: https://developer.apple.com/library/archive/samplecode/QuickLookDownloader/Listings/QuickLookDownloader_DownloadItem_m.html
archived_at: '2026-07-18T03:21:43.650771Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickLookDownloader](QuickLookDownloader.md)


[Next](LICENSE.txt.md)[Previous](QuickLookDownloader-MyDocument.m.md)

# QuickLookDownloader/DownloadItem.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 DownloadItem stores information of a downloaded item used by MyDocument.
 */

#import "DownloadItem.h"

#include <QuickLook/QuickLook.h>

static NSString *originalURLKey = @"downloadURL";
static NSString *bookmarkKey = @"bookmark";
static NSOperationQueue *downloadIconQueue = nil;
static NSDictionary *quickLookOptions = nil;

#define ICON_SIZE 48.0


@implementation DownloadItem

- (id)initWithOriginalURL:(NSURL *)downloadURL fileURL:(NSURL *)onDiskURL
{
    self = [super init];
    if (self != nil)
    {
        _originalURL = [downloadURL copy];
        _resolvedFileURL = [onDiskURL copy];
    }
    return self;
}

- (id)initWithSavedPropertyList:(id)propertyList
{
    self = [super init];
    if (self != nil)
    {
        if (![propertyList isKindOfClass:[NSDictionary class]])
        {
            return nil;
        }

        NSString *originalURLString = propertyList[originalURLKey];
        if (!originalURLString || ![originalURLString isKindOfClass:[NSString class]])
        {
            return nil;
        }

        _originalURL = [[NSURL alloc] initWithString:originalURLString];
        if (!self.originalURL)
        {
            return nil;
        }

        NSData *bookmarkData = propertyList[bookmarkKey];
        if (!bookmarkData || ![bookmarkData isKindOfClass:[NSData class]])
        {
            return nil;
        }

        // test if the file still exists
        _resolvedFileURL = [NSURL URLByResolvingBookmarkData:bookmarkData
                                                     options:(NSURLBookmarkResolutionWithoutUI | NSURLBookmarkResolutionWithoutMounting)
                                               relativeToURL:nil bookmarkDataIsStale:NULL error:NULL];
        if (!self.resolvedFileURL)
        {
            return nil;
        }
    }

    return self;
}

- (NSImage *)iconImage
{
    if (_iconImage == nil)
    {
        _iconImage = [[NSWorkspace sharedWorkspace] iconForFile:[self.resolvedFileURL path]];
        [_iconImage setSize:NSMakeSize(ICON_SIZE, ICON_SIZE)];
        if (!downloadIconQueue)
        {
            downloadIconQueue = [[NSOperationQueue alloc] init];
            [downloadIconQueue setMaxConcurrentOperationCount:2];
            quickLookOptions = @{(id)kQLThumbnailOptionIconModeKey: (id)kCFBooleanTrue};
        }
        [downloadIconQueue addOperationWithBlock:^{
            CGImageRef quickLookIcon = QLThumbnailImageCreate(NULL, (__bridge CFURLRef)self.resolvedFileURL, CGSizeMake(ICON_SIZE, ICON_SIZE), (__bridge CFDictionaryRef)quickLookOptions);
            if (quickLookIcon != NULL)
            {
                NSImage* betterIcon = [[NSImage alloc] initWithCGImage:quickLookIcon size:NSMakeSize(ICON_SIZE, ICON_SIZE)];
                [self performSelectorOnMainThread:@selector(setIconImage:) withObject:betterIcon waitUntilDone:NO];
                CFRelease(quickLookIcon);
            }
        }];
    }
    return _iconImage;
}

- (NSString *)displayName
{
    return [[self.resolvedFileURL path] lastPathComponent];
}

- (id)propertyListForSaving
{
    NSData *bookmarkData = [self.resolvedFileURL bookmarkDataWithOptions:NSURLBookmarkCreationMinimalBookmark includingResourceValuesForKeys:nil relativeToURL:nil error:NULL];
    if (!bookmarkData)
    {
        return nil;
    }
    return @{originalURLKey: [self.originalURL absoluteString],
            bookmarkKey: bookmarkData};
}

- (NSString *)description
{
    return [NSString stringWithFormat:@"<%@ %@ (from %@)>", [self class], self.resolvedFileURL, self.originalURL];
}

@end
```

[Next](LICENSE.txt.md)[Previous](QuickLookDownloader-MyDocument.m.md)

