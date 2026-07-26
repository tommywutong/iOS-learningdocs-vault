---
title: height
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/proposedviewsize/height
source_url: 'https://developer.apple.com/documentation/swiftui/proposedviewsize/height'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/proposedviewsize/height.json'
content_hash: 'sha256:c4bf348c7ae4889d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProposedViewSize](../proposedviewsize.md)

# height

<sub>Instance Property</sub>

The proposed vertical size measured in points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var height: CGFloat?
```

## Discussion

A value of `nil` represents an unspecified height proposal, which a view interprets to mean that it should use its ideal height.

## See Also

### Getting the proposal’s dimensions

- [width](width.md) — The proposed horizontal size measured in points.
