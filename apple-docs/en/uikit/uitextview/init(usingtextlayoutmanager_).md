---
title: 'init(usingTextLayoutManager:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextview/init(usingtextlayoutmanager:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/init(usingtextlayoutmanager:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/init%28usingtextlayoutmanager%3A%29.json'
content_hash: 'sha256:f8e2e345209a601e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# init(usingTextLayoutManager:)

<sub>Initializer</sub>

Creates a new text view, with or without a text layout manager depending on the Boolean value you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(usingTextLayoutManager: Bool)
```

## Parameters

- `usingTextLayoutManager` — A Boolean value that indicates whether the framework should create the text view with an [NSTextLayoutManager](../nstextlayoutmanager.md).

## See Also

### Initializing the text view

- [- initWithFrame:textContainer:](<init(frame_textcontainer_).md>) — Creates a new text view with the specified text container.
- [- initWithCoder:](<init(coder_).md>) — Creates a text view from data in an unarchiver.
