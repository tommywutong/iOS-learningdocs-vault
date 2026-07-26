---
title: CFRunLoopObserverContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopobservercontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopobservercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopobservercontext.json'
content_hash: 'sha256:5726efad7592d5fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopObserverContext

<sub>Structure</sub>

A structure that contains program-defined data and callbacks with which you can configure a CFRunLoopObserver object’s behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFRunLoopObserverContext
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfrunloopobservercontext/init().md>)
- [init(version:info:retain:release:copyDescription:)](<cfrunloopobservercontext/init(version_info_retain_release_copydescription_).md>)

### Instance Properties

- [copyDescription](cfrunloopobservercontext/copydescription.md) — A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [info](cfrunloopobservercontext/info.md) — An arbitrary pointer to program-defined data, which can be associated with the run loop observer at creation time. This pointer is passed to all the callbacks defined in the context.
- [release](cfrunloopobservercontext/release.md) — A release callback for your program-defined `info` pointer. Can be `NULL`.
- [retain](cfrunloopobservercontext/retain.md) — A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [version](cfrunloopobservercontext/version.md) — Version number of the structure. Must be `0`.
