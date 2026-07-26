---
title: UIFindInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifindinteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uifindinteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindinteractiondelegate.json'
content_hash: 'sha256:ebd01855c460d217'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFindInteractionDelegate

<sub>Protocol</sub>

A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIFindInteractionDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UITextView](uitextview.md)

## Topics

### Beginning the search

- [- findInteraction:sessionForView:](<uifindinteractiondelegate/findinteraction(__sessionfor_).md>) — Provides the object for managing the state, presentation, and behavior of the search.

### Decorating the searched content

- [- findInteraction:didBeginFindSession:](<uifindinteractiondelegate/findinteraction(__didbegin_).md>) — Informs the delegate when the interaction is about to present the find panel.
- [- findInteraction:didEndFindSession:](<uifindinteractiondelegate/findinteraction(__didend_).md>) — Informs the delegate when the interaction is about to dismiss the find panel.

## See Also

### Find and replace

- [UIFindInteraction](uifindinteraction.md) — An interaction that provides text finding and replacing operations using a system find panel.
- [UIFindSession](uifindsession.md) — An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [UITextSearchingFindSession](uitextsearchingfindsession.md) — A find session object that wraps a searchable object implementing the text-searching protocol.
- [UITextSearching](uitextsearching-3wkjv.md) — The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [UITextSearchOptions](uitextsearchoptions.md) — An object containing the configurable options for a text search.
- [UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md) — Constants that describe the style a find session uses to decorate the text.
- [WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md) — Constants that describe the method to use when searching text for words that match a string.
- [SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md) — Constants that describe the results summary the find panel UI includes.
