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
doc_path: '/documentation/metal/mtlbinaryarchive/serialize(to:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchive/serialize(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchive/serialize%28to%3A%29.json'
content_hash: 'sha256:155ebc9381aa3523'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBinaryArchive](../mtlbinaryarchive.md)

# serialize(to:)

<sub>Instance Method</sub>

Writes the contents of the archive to a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func serialize(to url: URL) throws
```

## Parameters

- `url` — The URL for the destination file.

## Discussion

The destination folder needs to exist when you call this method.
