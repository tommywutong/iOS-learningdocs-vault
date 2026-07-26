---
title: 'corners(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/roundedrectangularshape/corners(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/roundedrectangularshape/corners(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/roundedrectangularshape/corners%28in%3A%29.json'
content_hash: 'sha256:aa8bb054a48b2c5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RoundedRectangularShape](../roundedrectangularshape.md)

# corners(in:)

<sub>Instance Method</sub>

Resolved corners given a size. If the corner style of a shape is size-dependent, read the provided size and return values accordingly. This function could be called with a nil size when the size hasn’t been determined. In that case, return the best approximated value. For example, for a capsule shape, its corner radius is determined by the size. If size is not available, return `.fixed(.infinity)` to indicate that the corner should be as round as it could be.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func corners(in size: CGSize?) -> Self.Corners?
```
