---
title: attoseconds
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/attoseconds
source_url: 'https://developer.apple.com/documentation/swift/duration/attoseconds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/attoseconds.json'
content_hash: 'sha256:4b53521e6755e5ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# attoseconds

<sub>Instance Property</sub>

The number of attoseconds represented by this `Duration`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attoseconds: Int128 { get }
```

## Discussion

This property provides direct access to the underlying number of attoseconds that the current `Duration` represents.

```swift
let d = Duration.seconds(1)
print(d.attoseconds) // 1_000_000_000_000_000_000
```
