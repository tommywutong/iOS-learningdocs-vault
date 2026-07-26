---
title: 'tabletopGame(_:parent:automaticUpdate:interaction:)'
framework: TabletopKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/tabletopgame(_:parent:automaticupdate:interaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tabletopgame(_:parent:automaticupdate:interaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tabletopgame%28_%3Aparent%3Aautomaticupdate%3Ainteraction%3A%29.json'
content_hash: 'sha256:57252a8364598298'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tabletopGame(_:parent:automaticUpdate:interaction:)

<sub>Instance Method</sub>

Supplies a closure which returns a new interaction whenever needed.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency func tabletopGame(_ game: TabletopGame, parent: Entity, automaticUpdate: Bool = true, interaction make: @escaping (TabletopInteraction.Value) -> any TabletopInteraction.Delegate) -> some View

```

## See Also

### Creating a tabletop game

- [tabletopGame(_:parent:automaticUpdate:)](<tabletopgame(__parent_automaticupdate_).md>) — Adds a tabletop game to a view.
