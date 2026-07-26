---
title: redoActionName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/redoactionname
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/redoactionname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/redoactionname.json'
content_hash: 'sha256:57c954d3d65c7c86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# redoActionName

<sub>Instance Property</sub>

The name identifying the redo action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var redoActionName: String { get }
```

## Discussion

The redo action name. Returns an empty string (`@""`) if no action name has been assigned or if there is nothing to redo.

For example, if the menu title is “Redo Delete,” the string returned is “Delete.”

## See Also

### Managing the action name

- [undoActionName](undoactionname.md) — The name identifying the undo action.
- [setActionName(_:)](<setactionname(__)-cci9.md>) — Sets the name of the action associated with the Undo or Redo command using a localized string resource.
- [- setActionName:](<setactionname(__)-8lzip.md>) — Sets the name of the action associated with the Undo or Redo command.
