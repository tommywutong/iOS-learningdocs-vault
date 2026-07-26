---
title: 'init(forURL:title:target:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitargeteddragpreview/init(forurl:title:target:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitargeteddragpreview/init(forurl:title:target:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitargeteddragpreview/init%28forurl%3Atitle%3Atarget%3A%29.json'
content_hash: 'sha256:023750ccc388009b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITargetedDragPreview](../uitargeteddragpreview.md)

# init(forURL:title:target:)

<sub>Initializer</sub>

Initializes a new targeted drag item preview with a URL, a title, and a drag item preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(forURL url: URL, title: String?, target: UIDragPreviewTarget)
```

## Parameters

- `url` — An Internet address referencing a remote resource, such as a webpage.

- `title` — A title for the URL.

- `target` — A drag item preview target.

## Return Value

A drag preview for a URL with a title based on the specified drag item preview target.

## Discussion

This method creates a two-line drag item preview, with the title displayed on the first line. The second line is a textual representation of the URL that might not show the full URL string. Don’t use a file URL. Passing `nil` for the title is the same as calling [init(forURL:target:)](<init(forurl_target_).md>).

## See Also

### Initializing a targeted drag item preview

- [init(forURL:target:)](<init(forurl_target_).md>) — Initializes a new targeted drag item preview with a URL and a drag item preview.
