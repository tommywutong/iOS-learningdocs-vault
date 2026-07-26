---
title: UITextDropProposal.Action.insert
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/action/insert
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/action/insert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/action/insert.json'
content_hash: 'sha256:8a3f7fd3dc538d26'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITextDropProposal](../../uitextdropproposal.md) · [Action](../action.md)

# UITextDropProposal.Action.insert

<sub>Case</sub>

A text drop action style specifying that text is inserted at the provided location, without altering the surrounding text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case insert
```

## Discussion

The action ignores any selection present in the target text view.

## See Also

### Text drop actions

- [UITextDropActionReplaceAll](replaceall.md) — A text drop action style specifying that the dropped text replaces all text in the target text view.
- [UITextDropActionReplaceSelection](replaceselection.md) — A text drop action style specifying that if the target text view contains a selection, dropped text replaces it.
