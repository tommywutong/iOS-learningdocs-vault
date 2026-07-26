---
title: NavigationPath.CodableRepresentation
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationpath/codablerepresentation
source_url: 'https://developer.apple.com/documentation/swiftui/navigationpath/codablerepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationpath/codablerepresentation.json'
content_hash: 'sha256:ece42b3ee1894156'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationPath](../navigationpath.md)

# NavigationPath.CodableRepresentation

<sub>Structure</sub>

A serializable representation of a navigation path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CodableRepresentation
```

## Overview

When a navigation path contains elements that conform to the [Codable](../../swift/codable.md) protocol, you can use the path’s `CodableRepresentation` to convert the path to an external representation and to convert an external representation back into a navigation path.

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md)

## See Also

### Encoding a path

- [codable](codable.md) — A value that describes the contents of this path in a serializable format.
