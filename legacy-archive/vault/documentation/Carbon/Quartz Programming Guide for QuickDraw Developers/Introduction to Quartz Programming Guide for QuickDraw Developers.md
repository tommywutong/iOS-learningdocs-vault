---
title: Quartz Programming Guide for QuickDraw Developers
apple_id: TP40001098
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/QuickDrawToQuartz2D/tq_intro/tq_intro.html
archived_at: '2026-07-15T05:24:32.263367Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Strategies.md)

# Introduction to Quartz Programming Guide for QuickDraw Developers

Quartz is an advanced, two-dimensional drawing engine accessible from all Mac OS X application environments outside of the kernel. It provides low-level, lightweight 2D rendering with unmatched output fidelity regardless of display or printing device. Quartz is the Mac OS X replacement for QuickDraw. Quartz not only replaces QuickDraw, but because its imaging model is substantially different than that of QuickDraw, Quartz can offer more advanced drawing capabilities. The differences between imaging models mean that QuickDraw functions can’t simply be replaced by Quartz functions. Transitioning a QuickDraw application to one that uses only Quartz requires a thoughtful approach.

The purpose of this document is to help developers replace their QuickDraw code with Quartz code that achieves equivalent (or more) functionality. It provides strategies and guidance along with routines that use Quartz to achieve functionality similar to QuickDraw routines.

Any developer who uses QuickDraw functions in their Mac OS X application will benefit from reading this document. This document assumes that the reader has programming experience with the QuickDraw API. It also assumes basic knowledge of the Quartz imaging model. Before starting this document, you may want to read the overview of Quartz in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_. As you read this document, you may find it helpful to keep the programming guide as well as _Quartz 2D Reference Collection_ handy.

This document is organized into the following chapters:

- [Strategies](Strategies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrqgiwviucykjcummjqge) lists the tasks you should complete before rewriting your code and provides strategies for analyzing and revising your code. This chapter is important to read first, because it points to relevant sections in other chapters, or to other relevant resources.
- [Basic Drawing](Basic%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgawviucykjcummjqge) covers the fundamentals of drawing in Quartz with an emphasis on what’s different from QuickDraw.
- [Using Color](Using%20Color.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgywviucykjcummjqge) discusses QuickDraw and Quartz colors and shows how to create color spaces.
- [Converting PICT Data](Converting%20PICT%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgewviucykjcummjqge) shows how to convert PICT data so that it can be used in Quartz and shows how to move data to and from the pasteboard in Mac OS X.
- [Working With Bitmap Image Data](Working%20With%20Bitmap%20Image%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsg4wviucykjcummjqge) shows how, using Quartz, to accomplish a variety of image manipulation tasks that are equivalent to the sorts of tasks you could accomplish using QuickDraw.
- [Masking](Masking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrshawviucykjcummjqge), discusses how to replace mask regions in QuickDraw using masking techniques in Quartz.
- [Updating Regions](Updating%20Regions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgiwviucykjcummjqge) provides strategies and code examples for how to update windows and use overlay windows in Quartz in place of updating regions in QuickDraw.
- [Hit Testing](Hit%20Testing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrshewviucykjcummjqge) describes Quartz functions that are suited for hit testing and provides routines you can use for hit testing in Quartz.
- [Offscreen Drawing](Offscreen%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrsgmwviucykjcummjqge) discusses how to use bitmap graphics contexts and CGLayer objects for offscreen drawing.
- [Performance](Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrtgawviucykjcummjqge) outlines coding practices that ensure your code performs well.
- [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojyfvbuqmrrgewviucykjcummjqge) lists common QuickDraw terms and defines them in terms of Quartz terminology.

You might find these items of value as you move QuickDraw code to Quartz:

- JustDraw and MouseTracking code samples. These are available from the [Graphics & Imaging Quartz Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000424-TP30000559) on the ADC website.
- _[Color Management Overview](../../Graphics%20Imaging/Color%20Management%20Overview/Introduction%20to%20Color%20Management%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnby)_. This document provides a brief introduction to the principles of color perception, color spaces, and color management systems. To use color effectively in Quartz, you’ll want to be familiar with the concepts related to color and color spaces.
- Mailing lists. Join the [quartz-dev](http://lists.apple.com/mailman/listinfo/quartz-dev) mailing list to discuss problems using Quartz in Mac OS X. If you’re having a problem, chances are other developers have faced the same challenge and may be able to help you. Others like you are moving to Quartz from QuickDraw!
- Technical notes and Technical Q&As. Keep up to date on the latest technical information by visiting the [Graphics & Imaging Quartz Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000424-TP30000559). Technical notes and Q&A documents typically provide solutions for thorny problems that don’t crop up too often. If you can’t find a solution in a programming guide, look at these.
[Next](Strategies.md)

