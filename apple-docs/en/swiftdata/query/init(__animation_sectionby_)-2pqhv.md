---
title: 'init(_:animation:sectionBy:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/query/init(_:animation:sectionby:)-2pqhv'
source_url: 'https://developer.apple.com/documentation/swiftdata/query/init(_:animation:sectionby:)-2pqhv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query/init%28_%3Aanimation%3Asectionby%3A%29-2pqhv.json'
content_hash: 'sha256:e5d501e4d9209982'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Query](../query.md)

# init(_:animation:sectionBy:)

<sub>Initializer</sub>

Creates a sectioned query from a fetch descriptor, grouped by an optional String key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ descriptor: FetchDescriptor<Element>, animation: Animation, sectionBy sectionKeyPath: KeyPath<Element, String?>? = nil) where Result == [Element]
```

## See Also

### Creating an unsorted, sectioned query

- [init(_:animation:sectionBy:)](<init(__animation_sectionby_)-2em2m.md>) — Creates a sectioned query from a fetch descriptor, grouped into sections by a String key path. _(beta)_
- [init(_:transaction:sectionBy:)](<init(__transaction_sectionby_)-5814o.md>) — Creates a sectioned query from a fetch descriptor, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(_:transaction:sectionBy:)](<init(__transaction_sectionby_)-9sb87.md>) — Creates a sectioned query from a fetch descriptor, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
