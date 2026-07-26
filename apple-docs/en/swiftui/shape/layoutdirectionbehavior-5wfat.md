---
title: layoutDirectionBehavior
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shape/layoutdirectionbehavior-5wfat
source_url: 'https://developer.apple.com/documentation/swiftui/shape/layoutdirectionbehavior-5wfat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/layoutdirectionbehavior-5wfat.json'
content_hash: 'sha256:c2ffa9047a931552'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# layoutDirectionBehavior

<sub>Instance Property</sub>

Returns the behavior this shape should use for different layout directions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var layoutDirectionBehavior: LayoutDirectionBehavior { get }
```

## Discussion

If the layoutDirectionBehavior for a Shape is one that mirrors, the shape’s path will be mirrored horizontally when in the specified layout direction. When mirrored, the individual points of the path will be transformed.

Defaults to `.mirrors` when deploying on iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0 and later, and to `.fixed` if not. To mirror a path when deploying to earlier releases, either use `View.flipsForRightToLeftLayoutDirection` for a filled or stroked shape or conditionally mirror the points in the path of the shape.
