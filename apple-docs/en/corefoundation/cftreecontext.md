---
title: CFTreeContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftreecontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreecontext.json'
content_hash: 'sha256:e7b051db5ec4215e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeContext

<sub>Structure</sub>

Structure containing program-defined data and callbacks for a CFTree object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFTreeContext
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cftreecontext/init().md>)
- [init(version:info:retain:release:copyDescription:)](<cftreecontext/init(version_info_retain_release_copydescription_).md>)

### Instance Properties

- [copyDescription](cftreecontext/copydescription.md) — The callback used to provide a description of the `info` field.
- [info](cftreecontext/info.md) — A C pointer to a program-defined block of data, referred to as the information pointer.
- [release](cftreecontext/release.md) — The callback used to release a previously retained `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. This value may be `NULL`.
- [retain](cftreecontext/retain.md) — The callback used to retain the `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. This value may be `NULL`.
- [version](cftreecontext/version.md) — The version number of the structure type being passed in as a parameter to a CFTree creation function. This structure is version `0`.
