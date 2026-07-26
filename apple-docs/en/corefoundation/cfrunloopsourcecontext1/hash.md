---
title: hash
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopsourcecontext1/hash
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/hash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourcecontext1/hash.json'
content_hash: 'sha256:db0916c6e811f09b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopSourceContext1](../cfrunloopsourcecontext1.md)

# hash

<sub>Instance Property</sub>

A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hash: ((UnsafeRawPointer?) -> CFHashCode)!
```

## Parameters

- `info` — The `info` member of the [CFRunLoopSourceContext](../cfrunloopsourcecontext.md) or [CFRunLoopSourceContext1](../cfrunloopsourcecontext1.md) structure that was used when creating the run loop source.

## Return Value

A hash code value for `info`.

## Discussion

If a hash callback is not provided for a source, the `info` pointer is used.
