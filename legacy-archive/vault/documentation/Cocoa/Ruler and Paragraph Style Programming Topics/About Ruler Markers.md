---
title: Ruler and Paragraph Style Programming Topics
apple_id: 10000089i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2007-09-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Concepts/AboutRulerMarkers.html
archived_at: '2026-07-15T07:18:42.333604Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ruler and Paragraph Style Programming Topics](Introduction%20to%20Rulers%20and%20Paragraph%20Styles.md)


[Next](Setting%20Up%20a%20Ruler%20View.md)[Previous](About%20Ruler%20Views.md)

# About Ruler Markers

An `NSRulerMarker` object displays a symbol on an `NSRulerView` object, indicating a location for whatever graphic element it represents in the client of the ruler view (for example, a margin or tab setting, or the edges of a graphic on the page). A ruler marker comprises three primary attributes: the image it displays on the ruler view, the location of that image, and the object it represents. The `setImage:`, [setMarkerLocation:](https://developer.apple.com/documentation/appkit/nsrulermarker/1496255-markerlocation) and [setRepresentedObject:](https://developer.apple.com/documentation/appkit/nsrulermarker/1496244-representedobject) methods set each of these attributes, respectively. In addition, a ruler marker records an offset for the image, allowing it to be placed relative to the marker location much in the way a cursor’s hot spot relates a cursor image to the mouse location; the [setImageOrigin:](https://developer.apple.com/documentation/appkit/nsrulermarker/1496236-imageorigin) method establishes this offset.

Most of these attributes are set upon initialization by the [initWithRulerView:markerLocation:image:imageOrigin:](https://developer.apple.com/documentation/appkit/nsrulermarker/1496240-init) method. New ruler markers don’t have represented objects; the client typically establishes the represented object in its [rulerView:didAddMarker:](https://developer.apple.com/documentation/appkit/nsview/1532033-rulerview) method. A new ruler marker can be moved around in its ruler view, but not removed from it. The [setMovable:](https://developer.apple.com/documentation/appkit/nsrulermarker/1496247-ismovable) and [setRemovable:](https://developer.apple.com/documentation/appkit/nsrulermarker/1496238-removable) methods alter these default settings.

Represented objects allow the ruler view's client to distinguish among different attributes of the selection. In the ruler view client methods, the client can retrieve the marker’s represented object to determine what attribute to alter. Generic attributes can be represented by string or other value objects, such as the edge names “Left”, “Right”, “Top”, and “Bottom”. Attributes already implemented as objects can be represented by those objects. For example, the text system records tab stops as [NSTextTab](https://developer.apple.com/documentation/uikit/nstexttab) objects, which include the tab location and its alignment. When an `NSTextView` object is the client view of a ruler, it simply makes the `NSTextTab` objects the represented objects of the ruler markers.

[Next](Setting%20Up%20a%20Ruler%20View.md)[Previous](About%20Ruler%20Views.md)

