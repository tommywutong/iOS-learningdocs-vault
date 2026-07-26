---
title: 'makeIOHandle(url:compressionMethod:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（17.0 起废弃）, iPadOS 16.0+（17.0 起废弃）, Mac Catalyst 16.0+（17.0 起废弃）, macOS 13.0+（14.0 起废弃）, tvOS 16.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtldevice/makeiohandle(url:compressionmethod:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeiohandle(url:compressionmethod:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeiohandle%28url%3Acompressionmethod%3A%29.json'
content_hash: 'sha256:b4eef71810038fd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeIOHandle(url:compressionMethod:)

<sub>Instance Method</sub>

Creates an input/output file handle instance that represents a compressed file at a URL.

> [!warning] Deprecated
> Use [- newIOFileHandleWithURL:compressionMethod:error:](<makeiofilehandle(url_compressionmethod_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIOHandle(url: URL, compressionMethod: MTLIOCompressionMethod) throws -> any MTLIOFileHandle
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
- [- newIOFileHandleWithURL:compressionMethod:error:](<makeiofilehandle(url_compressionmethod_).md>) — Creates an input/output file handle instance that represents a compressed file at a URL.
- [- newIOHandleWithURL:error:](<makeiohandle(url_).md>) — Creates an input/output file handle instance that represents a file at a URL. _(deprecated)_
