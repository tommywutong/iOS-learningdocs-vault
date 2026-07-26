---
title: 'scrollRangeToVisible(_:inDocument:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-3wkjv/scrollrangetovisible(_:indocument:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/scrollrangetovisible(_:indocument:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/scrollrangetovisible%28_%3Aindocument%3A%29.json'
content_hash: 'sha256:a2ae2d164832f2c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# scrollRangeToVisible(_:inDocument:)

<sub>Instance Method</sub>

Scrolls to the containing view to make the text range visible.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func scrollRangeToVisible(_ range: UITextRange, inDocument: Self.DocumentIdentifier?)
```

## Parameters

- `range` — The text range to scroll to.

- `inDocument` — A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## Discussion

If the seachable object supports scrolling, use this method to implement scrolling your view to make the highlighted text range visible.

## Default Implementations

### UITextSearching Implementations

- [scrollRangeToVisible(_:inDocument:)](<scrollrangetovisible(__indocument_)-8v4iu.md>)

## See Also

### Displaying results

- [decorate(foundTextRange:document:usingStyle:)](<decorate(foundtextrange_document_usingstyle_).md>) — Applies the style to a specific text range to indicate found and highlighted results.
- [clearAllDecoratedFoundText()](<clearalldecoratedfoundtext().md>) — Clears the style from all found and highlighted results.
- [willHighlight(foundTextRange:document:)](<willhighlight(foundtextrange_document_).md>) — Informs the searchable object when the highlighted search result is about to change.
