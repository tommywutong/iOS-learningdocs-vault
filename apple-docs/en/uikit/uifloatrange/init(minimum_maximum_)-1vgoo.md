---
title: 'init(minimum:maximum:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifloatrange/init(minimum:maximum:)-1vgoo'
source_url: 'https://developer.apple.com/documentation/uikit/uifloatrange/init(minimum:maximum:)-1vgoo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifloatrange/init%28minimum%3Amaximum%3A%29-1vgoo.json'
content_hash: 'sha256:ae4f74697c822401'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFloatRange](../uifloatrange.md)

# init(minimum:maximum:)

<sub>Initializer</sub>

Returns a new float range structure from the given components.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(minimum: CGFloat, maximum: CGFloat)
```

## Parameters

- `minimum` — The minimum range value, which is typically less than or equal to `0`.

- `maximum` — The maximum range value, which is typically greater than or equal to `0`.

## Discussion

Float ranges are used in [UIAttachmentBehavior](../uiattachmentbehavior.md) objects to define the maximum range of translation or rotation for animations.
