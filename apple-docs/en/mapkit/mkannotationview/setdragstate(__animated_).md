---
title: 'setDragState(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, macOS 10.9+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkannotationview/setdragstate(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/setdragstate(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/setdragstate%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:f7c3a482cc8d4a26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# setDragState(_:animated:)

<sub>Instance Method</sub>

Sets the drag state for the annotation view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func setDragState(_ newDragState: MKAnnotationView.DragState, animated: Bool)
```

## Parameters

- `newDragState` — The new drag state for the annotation view.

- `animated` — If [true](../../swift/true.md), the map view animates the change to the new drag state; otherwise, the map view makes the change without animations.

## Discussion

Apps can override this method and use it to implement drag support for custom annotation views. As the system detects user actions that indicate a drag, it calls this method to update the drag state. In response to these changes, your custom implementation of this method needs to do the following:

- When the drag state changes to [MKAnnotationViewDragStateStarting](dragstate-swift.enum/starting.md), set the state to [MKAnnotationViewDragStateDragging](dragstate-swift.enum/dragging.md). If you perform an animation to indicate the beginning of a drag, and the `animated` parameter is [true](../../swift/true.md), perform that animation before changing the state.
- When the state changes to either [MKAnnotationViewDragStateCanceling](dragstate-swift.enum/canceling.md) or [MKAnnotationViewDragStateEnding](dragstate-swift.enum/ending.md), set the state to [MKAnnotationViewDragStateNone](dragstate-swift.enum/none.md). If you perform an animation at the end of a drag, and the `animated` parameter is [true](../../swift/true.md), perform that animation before changing the state.

The default implementation of this method sets the value of the [dragState](dragstate-swift.property.md) property to the value in the `newDragState` parameter only. Therefore, direct subclasses can call the inherited version of this method to change the drag state; otherwise, change the value in the [draggable](isdraggable.md) property directly.

Changing the state to [MKAnnotationViewDragStateDragging](dragstate-swift.enum/dragging.md) or [MKAnnotationViewDragStateNone](dragstate-swift.enum/none.md) is the way to signal to the map view when you finish performing animations. For example, when a drag operation begins for an annotation, the class executes an animation to lift the view off the map. Similarly, when the user drops the annotation, the class performs a drop animation. Even if you don’t perform any animations, call the inherited version of this method to update the [dragState](dragstate-swift.property.md) property.

Don’t try to stop a new drag operation by changing the state from [MKAnnotationViewDragStateStarting](dragstate-swift.enum/starting.md) to [MKAnnotationViewDragStateNone](dragstate-swift.enum/none.md). If you don’t want your annotation view to be draggable, set the [draggable](isdraggable.md) property to [false](../../swift/false.md).

## See Also

### Supporting drag operations

- [draggable](isdraggable.md) — A Boolean value that indicates whether the annotation view is draggable.
- [dragState](dragstate-swift.property.md) — The drag state of the annotation view.
