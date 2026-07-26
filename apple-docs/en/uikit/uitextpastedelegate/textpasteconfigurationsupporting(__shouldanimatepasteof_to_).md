---
title: 'textPasteConfigurationSupporting(_:shouldAnimatePasteOf:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:shouldanimatepasteof:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting(_:shouldanimatepasteof:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextpastedelegate/textpasteconfigurationsupporting%28_%3Ashouldanimatepasteof%3Ato%3A%29.json'
content_hash: 'sha256:df6ce949af704d4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextPasteDelegate](../uitextpastedelegate.md)

# textPasteConfigurationSupporting(_:shouldAnimatePasteOf:to:)

<sub>Instance Method</sub>

Asks the delegate if the paste or drop operation should be animated.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textPasteConfigurationSupporting(_ textPasteConfigurationSupporting: any UITextPasteConfigurationSupporting, shouldAnimatePasteOf attributedString: NSAttributedString, to textRange: UITextRange) -> Bool
```

## Parameters

- `textPasteConfigurationSupporting` — The object that received the paste or drop request.

- `attributedString` — The text that will be added to the text view.

- `textRange` — The position in the text view where the paste or drop operation will place the text.

## Return Value

[false](../../swift/false.md) if the paste or drop operation should not be animated; otherwise, [true](../../swift/true.md).

## Discussion

If you don’t want the system to animate the paste or drop operation, implement this method and return [false](../../swift/false.md). The operation is animated if you return [true](../../swift/true.md) or if this method isn’t implemented.
