---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextselection/attributes/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextselection/attributes/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextselection/attributes/subscript%28_%3A%29.json'
content_hash: 'sha256:03248c952643322a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [AttributedTextSelection](../../attributedtextselection.md) · [Attributes](../attributes.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns a sequence which iterates of the values of a single attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<K>(type: K.Type) -> some Sequence<Optional<K.Value>> where K : AttributedStringKey, K.Value : Sendable { get }
```

## Overview

In the case of a range selection, the returned sequence is based on the runs of the specified attribute, not the runs over all attributes.

```swift
selection.attributes(in: text)[MyAttribute.self].contains(myValue)
```
