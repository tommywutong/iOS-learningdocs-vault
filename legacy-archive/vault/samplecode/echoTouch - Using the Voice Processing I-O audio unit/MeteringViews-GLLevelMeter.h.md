---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/MeteringViews_GLLevelMeter_h.html
archived_at: '2026-07-18T03:29:07.207229Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](LICENSE.txt.md)[Previous](MeteringViews-MeterTable.h.md)

# MeteringViews/GLLevelMeter.h

```objc
/*
 </samplecode>
*/

#import <UIKit/UIKit.h>
#import <OpenGLES/EAGL.h>
#import <OpenGLES/ES1/gl.h>
#import <OpenGLES/ES1/glext.h>

#import "LevelMeter.h"

@interface GLLevelMeter : LevelMeter {
    GLint           _backingWidth;
    GLint           _backingHeight;
    EAGLContext     *_context;
    GLuint          _viewRenderbuffer, _viewFramebuffer;
}

@end
```

[Next](LICENSE.txt.md)[Previous](MeteringViews-MeterTable.h.md)

