---
title: Search
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/search
source_url: 'https://developer.apple.com/documentation/swiftui/search'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/search.json'
content_hash: 'sha256:6784212488fcb51b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Search

<sub>API Collection</sub>

Enable people to search for text or other content within your app.

## Overview

To present a search field in your app, create and manage storage for search text and optionally for discrete search terms known as _tokens_. Then bind the storage to the search field by applying the searchable view modifier to a view in your app.

![](../../../attachments/366a90bfb4ab3aea60848d447e01a437/search-hero@2x.png)

As people interact with the field, they implicitly modify the underlying storage and, thereby, the search parameters. Your app correspondingly updates other parts of its interface. To enhance the search interaction, you can also:

- Offer suggestions during search, for both text and tokens.
- Implement search scopes that help people to narrow the search space.
- Detect when people activate the search field, and programmatically dismiss the search field using environment values.

For design guidance, see [Searching](../design/human-interface-guidelines/searching.md) in the Human Interface Guidelines.

## Topics

### Searching your app’s data model

- [Adding a search interface to your app](adding-a-search-interface-to-your-app.md) — Present an interface that people can use to search for content in your app.
- [Performing a search operation](performing-a-search-operation.md) — Update search results based on search text and optional tokens that you store.
- [searchable(text:placement:prompt:)](<view/searchable(text_placement_prompt_).md>) — Marks this view as searchable, which configures the display of a search field.
- [searchable(text:tokens:placement:prompt:token:)](<view/searchable(text_tokens_placement_prompt_token_).md>) — Marks this view as searchable with text and tokens.
- [searchable(text:editableTokens:placement:prompt:token:)](<view/searchable(text_editabletokens_placement_prompt_token_).md>) — Marks this view as searchable, which configures the display of a search field.
- [SearchFieldPlacement](searchfieldplacement.md) — The placement of a search field in a view hierarchy.

### Making search suggestions

- [Suggesting search terms](suggesting-search-terms.md) — Provide suggestions to people searching for content in your app.
- [searchSuggestions(_:)](<view/searchsuggestions(__).md>) — Configures the search suggestions for this view.
- [searchSuggestions(_:for:)](<view/searchsuggestions(__for_).md>) — Configures how to display search suggestions within this view.
- [searchCompletion(_:)](<view/searchcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a search suggestion.
- [searchable(text:tokens:suggestedTokens:placement:prompt:token:)](<view/searchable(text_tokens_suggestedtokens_placement_prompt_token_).md>) — Marks this view as searchable with text, tokens, and suggestions.
- [SearchSuggestionsPlacement](searchsuggestionsplacement.md) — The ways that SwiftUI displays search suggestions.

### Limiting search scope

- [Scoping a search operation](scoping-a-search-operation.md) — Divide the search space into a few broad categories.
- [searchScopes(_:scopes:)](<view/searchscopes(__scopes_).md>) — Configures the search scopes for this view.
- [searchScopes(_:activation:_:)](<view/searchscopes(__activation___).md>) — Configures the search scopes for this view with the specified activation strategy.
- [SearchScopeActivation](searchscopeactivation.md) — The ways that searchable modifiers can show or hide search scopes.

### Detecting, activating, and dismissing search

- [Managing search interface activation](managing-search-interface-activation.md) — Programmatically detect and dismiss a search field.
- [isSearching](environmentvalues/issearching.md) — A Boolean value that indicates when the user is searching.
- [dismissSearch](environmentvalues/dismisssearch.md) — An action that ends the current search interaction.
- [DismissSearchAction](dismisssearchaction.md) — An action that can end a search interaction.
- [searchable(text:isPresented:placement:prompt:)](<view/searchable(text_ispresented_placement_prompt_).md>) — Marks this view as searchable with programmatic presentation of the search field.
- [searchable(text:tokens:isPresented:placement:prompt:token:)](<view/searchable(text_tokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [searchable(text:editableTokens:isPresented:placement:prompt:token:)](<view/searchable(text_editabletokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable, which configures the display of a search field.
- [searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](<view/searchable(text_tokens_suggestedtokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.

### Displaying toolbar content during search

- [searchPresentationToolbarBehavior(_:)](<view/searchpresentationtoolbarbehavior(__).md>) — Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [SearchPresentationToolbarBehavior](searchpresentationtoolbarbehavior.md) — A type that defines how the toolbar behaves when presenting search.

### Searching for text in a view

- [findNavigator(isPresented:)](<view/findnavigator(ispresented_).md>) — Programmatically presents the find and replace interface for text editor views.
- [findDisabled(_:)](<view/finddisabled(__).md>) — Prevents find and replace operations in a text editor.
- [replaceDisabled(_:)](<view/replacedisabled(__).md>) — Prevents replace operations in a text editor.
- [FindContext](findcontext.md) — The status of the find navigator for views which support text editing.

## See Also

### App structure

- [App organization](app-organization.md) — Define the entry point and top-level structure of your app.
- [Scenes](scenes.md) — Declare the user interface groupings that make up the parts of your app.
- [Windows](windows.md) — Display user interface content in a window or a collection of windows.
- [Immersive spaces](immersive-spaces.md) — Display unbounded content in a person’s surroundings.
- [Documents](documents.md) — Enable people to open and manage documents.
- [Navigation](navigation.md) — Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](modal-presentations.md) — Present content in a separate view that offers focused interaction.
- [Toolbars](toolbars.md) — Provide immediate access to frequently used commands and controls.
- [App extensions](app-extensions.md) — Extend your app’s basic functionality to other parts of the system, like by adding a Widget.
