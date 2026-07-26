---
title: 'CFFileDescriptorDisableCallBacks(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cffiledescriptordisablecallbacks(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptordisablecallbacks(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptordisablecallbacks%28_%3A_%3A%29.json'
content_hash: 'sha256:af7a8e69f9ad9650'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileDescriptorDisableCallBacks(_:_:)

<sub>Function</sub>

Disables callbacks for a given CFFileDescriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFFileDescriptorDisableCallBacks(_ f: CFFileDescriptor!, _ callBackTypes: CFOptionFlags)
```

## Parameters

- `f` — A CFFileDescriptor.

- `callBackTypes` — A bitmask that specifies which callbacks to disable (see [Callback Identifiers](1477595-callback-identifiers.md) for possible components).

## See Also

### Managing Callbacks

- [CFFileDescriptorEnableCallBacks](<cffiledescriptorenablecallbacks(____).md>) — Enables callbacks for a given CFFileDescriptor.
