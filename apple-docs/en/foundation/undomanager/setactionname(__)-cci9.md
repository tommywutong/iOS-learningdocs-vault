---
title: 'setActionName(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/undomanager/setactionname(_:)-cci9'
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/setactionname(_:)-cci9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/setactionname%28_%3A%29-cci9.json'
content_hash: 'sha256:f7da6564e4792ed3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# setActionName(_:)

<sub>Instance Method</sub>

Sets the name of the action associated with the Undo or Redo command using a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency final func setActionName(_ actionNameResource: LocalizedStringResource?)
```

## Parameters

- `actionNameResource` — The name of the action, as a [LocalizedStringResource](../localizedstringresource.md). Pass in `nil` to reset the action name currently associated with the menu command.

## Discussion

This version of `setActionName(_:)` takes a [LocalizedStringResource](../localizedstringresource.md). When using this version, [undoActionName](undoactionname.md), [redoActionName](redoactionname.md), [undoMenuItemTitle](undomenuitemtitle.md), and [redoMenuItemTitle](redomenuitemtitle.md) interpret the provided resource using the current locale.

The undo manager parses the parameter as Markdown using [init(localized:)](<../attributedstring/init(localized_).md>) in order to support inflection.

If `actionNameResource` is `nil`, the undo manager removes the action name currently associated with the menu command.

## See Also

### Managing the action name

- [undoActionName](undoactionname.md) — The name identifying the undo action.
- [redoActionName](redoactionname.md) — The name identifying the redo action.
- [- setActionName:](<setactionname(__)-8lzip.md>) — Sets the name of the action associated with the Undo or Redo command.
