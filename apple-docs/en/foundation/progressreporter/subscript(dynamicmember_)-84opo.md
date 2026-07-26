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
doc_path: '/documentation/foundation/progressreporter/subscript(dynamicmember:)-84opo'
source_url: 'https://developer.apple.com/documentation/foundation/progressreporter/subscript(dynamicmember:)-84opo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressreporter/subscript%28dynamicmember%3A%29-84opo.json'
content_hash: 'sha256:08d4e4d124b01420'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressReporter](../progressreporter.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Gets or sets custom URL properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final subscript<P>(dynamicMember key: KeyPath<ProgressManager.Properties, P.Type>) -> URL? where P : ProgressManager.Property, P.Summary == [URL?], P.Value == URL? { get }
```

## Parameters

- `key` — A key path to the custom URL property type.

## Overview

This subscript provides read-write access to custom progress properties where the value type is `URL?` and the summary type is `[URL?]`. If the property has not been set, the getter returns the property’s default value.
