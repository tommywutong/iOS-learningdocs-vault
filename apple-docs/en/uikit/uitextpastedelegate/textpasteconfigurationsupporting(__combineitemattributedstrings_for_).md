---
title: 'textPasteConfigurationSupporting(_:combineItemAttributedStrings:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:combineitemattributedstrings:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:combineitemattributedstrings:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting%28_%3Acombineitemattributedstrings%3Afor%3A%29.json'
content_hash: 'sha256:5dc6c7ec2dddb92c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextPasteDelegate](../uitextpastedelegate.md)

# textPasteConfigurationSupporting(_:combineItemAttributedStrings:for:)

<sub>Instance Method</sub>

Asks the delegate to combine multiple strings into a single attributed string.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textPasteConfigurationSupporting(_ textPasteConfigurationSupporting: any UITextPasteConfigurationSupporting, combineItemAttributedStrings itemStrings: [NSAttributedString], for textRange: UITextRange) -> NSAttributedString
```

## Parameters

- `textPasteConfigurationSupporting` — The object that received the paste or drop request.

- `itemStrings` — An array of attributed strings that will be combined to form a single attributed string.

- `textRange` — The position in the text view where the paste or drop operation will place the text.

## Return Value

An attributed string based on the combination of multiple strings.

## Discussion

You implement this method when you need to change how the item strings are combined to form the single attributed string. If this method isn’t implemented, the item strings are concatenated without any delimiters.

## See Also

### Pasting the text paste item

- [- textPasteConfigurationSupporting:performPasteOfAttributedString:toRange:](<textpasteconfigurationsupporting(__performpasteof_to_).md>) — Asks the delegate to explicitly handle the final incorporation of a pasted or dropped string of text into the text view.
