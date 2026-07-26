---
title: gestureForFailureRelationships
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscenedraginteraction/gestureforfailurerelationships
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenedraginteraction/gestureforfailurerelationships'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenedraginteraction/gestureforfailurerelationships.json'
content_hash: 'sha256:eea3d11129e87308'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowSceneDragInteraction](../uiwindowscenedraginteraction.md)

# gestureForFailureRelationships

<sub>Instance Property</sub>

The gesture that the drag interaction adds to the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var gestureForFailureRelationships: UIGestureRecognizer { get }
```

## Discussion

If your app provides other gestures in the same view hierarchy, you may want to set up failure requirements between your app’s gestures and the drag interaction’s gesture. To do this, use the [- requireGestureRecognizerToFail:](<../uigesturerecognizer/require(tofail_).md>) method to relate your gestures to this gesture. For example:

**Swift**

```swift
windowDragInteraction.gestureForFailureRelationships.require(toFail: swipeGesture)
```

**Objective-C**

```objc
[windowDragInteraction.gestureForFailureRelationships requireGestureRecognizerToFail:self.swipeGesture];
```
