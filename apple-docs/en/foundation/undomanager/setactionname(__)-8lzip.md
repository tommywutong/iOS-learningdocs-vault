---
title: 'setActionName(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/undomanager/setactionname(_:)-8lzip'
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/setactionname(_:)-8lzip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/setactionname%28_%3A%29-8lzip.json'
content_hash: 'sha256:0fb96871871332a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# setActionName(_:)

<sub>Instance Method</sub>

Sets the name of the action associated with the Undo or Redo command.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setActionName(_ actionName: String)
```

## Parameters

- `actionName` — The name of the action.

## Discussion

If `actionName` is an empty string, the undo manager removes the action name currently associated with the menu command.

## See Also

### Managing the action name

- [undoActionName](undoactionname.md) — The name identifying the undo action.
- [redoActionName](redoactionname.md) — The name identifying the redo action.
- [setActionName(_:)](<setactionname(__)-cci9.md>) — Sets the name of the action associated with the Undo or Redo command using a localized string resource.
