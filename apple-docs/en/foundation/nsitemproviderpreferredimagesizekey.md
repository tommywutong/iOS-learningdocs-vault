---
title: NSItemProviderPreferredImageSizeKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemproviderpreferredimagesizekey
source_url: 'https://developer.apple.com/documentation/foundation/nsitemproviderpreferredimagesizekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemproviderpreferredimagesizekey.json'
content_hash: 'sha256:22a670683ff557bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSItemProviderPreferredImageSizeKey

<sub>Global Variable</sub>

A key provided to the options dictionary to indicate a preferred image size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSItemProviderPreferredImageSizeKey: String
```

## Discussion

Use this key only with the [NSItemProvider](nsitemprovider.md) type coercion policy. Ensure the value is an [NSValue](nsvalue.md) object that contains a [CGSize](../corefoundation/cgsize.md) struct specifying the requested size, in points.
