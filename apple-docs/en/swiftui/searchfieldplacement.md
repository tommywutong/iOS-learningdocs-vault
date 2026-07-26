---
title: SearchFieldPlacement
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/searchfieldplacement
source_url: 'https://developer.apple.com/documentation/swiftui/searchfieldplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchfieldplacement.json'
content_hash: 'sha256:44d880e2cbafb0f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SearchFieldPlacement

<sub>Structure</sub>

The placement of a search field in a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SearchFieldPlacement
```

## Overview

You can give a preferred placement to any of the searchable modifiers, like [searchable(text:placement:prompt:)](<view/searchable(text_placement_prompt_).md>):

```swift
var body: some View {
    NavigationView {
        PrimaryView()
        SecondaryView()
        Text("Select a primary and secondary item")
    }
    .searchable(text: $text, placement: .sidebar)
}
```

Depending on the containing view hierachy, SwiftUI might not be able to fulfill your request.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting a search field placement

- [automatic](searchfieldplacement/automatic.md) — SwiftUI places the search field automatically.
- [navigationBarDrawer](searchfieldplacement/navigationbardrawer.md) — The search field appears in the navigation bar.
- [navigationBarDrawer(displayMode:)](<searchfieldplacement/navigationbardrawer(displaymode_).md>) — The search field appears in the navigation bar using the specified display mode.
- [sidebar](searchfieldplacement/sidebar.md) — The search field appears in the sidebar of a navigation view.
- [toolbar](searchfieldplacement/toolbar.md) — The search field appears in the toolbar.

### Supporting types

- [NavigationBarDrawerDisplayMode](searchfieldplacement/navigationbardrawerdisplaymode.md) — A mode that determines when to display a search field that appears in a navigation bar.

### Type Properties

- [toolbarPrincipal](searchfieldplacement/toolbarprincipal.md) — The search field appears in the principal section of the toolbar.

## See Also

### Searching your app’s data model

- [Adding a search interface to your app](adding-a-search-interface-to-your-app.md) — Present an interface that people can use to search for content in your app.
- [Performing a search operation](performing-a-search-operation.md) — Update search results based on search text and optional tokens that you store.
- [searchable(text:placement:prompt:)](<view/searchable(text_placement_prompt_).md>) — Marks this view as searchable, which configures the display of a search field.
- [searchable(text:tokens:placement:prompt:token:)](<view/searchable(text_tokens_placement_prompt_token_).md>) — Marks this view as searchable with text and tokens.
- [searchable(text:editableTokens:placement:prompt:token:)](<view/searchable(text_editabletokens_placement_prompt_token_).md>) — Marks this view as searchable, which configures the display of a search field.
