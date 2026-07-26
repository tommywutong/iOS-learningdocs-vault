---
title: invocation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsinvocationoperation/invocation
source_url: 'https://developer.apple.com/documentation/foundation/nsinvocationoperation/invocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinvocationoperation/invocation.json'
content_hash: 'sha256:8a74c2d874ec5e5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSInvocationOperation](../nsinvocationoperation.md)

# invocation

<sub>Instance Property</sub>

The receiver’s invocation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (retain, readonly) NSInvocation * invocation;
```

## Discussion

The invocation object identifying the target object, selector, and parameters to use to execute the operation’s task.

## See Also

### Related Documentation

- [initWithTarget:selector:object:](initwithtarget_selector_object_.md) — Returns an `NSInvocationOperation` object initialized with the specified target and selector.
- [initWithInvocation:](initwithinvocation_.md) — Returns an `NSInvocationOperation` object initialized with the specified invocation object.

### Getting Attributes

- [result](result.md) — The result of the invocation or method.
