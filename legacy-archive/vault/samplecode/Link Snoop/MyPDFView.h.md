---
title: Link Snoop
apple_id: DTS10003593
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/LinkSnoop/Listings/MyPDFView_h.html
archived_at: '2026-07-18T03:13:32.207269Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Link Snoop](Link%20Snoop.md)


[Next](MyPDFView.m.md)[Previous](MyDocument.m.md)

# MyPDFView.h

```objc
// ======================================================================================================================
//  MyPDFView.h
// ======================================================================================================================


#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>


@interface MyPDFView : PDFView
{
}

- (void) transformContextForPage: (PDFPage *) page;

@end
```

[Next](MyPDFView.m.md)[Previous](MyDocument.m.md)

