---
title: CFRunLoopSourceContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopsourcecontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsourcecontext.json'
content_hash: 'sha256:3ddd09fcca968b52'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopSourceContext

<sub>Structure</sub>

A structure that contains program-defined data and callbacks with which you can configure a version 0 CFRunLoopSource’s behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFRunLoopSourceContext
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfrunloopsourcecontext/init().md>)
- [init(version:info:retain:release:copyDescription:equal:hash:schedule:cancel:perform:)](<cfrunloopsourcecontext/init(version_info_retain_release_copydescription_equal_hash_schedule_cancel_perform_).md>)

### Instance Properties

- [cancel](cfrunloopsourcecontext/cancel.md)
- [copyDescription](cfrunloopsourcecontext/copydescription.md) — A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [equal](cfrunloopsourcecontext/equal.md) — An equality test callback for your program-defined `info` pointer. Can be `NULL`.
- [hash](cfrunloopsourcecontext/hash.md) — A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.
- [info](cfrunloopsourcecontext/info.md) — An arbitrary pointer to program-defined data, which can be associated with the CFRunLoopSource at creation time. This pointer is passed to all the callbacks defined in the context.
- [perform](cfrunloopsourcecontext/perform.md) — A perform callback for the run loop source. This callback is called when the source has fired.
- [release](cfrunloopsourcecontext/release.md) — A release callback for your program-defined `info` pointer. Can be `NULL`.
- [retain](cfrunloopsourcecontext/retain.md) — A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [schedule](cfrunloopsourcecontext/schedule.md) — A scheduling callback for the run loop source. This callback is called when the source is added to a run loop mode. Can be `NULL`.
- [version](cfrunloopsourcecontext/version.md) — Version number of the structure. Must be 0.

## See Also

### Data Types

- [CFRunLoopSourceContext1](cfrunloopsourcecontext1.md) — A structure that contains program-defined data and callbacks with which you can configure a version 1 CFRunLoopSource’s behavior.
