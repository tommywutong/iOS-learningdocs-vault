---
title: transformedValueClass()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/valuetransformer/transformedvalueclass()
source_url: 'https://developer.apple.com/documentation/foundation/valuetransformer/transformedvalueclass()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/valuetransformer/transformedvalueclass%28%29.json'
content_hash: 'sha256:67611c87ac5f42ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ValueTransformer](../valuetransformer.md)

# transformedValueClass()

<sub>Type Method</sub>

Returns the class of the value returned by the receiver for a forward transformation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func transformedValueClass() -> AnyClass
```

## Return Value

The class of the value returned by the receiver for a forward transformation.

## Discussion

A subclass should override this method to return the appropriate class.

## See Also

### Getting Information About a Transformer

- [+ allowsReverseTransformation](<allowsreversetransformation().md>) — Returns a Boolean value that indicates whether the receiver can reverse a transformation.
