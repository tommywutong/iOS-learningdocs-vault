---
title: 'insertTextPlaceholder(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/inserttextplaceholder(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/inserttextplaceholder(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/inserttextplaceholder%28with%3A%29.json'
content_hash: 'sha256:a43fa5f1e9fd8dad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# insertTextPlaceholder(with:)

<sub>Instance Method</sub>

Inserts a placeholder object to reserve visual space during text input.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func insertTextPlaceholder(with size: CGSize) -> UITextPlaceholder
```

## Parameters

- `size` — The size of the space to reserve.

## Return Value

The placeholder object that was inserted into the text input.

## Discussion

If the `size.height` is less than or equal to zero, then the placeholder displays inline using the current line’s height.

If the `size.height` is greater than zero, then the text input treats the placeholder as a paragraph of height `size.height`.

## See Also

### Managing placeholders

- [- removeTextPlaceholder:](<remove(__).md>) — Removes a placeholder object from the text input view.
- [UITextPlaceholder](../uitextplaceholder.md) — A placeholder object that reserves visual space in a text input view.
