---
title: 'translation(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/translation(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/translation(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/translation%28in%3A%29.json'
content_hash: 'sha256:c4ba270b5922182c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIGestureRecognizerRepresentableCoordinateSpaceConverter](../uigesturerecognizerrepresentablecoordinatespaceconverter.md)

# translation(in:)

<sub>Instance Method</sub>

Converts the represented gesture recognizer’s current translation to a SwiftUI coordinate space of an ancestor of the view the gesture recognizer is attached to.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func translation(in coordinateSpace: some CoordinateSpaceProtocol) -> CGPoint?
```

## Parameters

- `coordinateSpace` — The SwiftUI coordinate space to convert to.

## Discussion

If the gesture recognizer does not implement a `translationInView:` method, returns nil.
