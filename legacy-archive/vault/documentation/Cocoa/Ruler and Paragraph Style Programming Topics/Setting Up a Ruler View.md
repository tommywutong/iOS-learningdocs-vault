---
title: Ruler and Paragraph Style Programming Topics
apple_id: 10000089i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2007-09-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Tasks/SettingUpRulerView.html
archived_at: '2026-07-15T07:18:45.847439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ruler and Paragraph Style Programming Topics](Introduction%20to%20Rulers%20and%20Paragraph%20Styles.md)


[Next](Changing%20a%20Ruler%E2%80%99s%20Measurement%20Units.md)[Previous](About%20Ruler%20Markers.md)

# Setting Up a Ruler View

Adding a ruler view to a scroll view can be as simple as invoking the `NSScrollView` method [setHasHorizontalRuler:](https://developer.apple.com/documentation/appkit/nsscrollview/1403457-hashorizontalruler) and [setHasVerticalRuler:](https://developer.apple.com/documentation/appkit/nsscrollview/1403496-hasverticalruler) methods. These create instances of the default ruler view class, which you can change using the `NSScrollView` class method `setRulerViewClass:`. You can also set ruler views directly on a per-instance basis using [setHorizontalRulerView:](https://developer.apple.com/documentation/appkit/nsscrollview/1403498-horizontalrulerview) and [setVerticalRulerView:](https://developer.apple.com/documentation/appkit/nsscrollview/1403507-verticalrulerview). Once you’ve added rulers to a scroll view, you can hide and reveal them using [setRulersVisible:](https://developer.apple.com/documentation/appkit/nsscrollview/1403445-rulersvisible).

Beyond creating the rulers, you need take only two steps to set them up properly for use by the views contained within the scroll view: locate the zero marks of the rulers and reserve room for accessory views. You normally perform these steps only once, when setting up the `NSScrollView` object with rulers. However, if you allow the user to reset document attributes such as margins, you should change the zero mark locations as well. Also, if you reuse the scroll view by swapping in a new document view you may need to set up the rulers again with different settings.

The first step is to determine where you want the zero marks of the rulers to be located relative to the bounds origin of the document view. The zero marks are coincident with the bounds origin by default, but you can change this with the method [setOriginOffset:](https://developer.apple.com/documentation/appkit/nsrulerview/1535432-originoffset). This method takes an offset specified in the document view’s coordinate system. If you need to set the origin offset based on a point in a subview of the document view, such as a text view that’s inset on a page, use [convertPoint:fromView:](https://developer.apple.com/documentation/appkit/nsview/1483269-convertpoint) to realize it in the document view’s coordinate system. This Objective-C code fragment places the zero marks at the bounds origin of a client view, which lies somewhere inside the document view:

```
zero = [docView convertPoint:[clientView bounds].origin fromView:clientView];
[horizRuler setOriginOffset:zero.x - [docView bounds].origin.x];
```

After placing the zero marks, you should set up your rulers so that they don’t change in size as the user works within the document view. For example, if two different subviews of the document view use different accessory views, the ruler view enlarges itself as necessary each time you change the accessory view. Such changes are at best unsightly and at worst confusing to the user. To avoid this problem, calculate ahead of time the sizes of the largest accessory view and the largest markers, and set the ruler view’s required thickness for these elements using [setReservedThicknessForAccessoryView:](https://developer.apple.com/documentation/appkit/nsrulerview/1530160-reservedthicknessforaccessoryvie) and [setReservedThicknessForMarkers:](https://developer.apple.com/documentation/appkit/nsrulerview/1535112-reservedthicknessformarkers). For example, if you have two accessory views for the horizontal ruler, one `16.0` PostScript units high and the other `24.0`, invoke [setReservedThicknessForAccessoryView:](https://developer.apple.com/documentation/appkit/nsrulerview/1530160-reservedthicknessforaccessoryvie) with an argument of `24.0`.

[Next](Changing%20a%20Ruler%E2%80%99s%20Measurement%20Units.md)[Previous](About%20Ruler%20Markers.md)

