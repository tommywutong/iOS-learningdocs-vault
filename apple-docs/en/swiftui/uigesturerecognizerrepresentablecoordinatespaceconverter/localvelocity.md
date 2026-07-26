---
title: localVelocity
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/localvelocity
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/localvelocity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/localvelocity.json'
content_hash: 'sha256:7346abe588f19073'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIGestureRecognizerRepresentableCoordinateSpaceConverter](../uigesturerecognizerrepresentablecoordinatespaceconverter.md)

# localVelocity

<sub>Instance Property</sub>

The represented gesture recognizer’s current velocity in the coordinate space of the SwiftUI view it’s attached to.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@export(implementation) var localVelocity: CGPoint? { get }
```

## Discussion

If the gesture recognizer does not implement a `velocityInView:` method, returns nil.
