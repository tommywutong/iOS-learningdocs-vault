---
title: currentInputMode
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.2+（7.0 起废弃）, iPadOS 4.2+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitextinputmode/currentinputmode
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputmode/currentinputmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputmode/currentinputmode.json'
content_hash: 'sha256:0e5526e48614aa33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputMode](../uitextinputmode.md)

# currentInputMode

<sub>Type Method</sub>

Returns an instance representing the current text-input mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UITextInputMode *) currentInputMode;
```

## Return Value

An object representing the current input mode or `nil` if this object is not set by the text input system.

## See Also

### Getting the current and active text-input modes

- [activeInputModes](activeinputmodes.md) — The active text-input modes.
