---
title: localTranslation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/localtranslation
source_url: 'https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/localtranslation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/localtranslation.json'
content_hash: 'sha256:adefaef5f18a90bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIGestureRecognizerRepresentableCoordinateSpaceConverter](../uigesturerecognizerrepresentablecoordinatespaceconverter.md)

# localTranslation

<sub>Instance Property</sub>

The represented gesture recognizer’s current translation in the coordinate space of the SwiftUI view it’s attached to.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@export(implementation) var localTranslation: CGPoint? { get }
```

## Discussion

If the gesture recognizer does not implement a `translationInView:` method, returns nil.
