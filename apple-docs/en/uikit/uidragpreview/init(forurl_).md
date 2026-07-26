---
title: 'init(forURL:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidragpreview/init(forurl:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidragpreview/init(forurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragpreview/init%28forurl%3A%29.json'
content_hash: 'sha256:d78146f9697a72a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragPreview](../uidragpreview.md)

# init(forURL:)

<sub>Initializer</sub>

Initializes a new drag item preview with a URL.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(forURL url: URL)
```

## Parameters

- `url` — An Internet address referencing a remote resource, such as a webpage.

## Return Value

A drag preview for a URL.

## Discussion

This method creates a drag item preview of the URL. The URL preview is a one-line, textual representation that might not show the full URL string. Don’t use a file URL.

## See Also

### Initializing a drag item preview

- [- initWithView:](<init(view_).md>) — Initializes a new drag item preview with a view, using the default appearance parameters.
- [- initWithView:parameters:](<init(view_parameters_).md>) — Initializes a new drag item preview with a view and with a set of appearance parameters.
- [init(forURL:title:)](<init(forurl_title_).md>) — Initializes a drag item preview with a URL and title.
