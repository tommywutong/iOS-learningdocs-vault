---
title: 'filter(inheritedByAddedText:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributecontainer/filter(inheritedbyaddedtext:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/filter(inheritedbyaddedtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/filter%28inheritedbyaddedtext%3A%29.json'
content_hash: 'sha256:c8e60573c5975b4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeContainer](../attributecontainer.md)

# filter(inheritedByAddedText:)

<sub>Instance Method</sub>

Returns a copy of the attribute container with only attributes that specify the provided inheritance behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter(inheritedByAddedText: Bool) -> AttributeContainer
```

## Parameters

- `inheritedByAddedText` — An `inheritedByAddedText` value to filter. Attributes matching this value are included in the returned container.

## Return Value

A copy of the attribute container with only attributes whose `inheritedByAddedText` property matches the provided value.
