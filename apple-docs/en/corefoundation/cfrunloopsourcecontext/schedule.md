---
title: schedule
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopsourcecontext/schedule
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/schedule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourcecontext/schedule.json'
content_hash: 'sha256:44befa1ac34d1181'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopSourceContext](../cfrunloopsourcecontext.md)

# schedule

<sub>Instance Property</sub>

A scheduling callback for the run loop source. This callback is called when the source is added to a run loop mode. Can be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!
```

## Parameters

- `info` — The `info` member of the [CFRunLoopSourceContext](../cfrunloopsourcecontext.md) structure that was used when creating the run loop source.

- `rl` — The run loop in which the source is being scheduled.

- `mode` — The run loop mode in which the source is being scheduled.

## See Also

### Callbacks

- [cancel](cancel.md)
- [equal](equal.md) — An equality test callback for your program-defined `info` pointer. Can be `NULL`.
- [hash](hash.md) — A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.
- [perform](perform.md) — A perform callback for the run loop source. This callback is called when the source has fired.
