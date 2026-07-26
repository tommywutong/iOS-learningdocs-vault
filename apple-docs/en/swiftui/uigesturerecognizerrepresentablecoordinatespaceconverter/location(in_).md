---
title: 'location(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/location(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/location(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/location%28in%3A%29.json'
content_hash: 'sha256:067c3d9d6a2559f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIGestureRecognizerRepresentableCoordinateSpaceConverter](../uigesturerecognizerrepresentablecoordinatespaceconverter.md)

# location(in:)

<sub>Instance Method</sub>

Converts the represented gesture recognizer’s current location to a SwiftUI coordinate space  of an ancestor of the view the gesture recognizer is attached to.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func location(in coordinateSpace: some CoordinateSpaceProtocol) -> CGPoint
```

## Parameters

- `coordinateSpace` — The SwiftUI coordinate space to convert to.
