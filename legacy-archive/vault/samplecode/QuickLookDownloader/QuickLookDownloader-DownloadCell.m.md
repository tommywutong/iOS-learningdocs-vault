---
title: QuickLookDownloader
apple_id: DTS40009082
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: QuickLook
published: '2017-10-26'
source_url: https://developer.apple.com/library/archive/samplecode/QuickLookDownloader/Listings/QuickLookDownloader_DownloadCell_m.html
archived_at: '2026-07-18T03:21:43.570843Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickLookDownloader](QuickLookDownloader.md)


[Next](QuickLookDownloader-DownloadsTableView.m.md)[Previous](QuickLookDownloader-AppDelegate.m.md)

# QuickLookDownloader/DownloadCell.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 DownloadCell can display a title, an icon and a subtitle.
 */

#import "DownloadCell.h"

#define SUBTITLE_SIZE [NSFont smallSystemFontSize]

@implementation DownloadCell

- (id)copyWithZone:(NSZone *)zone
{
    DownloadCell *result = [super copyWithZone:zone];
    result.originalURL = [self.originalURL copy];
    return result;
}

- (void)drawWithFrame:(NSRect)cellFrame inView:(NSView *)controlView
{
    CGFloat textHeight = TEXT_SIZE;
    CGFloat subtitleHeight = SUBTITLE_SIZE;
    CGFloat totalHeight = textHeight + subtitleHeight + 6.0;

    CGFloat deltaY = (CGRectGetHeight(cellFrame) - totalHeight) / 2.0;

    cellFrame.size.height = totalHeight;
    cellFrame.origin.y += deltaY;

    cellFrame = NSIntegralRect(cellFrame);

    NSRect textFrame;
    NSRect subtextFrame;

    NSDivideRect(cellFrame, &textFrame, &subtextFrame, (TEXT_SIZE + 4.0), [controlView isFlipped] ? NSMinYEdge : NSMaxYEdge);

    [super drawWithFrame:textFrame inView:controlView];

    if (self.originalURL)
    {
        NSString *stringToDisplay = [self.originalURL absoluteString];
        static NSDictionary *attributes = nil;
        static NSDictionary *selectedAttributes = nil;

        if (!attributes)
        {
            attributes = @{NSForegroundColorAttributeName:[NSColor darkGrayColor],
                           NSFontAttributeName:[NSFont systemFontOfSize:SUBTITLE_SIZE]};
            selectedAttributes = @{NSForegroundColorAttributeName:[NSColor whiteColor],
                                   NSFontAttributeName:[NSFont systemFontOfSize:SUBTITLE_SIZE]};
        }

        [stringToDisplay drawInRect:subtextFrame withAttributes:([self backgroundStyle] == NSBackgroundStyleDark) ? selectedAttributes : attributes];
    }
}

@end
```

[Next](QuickLookDownloader-DownloadsTableView.m.md)[Previous](QuickLookDownloader-AppDelegate.m.md)

