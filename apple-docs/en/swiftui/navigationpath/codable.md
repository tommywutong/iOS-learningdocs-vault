---
title: codable
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationpath/codable
source_url: 'https://developer.apple.com/documentation/swiftui/navigationpath/codable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationpath/codable.json'
content_hash: 'sha256:9cc6c91a24ac2998'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationPath](../navigationpath.md)

# codable

<sub>Instance Property</sub>

A value that describes the contents of this path in a serializable format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var codable: NavigationPath.CodableRepresentation? { get }
```

## Discussion

This value is `nil` if any of the type-erased elements of the path don’t conform to the [Codable](../../swift/codable.md) protocol.

## See Also

### Encoding a path

- [CodableRepresentation](codablerepresentation.md) — A serializable representation of a navigation path.
