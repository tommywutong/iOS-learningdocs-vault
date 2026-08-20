---
title: TextEditPlus
apple_id: DTS10004025
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-07-28'
source_url: https://developer.apple.com/library/archive/samplecode/TextEditPlus/Listings/TextEditPlus_Step_2_MultiplePageView_h.html
archived_at: '2026-07-18T03:26:37.879880Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TextEditPlus](TextEditPlus.md)


[Next](TextEditPlus%20Step%202-MultiplePageView.m.md)[Previous](TextEditPlus%20Step%202-EncodingManager.m.md)

# TextEditPlus Step 2/MultiplePageView.h

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

[Next](TextEditPlus%20Step%202-MultiplePageView.m.md)[Previous](TextEditPlus%20Step%202-EncodingManager.m.md)

