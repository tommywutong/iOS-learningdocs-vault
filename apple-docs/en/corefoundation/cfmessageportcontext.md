---
title: CFMessagePortContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmessageportcontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportcontext.json'
content_hash: 'sha256:847ed75b88a0f6ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortContext

<sub>Structure</sub>

A structure that contains program-defined data and callbacks with which you can configure a CFMessagePort object’s behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFMessagePortContext
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfmessageportcontext/init().md>)
- [init(version:info:retain:release:copyDescription:)](<cfmessageportcontext/init(version_info_retain_release_copydescription_).md>)

### Instance Properties

- [copyDescription](cfmessageportcontext/copydescription.md) — A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [info](cfmessageportcontext/info.md) — An arbitrary pointer to program-defined data, which can be associated with the message port at creation time. This pointer is passed to all the callbacks defined in the context.
- [release](cfmessageportcontext/release.md) — A release callback for your program-defined `info` pointer. Can be `NULL`.
- [retain](cfmessageportcontext/retain.md) — A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [version](cfmessageportcontext/version.md) — Version number of the structure. Must be `0`.
