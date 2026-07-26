---
title: frameLength
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmethodsignature/framelength
source_url: 'https://developer.apple.com/documentation/foundation/nsmethodsignature/framelength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmethodsignature/framelength.json'
content_hash: 'sha256:1e3bc4c6245ed8b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMethodSignature](../nsmethodsignature.md)

# frameLength

<sub>Instance Property</sub>

The number of bytes that the arguments, taken together, occupy on the stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSUInteger frameLength;
```

## Discussion

This number varies with the hardware architecture the application runs on.

## See Also

### Getting Information on Argument Types

- [getArgumentTypeAtIndex:](getargumenttypeatindex_.md) — Returns the type encoding for the argument at a given index.
- [numberOfArguments](numberofarguments.md) — The number of arguments recorded in the receiver.
