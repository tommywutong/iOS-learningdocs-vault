---
title: 'init(forURL:target:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitargeteddragpreview/init(forurl:target:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitargeteddragpreview/init(forurl:target:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitargeteddragpreview/init%28forurl%3Atarget%3A%29.json'
content_hash: 'sha256:c2bb84ad0011d176'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITargetedDragPreview](../uitargeteddragpreview.md)

# init(forURL:target:)

<sub>Initializer</sub>

Initializes a new targeted drag item preview with a URL and a drag item preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(forURL url: URL, target: UIDragPreviewTarget)
```

## Parameters

- `url` — An Internet address referencing a remote resource, such as a webpage.

- `target` — A drag item preview target.

## Return Value

A targeted drag preview for a URL based on the drag item preview target.

## Discussion

This method creates a targeted drag item preview of the URL. The URL preview is a one-line, textual representation that might not show the full URL string. Don’t use a file URL.

## See Also

### Initializing a targeted drag item preview

- [init(forURL:title:target:)](<init(forurl_title_target_).md>) — Initializes a new targeted drag item preview with a URL, a title, and a drag item preview.
