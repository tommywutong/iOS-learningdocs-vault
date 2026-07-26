---
title: width
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/proposedviewsize/width
source_url: 'https://developer.apple.com/documentation/swiftui/proposedviewsize/width'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/proposedviewsize/width.json'
content_hash: 'sha256:fc1ece2c578374ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProposedViewSize](../proposedviewsize.md)

# width

<sub>Instance Property</sub>

The proposed horizontal size measured in points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var width: CGFloat?
```

## Discussion

A value of `nil` represents an unspecified width proposal, which a view interprets to mean that it should use its ideal width.

## See Also

### Getting the proposal’s dimensions

- [height](height.md) — The proposed vertical size measured in points.
