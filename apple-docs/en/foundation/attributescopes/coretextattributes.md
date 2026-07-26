---
title: AttributeScopes.CoreTextAttributes
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/coretextattributes
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/coretextattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/coretextattributes.json'
content_hash: 'sha256:2f0f8f347d04ed6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeScopes](../attributescopes.md)

# AttributeScopes.CoreTextAttributes

<sub>Structure</sub>

A namespace for attributes defined by CoreText.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CoreTextAttributes
```

## Overview

Note that this is _not_ an [AttributeScope](../attributescope.md), but merely a namespace for [AttributedStringKey](../attributedstringkey.md)s that describe CoreText concepts. Those attributes may be used by _other frameworks_ to describe those concepts. Unless documented otherwise, frameworks generally inidcate support for a certain attribute by adding it to the framework’s [AttributeScope](../attributescope.md).

CoreText specifically does not support Swift [AttributedStringKey](../attributedstringkey.md), and will not recognize the attributes nested in this namespace when used directly with CoreText API, no matter if used in an `AttributedString` or `NSAttributedString`.

## Topics

### Enumerations

- [LineHeightAttribute](coretextattributes/lineheightattribute.md) — An attribute for defining the height of lines in a text.
- [TextAlignmentAttribute](coretextattributes/textalignmentattribute.md) — An attribute defining the explicit horizontal alignment of a paragraph.
