---
title: 'scrollRangeToVisible:inDocument:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-53wjq/scrollrangetovisible:indocument:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/scrollrangetovisible:indocument:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-53wjq/scrollrangetovisible%3Aindocument%3A.json'
content_hash: 'sha256:048163c1614d72c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-53wjq.md)

# scrollRangeToVisible:inDocument:

<sub>Instance Method</sub>

Scrolls to the containing view to make the text range visible.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) scrollRangeToVisible:(UITextRange *) range inDocument:(UITextSearchDocumentIdentifier) document;
```

## Parameters

- `range` — The text range to scroll to.

- `document` — A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## Discussion

If the seachable object supports scrolling, use this method to implement scrolling your view to make the highlighted text range visible.

## See Also

### Displaying results

- [decorateFoundTextRange:inDocument:usingStyle:](decoratefoundtextrange_indocument_usingstyle_.md) — Applies the style to a specific text range to indicate found and highlighted results.
- [clearAllDecoratedFoundText](clearalldecoratedfoundtext.md) — Clears the style from all found and highlighted results.
- [willHighlightFoundTextRange:inDocument:](willhighlightfoundtextrange_indocument_.md) — Informs the searchable object when the highlighted search result is about to change.
