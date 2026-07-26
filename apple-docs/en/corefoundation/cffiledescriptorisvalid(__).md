---
title: 'CFFileDescriptorIsValid(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cffiledescriptorisvalid(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptorisvalid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptorisvalid%28_%3A%29.json'
content_hash: 'sha256:36c80d50140b6ba1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileDescriptorIsValid(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFFileDescriptorIsValid(_ f: CFFileDescriptor!) -> Bool
```

## Parameters

- `f` — A CFFileDescriptor.

## Return Value

`true` if the native file descriptor for `f` is valid, otherwise `false`.

## See Also

### Related Documentation

- [CFFileDescriptorInvalidate](<cffiledescriptorinvalidate(__).md>) — Invalidates a CFFileDescriptor object.

### Getting Information About a File Descriptor

- [CFFileDescriptorGetNativeDescriptor](<cffiledescriptorgetnativedescriptor(__).md>) — Returns the native file descriptor for a given CFFileDescriptor.
- [CFFileDescriptorGetContext](<cffiledescriptorgetcontext(____).md>) — Gets the context for a given CFFileDescriptor.
