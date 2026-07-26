---
title: Scope
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextformattingdefinition/scope
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformattingdefinition/scope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformattingdefinition/scope.json'
content_hash: 'sha256:18e5fcd29871d0e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md)

# Scope

<sub>Associated Type</sub>

The text formatting definition only allows usage of attributes in this attribute scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Scope : AttributeScope where Self.Scope == Self.Body.Scope
```
