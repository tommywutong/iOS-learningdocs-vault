---
title: 'init(textLineRects:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipreviewparameters/init(textlinerects:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewparameters/init(textlinerects:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewparameters/init%28textlinerects%3A%29.json'
content_hash: 'sha256:0fd806e988d6504b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewParameters](../uipreviewparameters.md)

# init(textLineRects:)

<sub>Initializer</sub>

Creates a preview parameters object with information about the text you want to preview.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(textLineRects: [NSValue])
```

## Parameters

- `textLineRects` — An array of text line rectangles in the coordinate system of the view being animated. UIKit clips the previewed content using the specified rectangles. Wrap each [CGRect](../../corefoundation/cgrect.md) in an [NSValue](../../foundation/nsvalue.md) object. If you specify an empty array, UIKit shows the entire view.

## Return Value

A new preview parameters object for a view containing text.

## See Also

### Creating preview parameters

- [- init](<init().md>) — Creates a default set of preview parameters.
