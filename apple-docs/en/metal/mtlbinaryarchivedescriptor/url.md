---
title: url
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbinaryarchivedescriptor/url
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchivedescriptor/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchivedescriptor/url.json'
content_hash: 'sha256:914cb2eddf289b19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBinaryArchiveDescriptor](../mtlbinaryarchivedescriptor.md)

# url

<sub>Instance Property</sub>

A URL to a Metal binary archive file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var url: URL? { get set }
```

## Discussion

You can use this method to load a binary archive you created with an [MTLBinaryArchive](../mtlbinaryarchive.md) instance’s [- serializeToURL:error:](<../mtlbinaryarchive/serialize(to_).md>) method.
