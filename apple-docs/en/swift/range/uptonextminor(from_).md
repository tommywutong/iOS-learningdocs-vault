---
title: 'upToNextMinor(from:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.10+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/uptonextminor(from:)'
source_url: 'https://developer.apple.com/documentation/swift/range/uptonextminor(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/uptonextminor%28from%3A%29.json'
content_hash: 'sha256:cfade00f88b14d24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# upToNextMinor(from:)

<sub>Type Method</sub>

Returns a requirement for a version range, starting at the given minimum version and going up to the next minor version.

<sub>macOS</sub>

```swift
static func upToNextMinor(from version: Version) -> Range<Bound> where Bound == Version
```

## Parameters

- `version` — The minimum version for the version range.
