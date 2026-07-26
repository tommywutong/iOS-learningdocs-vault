---
title: CFFileDescriptorCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cffiledescriptorcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptorcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptorcallback.json'
content_hash: 'sha256:da27ce1161cf9ca2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileDescriptorCallBack

<sub>Type Alias</sub>

Defines a structure for a callback for a CFFileDescriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFFileDescriptorCallBack = (CFFileDescriptor?, CFOptionFlags, UnsafeMutableRawPointer?) -> Void
```

## See Also

### Data Types

- [CFFileDescriptorNativeDescriptor](cffiledescriptornativedescriptor.md) — Defines a type for the native file descriptor.
- [CFFileDescriptorContext](cffiledescriptorcontext.md) — Defines a structure for the context of a CFFileDescriptor.
