---
title: multipleScenesNotSupported
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneerror/multiplescenesnotsupported
source_url: 'https://developer.apple.com/documentation/uikit/uisceneerror/multiplescenesnotsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneerror/multiplescenesnotsupported.json'
content_hash: 'sha256:7d9ac399e7b4097e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneError](../uisceneerror.md)

# multipleScenesNotSupported

<sub>Type Property</sub>

An error that indicates multiple scenes aren’t supported.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var multipleScenesNotSupported: UISceneError.Code { get }
```

## Discussion

This error code indicates that the app doesn’t support multiple scenes or the system was unable to display multiple scenes for your app.

## See Also

### Identifying an error cause

- [requestDenied](requestdenied.md) — An error that indicates the request was denied.
- [geometryRequestUnsupported](geometryrequestunsupported.md) — An error that indicates the geometry request is invalid or unsupported.
- [geometryRequestDenied](geometryrequestdenied.md) — An error that indicates the geometry request is valid but the system denied the request.
- [Code](code.md) — Error codes for issues with scenes.
