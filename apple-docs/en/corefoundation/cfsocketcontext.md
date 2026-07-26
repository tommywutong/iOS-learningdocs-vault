---
title: CFSocketContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocketcontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcontext.json'
content_hash: 'sha256:3abc1bf34855b70b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketContext

<sub>Structure</sub>

A structure that contains program-defined data and callbacks with which you can configure a CFSocket object’s behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFSocketContext
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfsocketcontext/init().md>)
- [init(version:info:retain:release:copyDescription:)](<cfsocketcontext/init(version_info_retain_release_copydescription_).md>)

### Instance Properties

- [copyDescription](cfsocketcontext/copydescription.md) — A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [info](cfsocketcontext/info.md) — An arbitrary pointer to program-defined data, which can be associated with the CFSocket object at creation time. This pointer is passed to all the callbacks defined in the context.
- [release](cfsocketcontext/release.md) — A release callback for your program-defined `info` pointer. Can be `NULL`.
- [retain](cfsocketcontext/retain.md) — A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [version](cfsocketcontext/version.md) — Version number of the structure. Must be `0`.

## See Also

### Data Types

- [CFSocketNativeHandle](cfsocketnativehandle.md) — Type for the platform-specific native socket handle.
- [CFSocketSignature](cfsocketsignature.md) — A structure that fully specifies the communication protocol and connection address of a CFSocket object.
