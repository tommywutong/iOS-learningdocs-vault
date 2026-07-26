---
title: 'CFFileDescriptorGetNativeDescriptor(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cffiledescriptorgetnativedescriptor(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptorgetnativedescriptor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptorgetnativedescriptor%28_%3A%29.json'
content_hash: 'sha256:4bce7bcc53b48ceb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileDescriptorGetNativeDescriptor(_:)

<sub>Function</sub>

Returns the native file descriptor for a given CFFileDescriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFFileDescriptorGetNativeDescriptor(_ f: CFFileDescriptor!) -> CFFileDescriptorNativeDescriptor
```

## Parameters

- `f` — A CFFileDescriptor.

## Return Value

The native file descriptor for `f`.

## See Also

### Related Documentation

- [CFFileDescriptorInvalidate](<cffiledescriptorinvalidate(__).md>) — Invalidates a CFFileDescriptor object.

### Getting Information About a File Descriptor

- [CFFileDescriptorIsValid](<cffiledescriptorisvalid(__).md>) — Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.
- [CFFileDescriptorGetContext](<cffiledescriptorgetcontext(____).md>) — Gets the context for a given CFFileDescriptor.
