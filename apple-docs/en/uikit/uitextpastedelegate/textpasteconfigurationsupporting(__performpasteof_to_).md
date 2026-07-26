---
title: 'textPasteConfigurationSupporting(_:performPasteOf:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:performpasteof:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:performpasteof:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting%28_%3Aperformpasteof%3Ato%3A%29.json'
content_hash: 'sha256:5a5781bb13470c8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextPasteDelegate](../uitextpastedelegate.md)

# textPasteConfigurationSupporting(_:performPasteOf:to:)

<sub>Instance Method</sub>

Asks the delegate to explicitly handle the final incorporation of a pasted or dropped string of text into the text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textPasteConfigurationSupporting(_ textPasteConfigurationSupporting: any UITextPasteConfigurationSupporting, performPasteOf attributedString: NSAttributedString, to textRange: UITextRange) -> UITextRange
```

## Return Value

A text range representing the position of the text added to the text view.

## Discussion

You implement this method when you want to handle pasting the final attributed string into the text view. If you don’t implement this method, the standard paste mechanism is used. When adding the attributed string to the text view, be sure to place the text at the provided text range. Placing the string elsewhere in the text view may confuse the user.

## See Also

### Pasting the text paste item

- [- textPasteConfigurationSupporting:combineItemAttributedStrings:forRange:](<textpasteconfigurationsupporting(__combineitemattributedstrings_for_).md>) — Asks the delegate to combine multiple strings into a single attributed string.
