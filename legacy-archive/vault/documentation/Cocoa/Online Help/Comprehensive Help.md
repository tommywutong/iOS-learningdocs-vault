---
title: Online Help
apple_id: 10000009i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2006-06-28'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OnlineHelp/Concepts/ComprehenHelp.html
archived_at: '2026-07-15T07:17:32.545771Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Online Help](Introduction%20to%20Online%20Help.md)


[Next](Tooltips.md)[Previous](Introduction%20to%20Online%20Help.md)

# Comprehensive Help

Most applications provide some form of on-line help that is more comprehensive and detailed than tooltips, such as conceptual or task help. NSHelpManager allows you to provide this sort of comprehensive help. Apple Help is HTML-based, so you can use a variety of tools to create your content. OS X uses the Help Viewer to display your comprehensive help.

The Help Viewer is a browser that displays standard HTML content. The Help Viewer is optimized to take advantage of AppleScript and the OS X search engine through the use of special HTML tags. Apple Help can access and display HTML content from remote HTTP servers, allowing you to install a core set of help content on the user's system and maintain less frequently accessed pages in a separate location.

If you’ve properly registered your help information in your application’s property list, when the user chooses the Help menu item the help file you have specified for your application is displayed. That file should be the starting point of your help, and should allow users to access whatever information they might need.

[Next](Tooltips.md)[Previous](Introduction%20to%20Online%20Help.md)

