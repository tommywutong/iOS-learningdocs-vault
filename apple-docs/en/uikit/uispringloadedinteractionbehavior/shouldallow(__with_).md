---
title: 'shouldAllow(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uispringloadedinteractionbehavior/shouldallow(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteractionbehavior/shouldallow(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteractionbehavior/shouldallow%28_%3Awith%3A%29.json'
content_hash: 'sha256:531d80a8bf3aaa07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISpringLoadedInteractionBehavior](../uispringloadedinteractionbehavior.md)

# shouldAllow(_:with:)

<sub>Instance Method</sub>

Returns a Boolean value that determines whether spring-loaded interaction should begin or should continue for the specified context.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func shouldAllow(_ interaction: UISpringLoadedInteraction, with context: any UISpringLoadedInteractionContext) -> Bool
```

## Parameters

- `interaction` — The spring-loaded interaction requesting the information.

- `context` — An object that provides information about the current drag operation.

## Return Value

[true](../../swift/true.md) if the spring-loaded interaction should begin or continue; otherwise, [false](../../swift/false.md).
