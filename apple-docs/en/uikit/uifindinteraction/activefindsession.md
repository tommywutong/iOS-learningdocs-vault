---
title: activeFindSession
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifindinteraction/activefindsession
source_url: 'https://developer.apple.com/documentation/uikit/uifindinteraction/activefindsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindinteraction/activefindsession.json'
content_hash: 'sha256:e68e3d5e0b01204f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindInteraction](../uifindinteraction.md)

# activeFindSession

<sub>Instance Property</sub>

The object that manages the state, presentation, and behavior of an active search.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var activeFindSession: UIFindSession? { get }
```

## Discussion

This property returns the session object managing the details of the search. When no seach is active, [findNavigatorVisible](isfindnavigatorvisible.md) is `false`, this returns `nil`.

## See Also

### Managing the search

- [- updateResultCount](<updateresultcount().md>) — Updates the results the interface displays for the active search.
