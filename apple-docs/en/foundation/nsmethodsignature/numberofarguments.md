---
title: numberOfArguments
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmethodsignature/numberofarguments
source_url: 'https://developer.apple.com/documentation/foundation/nsmethodsignature/numberofarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmethodsignature/numberofarguments.json'
content_hash: 'sha256:8118d1584cce9add'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMethodSignature](../nsmethodsignature.md)

# numberOfArguments

<sub>Instance Property</sub>

The number of arguments recorded in the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSUInteger numberOfArguments;
```

## Discussion

There are always at least two arguments, because an `NSMethodSignature` object includes the implicit arguments `self` and `_cmd`, which are the first two arguments passed to every method implementation.

## See Also

### Getting Information on Argument Types

- [getArgumentTypeAtIndex:](getargumenttypeatindex_.md) — Returns the type encoding for the argument at a given index.
- [frameLength](framelength.md) — The number of bytes that the arguments, taken together, occupy on the stack.
