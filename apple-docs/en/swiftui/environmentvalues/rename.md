---
title: rename
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/rename
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/rename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/rename.json'
content_hash: 'sha256:6ec28d83007fd958'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# rename

<sub>Instance Property</sub>

An action that activates the standard rename interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rename: RenameAction? { get }
```

## Discussion

Use the [renameAction(_:)](<../view/renameaction(__).md>) modifier to configure the rename action in the environment.

## See Also

### Renaming a document

- [RenameButton](../renamebutton.md) — A button that triggers a standard rename action.
- [renameAction(_:)](<../view/renameaction(__).md>) — Sets a closure to run for the rename action.
- [RenameAction](../renameaction.md) — An action that activates a standard rename interaction.
