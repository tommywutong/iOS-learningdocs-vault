---
title: SearchScopeActivation
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/searchscopeactivation
source_url: 'https://developer.apple.com/documentation/swiftui/searchscopeactivation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchscopeactivation.json'
content_hash: 'sha256:3c2260944bc83947'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SearchScopeActivation

<sub>Structure</sub>

The ways that searchable modifiers can show or hide search scopes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SearchScopeActivation
```

## Topics

### Getting search scope activiation types

- [automatic](searchscopeactivation/automatic.md) — The automatic activation of the scope bar.
- [onSearchPresentation](searchscopeactivation/onsearchpresentation.md) — An activation where the system shows search scopes after presenting search and hides search scopes after search cancellation.
- [onTextEntry](searchscopeactivation/ontextentry.md) — An activation where the system shows search scopes when typing begins in the search field and hides search scopes after search cancellation.

## See Also

### Limiting search scope

- [Scoping a search operation](scoping-a-search-operation.md) — Divide the search space into a few broad categories.
- [searchScopes(_:scopes:)](<view/searchscopes(__scopes_).md>) — Configures the search scopes for this view.
- [searchScopes(_:activation:_:)](<view/searchscopes(__activation___).md>) — Configures the search scopes for this view with the specified activation strategy.
