---
title: 'convert(globalPoint:to:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/convert(globalpoint:to:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/convert(globalpoint:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/convert%28globalpoint%3Ato%3A%29.json'
content_hash: 'sha256:988d92033c6dc83a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIGestureRecognizerRepresentableCoordinateSpaceConverter](../uigesturerecognizerrepresentablecoordinatespaceconverter.md)

# convert(globalPoint:to:)

<sub>Instance Method</sub>

Converts a point in the global coordinate space to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func convert(globalPoint: CGPoint, to coordinateSpace: some CoordinateSpaceProtocol = .local) -> CGPoint
```

## Parameters

- `globalPoint` — The point in the global coordinate space.

- `coordinateSpace` — The SwiftUI coordinate space to convert to.
