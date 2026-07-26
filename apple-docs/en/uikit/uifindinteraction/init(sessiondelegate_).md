---
title: 'init(sessionDelegate:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifindinteraction/init(sessiondelegate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifindinteraction/init(sessiondelegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindinteraction/init%28sessiondelegate%3A%29.json'
content_hash: 'sha256:7ff20acaf071aeff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindInteraction](../uifindinteraction.md)

# init(sessionDelegate:)

<sub>Initializer</sub>

Initializes a find interaction object with the delegate object you specify.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(sessionDelegate: any UIFindInteractionDelegate)
```

## Return Value

Returns a find interaction object with the associated delegate.

## Discussion

Create an object that conforms to the [UIFindInteractionDelegate](../uifindinteractiondelegate.md) protocol and assign it to this property.
