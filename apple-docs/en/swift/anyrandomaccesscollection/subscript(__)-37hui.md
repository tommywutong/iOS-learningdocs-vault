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
doc_path: '/documentation/swift/anyrandomaccesscollection/subscript(_:)-37hui'
source_url: 'https://developer.apple.com/documentation/swift/anyrandomaccesscollection/subscript(_:)-37hui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyrandomaccesscollection/subscript%28_%3A%29-37hui.json'
content_hash: 'sha256:c9f682a24506f8dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyRandomAccessCollection](../anyrandomaccesscollection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element indicated by `position`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: AnyRandomAccessCollection<Element>.Index) -> Element { get }
```

## Overview

> [!info] Precondition
> `position` indicates a valid position in `self` and `position != endIndex`.
