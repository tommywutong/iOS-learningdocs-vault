---
title: 'serialize(to:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldynamiclibrary/serialize(to:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldynamiclibrary/serialize(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldynamiclibrary/serialize%28to%3A%29.json'
content_hash: 'sha256:d810ca0129b714d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDynamicLibrary](../mtldynamiclibrary.md)

# serialize(to:)

<sub>Instance Method</sub>

Writes the contents of the dynamic library to a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func serialize(to url: URL) throws
```

## Parameters

- `url` — The URL for the destination file.

## Discussion

When the methods succeeds, the file contains a representation of the [MTLLibrary](../mtllibrary.md) from the [MTLDynamicLibrary](../mtldynamiclibrary.md) that creates it, as well as the binaries it has for the device your app is running on.

Such files may be combined with offline tools to contain the compiled code for multiple devices.

If this MTLDynamicLibrary was created from a file that contained compiled code for multiple devices, the compiled code for all other devices is not written (since only compiled code for the current device was loaded).
