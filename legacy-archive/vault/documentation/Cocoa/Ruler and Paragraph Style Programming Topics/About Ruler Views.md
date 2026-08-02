---
title: Ruler and Paragraph Style Programming Topics
apple_id: 10000089i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2007-09-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Concepts/AboutRulerViews.html
archived_at: '2026-07-15T07:18:42.835560Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ruler and Paragraph Style Programming Topics](Introduction%20to%20Rulers%20and%20Paragraph%20Styles.md)


[Next](About%20Ruler%20Markers.md)[Previous](Breaking%20Lines%20by%20Truncation.md)

# About Ruler Views

An NSRulerView resides in an NSScrollView, displaying a labeled ruler and markers for its client, the document view of the NSScrollView or a subview of the document view. The client view can add and remove markers representing its contents, such as graphic elements, margins, and text tabs. The NSRulerView tracks user manipulation of the markers and informs the client view of those actions. NSRulerView handles both horizontal and vertical rulers, which are tiled in the scroll view above and to the side of the content view, respectively. NSRulerViews are sometimes called simply ruler views or even rulers.

A ruler view comprises three regions. First is the ruler area, where the ruler’s baseline, hash marks, and labels are drawn. The ruler area is largely static, but it scales its hash marks to the document view’s coordinate system and can display the hash marks in arbitrary units. The second region is the marker area, where ruler markers (NSRulerMarker objects) representing elements of the client view are displayed. The marker area is more dynamic, changing with the selection and state of the client view. The final region is the accessory view area, which is by default not present but appears when you add an accessory view to the ruler view. An accessory view can contain additional controls for manipulating the ruler’s client view, such as alignment buttons or a set of markers that can be dragged onto the ruler.

A ruler view interacts with its client view in several ways. On appropriating the ruler view, the client view usually sets it up according to its needs. The client view can also dynamically update the ruler view’s markers as its layout changes. In its turn, the ruler view informs the client view of actions the user takes on the ruler markers, allowing the client view to approve or limit the actions and to update its state based on the results of the actions.

The appearance of a ruler is based on both the document view and the client view. The document view, as the backdrop within the scroll view, serves as the canvas on which any client views are laid. Because of the document view’s anchoring role, a ruler always draws its hash marks and labels relative to the document view’s coordinate system. A vertical ruler also checks whether the document view is flipped and acts accordingly. However, the ruler view treats subviews of the document view as items laid out within the coordinate system defined by the document view, and so doesn’t change its hash marks when a client view other than the document view is moved or scaled. For the client view’s convenience it does, however, express marker locations in the client view’s coordinate system. A few other operations that ruler views perform are defined in terms of the ruler’s own coordinate system. The discussion of a feature or method makes clear which coordinate system applies. Table 1 summarizes the coordinate systems involved in using ruler views.

__Table 1__  Coordinate systems used with ruler views

| Coordinate system | Used for |
| Client view | Marker locations |
| Document view | Calculating hash marks based on measurement units and scaling; origin offset for zero marks |
| Ruler view | Temporary ruler lines; component layout |
| Marker image | Image origin (which locates the image relative to the marker location) |

[Next](About%20Ruler%20Markers.md)[Previous](Breaking%20Lines%20by%20Truncation.md)

