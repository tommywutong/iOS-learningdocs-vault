---
title: equal
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopsourcecontext1/equal
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/equal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourcecontext1/equal.json'
content_hash: 'sha256:d8d1fa71cd7cecdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopSourceContext1](../cfrunloopsourcecontext1.md)

# equal

<sub>Instance Property</sub>

An equality test callback for your program-defined `info` pointer. Can be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!
```

## Parameters

- `info1` — The `info` member of the [CFRunLoopSourceContext](../cfrunloopsourcecontext.md) or [CFRunLoopSourceContext1](../cfrunloopsourcecontext1.md) structure that was used when creating the first run loop source to test.

- `info2` — The `info` member of the [CFRunLoopSourceContext](../cfrunloopsourcecontext.md) or [CFRunLoopSourceContext1](../cfrunloopsourcecontext1.md) structure that was used when creating the second run loop source to test.

## Return Value

`true` if `info1` and `info2` should be considered equal; otherwise `false`.

## Discussion

An equality test callback for your program-defined `info` pointer. Can be `NULL`.
