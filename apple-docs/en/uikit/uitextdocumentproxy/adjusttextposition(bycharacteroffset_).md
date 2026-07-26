---
title: 'adjustTextPosition(byCharacterOffset:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdocumentproxy/adjusttextposition(bycharacteroffset:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdocumentproxy/adjusttextposition(bycharacteroffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdocumentproxy/adjusttextposition%28bycharacteroffset%3A%29.json'
content_hash: 'sha256:a96d1ed654bf3015'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDocumentProxy](../uitextdocumentproxy.md)

# adjustTextPosition(byCharacterOffset:)

<sub>Instance Method</sub>

Moves the insertion point forward or backward in the current text input object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func adjustTextPosition(byCharacterOffset offset: Int)
```

## Parameters

- `offset` — The number of characters to adjust the insertion point by. A positive value moves the insertion point forward (according to the text storage direction for the current language). A negative value moves the insertion point backward.
