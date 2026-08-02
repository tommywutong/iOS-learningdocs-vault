---
title: ConditionalRendering
apple_id: DTS40010087
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-06-17'
source_url: https://developer.apple.com/library/archive/samplecode/ConditionalRendering/Listings/Readme_txt.html
archived_at: '2026-07-18T03:04:14.154283Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ConditionalRendering](ConditionalRendering.md)


[Next](main.m.md)[Previous](ConditionalRendering.md)

# Readme.txt

```
ConditionalRendering

================================================================================
DESCRIPTION:

This sample demonstrates how to do conditional rendering based on an occlusion 
query. The NV_conditional_render extension defines two functions, 
BeginConditionalRenderNV and EndConditionalRenderNV, between which rendering 
commands may be discarded based on the results of an occlusion query. If the 
specified occlusion query returns a non-zero value, rendering commands between 
these calls are executed; otherwise, they are all discarded.

================================================================================
BUILD REQUIREMENTS:

OS X v10.9 or later, Xcode 5.0 or later

================================================================================
RUNTIME REQUIREMENTS:

OS X v10.7 or later

================================================================================
Copyright (C) 2010~2014 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](ConditionalRendering.md)

