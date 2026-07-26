---
title: UIWritingToolsCoordinator.TextUpdateReason.undoRedo
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textupdatereason/undoredo
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textupdatereason/undoredo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textupdatereason/undoredo.json'
content_hash: 'sha256:3347b8601bc1996a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [TextUpdateReason](../textupdatereason.md)

# UIWritingToolsCoordinator.TextUpdateReason.undoRedo

<sub>Case</sub>

An operation that changed the view’s text as part of an undo or redo command.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case undoRedo
```

## Discussion

Specify this option when an undo or redo command initiated the change to your view.

## See Also

### Getting the reasons

- [UIWritingToolsCoordinatorTextUpdateReasonTyping](typing.md) — An operation that involved a person editing the text in your view.
