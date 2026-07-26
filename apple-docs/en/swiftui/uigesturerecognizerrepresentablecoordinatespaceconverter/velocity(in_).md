---
title: 'velocity(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/velocity(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/velocity(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/velocity%28in%3A%29.json'
content_hash: 'sha256:dbf25b2f409508b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIGestureRecognizerRepresentableCoordinateSpaceConverter](../uigesturerecognizerrepresentablecoordinatespaceconverter.md)

# velocity(in:)

<sub>Instance Method</sub>

Converts the represented gesture recognizer’s current velocity to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func velocity(in coordinateSpace: some CoordinateSpaceProtocol) -> CGPoint?
```

## Parameters

- `coordinateSpace` — The SwiftUI coordinate space to convert to.

## Discussion

If the gesture recognizer does not implement a `velocityInView:` method, returns nil.
