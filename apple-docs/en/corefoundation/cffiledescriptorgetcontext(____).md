---
title: 'CFFileDescriptorGetContext(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cffiledescriptorgetcontext(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptorgetcontext(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptorgetcontext%28_%3A_%3A%29.json'
content_hash: 'sha256:16467dcb360ccf50'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileDescriptorGetContext(_:_:)

<sub>Function</sub>

Gets the context for a given CFFileDescriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFFileDescriptorGetContext(_ f: CFFileDescriptor!, _ context: UnsafeMutablePointer<CFFileDescriptorContext>!)
```

## Parameters

- `f` — A CFFileDescriptor.

- `context` — Upon return, contains the context passed to `f` in [CFFileDescriptorCreate](<cffiledescriptorcreate(__________).md>).

## See Also

### Related Documentation

- [CFFileDescriptorCreate](<cffiledescriptorcreate(__________).md>) — Creates a new CFFileDescriptor.

### Getting Information About a File Descriptor

- [CFFileDescriptorGetNativeDescriptor](<cffiledescriptorgetnativedescriptor(__).md>) — Returns the native file descriptor for a given CFFileDescriptor.
- [CFFileDescriptorIsValid](<cffiledescriptorisvalid(__).md>) — Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.
