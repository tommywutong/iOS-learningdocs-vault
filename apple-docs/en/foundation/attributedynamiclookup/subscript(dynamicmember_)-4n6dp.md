---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-4n6dp'
source_url: 'https://developer.apple.com/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-4n6dp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedynamiclookup/subscript%28dynamicmember%3A%29-4n6dp.json'
content_hash: 'sha256:e7a5e704f26c23ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeDynamicLookup](../attributedynamiclookup.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Provides dynamic member lookup for translation attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<T>(dynamicMember keyPath: KeyPath<AttributeScopes.TranslationAttributes, T>) -> T where T : AttributedStringKey { get }
```

## Parameters

- `keyPath` — A key path to a property in the `TranslationAttributes` scope.

## Return Value

The attribute key type that can be used to get or set attribute values.

## Overview

This subscript enables the convenient dot-syntax access to translation attributes on [AttributedString](../attributedstring.md):

```swift
var text = AttributedString("Product Name")
text.skipsTranslation = true
```
