---
title: Search modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-search
source_url: 'https://developer.apple.com/documentation/swiftui/view-search'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-search.json'
content_hash: 'sha256:522a4f51a18a93d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Search modifiers

<sub>API Collection</sub>

Enable people to search for content in your app.

## Overview

Use search view modifiers to add search capability to your app. For more information, see [Search](search.md).

## Topics

### Displaying a search interface

- [searchable(text:placement:prompt:)](<view/searchable(text_placement_prompt_).md>) — Marks this view as searchable, which configures the display of a search field.
- [searchable(text:isPresented:placement:prompt:)](<view/searchable(text_ispresented_placement_prompt_).md>) — Marks this view as searchable with programmatic presentation of the search field.
- [searchPresentationToolbarBehavior(_:)](<view/searchpresentationtoolbarbehavior(__).md>) — Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [searchToolbarBehavior(_:)](<view/searchtoolbarbehavior(__).md>) — Configures the behavior for search in the toolbar.
- [searchSelection(_:)](<view/searchselection(__).md>) — Binds the selection of the search field associated with the nearest searchable modifier to the given [TextSelection](textselection.md) value.

### Searching with tokens

- [searchable(text:tokens:placement:prompt:token:)](<view/searchable(text_tokens_placement_prompt_token_).md>) — Marks this view as searchable with text and tokens.
- [searchable(text:tokens:isPresented:placement:prompt:token:)](<view/searchable(text_tokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable with text and tokens, as well as programmatic presentation.

### Searching with editable tokens

- [searchable(text:editableTokens:isPresented:placement:prompt:token:)](<view/searchable(text_editabletokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable, which configures the display of a search field.
- [searchable(text:editableTokens:placement:prompt:token:)](<view/searchable(text_editabletokens_placement_prompt_token_).md>) — Marks this view as searchable, which configures the display of a search field.

### Making search suggestions

- [searchSuggestions(_:)](<view/searchsuggestions(__).md>) — Configures the search suggestions for this view.
- [searchSuggestions(_:for:)](<view/searchsuggestions(__for_).md>) — Configures how to display search suggestions within this view.
- [searchCompletion(_:)](<view/searchcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a search suggestion.
- [searchable(text:tokens:suggestedTokens:placement:prompt:token:)](<view/searchable(text_tokens_suggestedtokens_placement_prompt_token_).md>) — Marks this view as searchable with text, tokens, and suggestions.
- [searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](<view/searchable(text_tokens_suggestedtokens_ispresented_placement_prompt_token_).md>) — Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.

### Limiting search scope

- [searchScopes(_:scopes:)](<view/searchscopes(__scopes_).md>) — Configures the search scopes for this view.
- [searchScopes(_:activation:_:)](<view/searchscopes(__activation___).md>) — Configures the search scopes for this view with the specified activation strategy.

### Searching through dictation

- [searchDictationBehavior(_:)](<view/searchdictationbehavior(__).md>) — Configures the dictation behavior for any search fields configured by the searchable modifier.

## See Also

### Providing interactivity

- [Input and event modifiers](view-input-and-events.md) — Supply actions for a view to perform in response to user input and system events.
- [Presentation modifiers](view-presentation.md) — Define additional views for the view to present under specified conditions.
- [State modifiers](view-state.md) — Access storage and provide child views with configuration data.
