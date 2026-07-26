---
title: 'init(frame:textContainer:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextview/init(frame:textcontainer:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/init(frame:textcontainer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/init%28frame%3Atextcontainer%3A%29.json'
content_hash: 'sha256:a0689bee9adbd928'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# init(frame:textContainer:)

<sub>Initializer</sub>

Creates a new text view with the specified text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(frame: CGRect, textContainer: NSTextContainer?)
```

## Parameters

- `frame` — The frame rectangle of the text view.

- `textContainer` — The text container to use for the receiver (can be `nil`).

## Return Value

An initialized text view.

## Discussion

This is the designated initializer for `UITextView` objects.

## See Also

### Initializing the text view

- [+ textViewUsingTextLayoutManager:](<init(usingtextlayoutmanager_).md>) — Creates a new text view, with or without a text layout manager depending on the Boolean value you specify.
- [- initWithCoder:](<init(coder_).md>) — Creates a text view from data in an unarchiver.
