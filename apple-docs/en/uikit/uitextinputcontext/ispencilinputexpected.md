---
title: isPencilInputExpected
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, tvOS 16.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputcontext/ispencilinputexpected
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputcontext/ispencilinputexpected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputcontext/ispencilinputexpected.json'
content_hash: 'sha256:7beaf2b6b0cd3714'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputContext](../uitextinputcontext.md)

# isPencilInputExpected

<sub>Instance Property</sub>

Returns a Boolean value that indicates whether someone is likely to use Apple Pencil for input.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isPencilInputExpected: Bool { get set }
```

## Discussion

When pencil input is likely, adjust your UI or perform any actions you need to accommodate that input. For example, you might adjust the size of UI elements to optimize them for handwriting input.

## See Also

### Getting the expected input type

- [dictationInputExpected](isdictationinputexpected.md) — Returns a Boolean value that indicates whether someone is likely to use dictation to input text to the app.
- [hardwareKeyboardInputExpected](ishardwarekeyboardinputexpected.md) — Returns a Boolean value that indicates whether someone is likely to enter text using a hardware keyboard.
