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
doc_path: '/documentation/swift/string/utf16view/subscript(_:)-5ta1h'
source_url: 'https://developer.apple.com/documentation/swift/string/utf16view/subscript(_:)-5ta1h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/utf16view/subscript%28_%3A%29-5ta1h.json'
content_hash: 'sha256:88b9981acd85bc9a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UTF16View](../utf16view.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the code unit at the given position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(idx: String.UTF16View.Index) -> UTF16.CodeUnit { get }
```

## Overview

The following example uses the subscript to print the value of a string’s first UTF-16 code unit.

```swift
let greeting = "Hello, friend!"
let i = greeting.utf16.startIndex
print("First character's UTF-16 code unit: \(greeting.utf16[i])")
// Prints "First character's UTF-16 code unit: 72"
```
