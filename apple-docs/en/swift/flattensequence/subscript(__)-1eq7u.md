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
doc_path: '/documentation/swift/flattensequence/subscript(_:)-1eq7u'
source_url: 'https://developer.apple.com/documentation/swift/flattensequence/subscript(_:)-1eq7u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/flattensequence/subscript%28_%3A%29-1eq7u.json'
content_hash: 'sha256:563590fb35359174'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FlattenSequence](../flattensequence.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at `position`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: FlattenSequence<Base>.Index) -> Base.Element.Element { get }
```

## Overview

> [!info] Precondition
> `position` is a valid position in `self` and `position != endIndex`.
