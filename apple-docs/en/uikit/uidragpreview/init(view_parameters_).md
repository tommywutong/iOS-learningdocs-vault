---
title: 'init(view:parameters:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidragpreview/init(view:parameters:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidragpreview/init(view:parameters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragpreview/init%28view%3Aparameters%3A%29.json'
content_hash: 'sha256:39ca9b05d68ad1e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragPreview](../uidragpreview.md)

# init(view:parameters:)

<sub>Initializer</sub>

Initializes a new drag item preview with a view and with a set of appearance parameters.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(view: UIView, parameters: UIDragPreviewParameters)
```

## Parameters

- `view` — A [UIView](../uiview.md) object representing the drag item.

- `parameters` — A [UIDragPreviewParameters](../uidragpreviewparameters.md) object containing appearance parameters for the drag item preview.

## Return Value

A drag preview that is based on the specified view and has specific appearance parameters.

## Discussion

Use this method to display a custom drag item preview based on the provided view and appearance parameters. The appearance parameters specify display options for the preview, such as a background color and a Bézier path of the visible area of the provided view. The appearance parameters affect only the display of the preview, and not the provided view. The drag item preview uses a snapshot of the view for the display, and it never changes or moves the view.

## See Also

### Initializing a drag item preview

- [- initWithView:](<init(view_).md>) — Initializes a new drag item preview with a view, using the default appearance parameters.
- [init(forURL:)](<init(forurl_).md>) — Initializes a new drag item preview with a URL.
- [init(forURL:title:)](<init(forurl_title_).md>) — Initializes a drag item preview with a URL and title.
