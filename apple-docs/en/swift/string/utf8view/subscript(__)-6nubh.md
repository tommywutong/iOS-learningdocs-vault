---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/utf8view/subscript(_:)-6nubh'
source_url: 'https://developer.apple.com/documentation/swift/string/utf8view/subscript(_:)-6nubh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/utf8view/subscript%28_%3A%29-6nubh.json'
content_hash: 'sha256:c053204296b99b3b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UTF8View](../utf8view.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the code unit at the given position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: String.UTF8View.Index) -> UTF8.CodeUnit { get }
```

## Overview

The following example uses the subscript to print the value of a string’s first UTF-8 code unit.

```swift
let greeting = "Hello, friend!"
let i = greeting.utf8.startIndex
print("First character's UTF-8 code unit: \(greeting.utf8[i])")
// Prints "First character's UTF-8 code unit: 72"
```
