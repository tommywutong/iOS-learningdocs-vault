---
title: GLCarbon1ContextPbuffer
apple_id: DTS10003144
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2004-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/GLCarbon1ContextPbuffer/Introduction/Intro.html
archived_at: '2026-07-18T03:09:51.469081Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# GLCarbon1ContextPbuffer

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2004-03-26 Demostrates using OpenGL pixel buffers with a single shared context. |
| __Build Requirements:__ | Xcode |
| __Runtime Requirements:__ | Mac OS X v10.3 |

Renders one of a number of mathematically defined surfaces into the pixel buffer and then uses this as the texture to draw on the faces of a simple cube a windowed drawable.
This sample specifically shows how to use a single context for both the window and the pbuffer drawables, switching between them for drawing, keeping consistent state. Two non-standard techniques are needed to make this sample possible:
First one can use the buffer naming facilities in AGL to allow a dummy context to share the windowed drawable with the main context in the app. Since AGL will destroy the accelerated surface associated with a windowed drawable when all contexts are detached, keeping the dummy context attached to the surface ensures the accelerated surface and its contents are maintained.
The second technique to work around an issue in AGL with drawable setting in Mac OS X v10.3. When AGL sets a Pbuffer as the drawable using aglSetPBuffer internal bookkeeping is not correctly updated resulting in AGL ignoring subsequent calls to aglSetDrawable when trying to set the drawable back to the window. The simple work around is to set the drawable to NULL then set it to the window. This should not cause measurable overhead and will ensure the drawable is set back to the window properly. It is expected this issue will be addressed in the future though this work around should always function properly.
The code should also show reasonably well formed Carbon OpenGL application providing a point of departure for developers using OpenGL in Carbon based applications.

[Next](main.c.md)

