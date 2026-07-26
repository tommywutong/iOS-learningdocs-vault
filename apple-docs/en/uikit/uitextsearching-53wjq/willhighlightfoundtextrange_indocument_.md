---
title: 'willHighlightFoundTextRange:inDocument:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-53wjq/willhighlightfoundtextrange:indocument:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/willhighlightfoundtextrange:indocument:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-53wjq/willhighlightfoundtextrange%3Aindocument%3A.json'
content_hash: 'sha256:67eb474d86269ade'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-53wjq.md)

# willHighlightFoundTextRange:inDocument:

<sub>Instance Method</sub>

Informs the searchable object when the highlighted search result is about to change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) willHighlightFoundTextRange:(UITextRange *) range inDocument:(UITextSearchDocumentIdentifier) document;
```

## Parameters

- `range` — The text range to highlight.

- `document` — A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## See Also

### Displaying results

- [decorateFoundTextRange:inDocument:usingStyle:](decoratefoundtextrange_indocument_usingstyle_.md) — Applies the style to a specific text range to indicate found and highlighted results.
- [clearAllDecoratedFoundText](clearalldecoratedfoundtext.md) — Clears the style from all found and highlighted results.
- [scrollRangeToVisible:inDocument:](scrollrangetovisible_indocument_.md) — Scrolls to the containing view to make the text range visible.
