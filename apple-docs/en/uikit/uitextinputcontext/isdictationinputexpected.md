---
title: isDictationInputExpected
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, tvOS 16.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputcontext/isdictationinputexpected
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputcontext/isdictationinputexpected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputcontext/isdictationinputexpected.json'
content_hash: 'sha256:5f65df9cd841785b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputContext](../uitextinputcontext.md)

# isDictationInputExpected

<sub>Instance Property</sub>

Returns a Boolean value that indicates whether someone is likely to use dictation to input text to the app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isDictationInputExpected: Bool { get set }
```

## Discussion

When dictation input is likely, adjust your UI or perform any actions you need to accommodate dictation input.

## See Also

### Getting the expected input type

- [hardwareKeyboardInputExpected](ishardwarekeyboardinputexpected.md) — Returns a Boolean value that indicates whether someone is likely to enter text using a hardware keyboard.
- [pencilInputExpected](ispencilinputexpected.md) — Returns a Boolean value that indicates whether someone is likely to use Apple Pencil for input.
