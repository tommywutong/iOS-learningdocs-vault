---
title: silentOnTouch
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/directtouchoptions/silentontouch
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/directtouchoptions/silentontouch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/directtouchoptions/silentontouch.json'
content_hash: 'sha256:2cd613ad0186ae0d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIAccessibility](../../uiaccessibility.md) · [DirectTouchOptions](../directtouchoptions.md)

# silentOnTouch

<sub>Type Property</sub>

Allows a direct touch area to immediately receive touch events without triggering VoiceOver audio.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var silentOnTouch: UIAccessibility.DirectTouchOptions { get }
```

## Discussion

You may want a user interface element that, when a person interacts with it, provides audio feedback that would conflict with VoiceOver. In a music creation app, for example, you can designate the keyboard as “silent on touch,” so that VoiceOver doesn’t compete with the keyboard sounds.
