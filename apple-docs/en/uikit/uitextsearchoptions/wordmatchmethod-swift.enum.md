---
title: UITextSearchOptions.WordMatchMethod
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchoptions/wordmatchmethod-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchoptions/wordmatchmethod-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchoptions/wordmatchmethod-swift.enum.json'
content_hash: 'sha256:ab66df6706104921'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchOptions](../uitextsearchoptions.md)

# UITextSearchOptions.WordMatchMethod

<sub>Enumeration</sub>

Constants that describe the method to use when searching text for words that match a string.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum WordMatchMethod
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITextSearchMatchMethodContains](wordmatchmethod-swift.enum/contains.md) — The word contains the search string.
- [UITextSearchMatchMethodStartsWith](wordmatchmethod-swift.enum/startswith.md) — The word contains the search string as a prefix.
- [UITextSearchMatchMethodFullWord](wordmatchmethod-swift.enum/fullword.md) — The word matches the search string exactly.

### Initializers

- [init(rawValue:)](<wordmatchmethod-swift.enum/init(rawvalue_).md>)

## See Also

### Find and replace

- [UIFindInteraction](../uifindinteraction.md) — An interaction that provides text finding and replacing operations using a system find panel.
- [UIFindInteractionDelegate](../uifindinteractiondelegate.md) — A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [UIFindSession](../uifindsession.md) — An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [UITextSearchingFindSession](../uitextsearchingfindsession.md) — A find session object that wraps a searchable object implementing the text-searching protocol.
- [UITextSearching](../uitextsearching-3wkjv.md) — The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [UITextSearchOptions](../uitextsearchoptions.md) — An object containing the configurable options for a text search.
- [UITextSearchFoundTextStyle](../uitextsearchfoundtextstyle.md) — Constants that describe the style a find session uses to decorate the text.
- [SearchResultDisplayStyle](../uifindsession/searchresultdisplaystyle-swift.enum.md) — Constants that describe the results summary the find panel UI includes.
