---
title: localVelocity
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/localvelocity
source_url: 'https://developer.apple.com/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/localvelocity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsgesturerecognizerrepresentablecoordinatespaceconverter/localvelocity.json'
content_hash: 'sha256:d468f2b9bb7abda5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSGestureRecognizerRepresentableCoordinateSpaceConverter](../nsgesturerecognizerrepresentablecoordinatespaceconverter.md)

# localVelocity

<sub>Instance Property</sub>

The represented gesture recognizer’s current velocity in the coordinate space of the SwiftUI view it’s attached to, or `nil` if the represented gesture recognizer doesn’t respond to `-velocityInView:` selector.

<sub>macOS</sub>

```swift
@export(implementation) var localVelocity: CGPoint? { get }
```
