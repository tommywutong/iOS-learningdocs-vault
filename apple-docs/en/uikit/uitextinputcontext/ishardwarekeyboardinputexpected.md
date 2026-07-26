---
title: isHardwareKeyboardInputExpected
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, tvOS 16.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputcontext/ishardwarekeyboardinputexpected
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputcontext/ishardwarekeyboardinputexpected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputcontext/ishardwarekeyboardinputexpected.json'
content_hash: 'sha256:3cc09d615ff1d7d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputContext](../uitextinputcontext.md)

# isHardwareKeyboardInputExpected

<sub>Instance Property</sub>

Returns a Boolean value that indicates whether someone is likely to enter text using a hardware keyboard.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHardwareKeyboardInputExpected: Bool { get set }
```

## Discussion

When hardware keyboard input is likely, adjust your UI or perform any actions you need to accommodate that input.

## See Also

### Getting the expected input type

- [dictationInputExpected](isdictationinputexpected.md) — Returns a Boolean value that indicates whether someone is likely to use dictation to input text to the app.
- [pencilInputExpected](ispencilinputexpected.md) — Returns a Boolean value that indicates whether someone is likely to use Apple Pencil for input.
