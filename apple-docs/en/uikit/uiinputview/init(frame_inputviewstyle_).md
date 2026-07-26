---
title: 'init(frame:inputViewStyle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiinputview/init(frame:inputviewstyle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiinputview/init(frame:inputviewstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputview/init%28frame%3Ainputviewstyle%3A%29.json'
content_hash: 'sha256:70496ef3b0e31741'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputView](../uiinputview.md)

# init(frame:inputViewStyle:)

<sub>Initializer</sub>

Initializes and returns an input view using the specified style information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(frame: CGRect, inputViewStyle: UIInputView.Style)
```

## Parameters

- `frame` — The frame rectangle for the view, measured in points. The origin of the frame is relative to the superview in which you plan to add it.

- `inputViewStyle` — The style to use when altering the appearance of the view and its subviews. For a list of possible values, see [Style](style.md)

## Return Value

An initialized view object or `nil` if the view could not be initialized.

## Discussion

This method is the designated initializer for the view and must be called by your subclass at initialization time.

## See Also

### Initializing an input view

- [- initWithCoder:](<init(coder_).md>) — Creates an input view from data in an unarchiver.
