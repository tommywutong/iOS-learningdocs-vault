---
title: valueTransformerNames()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/valuetransformer/valuetransformernames()
source_url: 'https://developer.apple.com/documentation/foundation/valuetransformer/valuetransformernames()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/valuetransformer/valuetransformernames%28%29.json'
content_hash: 'sha256:c1bc97fd86110e2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ValueTransformer](../valuetransformer.md)

# valueTransformerNames()

<sub>Type Method</sub>

Returns an array of all the registered value transformers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func valueTransformerNames() -> [NSValueTransformerName]
```

## Return Value

An array of all the registered value transformers.

## See Also

### Using the Name-Based Registry

- [+ setValueTransformer:forName:](<setvaluetransformer(__forname_).md>) — Registers the provided value transformer with a given identifier.
- [+ valueTransformerForName:](<init(forname_).md>) — Returns the value transformer identified by a given identifier.
- [NSValueTransformerName](../nsvaluetransformername.md) — Named value transformers defined by `NSValueTransformer`.
