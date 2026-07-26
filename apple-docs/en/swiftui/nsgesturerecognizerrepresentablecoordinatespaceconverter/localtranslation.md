---
title: localTranslation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/localtranslation
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/localtranslation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/localtranslation.json'
content_hash: 'sha256:da70c1719fcbcbde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSGestureRecognizerRepresentableCoordinateSpaceConverter](../nsgesturerecognizerrepresentablecoordinatespaceconverter.md)

# localTranslation

<sub>Instance Property</sub>

The represented gesture recognizer’s current translation in the coordinate space of the SwiftUI view it’s attached to, or `nil` if the represented gesture recognizer doesn’t respond to `-translationInView:` selector.

<sub>macOS</sub>

```swift
@export(implementation) var localTranslation: CGPoint? { get }
```
