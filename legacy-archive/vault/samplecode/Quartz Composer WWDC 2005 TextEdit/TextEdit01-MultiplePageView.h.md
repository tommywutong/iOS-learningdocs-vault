---
title: Quartz Composer WWDC 2005 TextEdit
apple_id: DTS10003654
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/QuartzComposer_WWDC_TextEdit/Listings/TextEdit_01_MultiplePageView_h.html
archived_at: '2026-07-18T03:21:30.995715Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz Composer WWDC 2005 TextEdit](Quartz%20Composer%20WWDC%202005%20TextEdit.md)


[Next](TextEdit01-MultiplePageView.m.md)[Previous](TextEdit01-EncodingManager.m.md)

# TextEdit_01/MultiplePageView.h

```objc
#import <Cocoa/Cocoa.h>

@interface MultiplePageView : NSView {
    NSPrintInfo *printInfo;
    NSColor *lineColor;
    NSColor *marginColor;
    unsigned numPages;
}

- (void)setPrintInfo:(NSPrintInfo *)anObject;
- (NSPrintInfo *)printInfo;
- (float)pageSeparatorHeight;
- (NSSize)documentSizeInPage;   /* Returns the area where the document can draw */
- (NSRect)documentRectForPageNumber:(unsigned)pageNumber;   /* First page is page 0 */
- (NSRect)pageRectForPageNumber:(unsigned)pageNumber;   /* First page is page 0 */
- (void)setNumberOfPages:(unsigned)num;
- (unsigned)numberOfPages;
- (void)setLineColor:(NSColor *)color;
- (NSColor *)lineColor;
- (void)setMarginColor:(NSColor *)color;
- (NSColor *)marginColor;

@end
```

[Next](TextEdit01-MultiplePageView.m.md)[Previous](TextEdit01-EncodingManager.m.md)

