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
doc_path: '/documentation/swift/lazymapsequence/subscript(_:)-36b2w'
source_url: 'https://developer.apple.com/documentation/swift/lazymapsequence/subscript(_:)-36b2w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazymapsequence/subscript%28_%3A%29-36b2w.json'
content_hash: 'sha256:feff37fcbf8bae96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyMapSequence](../lazymapsequence.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at `position`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: Base.Index) -> Element { get }
```

## Overview

> [!info] Precondition
> `position` is a valid position in `self` and `position != endIndex`.
