---
title: CFStreamClientContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreamclientcontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamclientcontext.json'
content_hash: 'sha256:264db34d7a19b6b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStreamClientContext

<sub>Structure</sub>

A structure that contains program-defined data and callbacks with which you can configure a stream’s client behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFStreamClientContext
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfstreamclientcontext/init().md>)
- [init(version:info:retain:release:copyDescription:)](<cfstreamclientcontext/init(version_info_retain_release_copydescription_).md>)

### Instance Properties

- [copyDescription](cfstreamclientcontext/copydescription.md) — A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [info](cfstreamclientcontext/info.md) — An arbitrary pointer to program-defined data, which can be associated with the client. This pointer is passed to the callbacks defined in the context and to the client callback function [CFReadStreamClientCallBack](cfreadstreamclientcallback.md).
- [release](cfstreamclientcontext/release.md) — A release callback for your program-defined `info` pointer. Can be `NULL`.
- [retain](cfstreamclientcontext/retain.md) — A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [version](cfstreamclientcontext/version.md) — Version number of the structure. Must be `0`.
