---
title: Quartz Programming Guide for QuickDraw Developers
apple_id: TP40001098
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/QuickDrawToQuartz2D/tq_glossary/tq_glossary.html
archived_at: '2026-07-15T05:24:31.889652Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Programming Guide for QuickDraw Developers](Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __blitting__

  The process of moving bits from a back buffer to an onscreen location. Blitting is not necessary (not recommended) when using Quartz.

- __bitmap__

  In Quartz, any two-dimensional array of pixel data in a standard format. Not to be confused with the `BitMap` data type in QuickDraw, which is a 1-bit pixel array.

- __bitmap graphics context__

  A bit-based offscreen drawing destination.

- __CG__

  The prefix used for functions in the Quartz API. See also [Core Graphics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrrgewueqsdijducrcj).

- __CGLayer__

  An offscreen graphics context, introduced in Mac OS X v10.4, suited for high-quality offscreen rendering of content that you plan to reuse.

- __clipboard__

  See [pasteboard](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrrgewueqsdinbeurkj).

- __Core Graphics__

  The name of the framework in which the Quartz API resides—CoreGraphics.framework. The Quartz API is sometimes referred to as the Core Graphics API.

- __CopyBits__

  A QuickDraw function that has no direct replacement in Quartz, primarily because Quartz does not use a bit-based graphics model, as QuickDraw does.

- __filling__

  A drawing operation that paints an area contained within a path, using either a solid color or a pattern. Quartz has two rules that it can use to determine whether a point should be filled—the winding number rule and the even-odd rule. See Quartz 2D Programming Guide for a detailed discussion of these rules.

- __framing__

  See [stroking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrrgewueqsdi5beursd).

- __grafport__

  See [graphics context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrrgewueqsdjbeuqqsh).

- __graphics context__

  In Quartz, an abstraction for a drawing destination. There are different flavors—window, printing, PDF, OpenGL, and bitmap.

- __graphics state__

  Defines the drawing parameter settings (line width, fill color, and many other parameters) for a specific graphics context.

- __GWorld__

  An offscreen drawing context. In Quartz, see [bitmap graphics context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrrgewueqsdindesq2i) and [CGLayer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrrgewueqsdivbegr2b).

- __ImageIO__

  A framework, introduced in Mac OS X v10.4, that provides functions for moving image data into and out of Quartz. Image IO functions are in the ImageIO framework. They use the CG prefix.

- __pasteboard__

  A standardized mechanism for exchanging data within applications or between applications. The most familiar use for pasteboards is handling copy and paste operations.

- __painting__

  For the Quartz equivalent of the QuickDraw painting operation (such as that used for the QuickDraw function `PaintOval`), see [filling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrrgewueqsdi5euossf).

- __pixel manipulation__

  The process of operating on bits. Quartz does not provide functions that operate on a pixel-by-pixel bases. Core Image provides support for image processing on a per-pixel basis.

- __Quartz Compositor__

  An advanced windowing system that manages the onscreen presentation of Quartz, OpenGL, and QuickTime content, much as a video mixer does.

- __resolution independence__

  A feature that supports drawing to an abstract space such that drawing is the same size when rendered for raster devices of any native resolution.

- __stroking__

  A drawing operation which paints a line that straddles a path.

[Previous](Document%20Revision%20History.md)

