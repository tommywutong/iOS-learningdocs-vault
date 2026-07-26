---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/progressreporter/subscript(dynamicmember:)-114si'
source_url: 'https://developer.apple.com/documentation/foundation/progressreporter/subscript(dynamicmember:)-114si'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressreporter/subscript%28dynamicmember%3A%29-114si.json'
content_hash: 'sha256:80ccf87641296849'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressReporter](../progressreporter.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Gets or sets custom string properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final subscript<P>(dynamicMember key: KeyPath<ProgressManager.Properties, P.Type>) -> String? where P : ProgressManager.Property, P.Summary == [String?], P.Value == String? { get }
```

## Parameters

- `key` — A key path to the custom string property type.

## Overview

This subscript provides read-write access to custom progress properties where the value type is `String?` and the summary type is `[String?]`. If the property has not been set, the getter returns the property’s default value.
