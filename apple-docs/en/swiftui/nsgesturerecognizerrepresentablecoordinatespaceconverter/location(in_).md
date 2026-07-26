---
title: 'location(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/location(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/location(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/location%28in%3A%29.json'
content_hash: 'sha256:23ac275ac0858fb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSGestureRecognizerRepresentableCoordinateSpaceConverter](../nsgesturerecognizerrepresentablecoordinatespaceconverter.md)

# location(in:)

<sub>Instance Method</sub>

Converts the represented gesture recognizer’s current location to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

<sub>macOS</sub>

```swift
func location(in coordinateSpace: some CoordinateSpaceProtocol) -> CGPoint
```

## Parameters

- `coordinateSpace` — The SwiftUI coordinate space to convert to.

## Return Value

The represrnted gesture recognizer’s current location converted into the given `coordinateSpace`.
