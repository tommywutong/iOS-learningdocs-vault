---
title: 'makeIOHandle(url:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（17.0 起废弃）, iPadOS 16.0+（17.0 起废弃）, Mac Catalyst 16.0+（17.0 起废弃）, macOS 13.0+（14.0 起废弃）, tvOS 16.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtldevice/makeiohandle(url:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeiohandle(url:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeiohandle%28url%3A%29.json'
content_hash: 'sha256:d686e77b1a6a1341'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeIOHandle(url:)

<sub>Instance Method</sub>

Creates an input/output file handle instance that represents a file at a URL.

> [!warning] Deprecated
> Use [- newIOFileHandleWithURL:error:](<makeiofilehandle(url_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIOHandle(url: URL) throws -> any MTLIOFileHandle
```

## Parameters

- `url` — The URL to a resource file in the file system.

## Return Value

A new [MTLIOFileHandle](../mtliofilehandle.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

For information about using input/output command queues and file handles, see [Resource loading](../resource-loading.md).

## See Also

### Creating I/O file handles

- [- newIOFileHandleWithURL:error:](<makeiofilehandle(url_).md>) — Creates an input/output file handle instance that represents a file at a URL.
- [- newIOFileHandleWithURL:compressionMethod:error:](<makeiofilehandle(url_compressionmethod_).md>) — Creates an input/output file handle instance that represents a compressed file at a URL.
- [- newIOHandleWithURL:compressionMethod:error:](<makeiohandle(url_compressionmethod_).md>) — Creates an input/output file handle instance that represents a compressed file at a URL. _(deprecated)_
