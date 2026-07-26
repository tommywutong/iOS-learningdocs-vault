---
title: UITextDropProposal.Performer.delegate
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/performer/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/performer/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/performer/delegate.json'
content_hash: 'sha256:04b8c3850f7ddaff'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITextDropProposal](../../uitextdropproposal.md) · [Performer](../performer.md)

# UITextDropProposal.Performer.delegate

<sub>Case</sub>

A performer type that indicates the delegate object is responsible for doing the drop operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case delegate
```

## Discussion

If this performer is used, the delegate must implement the [- textDroppableView:willPerformDrop:](<../../uitextdropdelegate/textdroppableview(__willperformdrop_).md>) method. Otherwise, the text view handles the drop operation, which is the same behavior as specifying [UITextDropPerformerView](view.md) as the performer.

## See Also

### Performers

- [UITextDropPerformerView](view.md) — A performer type that indicates that the text view is responsible for doing the drop operation.
