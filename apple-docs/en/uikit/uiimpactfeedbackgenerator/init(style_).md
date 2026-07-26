---
title: 'init(style:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiimpactfeedbackgenerator/init(style:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/init(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimpactfeedbackgenerator/init%28style%3A%29.json'
content_hash: 'sha256:29b5814936691466'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImpactFeedbackGenerator](../uiimpactfeedbackgenerator.md)

# init(style:)

<sub>Initializer</sub>

Creates an impact feedback generator with the specified style.

> [!warning] Deprecated
> Use [+ feedbackGeneratorWithStyle:forView:](<init(style_view_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(style: UIImpactFeedbackGenerator.FeedbackStyle)
```

## Parameters

- `style` — A value representing the mass of the colliding objects. For a list of valid feedback styles, see the [FeedbackStyle](feedbackstyle.md) enumeration.

## Return Value

A newly initialized feedback generator.

## Discussion

For more information on using feedback generators, see `Using feedback generators`.
