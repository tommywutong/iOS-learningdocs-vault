---
title: Ruler and Paragraph Style Programming Topics
apple_id: 10000089i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2007-09-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Tasks/UpdatingRulerView.html
archived_at: '2026-07-15T07:18:47.656038Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ruler and Paragraph Style Programming Topics](Introduction%20to%20Rulers%20and%20Paragraph%20Styles.md)


[Next](Document%20Revision%20History.md)[Previous](Letting%20Users%20Manipulate%20Markers.md)

# Updating the Ruler View

A single client view may contain many selectable items, such as graphic shapes or paragraphs of text with different ruler settings. When the selection changes, the client must reset the ruler view’s markers based on the new selection. This kind of updating is fairly straightforward and can be performed as described in [Using a Ruler View’s Client](Using%20a%20Ruler%20View%E2%80%99s%20Client.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3tmlkcijbuossdirfa) for situations where the client view itself changes.

Another kind of updating is needed when you want to support dynamic updating of ruler markers as the user manipulates the elements of the client view. For example, when the user moves a shape, you want the ruler markers to relocate when the user finishes moving it. Any method that changes relevant attributes of the selection should update the ruler markers, whether by replacing them as a set or by checking each one present and updating its location.

You can even put such updating code within a modal loop that handles dragging items around in the client view, so that the markers track the position of the selected item. This can be a fairly heavyweight operation to perform while also handling movement of the selected item, however. In support of a lighter weight means of showing this information, NSRulerView allows you to draw temporary ruler lines that can be drawn and erased very quickly. One method, `moveRulerlineFromLocation:toLocation:`, controls the drawing of ruler lines. It takes two locations expressed in the NSRulerView’s coordinate system, erasing the ruler line at the old location and redrawing it at the new. To create a new ruler line, specify `–1.0` as the old location; to erase one completely, specify `–1.0` as the new location. Although you’re responsible for keeping track of the locations to erase and redraw, this isn’t as cumbersome or inefficient as sifting through or replacing the markers themselves.

[Next](Document%20Revision%20History.md)[Previous](Letting%20Users%20Manipulate%20Markers.md)

