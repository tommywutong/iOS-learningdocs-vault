---
title: 'init(view:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidragpreview/init(view:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidragpreview/init(view:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragpreview/init%28view%3A%29.json'
content_hash: 'sha256:ca30444348e8f571'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragPreview](../uidragpreview.md)

# init(view:)

<sub>Initializer</sub>

Initializes a new drag item preview with a view, using the default appearance parameters.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(view: UIView)
```

## Parameters

- `view` — A [UIView](../uiview.md) object representing the drag item.

## Return Value

A drag preview that is based on the specified view.

## Discussion

Use this method to display a drag item preview based on a view that you provide. The preview displays a snapshot of the provided view. Changes to the view don’t appear after the preview is shown, and the preview doesn’t change or move the view.

## See Also

### Initializing a drag item preview

- [- initWithView:parameters:](<init(view_parameters_).md>) — Initializes a new drag item preview with a view and with a set of appearance parameters.
- [init(forURL:)](<init(forurl_).md>) — Initializes a new drag item preview with a URL.
- [init(forURL:title:)](<init(forurl_title_).md>) — Initializes a drag item preview with a URL and title.
