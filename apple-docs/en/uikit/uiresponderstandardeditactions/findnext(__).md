---
title: 'findNext(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponderstandardeditactions/findnext(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/findnext(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponderstandardeditactions/findnext%28_%3A%29.json'
content_hash: 'sha256:ff311e88f95e39d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponderStandardEditActions](../uiresponderstandardeditactions.md)

# findNext(_:)

<sub>Instance Method</sub>

Finds the next match in your app’s interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func findNext(_ sender: Any?)
```

## Parameters

- `sender` — The object calling this method.

## Discussion

UIKit calls this method when the user selects the Find Next command from an editing menu. Your implementation should highlight the next result in the UI for finding textual content in your view.

For example, a view using a find interaction might call [- highlightNextResultInDirection:](<../uifindsession/highlightnextresult(in_).md>) to update the find session.

## See Also

### Handling find and replace commands

- [- find:](<find(__).md>) — Begins a search for content in your app’s interface.
- [- findPrevious:](<findprevious(__).md>) — Finds the previous match in your app’s interface.
- [- findAndReplace:](<findandreplace(__).md>) — Begins a search for content in your app’s interface and provides a replacement.
- [- useSelectionForFind:](<useselectionforfind(__).md>) — Begins a search for the selected content in your app’s interface.
