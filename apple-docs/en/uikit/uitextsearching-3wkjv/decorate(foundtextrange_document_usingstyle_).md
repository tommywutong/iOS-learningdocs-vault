---
title: 'decorate(foundTextRange:document:usingStyle:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-3wkjv/decorate(foundtextrange:document:usingstyle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/decorate(foundtextrange:document:usingstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/decorate%28foundtextrange%3Adocument%3Ausingstyle%3A%29.json'
content_hash: 'sha256:e08ddcfc63ca2825'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# decorate(foundTextRange:document:usingStyle:)

<sub>Instance Method</sub>

Applies the style to a specific text range to indicate found and highlighted results.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func decorate(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, usingStyle: UITextSearchFoundTextStyle)
```

## Parameters

- `foundTextRange` — The text range to decorate.

- `document` — A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

- `usingStyle` — The style to decorate the text: highlighted, found, or normal.

## Discussion

The system calls this method during a find session to display the results of a search in your custom view. Your implenentation should decorate matching text ranges for the given style to indicate the found and highlighted result.

## See Also

### Displaying results

- [clearAllDecoratedFoundText()](<clearalldecoratedfoundtext().md>) — Clears the style from all found and highlighted results.
- [willHighlight(foundTextRange:document:)](<willhighlight(foundtextrange_document_).md>) — Informs the searchable object when the highlighted search result is about to change.
- [scrollRangeToVisible(_:inDocument:)](<scrollrangetovisible(__indocument_).md>) — Scrolls to the containing view to make the text range visible.
