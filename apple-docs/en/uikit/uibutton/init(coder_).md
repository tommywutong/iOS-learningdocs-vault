---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/init%28coder%3A%29.json'
content_hash: 'sha256:46e4710bbc9944bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# init(coder:)

<sub>Initializer</sub>

Creates a new button with data in an unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder` — An unarchiver object.

## See Also

### Creating buttons

- [- initWithFrame:](<init(frame_).md>) — Creates a new button with the specified frame.
- [- initWithFrame:primaryAction:](<init(frame_primaryaction_).md>) — Creates a new button with the specified frame, registers the primary action event, and sets the title and image to the action’s title and image.
