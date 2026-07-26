---
title: UIScene.OpenURLOptions
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/openurloptions
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/openurloptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/openurloptions.json'
content_hash: 'sha256:07e4a1fc832fc722'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# UIScene.OpenURLOptions

<sub>Class</sub>

Options that UIKit provides when asking your app to open a URL.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class OpenURLOptions
```

## Overview

Don’t create a [OpenURLOptions](openurloptions.md) object directly. UIKit creates one for you when your app receives a request to open a URL. Use the information in the object to determine how to respond to the URL.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Specifying the URL details

- [sourceApplication](openurloptions/sourceapplication.md) — The bundle ID of the app that originated the request.
- [annotation](openurloptions/annotation.md) — A property-list object that contains the annotation data provided by a document interaction controller.
- [eventAttribution](openurloptions/eventattribution.md) — An event attribution associated with the URL to open.

### Specifying the behavior options

- [openInPlace](openurloptions/openinplace.md) — A Boolean value that indicates whether you should open the URL at its current location instead of copying it to your app’s container.

## See Also

### Getting the URL

- [URL](../uiopenurlcontext/url.md) — The URL to open.
- [options](../uiopenurlcontext/options.md) — Additional information for determining how to open the URL.
