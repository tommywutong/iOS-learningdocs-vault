---
title: AttributedTextFormatting.AttributeContainerProxy
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextformatting/attributecontainerproxy
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/attributecontainerproxy.json'
content_hash: 'sha256:5988f2bf268702b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextFormatting](../attributedtextformatting.md)

# AttributedTextFormatting.AttributeContainerProxy

<sub>Structure</sub>

A proxy for a partially validated set of attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct AttributeContainerProxy<Scope, Attribute> where Scope : AttributeScope, Attribute : AttributedStringKey, Attribute.Value : Sendable
```

## Overview

Exposes `Attribute` as read-write and all other attributes as read-only. The type automatically queries the underlying [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md) to constrain values that are accessed.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Structures

- [Scoped](attributecontainerproxy/scoped.md) — A scoped proxy for a partially validated set of attributes.

### Subscripts

- [subscript(_:)](<attributecontainerproxy/subscript(__).md>) — Access the value of the attribute to constrain.
- [subscript(dynamicMember:)](<attributecontainerproxy/subscript(dynamicmember_).md>) — Access the value of the attribute to constrain.
