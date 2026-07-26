---
title: 'filter(runBoundaries:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributecontainer/filter(runboundaries:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/filter(runboundaries:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/filter%28runboundaries%3A%29.json'
content_hash: 'sha256:0446d6ac806e774e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeContainer](../attributecontainer.md)

# filter(runBoundaries:)

<sub>Instance Method</sub>

Returns a copy of the attribute container with only attributes that have the provided run boundaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter(runBoundaries: AttributedString.AttributeRunBoundaries?) -> AttributeContainer
```

## Parameters

- `runBoundaries` — The required `runBoundaries` value of the filtered attributes. If `nil` is provided, only attributes not bound to any specific boundary will be returned.

## Return Value

A copy of the attribute container with only attributes whose `runBoundaries` property matches the provided value.
