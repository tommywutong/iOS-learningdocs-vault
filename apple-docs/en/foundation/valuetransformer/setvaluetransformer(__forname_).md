---
title: 'setValueTransformer(_:forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/valuetransformer/setvaluetransformer(_:forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/valuetransformer/setvaluetransformer(_:forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/valuetransformer/setvaluetransformer%28_%3Aforname%3A%29.json'
content_hash: 'sha256:0975bfc930eb62ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ValueTransformer](../valuetransformer.md)

# setValueTransformer(_:forName:)

<sub>Type Method</sub>

Registers the provided value transformer with a given identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setValueTransformer(_ transformer: ValueTransformer?, forName name: NSValueTransformerName)
```

## Parameters

- `transformer` — The transformer to register.

- `name` — The name for `transformer`.

## See Also

### Related Documentation

- [Value Transformer Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ValueTransformers/ValueTransformers.html#//apple_ref/doc/uid/10000175i)

### Using the Name-Based Registry

- [+ valueTransformerForName:](<init(forname_).md>) — Returns the value transformer identified by a given identifier.
- [+ valueTransformerNames](<valuetransformernames().md>) — Returns an array of all the registered value transformers.
- [NSValueTransformerName](../nsvaluetransformername.md) — Named value transformers defined by `NSValueTransformer`.
