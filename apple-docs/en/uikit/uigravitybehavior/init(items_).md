---
title: 'init(items:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigravitybehavior/init(items:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigravitybehavior/init(items:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigravitybehavior/init%28items%3A%29.json'
content_hash: 'sha256:561dac31e09d7ac2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGravityBehavior](../uigravitybehavior.md)

# init(items:)

<sub>Initializer</sub>

Initializes a gravity behavior with an array of dynamic items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(items: [any UIDynamicItem])
```

## Parameters

- `items` — The dynamic items that you want to be subject to the gravity behavior.

## Return Value

The initialized gravity behavior, or `nil` if there was a problem initializing the object.
