---
title: 'accessibilityZoomIn(at:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/accessibilityzoomin(at:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityzoomin(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityzoomin%28at%3A%29.json'
content_hash: 'sha256:fefad85c747fd38f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityZoomIn(at:)

<sub>Instance Method</sub>

Zooms in on the content at the specified point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityZoomIn(at point: CGPoint) -> Bool
```

## Parameters

- `point` — The point where a person performs the zoom in action.

## Return Value

[YES](../yes.md) if this method successfully handles zooming; otherwise, [NO](../no.md). By default, this method returns [NO](../no.md).

## Discussion

If your element has the [supportsZoom](../../uikit/uiaccessibilitytraits/supportszoom.md) trait, you need to implement this method and [- accessibilityZoomOutAtPoint:](<accessibilityzoomout(at_).md>). Use this method to zoom in at the specified point. For example, if the element allows an expand gesture to zoom in to the view’s content, implement this method so that the VoiceOver zoom action receives the same behavior.
