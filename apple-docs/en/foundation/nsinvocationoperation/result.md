---
title: result
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsinvocationoperation/result
source_url: 'https://developer.apple.com/documentation/foundation/nsinvocationoperation/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinvocationoperation/result.json'
content_hash: 'sha256:68e4864bce67794a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSInvocationOperation](../nsinvocationoperation.md)

# result

<sub>Instance Property</sub>

The result of the invocation or method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (retain, readonly, nullable) id result;
```

## Discussion

The object returned by the method or an [NSValue](../nsvalue.md) object containing the return value if it is not an object. `nil` if the method or invocation is not finished executing.

If an exception was raised during the execution of the method or invocation, accessing this property raises that exception again. If the operation was cancelled or the invocation or method has a `void` return type, accessing this property raises an exception; see [Result Exceptions](../result-exceptions.md).

## See Also

### Getting Attributes

- [invocation](invocation.md) — The receiver’s invocation object.
