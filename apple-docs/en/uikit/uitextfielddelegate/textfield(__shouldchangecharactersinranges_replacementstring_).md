---
title: 'textField(_:shouldChangeCharactersInRanges:replacementString:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfield(_:shouldchangecharactersinranges:replacementstring:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:shouldchangecharactersinranges:replacementstring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfield%28_%3Ashouldchangecharactersinranges%3Areplacementstring%3A%29.json'
content_hash: 'sha256:69e739ad72568007'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textField(_:shouldChangeCharactersInRanges:replacementString:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textField(_ textField: UITextField, shouldChangeCharactersInRanges ranges: [NSValue], replacementString string: String) -> Bool
```

## Parameters

- `textField` — The text field asking the delegate

- `ranges` — The ranges of the text that should be deleted before replacing

## Return Value

Returns YES if the text at the `ranges` should be replaced.

## Discussion

Asks the delegate if the text at the specified `ranges` should be replaced with `string`.

If this method returns YES then the text field will, at its own discretion, choose any one of the specified `ranges` of text and replace it with the specified `replacementString` before deleting the text at the other ranges.
