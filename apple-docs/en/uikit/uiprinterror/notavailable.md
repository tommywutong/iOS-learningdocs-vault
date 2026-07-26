---
title: notAvailable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterror/notavailable
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterror/notavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterror/notavailable.json'
content_hash: 'sha256:6b35d1eb9f49b636'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintError](../uiprinterror.md)

# notAvailable

<sub>Type Property</sub>

The device doesn’t support printing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var notAvailable: UIPrintError.Code { get }
```

## See Also

### Accessing error codes

- [Code](code.md) — Constants that specify the print error code.
- [noContent](nocontent.md) — UIKit hasn’t assigned a print formatter, page renderer, or printing item to print.
- [unknownImageFormat](unknownimageformat.md) — An image is in a format that UIKit doesn’t recognize for printing.
- [jobFailed](jobfailed.md) — An internal error occurred with the print job.
