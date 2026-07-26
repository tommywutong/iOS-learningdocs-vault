---
title: unknownImageFormat
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterror/unknownimageformat
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterror/unknownimageformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterror/unknownimageformat.json'
content_hash: 'sha256:261d979b8a97a94b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintError](../uiprinterror.md)

# unknownImageFormat

<sub>Type Property</sub>

An image is in a format that UIKit doesn’t recognize for printing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var unknownImageFormat: UIPrintError.Code { get }
```

## See Also

### Accessing error codes

- [Code](code.md) — Constants that specify the print error code.
- [notAvailable](notavailable.md) — The device doesn’t support printing.
- [noContent](nocontent.md) — UIKit hasn’t assigned a print formatter, page renderer, or printing item to print.
- [jobFailed](jobfailed.md) — An internal error occurred with the print job.
