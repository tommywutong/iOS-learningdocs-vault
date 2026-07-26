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
doc_path: '/documentation/foundation/progressmanager/subscript(dynamicmember:)-1qb7p'
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/subscript(dynamicmember:)-1qb7p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/subscript%28dynamicmember%3A%29-1qb7p.json'
content_hash: 'sha256:373d1995469b4078'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressManager](../progressmanager.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Gets or sets custom integer properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final subscript<P>(dynamicMember key: KeyPath<ProgressManager.Properties, P.Type>) -> Int where P : ProgressManager.Property, P.Summary == Int, P.Value == Int { get set }
```

## Parameters

- `key` — A key path to the custom integer property type.

## Overview

This subscript provides read-write access to custom progress properties where both the value and summary types are `Int`. If the property has not been set, the getter returns the property’s default value.
