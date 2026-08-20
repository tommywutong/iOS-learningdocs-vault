---
title: QTMetadataEditor
apple_id: DTS40007652
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2010-05-27'
source_url: https://developer.apple.com/library/archive/samplecode/QTMetadataEditor/Listings/MyValueFormatter_h.html
archived_at: '2026-07-18T03:21:02.789582Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMetadataEditor](QTMetadataEditor.md)


[Next](MyValueFormatter.m.md)[Previous](MySplitViewWithDropSupport.m.md)

# MyValueFormatter.h

```objc
/* MyValueFormatter */

#import <Cocoa/Cocoa.h>

@interface MyValueFormatter : NSFormatter
{
}
+ (NSString *)hexStringFromData:(NSData*) dataValue;
+ (NSData *)dataFromHexString:(NSString*) dataValue;
@end
```

[Next](MyValueFormatter.m.md)[Previous](MySplitViewWithDropSupport.m.md)

