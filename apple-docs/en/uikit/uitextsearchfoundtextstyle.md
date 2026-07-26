---
title: UITextSearchFoundTextStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchfoundtextstyle
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchfoundtextstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchfoundtextstyle.json'
content_hash: 'sha256:d4b5b964d94d1952'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSearchFoundTextStyle

<sub>Enumeration</sub>

Constants that describe the style a find session uses to decorate the text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UITextSearchFoundTextStyle
```

## Overview

Use [UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md) to identify ranges of text your app decorates to indicate matches, highlighted matches and non-matching text.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UITextSearchFoundTextStyleNormal](uitextsearchfoundtextstyle/normal.md) — A style that indicates the text isn’t a match.
- [UITextSearchFoundTextStyleFound](uitextsearchfoundtextstyle/found.md) — A style that indicates the text is a match, but not highlighted.
- [UITextSearchFoundTextStyleHighlighted](uitextsearchfoundtextstyle/highlighted.md) — A style that indicates the text is a highlighted match.

### Initializers

- [init(rawValue:)](<uitextsearchfoundtextstyle/init(rawvalue_).md>)

## See Also

### Find and replace

- [UIFindInteraction](uifindinteraction.md) — An interaction that provides text finding and replacing operations using a system find panel.
- [UIFindInteractionDelegate](uifindinteractiondelegate.md) — A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [UIFindSession](uifindsession.md) — An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [UITextSearchingFindSession](uitextsearchingfindsession.md) — A find session object that wraps a searchable object implementing the text-searching protocol.
- [UITextSearching](uitextsearching-3wkjv.md) — The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [UITextSearchOptions](uitextsearchoptions.md) — An object containing the configurable options for a text search.
- [WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md) — Constants that describe the method to use when searching text for words that match a string.
- [SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md) — Constants that describe the results summary the find panel UI includes.
