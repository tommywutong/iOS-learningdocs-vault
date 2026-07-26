---
title: invoke
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsinvocation/invoke
source_url: 'https://developer.apple.com/documentation/foundation/nsinvocation/invoke'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinvocation/invoke.json'
content_hash: 'sha256:aee39b032a0ad21f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSInvocation](../nsinvocation.md)

# invoke

<sub>Instance Method</sub>

Sends the receiver’s message (with arguments) to its target and sets the return value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) invoke;
```

## Discussion

You must set the receiver’s target, selector, and argument values before calling this method.

## See Also

### Related Documentation

- [selector](selector.md) — The receiver’s selector, or 0 if it hasn’t been set.
- [setArgument:atIndex:](setargument_atindex_.md) — Sets an argument of the receiver.
- [getReturnValue:](getreturnvalue_.md) — Gets the invocation’s return value.

### Dispatching an Invocation

- [invokeWithTarget:](invokewithtarget_.md) — Sets the receiver’s target, sends the receiver’s message (with arguments) to that target, and sets the return value.
