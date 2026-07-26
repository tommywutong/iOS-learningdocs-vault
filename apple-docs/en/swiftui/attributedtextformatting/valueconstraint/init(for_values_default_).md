---
title: 'init(for:values:default:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextformatting/valueconstraint/init(for:values:default:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/valueconstraint/init(for:values:default:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/valueconstraint/init%28for%3Avalues%3Adefault%3A%29.json'
content_hash: 'sha256:350698988c786a7a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [AttributedTextFormatting](../../attributedtextformatting.md) · [ValueConstraint](../valueconstraint.md)

# init(for:values:default:)

<sub>Initializer</sub>

Create a definition that constrains an attribute’s value to a defined set of allowed values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(for attribute: AttributeKey.Type, values allowedValues: Set<AttributeKey.Value?>, default defaultValue: AttributeKey.Value?)
```

## Parameters

- `allowedValues` — A set of values that are permitted.

- `defaultValue` — A single permitted value that is used to replace any values that are not in the set of `allowedValues`.
