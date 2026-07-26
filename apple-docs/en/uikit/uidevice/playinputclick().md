---
title: playInputClick()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/playinputclick()
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/playinputclick()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/playinputclick%28%29.json'
content_hash: 'sha256:24ce181605669e61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# playInputClick()

<sub>Instance Method</sub>

Plays an input click in an enabled input view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func playInputClick()
```

## Discussion

Use this method to play the standard system keyboard click in response to a user tapping in a custom input or keyboard accessory view. A click plays only if the user has enabled keyboard clicks in Settings \> Sounds, and only if the input view is itself enabled and visible.

To enable a custom input or accessory view for input clicks, perform the following two steps:

1. Adopt the [UIInputViewAudioFeedback](../uiinputviewaudiofeedback.md) protocol in your input view class.
2. Implement the [enableInputClicksWhenVisible](../uiinputviewaudiofeedback/enableinputclickswhenvisible.md) delegate method to return [true](../../swift/true.md).

For more information, see [Text Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009542).
