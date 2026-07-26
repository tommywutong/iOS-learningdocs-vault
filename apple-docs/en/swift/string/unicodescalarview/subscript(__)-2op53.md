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
doc_path: '/documentation/swift/string/unicodescalarview/subscript(_:)-2op53'
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/subscript(_:)-2op53'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/subscript%28_%3A%29-2op53.json'
content_hash: 'sha256:6af60abf0cda69b4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the Unicode scalar value at the given position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: String.UnicodeScalarView.Index) -> Unicode.Scalar { get }
```

## Parameters

- `position` — A valid index of the character view. `position` must be less than the view’s end index.

## Overview

The following example searches a string’s Unicode scalars view for a capital letter and then prints the character and Unicode scalar value at the found index:

```swift
let greeting = "Hello, friend!"
if let i = greeting.unicodeScalars.firstIndex(where: { "A"..."Z" ~= $0 }) {
    print("First capital letter: \(greeting.unicodeScalars[i])")
    print("Unicode scalar value: \(greeting.unicodeScalars[i].value)")
}
// Prints "First capital letter: H"
// Prints "Unicode scalar value: 72"
```
