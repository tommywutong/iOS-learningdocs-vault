---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifindinteraction/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uifindinteraction/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindinteraction/delegate.json'
content_hash: 'sha256:4b1e1a04bccd2bb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindInteraction](../uifindinteraction.md)

# delegate

<sub>Instance Property</sub>

An object that updates your app’s presentation and provides the session object for managing the interaction’s search.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIFindInteractionDelegate)? { get }
```

## See Also

### Managing find interactions

- [- presentFindNavigatorShowingReplace:](<presentfindnavigator(showingreplace_).md>) — Begins a search, displaying the find panel.
- [- dismissFindNavigator](<dismissfindnavigator().md>) — Dismisses the find panel, if present.
- [- findNext](<findnext().md>) — Highlights the next found result in the content, relative to the currently highlighted result.
- [- findPrevious](<findprevious().md>) — Highlights the previously found result in the document, relative to the currently highlighted result.
