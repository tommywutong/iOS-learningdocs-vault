---
title: 'insertText(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uikeyinput/inserttext(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uikeyinput/inserttext(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyinput/inserttext%28_%3A%29.json'
content_hash: 'sha256:55cb91961e10d60f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyInput](../uikeyinput.md)

# insertText(_:)

<sub>Instance Method</sub>

Inserts a character into the displayed text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertText(_ text: String)
```

## Parameters

- `text` — A string object representing the character typed on the system keyboard.

## Discussion

Add the character `text` to your class’s backing store at the index corresponding to the cursor and redisplay the text.

## See Also

### Inserting and deleting text

- [- deleteBackward](<deletebackward().md>) — Deletes a character from the displayed text.
- [hasText](hastext.md) — A Boolean value that indicates whether the text-entry object has any text.
