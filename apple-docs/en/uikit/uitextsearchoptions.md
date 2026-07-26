---
title: UITextSearchOptions
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchoptions
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchoptions.json'
content_hash: 'sha256:12f7e51ab1054661'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSearchOptions

<sub>Class</sub>

An object containing the configurable options for a text search.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITextSearchOptions
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Configuring searches

- [stringCompareOptions](uitextsearchoptions/stringcompareoptions.md) — The options to use in comparisons when searching text for matches to a string.
- [wordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.property.md) — The method to use when searching text for matches to words.
- [WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md) — Constants that describe the method to use when searching text for words that match a string.

## See Also

### Find and replace

- [UIFindInteraction](uifindinteraction.md) — An interaction that provides text finding and replacing operations using a system find panel.
- [UIFindInteractionDelegate](uifindinteractiondelegate.md) — A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [UIFindSession](uifindsession.md) — An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [UITextSearchingFindSession](uitextsearchingfindsession.md) — A find session object that wraps a searchable object implementing the text-searching protocol.
- [UITextSearching](uitextsearching-3wkjv.md) — The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md) — Constants that describe the style a find session uses to decorate the text.
- [WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md) — Constants that describe the method to use when searching text for words that match a string.
- [SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md) — Constants that describe the results summary the find panel UI includes.
