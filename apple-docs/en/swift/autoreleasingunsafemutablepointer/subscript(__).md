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
doc_path: '/documentation/swift/autoreleasingunsafemutablepointer/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/autoreleasingunsafemutablepointer/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/autoreleasingunsafemutablepointer/subscript%28_%3A%29.json'
content_hash: 'sha256:d07f1fe4ce8f8419'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AutoreleasingUnsafeMutablePointer](../autoreleasingunsafemutablepointer.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Access the `i`th element of the raw array pointed to by `self`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: Int) -> Pointee { get }
```

## Overview

> [!info] Precondition
> `self != nil`.

## See Also

### Accessing a Pointer’s Memory

- [pointee](pointee.md) — Retrieve or set the `Pointee` instance referenced by `self`.
