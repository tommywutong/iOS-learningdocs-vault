---
title: CFRunLoopTimerContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunlooptimercontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooptimercontext.json'
content_hash: 'sha256:c97483371e6cd37c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopTimerContext

<sub>Structure</sub>

A structure that contains program-defined data and callbacks with which you can configure a CFRunLoopTimer’s behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFRunLoopTimerContext
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfrunlooptimercontext/init().md>)
- [init(version:info:retain:release:copyDescription:)](<cfrunlooptimercontext/init(version_info_retain_release_copydescription_).md>)

### Instance Properties

- [copyDescription](cfrunlooptimercontext/copydescription.md) — A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [info](cfrunlooptimercontext/info.md) — An arbitrary pointer to program-defined data, which can be associated with the run loop timer at creation time. This pointer is passed to all the callbacks defined in the context.
- [release](cfrunlooptimercontext/release.md) — A release callback for your program-defined `info` pointer. Can be `NULL`.
- [retain](cfrunlooptimercontext/retain.md) — A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [version](cfrunlooptimercontext/version.md) — Version number of the structure. Must be 0.
