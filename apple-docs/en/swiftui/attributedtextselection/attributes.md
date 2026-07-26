---
title: AttributedTextSelection.Attributes
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextselection/attributes
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextselection/attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextselection/attributes.json'
content_hash: 'sha256:f7eb61bae9b1a642'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextSelection](../attributedtextselection.md)

# AttributedTextSelection.Attributes

<sub>Structure</sub>

A sequence of all attribute values a selection has in a certain text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Attributes<Text>
```

## Overview

The values of a selection are the attribute values of each run that is fully or partially selected, or the typing attributes in the case the selection is an insertion point.

By default, the sequence contains the attribute container for every run or the typing attributes. Use the [Attributes](attributes.md)’ subscript to obtain only the values for a single attribute:

```swift
selection.attributes(in: text)[\.foregroundColor].contains(.red)
```

## Relationships

- **Conforms To**: [Sequence](../../swift/sequence.md)

## Topics

### Subscripts

- [subscript(_:)](<attributes/subscript(__).md>) — Returns a sequence which iterates of the values of a single attribute.
