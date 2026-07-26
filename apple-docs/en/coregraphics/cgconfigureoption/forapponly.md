---
title: forAppOnly
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgconfigureoption/forapponly
source_url: 'https://developer.apple.com/documentation/coregraphics/cgconfigureoption/forapponly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgconfigureoption/forapponly.json'
content_hash: 'sha256:579612d2f5e98848'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGConfigureOption](../cgconfigureoption.md)

# forAppOnly

<sub>Type Property</sub>

Changes persist for the lifetime of the current application. After the application terminates, the display configuration settings revert to the current login session.

<sub>Mac Catalyst, macOS</sub>

```swift
static var forAppOnly: CGConfigureOption { get }
```

## See Also

### Type Properties

- [kCGConfigureForSession](forsession.md) — Changes persist for the lifetime of the current login session. After the current session terminates, the displays revert to the last saved permanent configuration.
- [kCGConfigurePermanently](permanently.md)
