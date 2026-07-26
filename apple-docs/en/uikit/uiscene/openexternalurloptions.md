---
title: UIScene.OpenExternalURLOptions
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/openexternalurloptions
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/openexternalurloptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/openexternalurloptions.json'
content_hash: 'sha256:4d231689d8301a88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# UIScene.OpenExternalURLOptions

<sub>Class</sub>

Options you specify when asking a scene to open a URL.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class OpenExternalURLOptions
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Specifying the link options

- [universalLinksOnly](openexternalurloptions/universallinksonly.md) — A Boolean value that indicates whether URLs must be universal links and have a configured app to open them.

### Measuring ad taps

- [eventAttribution](openexternalurloptions/eventattribution.md) — An object you use to send tap event attribution data to the browser for Private Click Measurement.

## See Also

### URL management

- [UIOpenURLContext](../uiopenurlcontext.md) — A system-provided object that contains the information you need to open a single URL.
