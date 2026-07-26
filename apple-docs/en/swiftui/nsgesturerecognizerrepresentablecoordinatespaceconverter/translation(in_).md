---
title: 'translation(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/translation(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/translation(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/translation%28in%3A%29.json'
content_hash: 'sha256:bcf0bf3864168153'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSGestureRecognizerRepresentableCoordinateSpaceConverter](../nsgesturerecognizerrepresentablecoordinatespaceconverter.md)

# translation(in:)

<sub>Instance Method</sub>

Converts the represented gesture recognizer’s current translation to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

<sub>macOS</sub>

```swift
func translation(in coordinateSpace: some CoordinateSpaceProtocol) -> CGPoint?
```

## Parameters

- `coordinateSpace` — The SwiftUI coordinate space to convert to.

## Return Value

The represented gesture recognizer’s current translation converted to the given `coordinateSpace`, or `nil` if the represented gesture recognizer doesn’t respond to `-translationInView:` selector.
