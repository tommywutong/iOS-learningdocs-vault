---
title: 'getArgumentTypeAtIndex:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmethodsignature/getargumenttypeatindex:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmethodsignature/getargumenttypeatindex:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmethodsignature/getargumenttypeatindex%3A.json'
content_hash: 'sha256:5590e1594964c841'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMethodSignature](../nsmethodsignature.md)

# getArgumentTypeAtIndex:

<sub>Instance Method</sub>

Returns the type encoding for the argument at a given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (const char *) getArgumentTypeAtIndex:(NSUInteger) idx;
```

## Parameters

- `idx` — The index of the argument to get.

## Return Value

The type encoding for the argument at `idx`.

## Discussion

Indexes begin with 0. The implicit arguments `self` (of type `id`) and `_cmd` (of type `SEL`) are at indexes 0 and 1; explicit arguments begin at index 2.

> [!important] Important
> If `index` exceeds the number of arguments, `NSInvalidArgumentException` is raised.

## See Also

### Getting Information on Argument Types

- [numberOfArguments](numberofarguments.md) — The number of arguments recorded in the receiver.
- [frameLength](framelength.md) — The number of bytes that the arguments, taken together, occupy on the stack.
