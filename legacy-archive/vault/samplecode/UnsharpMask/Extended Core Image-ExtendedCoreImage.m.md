---
title: UnsharpMask
apple_id: DTS10003724
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: Automator
published: '2005-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/UnsharpMask/Listings/Extended_Core_Image_ExtendedCoreImage_m.html
archived_at: '2026-07-18T03:27:35.619034Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnsharpMask](UnsharpMask.md)


[Next](Save%20Image%20To%20File%20%28Step%201%29-Save%20Image%20To%20File.h.md)[Previous](Extended%20Core%20Image-ExtendedCoreImage.h.md)

# Extended Core Image/ExtendedCoreImage.m

```objc
/*
 ExtendedCoreImage.m
 ExtendedCoreImage

 Copyright (c) 2005, Apple Computer, Inc., all rights reserved.
*/

#import "ExtendedCoreImage.h"
#import <QuartzCore/CIImagePrivate.h>

@implementation CIImage (WWDCAutomatorDemo)

- (NSURL *)fileURL
{
    id userInfo = [self userInfo];
    if ([userInfo isKindOfClass:[NSURL class]])
    {
        return (NSURL *)userInfo;
    }

    return nil;
}

- (void)setFileURL:(NSURL *)url
{
    [self setUserInfo:url];
}

@end
```

[Next](Save%20Image%20To%20File%20%28Step%201%29-Save%20Image%20To%20File.h.md)[Previous](Extended%20Core%20Image-ExtendedCoreImage.h.md)

