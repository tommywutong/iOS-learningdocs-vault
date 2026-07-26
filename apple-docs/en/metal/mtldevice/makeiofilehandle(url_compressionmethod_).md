---
title: 'makeIOFileHandle(url:compressionMethod:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeiofilehandle(url:compressionmethod:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeiofilehandle(url:compressionmethod:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeiofilehandle%28url%3Acompressionmethod%3A%29.json'
content_hash: 'sha256:fb9316d621852329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeIOFileHandle(url:compressionMethod:)

<sub>Instance Method</sub>

Creates an input/output file handle instance that represents a compressed file at a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIOFileHandle(url: URL, compressionMethod: MTLIOCompressionMethod) throws -> any MTLIOFileHandle
```

## Parameters

- `url` — A location URL to a compressed file in the file system.

- `compressionMethod` — The file’s compression format.

## Return Value

A new [MTLIOFileHandle](../mtliofilehandle.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

For information about using input/output command queues and file handles, see [Resource loading](../resource-loading.md).

## See Also

### Creating I/O file handles

- [- newIOFileHandleWithURL:error:](<makeiofilehandle(url_).md>) — Creates an input/output file handle instance that represents a file at a URL.
- [- newIOHandleWithURL:error:](<makeiohandle(url_).md>) — Creates an input/output file handle instance that represents a file at a URL. _(deprecated)_
- [- newIOHandleWithURL:compressionMethod:error:](<makeiohandle(url_compressionmethod_).md>) — Creates an input/output file handle instance that represents a compressed file at a URL. _(deprecated)_
