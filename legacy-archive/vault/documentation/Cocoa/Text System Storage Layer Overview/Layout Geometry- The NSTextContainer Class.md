---
title: Text System Storage Layer Overview
apple_id: 10000087i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/Concepts/LayoutGeometry.html
archived_at: '2026-07-15T07:20:26.727619Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System Storage Layer Overview](Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md)


[Next](Creating%20Text%20Storage.md)[Previous](The%20Storage%20Layer-%20The%20NSTextStorage%20Class.md)

# Layout Geometry: The NSTextContainer Class

An [NSTextContainer](https://developer.apple.com/documentation/appkit/nstextcontainer) object defines the area on a page in which the Cocoa text system lays out text. By default, a text container defines a simple, rectangular area, but you can create subclasses that define areas with any geometrical shape, including regions with holes around which text flows.

`NSTextContainer` provides one of the four primary text objects in the Cocoa text system. Text containers work with text storage objects, layout managers, and text views to store, lay out, and display attributed text strings. In particular, a text container works directly with a layout manager, which uses an [NSTypesetter](https://developer.apple.com/documentation/appkit/nstypesetter) object to generate line-fragment rectangles in which to place glyphs (character shapes), as described in [Line Fragment Generation](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextLayout/Concepts/CalcTextLayout.html#//apple_ref/doc/uid/20000847)

When the typesetter generates line fragments, the text container is particularly concerned with the direction in which text layout proceeds. There are two aspects to layout direction: line sweep and line movement. Line sweep is the direction in which the system lays out glyphs within lines. Line movement is the direction in which the system lays out lines upon the page. The typesetter object determines these parameters and passes them as constant values to the text container. Both line sweep and line movement can proceed from left to right, right to left, top to bottom, and bottom to top. In addition, the typesetter can specify no line movement.

The layout manager maintains an array of text containers. It sends a message to its delegate whenever it fills a text container, and the delegate can then add a new text container to be filled. If a text container changes size, or if changes to laid-out text in a container invalidate layout at that point, then the system invalidates the layout in all the subsequent containers in the layout manager’s array.

You can specify that a text container track the size of its text view; that is, if the user resizes the view, the text container resizes itself to match. For more information, see [Tracking the Size of a Text View](Tracking%20the%20Size%20of%20a%20Text%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdolkdjjbeeskbifda).

`NSTextContainer` instances have methods for initialization, managing connection to layout managers and text views, getting and setting the container size, generating line fragments, and hit-testing. In addition, `NSTextContainer` has methods for getting and setting the amount of padding to apply to line fragments. Line fragment padding is extra space included at the ends of line fragments so laid-out glyphs don’t directly touch other elements on the page, such as graphics.

[Next](Creating%20Text%20Storage.md)[Previous](The%20Storage%20Layer-%20The%20NSTextStorage%20Class.md)

