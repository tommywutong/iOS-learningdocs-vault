---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/taskpriority/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/taskpriority/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskpriority/init%28_%3A%29.json'
content_hash: 'sha256:a6bf21e8b61ce096'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskPriority](../taskpriority.md)

# init(_:)

<sub>Initializer</sub>

Convert this `UnownedJob/Priority` to a [TaskPriority](../taskpriority.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ p: JobPriority)
```

## Discussion

Most values are directly interchangeable, but this initializer reserves the right to fail for certain values.
