---
title: AttributedTextFormatting.AttributeContainerProxy.Scoped
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextformatting/attributecontainerproxy/scoped
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy/scoped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/attributecontainerproxy/scoped.json'
content_hash: 'sha256:bc2f4da4faa921e5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [AttributedTextFormatting](../../attributedtextformatting.md) · [AttributeContainerProxy](../attributecontainerproxy.md)

# AttributedTextFormatting.AttributeContainerProxy.Scoped

<sub>Structure</sub>

A scoped proxy for a partially validated set of attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct Scoped<Subscope> where Subscope : AttributeScope
```

## Overview

Exposes `Attribute` as read-write and all other attributes in the scope as read-only. The type automatically queries the underlying [AttributedTextFormattingDefinition](../../attributedtextformattingdefinition.md) to constrain values that are accessed.

> [!note] Note
> This is equivalent to an [AttributeContainerProxy](../attributecontainerproxy.md), except it only provides dynamic member lookup for attributes in a certain `Subscope`.

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Subscripts

- [subscript(dynamicMember:)](<scoped/subscript(dynamicmember_).md>) — Access the value of the attribute to constrain.
