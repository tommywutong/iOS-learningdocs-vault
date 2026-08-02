---
title: Online Help
apple_id: 10000009i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2006-06-28'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OnlineHelp/Concepts/Tooltips.html
archived_at: '2026-07-15T07:17:33.049149Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Online Help](Introduction%20to%20Online%20Help.md)


[Next](Specifying%20the%20Comprehensive%20Help%20File.md)[Previous](Comprehensive%20Help.md)

# Tooltips

A tooltip is a bit of text that provides information about a view. If the user holds the cursor over the view for more than the default delay, the tooltip text is displayed in a small framed rectangle next to the cursor. By default, a view does not display a tooltip. To turn on tooltip display for a view, you invoke the `setToolTip:` method to install tooltip text for the view. To turn display off, you invoke `setToolTip:` with an empty string.

See _[Providing Help Tags in Carbon](../../Carbon/Providing%20Help%20Tags%20in%20Carbon/Introduction%20to%20Providing%20Help%20Tags%20in%20Carbon.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgmzdk)_ for guidance in writing tooltips.

If you do not want the tool tip to be displayed for the entire view, you can create one or more tool tips that apply to only sections of the view. The tool tip text also can be either static or determined when the tool tip is displayed. To create a tool tip for only a section of the view, you invoke `addToolTipRect:owner:userData:` with a rectangle identifying the tool tip area and an object, the owner, that can later provide the tool tip text. To remove individual tool tips created with this method, you invoke `removeToolTip:` with a tag identifying the tool tip. To remove all tool tips assigned to the view, you invoke `removeAllToolTips`.

[Next](Specifying%20the%20Comprehensive%20Help%20File.md)[Previous](Comprehensive%20Help.md)

