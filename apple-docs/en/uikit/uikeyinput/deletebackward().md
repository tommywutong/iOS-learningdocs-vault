---
title: deleteBackward()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeyinput/deletebackward()
source_url: 'https://developer.apple.com/documentation/uikit/uikeyinput/deletebackward()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyinput/deletebackward%28%29.json'
content_hash: 'sha256:ed59b50f63f7dca4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyInput](../uikeyinput.md)

# deleteBackward()

<sub>Instance Method</sub>

Deletes a character from the displayed text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func deleteBackward()
```

## Discussion

Remove the character just before the cursor from your class’s backing store and redisplay the text.

## See Also

### Inserting and deleting text

- [- insertText:](<inserttext(__).md>) — Inserts a character into the displayed text.
- [hasText](hastext.md) — A Boolean value that indicates whether the text-entry object has any text.
