---
title: 'signatureWithObjCTypes:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmethodsignature/signaturewithobjctypes:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmethodsignature/signaturewithobjctypes:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmethodsignature/signaturewithobjctypes%3A.json'
content_hash: 'sha256:1021acbd2beb2982'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMethodSignature](../nsmethodsignature.md)

# signatureWithObjCTypes:

<sub>Type Method</sub>

Returns an `NSMethodSignature` object for the given Objective-C method type string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSMethodSignature *) signatureWithObjCTypes:(const char *) types;
```

## Parameters

- `types` — An array of characters containing the type encodings for the method arguments.

## Return Value

An `NSMethodSignature` object for the given Objective-C method type string in `types`.
