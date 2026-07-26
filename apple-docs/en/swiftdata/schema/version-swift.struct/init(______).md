---
title: 'init(_:_:_:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/schema/version-swift.struct/init(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/version-swift.struct/init(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/version-swift.struct/init%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a68e9468724dfc28'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftData](../../../swiftdata.md) · [Schema](../../schema.md) · [Version](../version-swift.struct.md)

# init(_:_:_:)

<sub>Initializer</sub>

Initializes a version struct with the provided components of a semantic version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ major: Int, _ minor: Int, _ patch: Int)
```

## Parameters

- `major` — The major version number.

- `minor` — The minor version number.

- `patch` — The patch version number.

## Discussion

> [!info] Precondition
> `major >= 0 && minor >= 0 && patch >= 0`.
