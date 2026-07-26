---
title: 'initWithTarget:selector:object:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsinvocationoperation/initwithtarget:selector:object:'
source_url: 'https://developer.apple.com/documentation/foundation/nsinvocationoperation/initwithtarget:selector:object:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinvocationoperation/initwithtarget%3Aselector%3Aobject%3A.json'
content_hash: 'sha256:6346430363a27770'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSInvocationOperation](../nsinvocationoperation.md)

# initWithTarget:selector:object:

<sub>Instance Method</sub>

Returns an `NSInvocationOperation` object initialized with the specified target and selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithTarget:(id) target selector:(SEL) sel object:(id) arg;
```

## Parameters

- `target` — The object defining the specified selector.

- `sel` — The selector to invoke when running the operation. The selector may take 0 or 1 parameters; if it accepts a parameter, the type of that parameter must be `id`. The return type of the method may be `void`, a scalar value, or an object that can be returned as an `id` type.

- `arg` — The parameter object to pass to the selector. If the selector does not take an argument, specify `nil`.

## Return Value

An initialized `NSInvocationOperation` object or `nil` if the target object does not implement the specified selector.

## Discussion

If you specify a selector with a non-void return type, you can get the return value by calling the [result](result.md) method after the operation finishes executing. The receiver tells the invocation object to retain its arguments.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)

### Initialization

- [initWithInvocation:](initwithinvocation_.md) — Returns an `NSInvocationOperation` object initialized with the specified invocation object.
