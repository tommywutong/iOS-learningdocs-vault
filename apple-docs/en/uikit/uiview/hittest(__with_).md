---
title: 'hitTest(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/hittest(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/hittest(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/hittest%28_%3Awith%3A%29.json'
content_hash: 'sha256:1bf44d8f3498c00e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# hitTest(_:with:)

<sub>Instance Method</sub>

Returns the farthest descendant in the view hierarchy of the current view, including itself, that contains the specified point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func hitTest(_ point: CGPoint, with event: UIEvent?) -> UIView?
```

## Parameters

- `point` — A point in the view’s local coordinate system.

- `event` — The event that warrants a call to this method. If you’re calling this method from outside your event-handling code, you can specify `nil`.

## Return Value

The view object that’s the farthest descendent of the current view and contains `point`. Returns `nil` if the point lies completely outside the view hierarchy of the current view.

## Discussion

This method traverses the view hierarchy by calling the [- pointInside:withEvent:](<point(inside_with_).md>) method of each subview to determine which subview to send a touch event to. If [- pointInside:withEvent:](<point(inside_with_).md>) returns [true](../../swift/true.md), this method continues to traverse the subview hierarchy until it finds the frontmost view that contains the specified point. If a view doesn’t contain the point, this method ignores its branch of the view hierarchy. You rarely need to call this method yourself, but you might override it to hide touch events from subviews.

This method ignores view objects that are hidden, that have disabled user interactions, or that have an alpha level less than `0.01`. This method doesn’t take the view’s content into account when determining a hit, so it can return a view even if the specified point is in a transparent portion of that view’s content.

This method doesn’t report points that lie outside the view’s bounds as hits, even if they actually lie within one of the view’s subviews. This situation can occur if the view’s [clipsToBounds](clipstobounds.md) property is [false](../../swift/false.md) and the affected subview extends beyond the view’s bounds.

> [!note] Note
> When the system calls this method to perform hit-testing for event routing, it expects the resulting view to be part of a [UIWindow](../uiwindow.md) hierarchy.

## See Also

### Hit-testing in a view

- [- pointInside:withEvent:](<point(inside_with_).md>) — Returns a Boolean value indicating whether the receiver contains the specified point.
