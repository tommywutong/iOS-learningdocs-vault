---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Classes_OSX_GLEssentialsFullscreenWindow_h.html
archived_at: '2026-07-18T03:10:01.591409Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Classes-iOS-ES2Renderer.h.md)[Previous](GLEssentials-Source-Classes-OSX-GLEssentialsGLView.m.md)

# GLEssentials/Source/Classes/OSX/GLEssentialsFullscreenWindow.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Fullscreen window class.
  All logic here could have been done in the window controller except that, by default, borderless windows cannot be made key and input cannot go to them.
  Therefore, this class exists to override canBecomeKeyWindow allowing this borderless window to accept inputs.
  This class is not part of the NIB and entirely managed in code by the window controller.
 */
#import <Cocoa/Cocoa.h>

@interface GLEssentialsFullscreenWindow : NSWindow

@end
```

[Next](GLEssentials-Source-Classes-iOS-ES2Renderer.h.md)[Previous](GLEssentials-Source-Classes-OSX-GLEssentialsGLView.m.md)

