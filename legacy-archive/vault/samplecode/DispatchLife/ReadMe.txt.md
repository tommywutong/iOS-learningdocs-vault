---
title: DispatchLife
apple_id: DTS40007759
resource_type: Sample Code
platform: macOS
topic: Performance
technology: null
published: '2009-05-29'
source_url: https://developer.apple.com/library/archive/samplecode/DispatchLife/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:07:01.552906Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DispatchLife](DispatchLife.md)


[Next](main.m.md)[Previous](DispatchLife.md)

# ReadMe.txt

```
### DispatchLife ###

===========================================================================
DESCRIPTION:

The classic game of Life showing use of dispatch queues as lightweight threads (each cell is a queue), and an example of how to avoid overloading a slow queue (OpenGL or curses screen updates) with many requests (cell updates) by using a timer to drive the screen updates and allowing the cells to update as fast as they can.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X version 10.6 Snow Leopard

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X version 10.6 Snow Leopard

===========================================================================
PACKAGING LIST:

DispatchLife.c      - Simulation engine using GCD.
DispatchLifeGLView.h    - OpenGL view for visualization.
DispatchLifeGLView.m    - OpenGL view for visualization.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.2
- Updated to use current GCD source API.
Version 1.1
- Updated to use current GCD API.
- Added OpenGL view for visualization.
Version 1.0
- First version (WWDC 2008).

===========================================================================
Copyright (C) 2008-2009 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](DispatchLife.md)

