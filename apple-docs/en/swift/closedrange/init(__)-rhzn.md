---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/closedrange/init(_:)-rhzn'
source_url: 'https://developer.apple.com/documentation/swift/closedrange/init(_:)-rhzn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/init%28_%3A%29-rhzn.json'
content_hash: 'sha256:055a14089f4cb3f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ClosedRange](../closedrange.md)

# init(_:)

<sub>Initializer</sub>

Now that Range is conditionally a collection when Bound: Strideable, CountableRange is no longer needed. This is a deprecated initializer for any remaining uses of Range(countableRange).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ other: ClosedRange<Bound>)
```
