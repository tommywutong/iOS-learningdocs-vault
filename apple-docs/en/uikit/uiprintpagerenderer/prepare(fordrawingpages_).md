---
title: 'prepare(forDrawingPages:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintpagerenderer/prepare(fordrawingpages:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/prepare(fordrawingpages:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/prepare%28fordrawingpages%3A%29.json'
content_hash: 'sha256:15cdec55fea2a44e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# prepare(forDrawingPages:)

<sub>Instance Method</sub>

Prepares the renderer for drawing a range of pages.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func prepare(forDrawingPages range: NSRange)
```

## Parameters

- `range` — A range of pages.

## Discussion

UIKit calls this method before it requests drawing for a range of pages. You can optionally override this method to perform setup tasks. The default implementation does nothing.
