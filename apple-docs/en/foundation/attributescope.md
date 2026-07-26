---
title: AttributeScope
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescope
source_url: 'https://developer.apple.com/documentation/foundation/attributescope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescope.json'
content_hash: 'sha256:35d36ce92d2de925'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# AttributeScope

<sub>Protocol</sub>

A type that organizes attributes into a grouping, and supports dynamic member lookup and serialization of attribute keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AttributeScope : DecodingConfigurationProviding, EncodingConfigurationProviding, SendableMetatype
```

## Overview

Attribute owners — typically frameworks — define attributes with [AttributedStringKey](attributedstringkey.md) types. To allow access to attributes with dynamic member lookup, owners create one or more structures that conform to [AttributeScope](attributescope.md). The scopes provide short names for their attributes that map to the [AttributedStringKey](attributedstringkey.md) type. The following example shows how to do this:

```swift
struct TextStyleAttributes : AttributeScope {
    let foregroundColor : ForegroundColorAttribute // ForegroundColorAttribute.Value == Color
    let backgroundColor : BackgroundColorAttribute // BackgroundColorAttribute.Value == Color
    let underlineStyle : UnderlineStyleAttribute // UnderlineStyleAttribute.Value == UnderlineStyle
    // etc.
}
```

This allows callers to use a syntax like `myAttributedString.foregroundColor = .red`.

## Relationships

- **Inherits From**: [DecodingConfigurationProviding](decodingconfigurationproviding.md), [EncodingConfigurationProviding](encodingconfigurationproviding.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [AccessibilityAttributes](attributescopes/accessibilityattributes.md), [AppKitAttributes](attributescopes/appkitattributes.md), [FoundationAttributes](attributescopes/foundationattributes.md), [NumberFormatAttributes](attributescopes/foundationattributes/numberformatattributes.md), [SpeechAttributes](attributescopes/speechattributes.md), [SwiftUIAttributes](attributescopes/swiftuiattributes.md), [TranslationAttributes](attributescopes/translationattributes.md), [UIKitAttributes](attributescopes/uikitattributes.md)

## Topics

### Supporting Coding Configurations

- [encodingConfiguration](attributescope/encodingconfiguration.md) — The configuration for encoding the attribute scope.
- [decodingConfiguration](attributescope/decodingconfiguration.md) — The configuration for decoding the attribute scope.

### Type Properties

- [attributeKeys](attributescope/attributekeys.md) — A list of all attribute keys contained within this scope and any sub-scopes.
