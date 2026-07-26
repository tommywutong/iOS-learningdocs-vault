---
title: UIPrintError.Code
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterror/code
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterror/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterror/code.json'
content_hash: 'sha256:fff931e28e9e5cbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintError](../uiprinterror.md)

# UIPrintError.Code

<sub>Enumeration</sub>

Constants that specify the print error code.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error codes

- [UIPrintingNotAvailableError](code/notavailable.md) — The device doesn’t support printing.
- [UIPrintNoContentError](code/nocontent.md) — UIKit hasn’t assigned a print formatter, page renderer, or printing item to print.
- [UIPrintUnknownImageFormatError](code/unknownimageformat.md) — An image is in a format that UIKit doesn’t recognize for printing.
- [UIPrintJobFailedError](code/jobfailed.md) — An internal error occurred with the print job.

### Global variables

- [Print error global variables](../print-error-global-variables.md) — Global variables associated with print errors.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Handling printing errors

- [UIPrintErrorDomain](../uiprinterrordomain.md) — The string constant that defines the UIKit printing error domain.
- [UIPrintError](../uiprinterror.md) — A structure that contains information about a printing error.
