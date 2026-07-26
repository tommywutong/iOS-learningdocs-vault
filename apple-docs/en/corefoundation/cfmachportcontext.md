---
title: CFMachPortContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmachportcontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportcontext.json'
content_hash: 'sha256:685d2fff4adc9a04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortContext

<sub>Structure</sub>

A structure that contains program-defined data and callbacks with which you can configure a CFMachPort object’s behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFMachPortContext
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfmachportcontext/init().md>)
- [init(version:info:retain:release:copyDescription:)](<cfmachportcontext/init(version_info_retain_release_copydescription_).md>)

### Instance Properties

- [copyDescription](cfmachportcontext/copydescription.md) — A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [info](cfmachportcontext/info.md) — An arbitrary pointer to program-defined data, which can be associated with the CFMachPort object at creation time. This pointer is passed to all the callbacks defined in the context.
- [release](cfmachportcontext/release.md) — A release callback for your program-defined `info` pointer. Can be `NULL`.
- [retain](cfmachportcontext/retain.md) — A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [version](cfmachportcontext/version.md) — Version number of the structure. Must be `0`.
