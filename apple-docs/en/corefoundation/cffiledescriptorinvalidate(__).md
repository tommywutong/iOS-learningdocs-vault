---
title: 'CFFileDescriptorInvalidate(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cffiledescriptorinvalidate(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptorinvalidate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptorinvalidate%28_%3A%29.json'
content_hash: 'sha256:ddbdbede2da422d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileDescriptorInvalidate(_:)

<sub>Function</sub>

Invalidates a CFFileDescriptor object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFFileDescriptorInvalidate(_ f: CFFileDescriptor!)
```

## Parameters

- `f` — A CFFileDescriptor.

## Discussion

Once invalidated, the CFFileDescriptor object will no longer be read from or written to at the Core Fundation level.

If you passed `true` for the `closeOnInvalidate` parameter when you called [CFFileDescriptorCreate](<cffiledescriptorcreate(__________).md>), this function also closes the underlying file descriptor. If you passed `false`, you must close the descriptor yourself _after_ invalidating the CFFileDescriptor object.

> [!important] Important
> You must invalidate the CFFileDescriptor before closing the underlying file descriptor.

## See Also

### Related Documentation

- [CFFileDescriptorGetNativeDescriptor](<cffiledescriptorgetnativedescriptor(__).md>) — Returns the native file descriptor for a given CFFileDescriptor.
- [CFFileDescriptorIsValid](<cffiledescriptorisvalid(__).md>) — Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.
