---
title: documentInfo
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicspdfrendererformat/documentinfo
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrendererformat/documentinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrendererformat/documentinfo.json'
content_hash: 'sha256:f75c65c778a431c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRendererFormat](../uigraphicspdfrendererformat.md)

# documentInfo

<sub>Instance Property</sub>

A dictionary that specifies additional information to be associated with the PDFs created by the PDF renderer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var documentInfo: [String : Any] { get set }
```

## Discussion

You can use these keys to specify additional metadata and security information for the PDF, such as the author or the password for accessing it.

The keys used in this dictionary are described in  [Auxiliary Dictionary Keys](../../coregraphics/auxiliary-dictionary-keys.md).
