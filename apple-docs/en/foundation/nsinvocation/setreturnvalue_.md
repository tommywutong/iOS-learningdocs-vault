---
title: 'setReturnValue:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsinvocation/setreturnvalue:'
source_url: 'https://developer.apple.com/documentation/foundation/nsinvocation/setreturnvalue:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinvocation/setreturnvalue%3A.json'
content_hash: 'sha256:23be46eb34503092'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSInvocation](../nsinvocation.md)

# setReturnValue:

<sub>Instance Method</sub>

Sets the receiver’s return value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) setReturnValue:(void *) retLoc;
```

## Parameters

- `retLoc` — An untyped buffer whose contents are copied as the receiver’s return value.

## Discussion

This value is normally set when you send an [invoke](invoke.md) or [invokeWithTarget:](invokewithtarget_.md) message.

## See Also

### Related Documentation

- [methodReturnLength](../nsmethodsignature/methodreturnlength.md) — The number of bytes required for the return value.
- [methodReturnType](../nsmethodsignature/methodreturntype.md) — A C string encoding the return type of the method in Objective-C type encoding.

### Configuring an Invocation Object

- [selector](selector.md) — The receiver’s selector, or 0 if it hasn’t been set.
- [target](target.md) — The receiver’s target, or `nil` if the receiver has no target.
- [setArgument:atIndex:](setargument_atindex_.md) — Sets an argument of the receiver.
- [getArgument:atIndex:](getargument_atindex_.md) — Returns by indirection the receiver’s argument at a specified index.
- [argumentsRetained](argumentsretained.md) — A Boolean value that indicates if the receiver has retained its arguments.
- [retainArguments](retainarguments.md) — If the receiver hasn’t already done so, retains the target and all object arguments of the receiver and copies all of its C-string arguments and blocks. If a returnvalue has been set, this is also retained or copied.
- [getReturnValue:](getreturnvalue_.md) — Gets the invocation’s return value.
