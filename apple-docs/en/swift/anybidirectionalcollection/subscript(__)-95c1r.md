---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anybidirectionalcollection/subscript(_:)-95c1r'
source_url: 'https://developer.apple.com/documentation/swift/anybidirectionalcollection/subscript(_:)-95c1r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anybidirectionalcollection/subscript%28_%3A%29-95c1r.json'
content_hash: 'sha256:7bb0244791653827'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyBidirectionalCollection](../anybidirectionalcollection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element indicated by `position`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: AnyBidirectionalCollection<Element>.Index) -> Element { get }
```

## Overview

> [!info] Precondition
> `position` indicates a valid position in `self` and `position != endIndex`.
