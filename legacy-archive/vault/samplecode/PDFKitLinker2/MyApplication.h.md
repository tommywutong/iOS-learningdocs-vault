---
title: PDFKitLinker2
apple_id: DTS10003594
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-08-10'
source_url: https://developer.apple.com/library/archive/samplecode/PDFKitLinker2/Listings/MyApplication_h.html
archived_at: '2026-07-18T03:18:25.943482Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PDFKitLinker2](PDFKitLinker2.md)


[Next](MyApplication.m.md)[Previous](Controller.m.md)

# MyApplication.h

```objc
// ======================================================================================================================
//  MyApplication.h
// ======================================================================================================================


#import <Cocoa/Cocoa.h>


@interface MyApplication : NSApplication
{
    IBOutlet NSPanel            *_findPanel;
    IBOutlet NSTextField        *_findPanelSearchField;
    IBOutlet NSButton           *_ignoreCaseCheckbox;
}

- (int) findOptions;
- (void) findNext: (id) sender;
- (void) findNextAndOrderOutFindPanel: (id) sender;
- (void) findPrevious: (id) sender;

@end
```

[Next](MyApplication.m.md)[Previous](Controller.m.md)

