---
title: UIFindSession.SearchResultDisplayStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifindsession/searchresultdisplaystyle-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uifindsession/searchresultdisplaystyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindsession/searchresultdisplaystyle-swift.enum.json'
content_hash: 'sha256:25b8a21a1a1dd3fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindSession](../uifindsession.md)

# UIFindSession.SearchResultDisplayStyle

<sub>Enumeration</sub>

Constants that describe the results summary the find panel UI includes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum SearchResultDisplayStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIFindSessionSearchResultDisplayStyleCurrentAndTotal](searchresultdisplaystyle-swift.enum/currentandtotal.md) — The find panel includes the total number of results the session reports and the index of the target result.
- [UIFindSessionSearchResultDisplayStyleTotal](searchresultdisplaystyle-swift.enum/total.md) — The find panel includes the total number of results the session reports.
- [UIFindSessionSearchResultDisplayStyleNone](searchresultdisplaystyle-swift.enum/none.md) — The find panel doesn’t include the number of results the session reports.

### Initializers

- [init(rawValue:)](<searchresultdisplaystyle-swift.enum/init(rawvalue_).md>)

## See Also

### Find and replace

- [UIFindInteraction](../uifindinteraction.md) — An interaction that provides text finding and replacing operations using a system find panel.
- [UIFindInteractionDelegate](../uifindinteractiondelegate.md) — A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [UIFindSession](../uifindsession.md) — An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [UITextSearchingFindSession](../uitextsearchingfindsession.md) — A find session object that wraps a searchable object implementing the text-searching protocol.
- [UITextSearching](../uitextsearching-3wkjv.md) — The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [UITextSearchOptions](../uitextsearchoptions.md) — An object containing the configurable options for a text search.
- [UITextSearchFoundTextStyle](../uitextsearchfoundtextstyle.md) — Constants that describe the style a find session uses to decorate the text.
- [WordMatchMethod](../uitextsearchoptions/wordmatchmethod-swift.enum.md) — Constants that describe the method to use when searching text for words that match a string.
