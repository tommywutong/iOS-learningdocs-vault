---
title: UITextSearchingFindSession
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchingfindsession
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchingfindsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchingfindsession.json'
content_hash: 'sha256:65275cdf91451cf3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSearchingFindSession

<sub>Class</sub>

A find session object that wraps a searchable object implementing the text-searching protocol.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITextSearchingFindSession
```

## Overview

Implement the [UITextSearching](uitextsearching-53wjq.md) protocol on the class that encapsulates the searchable content for your view to use an instance of [UITextSearchingFindSession](uitextsearchingfindsession.md) as the session object. Alternatively, you can subclass [UIFindSession](uifindsession.md) to manage the details of the session using a custom class.

The find session’s reference to [searchableObject](uitextsearchingfindsession/searchableobject.md) is weakly held to avoid a retain cycle if the view you install the interaction on is the searchable object itself. Ensure that your app maintains a strong reference to the searchable object.

## Relationships

- **Inherits From**: [UIFindSession](uifindsession.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a text searching find session

- [- initWithSearchableObject:](<uitextsearchingfindsession/init(searchableobject_)-9zc4e.md>) — Initializes an object to manage the search for the searchable object you specify.
- [init(searchableObject:)](<uitextsearchingfindsession/init(searchableobject_)-7swl5.md>) — Initializes an object to manage the search for the searchable object you specify.

### Getting the searchable object

- [searchableObject](uitextsearchingfindsession/searchableobject.md) — The object to search, responsible for performing the search operation and decorating the results.

## See Also

### Find and replace

- [UIFindInteraction](uifindinteraction.md) — An interaction that provides text finding and replacing operations using a system find panel.
- [UIFindInteractionDelegate](uifindinteractiondelegate.md) — A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [UIFindSession](uifindsession.md) — An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [UITextSearching](uitextsearching-3wkjv.md) — The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [UITextSearchOptions](uitextsearchoptions.md) — An object containing the configurable options for a text search.
- [UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md) — Constants that describe the style a find session uses to decorate the text.
- [WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md) — Constants that describe the method to use when searching text for words that match a string.
- [SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md) — Constants that describe the results summary the find panel UI includes.
