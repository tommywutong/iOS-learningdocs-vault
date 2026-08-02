---
title: ColorSyncDevices-Cocoa
apple_id: DTS10000387
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ColorSyncDevices-Cocoa/Listings/ColorSyncDevice_h.html
archived_at: '2026-07-18T03:04:00.451534Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ColorSyncDevices-Cocoa](ColorSyncDevices-Cocoa.md)


[Next](ColorSyncDevice.m.md)[Previous](ColorDevice.m.md)

# ColorSyncDevice.h

```objc
//
//  ColorSyncDevice.h
//  ColorSyncDevices-Cocoa
//
//  Created by Scott Kuechle on Sun Sep 08 2002.
//  Copyright (c) 2001 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>



@interface ColorSyncDevice : NSObject {
    NSString *relativePath;
    ColorSyncDevice *parent;
    NSMutableArray *children;
}

+ (ColorSyncDevice *)rootItem;

@end
```

[Next](ColorSyncDevice.m.md)[Previous](ColorDevice.m.md)

