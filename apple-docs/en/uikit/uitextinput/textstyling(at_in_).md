---
title: 'textStyling(at:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/textstyling(at:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/textstyling(at:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/textstyling%28at%3Ain%3A%29.json'
content_hash: 'sha256:07eda86e749f9a27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# textStyling(at:in:)

<sub>Instance Method</sub>

Returns a dictionary with properties that specify how to style the text at a certain location in a document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textStyling(at position: UITextPosition, in direction: UITextStorageDirection) -> [NSAttributedString.Key : Any]?
```

## Parameters

- `position` — An object that indicates a location in the text of a document.

- `direction` — The direction of the styling attributes in text storage.

## Return Value

A dictionary whose elements are one or more of the key-value pairs defining text color, font, and background color. See [Style dictionary keys](../style-dictionary-keys.md) for descriptions of these key-value pairs.

## Discussion

Text styling information can affect, for example, the appearance of a correction rectangle.
