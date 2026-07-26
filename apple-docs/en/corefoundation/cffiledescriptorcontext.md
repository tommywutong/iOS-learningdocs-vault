---
title: CFFileDescriptorContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cffiledescriptorcontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptorcontext.json'
content_hash: 'sha256:e41e9c7bc0cab6ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileDescriptorContext

<sub>Structure</sub>

Defines a structure for the context of a CFFileDescriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFFileDescriptorContext
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cffiledescriptorcontext/init().md>)
- [init(version:info:retain:release:copyDescription:)](<cffiledescriptorcontext/init(version_info_retain_release_copydescription_).md>)

### Instance Properties

- [copyDescription](cffiledescriptorcontext/copydescription.md) — The callback used to create a descriptive string representation of the CFFileDescriptor.
- [info](cffiledescriptorcontext/info.md)
- [release](cffiledescriptorcontext/release.md) — The release callback used by the CFFileDescriptor.
- [retain](cffiledescriptorcontext/retain.md) — The retain callback used by the CFFileDescriptor.
- [version](cffiledescriptorcontext/version.md) — The version number of this structure. If not one of the defined version numbers for this opaque type, the behavior is undefined. The current version of this structure is 0.

## See Also

### Data Types

- [CFFileDescriptorNativeDescriptor](cffiledescriptornativedescriptor.md) — Defines a type for the native file descriptor.
- [CFFileDescriptorCallBack](cffiledescriptorcallback.md) — Defines a structure for a callback for a CFFileDescriptor.
