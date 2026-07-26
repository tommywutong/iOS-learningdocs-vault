---
title: URL.Template.Value
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/template/value
source_url: 'https://developer.apple.com/documentation/foundation/url/template/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/template/value.json'
content_hash: 'sha256:e6695464e49fa0d1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [Template](../template.md)

# URL.Template.Value

<sub>Structure</sub>

The value of a variable used for expanding a template.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Value
```

## Overview

A value can either be some text, a list, or an associate list (a dictionary).

### Examples

```swift
let hello: URL.Template.Value = .text("Hello World!")
let list: URL.Template.Value = .list(["red", "green", "blue"])
let keys: URL.Template.Value = .associativeList([
    "semi": ";",
    "dot": ".",
    "comma": ",",
])
```

Alternatively, for constants, the `ExpressibleBy…Literal` implementations can be used, i.e.

```swift
let hello: URL.Template.Value = "Hello World!"
let list: URL.Template.Value = ["red", "green", "blue"]
let keys: URL.Template.Value = [
    "semi": ";",
    "dot": ".",
    "comma": ",",
]
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [CustomStringConvertible](../../../swift/customstringconvertible.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [ExpressibleByArrayLiteral](../../../swift/expressiblebyarrayliteral.md), [ExpressibleByDictionaryLiteral](../../../swift/expressiblebydictionaryliteral.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Type Methods

- [associativeList(_:)](<value/associativelist(__).md>) — An associative list value (ordered key-value pairs) to be used with a `URL.Template`.
- [list(_:)](<value/list(__).md>) — A list value (an array of `String`s) to be used with a `URL.Template`.
- [text(_:)](<value/text(__).md>) — A text value to be used with a `URL.Template`.
