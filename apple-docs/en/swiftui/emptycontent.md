---
title: EmptyContent
framework: SwiftUI
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/emptycontent
source_url: 'https://developer.apple.com/documentation/swiftui/emptycontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/emptycontent.json'
content_hash: 'sha256:d58d307dcf9ee885'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EmptyContent

<sub>Type Alias</sub>

Content which contains nothing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias EmptyContent = EmptyView
```

## Discussion

You will rarely, if ever, need to create an `EmptyContent` directly. Instead, `EmptyContent` represents the absence of content.

This type should be conformed to builder DSL protocols to represent empty content in that DSL.

DSLs should use `EmptyContent` in situations where a content type defines one or more children with generic parameters, and allows the child content to be absent. When absent, the child content’s type in the generic type parameter is `EmptyContent`. `ContentBuilder` also returns `EmptyContent` from `buildBlock()`.

`EmptyContent` defines a `body` property of type `Never` to improve the ergonomics of conforming to multiple DSL protocols, which should all use `Never` as the universal “primitive body” type.

## See Also

### Supporting content types

- [TupleContent](tuplecontent.md) — Content created from a tuple of content to be treated as siblings.
