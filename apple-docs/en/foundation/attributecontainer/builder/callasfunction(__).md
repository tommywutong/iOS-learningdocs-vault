---
title: 'callAsFunction(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributecontainer/builder/callasfunction(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/builder/callasfunction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/builder/callasfunction%28_%3A%29.json'
content_hash: 'sha256:3f787b0bb0788da8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeContainer](../../attributecontainer.md) · [Builder](../builder.md)

# callAsFunction(_:)

<sub>Instance Method</sub>

Builds an attribute container by setting an attribute and returning a modified attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func callAsFunction(_ value: T.Value) -> AttributeContainer where T.Value : Sendable
```

## Parameters

- `value` — The value to set on the returned attribute container.

## Return Value

An attribute container with the provided value set on the builder’s [AttributedStringKey](../../attributedstringkey.md).
