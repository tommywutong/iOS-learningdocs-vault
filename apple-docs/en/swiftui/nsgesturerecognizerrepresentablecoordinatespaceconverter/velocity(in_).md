---
title: 'velocity(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/velocity(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/velocity(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/velocity%28in%3A%29.json'
content_hash: 'sha256:1da7f5ff44dc7cec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSGestureRecognizerRepresentableCoordinateSpaceConverter](../nsgesturerecognizerrepresentablecoordinatespaceconverter.md)

# velocity(in:)

<sub>Instance Method</sub>

Converts the represented gesture recognizer’s current velocity to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

<sub>macOS</sub>

```swift
func velocity(in coordinateSpace: some CoordinateSpaceProtocol) -> CGPoint?
```

## Parameters

- `coordinateSpace` — The SwiftUI coordinate space to convert to.

## Return Value

The represented gesture recognizer’s current velocity converted to the given `coordinateSpace`, or `nil` if the represented gesture recognizer doesn’t respond to `-velocityInView:` selector.
