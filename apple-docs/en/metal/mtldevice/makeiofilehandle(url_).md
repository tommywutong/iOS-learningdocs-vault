---
title: 'makeIOFileHandle(url:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeiofilehandle(url:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeiofilehandle(url:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeiofilehandle%28url%3A%29.json'
content_hash: 'sha256:5437cee55e59b5d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeIOFileHandle(url:)

<sub>Instance Method</sub>

Creates an input/output file handle instance that represents a file at a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIOFileHandle(url: URL) throws -> any MTLIOFileHandle
```

## Parameters

- `url` — The URL to a resource file in the file system.

## Return Value

A new [MTLIOFileHandle](../mtliofilehandle.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

For information about using input/output command queues and file handles, see [Resource loading](../resource-loading.md).

## See Also

### Creating I/O file handles

- [- newIOFileHandleWithURL:compressionMethod:error:](<makeiofilehandle(url_compressionmethod_).md>) — Creates an input/output file handle instance that represents a compressed file at a URL.
- [- newIOHandleWithURL:error:](<makeiohandle(url_).md>) — Creates an input/output file handle instance that represents a file at a URL. _(deprecated)_
- [- newIOHandleWithURL:compressionMethod:error:](<makeiohandle(url_compressionmethod_).md>) — Creates an input/output file handle instance that represents a compressed file at a URL. _(deprecated)_
