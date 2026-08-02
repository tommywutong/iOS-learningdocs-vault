---
title: Link Snoop
apple_id: DTS10003593
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/LinkSnoop/Listings/MyWindowController_h.html
archived_at: '2026-07-18T03:13:32.291586Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Link Snoop](Link%20Snoop.md)


[Next](MyWindowController.m.md)[Previous](MyPDFView.m.md)

# MyWindowController.h

```objc
// ======================================================================================================================
//  MyWindowController.h
// ======================================================================================================================


#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import "MyPDFView.h"


@interface MyWindowController : NSWindowController
{
    NSMutableArray                  *_linkList;
    int                             _scanPageIndex;
    IBOutlet NSSplitView            *_splitView;
    IBOutlet MyPDFView              *_pdfView;
    IBOutlet NSTableView            *_linksTable;
    IBOutlet NSTextField            *_linkCount;
}

- (PDFAnnotation *) activeAnnotation;

@end
```

[Next](MyWindowController.m.md)[Previous](MyPDFView.m.md)

