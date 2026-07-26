---
title: allowsReverseTransformation()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/valuetransformer/allowsreversetransformation()
source_url: 'https://developer.apple.com/documentation/foundation/valuetransformer/allowsreversetransformation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/valuetransformer/allowsreversetransformation%28%29.json'
content_hash: 'sha256:ba79d02e2e992637'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ValueTransformer](../valuetransformer.md)

# allowsReverseTransformation()

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the receiver can reverse a transformation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func allowsReverseTransformation() -> Bool
```

## Return Value

[true](../../swift/true.md) if the receiver supports reverse value transformations, otherwise [false](../../swift/false.md).

The default is [true](../../swift/true.md).

## Discussion

Subclasses should override this method to return [false](../../swift/false.md) if they do not support reverse value transformations.

## See Also

### Getting Information About a Transformer

- [+ transformedValueClass](<transformedvalueclass().md>) — Returns the class of the value returned by the receiver for a forward transformation.
