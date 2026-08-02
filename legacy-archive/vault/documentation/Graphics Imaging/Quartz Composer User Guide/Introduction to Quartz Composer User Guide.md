---
title: Quartz Composer User Guide
apple_id: TP40005381
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: Quartz
published: '2007-07-17'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposerUserGuide/qc_intro/qc_intro.html
archived_at: '2026-07-15T07:37:37.878676Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Quartz%20Composer%20Basic%20Concepts.md)

# Introduction to Quartz Composer User Guide

Quartz Composer is a development tool for processing and rendering graphical data. Its visual programming environment lets you develop graphic processing modules, called compositions, without writing a single line of code. Quartz Composer is also a framework that lets you programmatically access, manage, and manipulate compositions created with the development tool. This document, however, is a guide to the Quartz Composer development tool supplied in OS X v10.5. By reading this guide, you’ll get an introduction to using the Quartz Composer editor and find out how to use it to create a composition. You’ll also see how to use compositions as screen savers and in QuickTime movies.

You should read this document if you are a developer or visual designer who wants to:

- Get an orientation to the Quartz Composer development tool supplied in OS X v10.5
- Create compositions that process graphical content
- Experiment with the latest OS X graphics technologies

Quartz Composer brings together a rich set of graphical and nongraphical technologies, including Quartz 2D, Core Image, Core Video, OpenGL, QuickTime, MIDI System Services, RSS (Really Simple Syndication), and XML. The development tool lets you explore the visual technologies available in OS X without needing to learn the programming interface for that technology.

The information in this document pertains to OS X v10.5.

This document is organized as follows:

- [Quartz Composer Basic Concepts](Quartz%20Composer%20Basic%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobrfvbuqmrrgiwvgvzz) defines the terms used in Quartz Composer and describes the evaluation model and the coordinate system.
- [The Quartz Composer User Interface](The%20Quartz%20Composer%20User%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobrfvbuqmrqgiwviucykjcummjqge) gives an overview of the editor, the viewer, the patch creator, and the other user interface elements in the tool supplied in OS X v10.5.
- [Basic and Advanced Tasks, Tips, and Tricks](Basic%20and%20Advanced%20Tasks%2C%20Tips%2C%20and%20Tricks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobrfvbuqmrqgmwviucykjcummjqge) describes the fundamental operations needed to create a composition, gives timesaving tips, and shows how to use some of the more advanced features.
- [Tutorial: Creating a Composition](Tutorial-%20Creating%20a%20Composition.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobrfvbuqmrrgmwvgvzt) provides step-by-step instructions for creating a composition and using it as a screen saver and a QuickTime movie.
- [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobrfvbuqmrrgewviucykjcummjqge) defines the new terms used in the document.

- Sample Quartz compositions are available in `/Developer/Examples/Quartz Composer`.
- The Quartz Composer developer mailing list ([quartzcomposer-dev](http://lists.apple.com/mailman/listinfo/quartzcomposer-dev)) is an excellent place to discuss issues or topics with other Quartz Composer developers.
- _[Quartz Composer Programming Guide](../Quartz%20Composer%20Programming%20Guide/Introduction%20to%20Quartz%20Composer%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjx)_ describes how to use the Quartz Composer framework to integrate compositions into an application.
- _[Quartz Composer Custom Patch Programming Guide](../Quartz%20Composer%20Custom%20Patch%20Programming%20Guide/Introduction%20to%20Quartz%20Composer%20Custom%20Patch%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2doobx)_ provides instructions on creating your own patches that you can then use in the Quartz Composer development tool.
[Next](Quartz%20Composer%20Basic%20Concepts.md)

