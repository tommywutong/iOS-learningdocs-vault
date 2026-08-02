---
title: Pasteboard Manager Programming Guide
apple_id: TP40001439
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Pasteboard_Prog_Guide/paste_intro/paste_intro.html
archived_at: '2026-07-15T05:23:55.108549Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Pasteboard%20Manager%20Concepts.md)

# Introduction to Pasteboard Manager Programming Guide

Pasteboards are the standard data interchange mechanism for applications on Mac OS X, supported in both Carbon and Cocoa. The Pasteboard Manager is the Carbon programming interface for creating and accessing pasteboards.

This document is for Carbon developers who want to use pasteboards in their applications. The most common uses for the pasteboard are:

- to enable copy-and-paste actions using the Clipboard
- to implement drag-and-drop behavior
- to copy or retrieve text in the standard search field
- to transfer data to and from Mac OS X services (using either the Services menu or Translation Services)

You can also use pasteboards for any other purpose, such as implementing a proprietary clipboard. Pasteboard Manager pasteboards are fully-compatible with Cocoa NSPasteboard objects.

The Pasteboard Manager is available in Mac OS X v10.3 and later.

The Pasteboard Manager replaces both the older Scrap Manager and the Drag Manager’s drag flavor APIs. While the Scrap Manager is still supported, the Pasteboard Manager provides greater flexibility and functionality.

This document is organized into the following chapters:

- [Pasteboard Manager Concepts](Pasteboard%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimzzfvbuqmrqgqwugsscjbeugr2k) describes pasteboard terminology and concepts.
- [Pasteboard Manager Tasks](Pasteboard%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimzzfvbuqmrqgiwueqsdi5bugrsf) describes how to use the Pasteboard Manager in common tasks, such as cut-and-paste and drag-and-drop.
- [Scrap Manager Versus the Pasteboard Manager](Scrap%20Manager%20Versus%20the%20Pasteboard%20Manager.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimzzfvbuqmrqgmwugsscjbdeqsse) specifies replacement APIs for Scrap Manager functions.

In addition to this document, you may find the following documents useful:

- If you are not familar with uniform type identifiers (UTIs), you should read _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_.
- If you are not already familiar with Carbon events, you should read _[Carbon Event Manager Programming Guide](../Carbon%20Event%20Manager%20Programming%20Guide/Introduction%20to%20Carbon%20Event%20Manager%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobz)_.
- If you are not familiar with using HIViews, you should read _[HIView Programming Guide](../HIView%20Programming%20Guide/Introduction%20to%20HIView%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrt)_.
- For more information about implementing services, see _[Setting Up Your Carbon Application to Use the Services Menu](../Setting%20Up%20Your%20Carbon%20Application%20to%20Use%20the%20Services%20Menu/Introduction%20to%20Setting%20Up%20Your%20Carbon%20Application%20to%20Use%20the%20Services%20Menu.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojt)_.
[Next](Pasteboard%20Manager%20Concepts.md)

