---
title: forSession
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgconfigureoption/forsession
source_url: 'https://developer.apple.com/documentation/coregraphics/cgconfigureoption/forsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgconfigureoption/forsession.json'
content_hash: 'sha256:a16d7dbce7899d6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGConfigureOption](../cgconfigureoption.md)

# forSession

<sub>Type Property</sub>

Changes persist for the lifetime of the current login session. After the current session terminates, the displays revert to the last saved permanent configuration.

<sub>Mac Catalyst, macOS</sub>

```swift
static var forSession: CGConfigureOption { get }
```

## See Also

### Type Properties

- [kCGConfigureForAppOnly](forapponly.md) — Changes persist for the lifetime of the current application. After the application terminates, the display configuration settings revert to the current login session.
- [kCGConfigurePermanently](permanently.md)
