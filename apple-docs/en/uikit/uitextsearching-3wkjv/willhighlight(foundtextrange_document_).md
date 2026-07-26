---
title: 'willHighlight(foundTextRange:document:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-3wkjv/willhighlight(foundtextrange:document:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/willhighlight(foundtextrange:document:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/willhighlight%28foundtextrange%3Adocument%3A%29.json'
content_hash: 'sha256:3641cc39937a8563'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# willHighlight(foundTextRange:document:)

<sub>Instance Method</sub>

Informs the searchable object when the highlighted search result is about to change.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func willHighlight(foundTextRange: UITextRange, document: Self.DocumentIdentifier?)
```

## Parameters

- `foundTextRange` — The text range to highlight.

- `document` — A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## Default Implementations

### UITextSearching Implementations

- [willHighlight(foundTextRange:document:)](<willhighlight(foundtextrange_document_)-55xf1.md>)

## See Also

### Displaying results

- [decorate(foundTextRange:document:usingStyle:)](<decorate(foundtextrange_document_usingstyle_).md>) — Applies the style to a specific text range to indicate found and highlighted results.
- [clearAllDecoratedFoundText()](<clearalldecoratedfoundtext().md>) — Clears the style from all found and highlighted results.
- [scrollRangeToVisible(_:inDocument:)](<scrollrangetovisible(__indocument_).md>) — Scrolls to the containing view to make the text range visible.
