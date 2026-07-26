---
title: 'initWithInvocation:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsinvocationoperation/initwithinvocation:'
source_url: 'https://developer.apple.com/documentation/foundation/nsinvocationoperation/initwithinvocation:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinvocationoperation/initwithinvocation%3A.json'
content_hash: 'sha256:eff688d6889042f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSInvocationOperation](../nsinvocationoperation.md)

# initWithInvocation:

<sub>Instance Method</sub>

Returns an `NSInvocationOperation` object initialized with the specified invocation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithInvocation:(NSInvocation *) inv;
```

## Parameters

- `inv` — The invocation object identifying the target object, selector, and parameter objects.

## Return Value

An initialized `NSInvocationOperation` object or `nil` if the object could not be initialized.

## Discussion

This method is the designated initializer. The receiver tells the invocation object to retain its arguments.

## See Also

### Initialization

- [initWithTarget:selector:object:](initwithtarget_selector_object_.md) — Returns an `NSInvocationOperation` object initialized with the specified target and selector.
