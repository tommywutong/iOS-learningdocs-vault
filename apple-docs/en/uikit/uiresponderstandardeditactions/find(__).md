---
title: 'find(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponderstandardeditactions/find(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/find(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponderstandardeditactions/find%28_%3A%29.json'
content_hash: 'sha256:b265f17bef087c9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponderStandardEditActions](../uiresponderstandardeditactions.md)

# find(_:)

<sub>Instance Method</sub>

Begins a search for content in your app’s interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func find(_ sender: Any?)
```

## Parameters

- `sender` — The object calling this method.

## Discussion

UIKit calls this method when the user selects the Find command from an editing menu. Your implementation should present the UI for finding textual content in your view.

For example, a view using a find interaction might call [- presentFindNavigatorShowingReplace:](<../uifindinteraction/presentfindnavigator(showingreplace_).md>) to present the system find panel.

## See Also

### Handling find and replace commands

- [- findNext:](<findnext(__).md>) — Finds the next match in your app’s interface.
- [- findPrevious:](<findprevious(__).md>) — Finds the previous match in your app’s interface.
- [- findAndReplace:](<findandreplace(__).md>) — Begins a search for content in your app’s interface and provides a replacement.
- [- useSelectionForFind:](<useselectionforfind(__).md>) — Begins a search for the selected content in your app’s interface.
