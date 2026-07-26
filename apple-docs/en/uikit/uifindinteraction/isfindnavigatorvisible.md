---
title: isFindNavigatorVisible
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifindinteraction/isfindnavigatorvisible
source_url: 'https://developer.apple.com/documentation/uikit/uifindinteraction/isfindnavigatorvisible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindinteraction/isfindnavigatorvisible.json'
content_hash: 'sha256:df52a40b1cec1a64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindInteraction](../uifindinteraction.md)

# isFindNavigatorVisible

<sub>Instance Property</sub>

A Boolean value that indicates when the find panel displays onscreen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isFindNavigatorVisible: Bool { get }
```

## Discussion

The value of this property is `YES` when the find panel displays; otherwise, `NO`.

## See Also

### Configuring the find panel

- [searchText](searchtext.md) — The search query with which to prepopulate the find panel’s search text field.
- [replacementText](replacementtext.md) — The replacement string with which to prepopulate the find panel’s replace text field.
- [optionsMenuProvider](optionsmenuprovider.md) — A closure that populates the search options for a find interaction.
