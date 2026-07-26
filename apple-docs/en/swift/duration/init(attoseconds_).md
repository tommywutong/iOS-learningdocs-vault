---
title: 'init(attoseconds:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/init(attoseconds:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/init(attoseconds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/init%28attoseconds%3A%29.json'
content_hash: 'sha256:c19d5a319ca120b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# init(attoseconds:)

<sub>Initializer</sub>

Construct a `Duration` from the given number of attoseconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(attoseconds: Int128)
```

## Parameters

- `attoseconds` — The total duration expressed in attoseconds.

## Discussion

This directly constructs a `Duration` from the given number of attoseconds.

```swift
let d = Duration(attoseconds: 1_000_000_000_000_000_000)
print(d) // 1.0 seconds
```
