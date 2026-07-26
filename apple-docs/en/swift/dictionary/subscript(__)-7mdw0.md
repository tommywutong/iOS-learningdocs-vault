---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/dictionary/subscript(_:)-7mdw0'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/subscript(_:)-7mdw0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/subscript%28_%3A%29-7mdw0.json'
content_hash: 'sha256:48c1f14169465f07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the value at the given key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(keyPath: [String]) -> USDValue? { get set }
```

## Overview

Reads return `nil` if no value is present at the path. Assigning a non-`nil` value sets it at the path, creating intermediate dictionaries as needed; assigning `nil` erases the value at the path.
