---
title: 'decorateFoundTextRange:inDocument:usingStyle:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-53wjq/decoratefoundtextrange:indocument:usingstyle:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/decoratefoundtextrange:indocument:usingstyle:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-53wjq/decoratefoundtextrange%3Aindocument%3Ausingstyle%3A.json'
content_hash: 'sha256:6f7cafc5229db208'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-53wjq.md)

# decorateFoundTextRange:inDocument:usingStyle:

<sub>Instance Method</sub>

Applies the style to a specific text range to indicate found and highlighted results.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) decorateFoundTextRange:(UITextRange *) range inDocument:(UITextSearchDocumentIdentifier) document usingStyle:(UITextSearchFoundTextStyle) style;
```

## Parameters

- `range` — The text range to decorate.

- `document` — A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

- `style` — The style to decorate the text: highlighted, found, or normal.

## Discussion

The system calls this method during a find session to display the results of a search in your custom view. Your implenentation should decorate matching text ranges for the given style to indicate the found and highlighted result.

## See Also

### Displaying results

- [clearAllDecoratedFoundText](clearalldecoratedfoundtext.md) — Clears the style from all found and highlighted results.
- [willHighlightFoundTextRange:inDocument:](willhighlightfoundtextrange_indocument_.md) — Informs the searchable object when the highlighted search result is about to change.
- [scrollRangeToVisible:inDocument:](scrollrangetovisible_indocument_.md) — Scrolls to the containing view to make the text range visible.
