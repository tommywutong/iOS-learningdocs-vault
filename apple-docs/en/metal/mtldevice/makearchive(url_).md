---
title: 'makeArchive(url:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makearchive(url:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makearchive(url:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makearchive%28url%3A%29.json'
content_hash: 'sha256:cb32a0949b813d39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeArchive(url:)

<sub>Instance Method</sub>

Creates a new archive from data available at an `NSURL` address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeArchive(url: URL) throws -> any MTL4Archive
```

## Parameters

- `url` — An `NSURL` instance that represents the path from which the device loads the [MTL4Archive](../mtl4archive.md).

## Return Value

A [MTL4Archive](../mtl4archive.md) instance, or `nil` if the function failed.
