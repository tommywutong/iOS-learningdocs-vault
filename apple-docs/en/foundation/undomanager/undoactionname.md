---
title: undoActionName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/undoactionname
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/undoactionname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/undoactionname.json'
content_hash: 'sha256:b5c9c96b61510144'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# undoActionName

<sub>Instance Property</sub>

The name identifying the undo action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var undoActionName: String { get }
```

## Discussion

The undo action name. Returns an empty string (`@""`) if no action name has been assigned or if there is nothing to undo.

For example, if the menu title is “Undo Delete,” the string returned is “Delete.”

## See Also

### Managing the action name

- [redoActionName](redoactionname.md) — The name identifying the redo action.
- [setActionName(_:)](<setactionname(__)-cci9.md>) — Sets the name of the action associated with the Undo or Redo command using a localized string resource.
- [- setActionName:](<setactionname(__)-8lzip.md>) — Sets the name of the action associated with the Undo or Redo command.
