---
title: UITextDropProposal.Performer.view
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/performer/view
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/performer/view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/performer/view.json'
content_hash: 'sha256:aa18393b602dd1ff'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITextDropProposal](../../uitextdropproposal.md) · [Performer](../performer.md)

# UITextDropProposal.Performer.view

<sub>Case</sub>

A performer type that indicates that the text view is responsible for doing the drop operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case view
```

## Discussion

This performer is the default for a [UITextDropProposal](../../uitextdropproposal.md) object. If this performer is used, the [- textDroppableView:willPerformDrop:](<../../uitextdropdelegate/textdroppableview(__willperformdrop_).md>) method is called (if implemented). However, implementing the delegate method isn’t required when using this performer.

## See Also

### Performers

- [UITextDropPerformerDelegate](delegate.md) — A performer type that indicates the delegate object is responsible for doing the drop operation.
