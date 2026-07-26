---
title: findInteraction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/findinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/findinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/findinteraction.json'
content_hash: 'sha256:74127f468dcb7b6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# findInteraction

<sub>Instance Property</sub>

The text view’s built-in find interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var findInteraction: UIFindInteraction? { get }
```

## Discussion

Set [findInteractionEnabled](isfindinteractionenabled.md) to `true` to enable the text view’s built-in find interaction. This method returns `nil` when the interaction isn’t enabled.

Call [- presentFindNavigatorShowingReplace:](<../uifindinteraction/presentfindnavigator(showingreplace_).md>) on the [UIFindInteraction](../uifindinteraction.md) object returned by this method to invoke the find interaction and display the find panel.

## See Also

### Supporting Find and Replace

- [findInteractionEnabled](isfindinteractionenabled.md) — A Boolean value that enables a text view’s built-in find interaction.
