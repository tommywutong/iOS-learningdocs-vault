---
title: avTouch
apple_id: DTS40008636
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2014-02-12'
source_url: https://developer.apple.com/library/archive/samplecode/avTouch/Listings/Classes_GLLevelMeter_h.html
archived_at: '2026-07-18T03:28:56.200997Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [avTouch](avTouch.md)


[Next](Classes-GLLevelMeter.m.md)[Previous](Classes-CASound.mm.md)

# Classes/GLLevelMeter.h

```objc
/*

<codex>

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

[Next](Classes-GLLevelMeter.m.md)[Previous](Classes-CASound.mm.md)

