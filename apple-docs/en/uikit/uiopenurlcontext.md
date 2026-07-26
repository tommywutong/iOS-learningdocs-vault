---
title: UIOpenURLContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiopenurlcontext
source_url: 'https://developer.apple.com/documentation/uikit/uiopenurlcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiopenurlcontext.json'
content_hash: 'sha256:9dd98d1714d978af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIOpenURLContext

<sub>Class</sub>

A system-provided object that contains the information you need to open a single URL.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIOpenURLContext
```

## Overview

UIKit provides a [UIOpenURLContext](uiopenurlcontext.md) object when your app receives a URL to open, such as in your implementation of [- scene:openURLContexts:](<uiscenedelegate/scene(__openurlcontexts_).md>). The object contains the URL itself and any options needed to handle the URL correctly. Don’t create [UIOpenURLContext](uiopenurlcontext.md) objects yourself.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the URL

- [URL](uiopenurlcontext/url.md) — The URL to open.
- [options](uiopenurlcontext/options.md) — Additional information for determining how to open the URL.
- [OpenURLOptions](uiscene/openurloptions.md) — Options that UIKit provides when asking your app to open a URL.

## See Also

### URL management

- [OpenExternalURLOptions](uiscene/openexternalurloptions.md) — Options you specify when asking a scene to open a URL.
