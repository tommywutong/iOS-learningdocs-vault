---
title: 'upToNextMajor(from:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.10+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/uptonextmajor(from:)'
source_url: 'https://developer.apple.com/documentation/swift/range/uptonextmajor(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/uptonextmajor%28from%3A%29.json'
content_hash: 'sha256:f10d9ab12dcbb5f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# upToNextMajor(from:)

<sub>Type Method</sub>

Returns a requirement for a version range, starting at the given minimum version and going up to the next major version. This is the recommended version requirement.

<sub>macOS</sub>

```swift
static func upToNextMajor(from version: Version) -> Range<Bound> where Bound == Version
```

## Parameters

- `version` — The minimum version for the version range.
