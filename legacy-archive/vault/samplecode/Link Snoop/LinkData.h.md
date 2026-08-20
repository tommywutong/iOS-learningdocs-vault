---
title: Link Snoop
apple_id: DTS10003593
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/LinkSnoop/Listings/LinkData_h.html
archived_at: '2026-07-18T03:13:32.005662Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Link Snoop](Link%20Snoop.md)


[Next](LinkData.m.md)[Previous](Controller.m.md)

# LinkData.h

```objc
// ======================================================================================================================
//  LinkData.h
// ======================================================================================================================


#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>


@interface LinkData : NSObject
{
    PDFAnnotation   *_annotation;
    PDFDestination  *_destination;
    NSString        *_text;
}

- (id) initWithAnnotation: (PDFAnnotation *) annotation;
- (PDFAnnotation *) annotation;
- (NSString *) text;
- (PDFDestination *) destination;
- (PDFSelection *) selection;

@end
```

[Next](LinkData.m.md)[Previous](Controller.m.md)

