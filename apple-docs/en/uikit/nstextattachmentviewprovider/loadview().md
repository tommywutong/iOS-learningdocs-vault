---
title: loadView()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachmentviewprovider/loadview()
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider/loadview()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentviewprovider/loadview%28%29.json'
content_hash: 'sha256:7c9284903111a770'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachmentViewProvider](../nstextattachmentviewprovider.md)

# loadView()

<sub>Instance Method</sub>

Draws the custom view hierarchy that text attachment view subclasses implement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func loadView()
```

## Discussion

Use this method to create a custom view hierarchy. Don’t call this method directly, the framework calls it at the appropriate time.
