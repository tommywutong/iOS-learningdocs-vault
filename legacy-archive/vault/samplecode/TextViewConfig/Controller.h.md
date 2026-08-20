---
title: TextViewConfig
apple_id: DTS10000410
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TextViewConfig/Listings/Controller_h.html
archived_at: '2026-07-18T03:26:42.804217Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TextViewConfig](TextViewConfig.md)


[Next](Controller.m.md)[Previous](main.m.md)

# Controller.h

```objc
/*
        Controller.h
        TextViewConfig

        Author: DD
*/

#import <AppKit/AppKit.h>

@interface Controller : NSObject {
    IBOutlet NSTextView *singleTextView;
    IBOutlet NSView *customView;
}

@end
```

[Next](Controller.m.md)[Previous](main.m.md)

