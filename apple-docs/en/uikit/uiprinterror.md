---
title: UIPrintError
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterror
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterror.json'
content_hash: 'sha256:ccc86e527212c472'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPrintError

<sub>Structure</sub>

A structure that contains information about a printing error.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct UIPrintError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing error codes

- [Code](uiprinterror/code.md) — Constants that specify the print error code.
- [notAvailable](uiprinterror/notavailable.md) — The device doesn’t support printing.
- [noContent](uiprinterror/nocontent.md) — UIKit hasn’t assigned a print formatter, page renderer, or printing item to print.
- [unknownImageFormat](uiprinterror/unknownimageformat.md) — An image is in a format that UIKit doesn’t recognize for printing.
- [jobFailed](uiprinterror/jobfailed.md) — An internal error occurred with the print job.

### Getting error information

- [errorDomain](uiprinterror/errordomain.md) — The printing error domain.

## See Also

### Handling printing errors

- [UIPrintErrorDomain](uiprinterrordomain.md) — The string constant that defines the UIKit printing error domain.
- [Code](uiprinterror/code.md) — Constants that specify the print error code.
