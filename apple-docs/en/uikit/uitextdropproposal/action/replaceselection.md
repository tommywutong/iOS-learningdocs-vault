---
title: UITextDropProposal.Action.replaceSelection
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdropproposal/action/replaceselection
source_url: 'https://developer.apple.com/documentation/uikit/uitextdropproposal/action/replaceselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdropproposal/action/replaceselection.json'
content_hash: 'sha256:e723eaa39e09ceb0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITextDropProposal](../../uitextdropproposal.md) · [Action](../action.md)

# UITextDropProposal.Action.replaceSelection

<sub>Case</sub>

A text drop action style specifying that if the target text view contains a selection, dropped text replaces it.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case replaceSelection
```

## Discussion

If the text view does not contain a selection, dropped text is inserted at the provided location, without altering the surrounding text.

## See Also

### Text drop actions

- [UITextDropActionInsert](insert.md) — A text drop action style specifying that text is inserted at the provided location, without altering the surrounding text.
- [UITextDropActionReplaceAll](replaceall.md) — A text drop action style specifying that the dropped text replaces all text in the target text view.
