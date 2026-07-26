---
title: setDefaultResult()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextpasteitem/setdefaultresult()
source_url: 'https://developer.apple.com/documentation/uikit/uitextpasteitem/setdefaultresult()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextpasteitem/setdefaultresult%28%29.json'
content_hash: 'sha256:7784af03ebc995e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextPasteItem](../uitextpasteitem.md)

# setDefaultResult()

<sub>Instance Method</sub>

Sets the text paste item’s value to the default value based on the item provider’s data.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setDefaultResult()
```

## Discussion

You call this method, as a fallback, for any items you don’t handle. Setting the default result when the item provider’s data isn’t supported is the same as calling the [- setNoResult](<setnoresult().md>) method.

## See Also

### Setting a text paste item’s result value

- [- setStringResult:](<setresult(string_).md>) — Sets a text paste item’s textual value to a specified plaintext string from the item provider.
- [- setAttributedStringResult:](<setresult(attributedstring_).md>) — Sets a text paste item’s textual value to a specified attributed string from the item provider.
- [- setAttachmentResult:](<setresult(attachment_).md>) — Sets a text paste item’s attachment value to a specified value.
- [- setNoResult](<setnoresult().md>) — Sets the text paste item’s textual value to not include data from the item provider.
