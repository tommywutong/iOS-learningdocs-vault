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
doc_path: '/documentation/swift/anycollection/subscript(_:)-87z1l'
source_url: 'https://developer.apple.com/documentation/swift/anycollection/subscript(_:)-87z1l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anycollection/subscript%28_%3A%29-87z1l.json'
content_hash: 'sha256:080c2651883c7320'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyCollection](../anycollection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element indicated by `position`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: AnyCollection<Element>.Index) -> Element { get }
```

## Overview

> [!info] Precondition
> `position` indicates a valid position in `self` and `position != endIndex`.
