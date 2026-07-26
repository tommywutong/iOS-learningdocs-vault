---
title: permanently
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgconfigureoption/permanently
source_url: 'https://developer.apple.com/documentation/coregraphics/cgconfigureoption/permanently'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgconfigureoption/permanently.json'
content_hash: 'sha256:90da03ecaeb66ad7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGConfigureOption](../cgconfigureoption.md)

# permanently

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var permanently: CGConfigureOption { get }
```

## Discussion

Changes persist in future login sessions by the same user. If the requested changes cannot be supported by the Aqua UI (resolution and pixel depth constraints apply), the settings for the current login session are used instead, and any changes have session scope.

## See Also

### Type Properties

- [kCGConfigureForAppOnly](forapponly.md) — Changes persist for the lifetime of the current application. After the application terminates, the display configuration settings revert to the current login session.
- [kCGConfigureForSession](forsession.md) — Changes persist for the lifetime of the current login session. After the current session terminates, the displays revert to the last saved permanent configuration.
