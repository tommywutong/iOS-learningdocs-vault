---
title: UIDocumentPickerMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uidocumentpickermode
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickermode.json'
content_hash: 'sha256:8926f8661b232acd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocumentPickerMode

<sub>Enumeration</sub>

Modes that define the type of file transfer operation that the document picker uses.

> [!warning] Deprecated
> Use [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) initializers instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIDocumentPickerMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIDocumentPickerModeImport](uidocumentpickermode/import.md) — The document picker imports a file from outside the app’s sandbox. _(deprecated)_
- [UIDocumentPickerModeOpen](uidocumentpickermode/open.md) — The document picker opens an external file outside the app’s sandbox. _(deprecated)_
- [UIDocumentPickerModeExportToService](uidocumentpickermode/exporttoservice.md) — The document picker exports a local file to a destination outside the app’s sandbox. _(deprecated)_
- [UIDocumentPickerModeMoveToService](uidocumentpickermode/movetoservice.md) — The document picker moves a local file outside the app’s sandbox and provides access to it as an external file. _(deprecated)_

### Initializers

- [init(rawValue:)](<uidocumentpickermode/init(rawvalue_).md>) _(deprecated)_

## See Also

### Configuring a document picker

- [shouldShowFileExtensions](uidocumentpickerviewcontroller/shouldshowfileextensions.md) — A Boolean value that determines whether the browser always shows file extensions.
- [documentPickerMode](uidocumentpickerviewcontroller/documentpickermode.md) — The type of file transfer operation that the document picker uses. _(deprecated)_
