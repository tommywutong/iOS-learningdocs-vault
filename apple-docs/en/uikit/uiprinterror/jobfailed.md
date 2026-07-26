---
title: jobFailed
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterror/jobfailed
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterror/jobfailed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterror/jobfailed.json'
content_hash: 'sha256:19c7c32eaeeffc30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintError](../uiprinterror.md)

# jobFailed

<sub>Type Property</sub>

An internal error occurred with the print job.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var jobFailed: UIPrintError.Code { get }
```

## See Also

### Accessing error codes

- [Code](code.md) — Constants that specify the print error code.
- [notAvailable](notavailable.md) — The device doesn’t support printing.
- [noContent](nocontent.md) — UIKit hasn’t assigned a print formatter, page renderer, or printing item to print.
- [unknownImageFormat](unknownimageformat.md) — An image is in a format that UIKit doesn’t recognize for printing.
