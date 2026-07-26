---
title: RenameAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/renameaction
source_url: 'https://developer.apple.com/documentation/swiftui/renameaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/renameaction.json'
content_hash: 'sha256:f741883bc3a44a61'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RenameAction

<sub>Structure</sub>

An action that activates a standard rename interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RenameAction
```

## Overview

Use the [renameAction(_:)](<view/renameaction(__).md>) modifier to configure the rename action in the environment.

## Topics

### Calling the action

- [callAsFunction()](<renameaction/callasfunction().md>) — Triggers the standard rename action provided through the environment.

## See Also

### Renaming a document

- [RenameButton](renamebutton.md) — A button that triggers a standard rename action.
- [renameAction(_:)](<view/renameaction(__).md>) — Sets a closure to run for the rename action.
- [rename](environmentvalues/rename.md) — An action that activates the standard rename interaction.
