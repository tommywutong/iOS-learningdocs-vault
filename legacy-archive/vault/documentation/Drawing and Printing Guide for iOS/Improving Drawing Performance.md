---
title: Drawing and Printing Guide for iOS
apple_id: TP40010156
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Graphics & Animation
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/DrawingTips/DrawingTips.html
archived_at: '2026-07-15T04:56:08.526713Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Drawing and Printing Guide for iOS](About%20Drawing%20and%20Printing%20in%20iOS.md)


[Next](Supporting%20High-Resolution%20Screens%20In%20Views.md)[Previous](Printing.md)

# Improving Drawing Performance

Drawing is a relatively expensive operation on any platform, and optimizing your drawing code should always be an important step in your development process. Table A-1 lists several tips for ensuring that your drawing code is as optimal as possible. In addition to these tips, you should always use the available performance tools to test your code and remove hotspots and redundancies.

__Table A-1__  Tips for improving drawing performance

| Tip | Action |
| Draw minimally | During each update cycle, you should update only the portions of your view that actually changed. If you are using the [drawRect:](https://developer.apple.com/documentation/uikit/uiview/1622529-draw) method of `UIView` to do your drawing, use the update rectangle passed to that method to limit the scope of your drawing. For OpenGL drawing, you must track updates yourself. |
| Call [setNeedsDisplay:](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay) judiciously | If you are calling [setNeedsDisplay:](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay), always spend the time to calculate the actual area that you need to redraw. Don’t just pass a rectangle containing the entire view.  Also, don’t call [setNeedsDisplay:](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay) unless you actually need to redraw content. If the content hasn’t actually changed, don’t redraw it. |
| Mark opaque views as such | Compositing a view whose contents are opaque requires much less effort than compositing one that is partially transparent. To make a view opaque, the contents of the view must not contain any transparency and the [opaque](https://developer.apple.com/documentation/uikit/uiview/1622622-isopaque) property of the view must be set to `YES`. |
| Reuse table cells and views during scrolling | Creating new views during scrolling should be avoided at all costs. Taking the time to create new views reduces the amount of time available for updating the screen, which leads to uneven scrolling behavior. |
| Reuse paths by modifying the current transformation matrix | By modifying the current transformation matrix, you can use a single path to draw content on different parts of the screen. For details, see [Using Coordinate Transforms to Improve Drawing Performance](iOS%20Drawing%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjufvjvona). |
| Avoid clearing the previous content during scrolling | By default, UIKit clears a view’s current context buffer prior to calling its [drawRect:](https://developer.apple.com/documentation/uikit/uiview/1622529-draw) method to update that same area. If you are responding to scrolling events in your view, clearing this region repeatedly during scrolling updates can be expensive. To disable the behavior, you can change the value in the [clearsContextBeforeDrawing](https://developer.apple.com/documentation/uikit/uiview/1622449-clearscontextbeforedrawing) property to `NO`. |
| Minimize graphics state changes while drawing | Changing the graphics state requires work by the underlying graphics subsystems. If you need to draw content that uses similar state information, try to draw that content together to reduce the number of state changes needed. |
| Use Instruments to debug your performance | The Core Animation instrument can help you spot drawing performance problems in your app. In particular:   - Flash Updated Regions makes it easy to see what parts of your view are actually being updated. - Color Misaligned Images helps you see images that are aligned poorly, which results in both fuzzy images and poor performance.   For more information, see [Measuring Graphics Performance in Your iOS Device](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/ExportingandImportingTraceData.html#//apple_ref/doc/uid/TP40004652-CH14) in _[Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)_. |

[Next](Supporting%20High-Resolution%20Screens%20In%20Views.md)[Previous](Printing.md)

