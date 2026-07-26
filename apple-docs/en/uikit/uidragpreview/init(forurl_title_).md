---
title: 'init(forURL:title:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidragpreview/init(forurl:title:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidragpreview/init(forurl:title:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragpreview/init%28forurl%3Atitle%3A%29.json'
content_hash: 'sha256:d0101139a4ef8a99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragPreview](../uidragpreview.md)

# init(forURL:title:)

<sub>Initializer</sub>

Initializes a drag item preview with a URL and title.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(forURL url: URL, title: String?)
```

## Parameters

- `url` — An Internet address referencing a remote resource, such as a webpage.

- `title` — A title for the URL.

## Return Value

A drag preview for a URL that has a title.

## Discussion

This method creates a two-line drag item preview, with the title displayed on the first line. The second line is a textual representation of the URL that might not show the full URL string. Don’t use a file URL. Passing `nil` for the title is the same as calling [init(forURL:)](<init(forurl_).md>).

## See Also

### Initializing a drag item preview

- [- initWithView:](<init(view_).md>) — Initializes a new drag item preview with a view, using the default appearance parameters.
- [- initWithView:parameters:](<init(view_parameters_).md>) — Initializes a new drag item preview with a view and with a set of appearance parameters.
- [init(forURL:)](<init(forurl_).md>) — Initializes a new drag item preview with a URL.
