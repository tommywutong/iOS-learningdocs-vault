---
title: 'init(url:in:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentpickerviewcontroller/init(url:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(url:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentpickerviewcontroller/init%28url%3Ain%3A%29.json'
content_hash: 'sha256:3441bf812eca04b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentPickerViewController](../uidocumentpickerviewcontroller.md)

# init(url:in:)

<sub>Initializer</sub>

Initializes and returns a document picker that can export or copy the specified document.

> [!warning] Deprecated
> Use [- initForExportingURLs:](<init(forexporting_).md>) or [- initForExportingURLs:asCopy:](<init(forexporting_ascopy_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(url: URL, in mode: UIDocumentPickerMode)
```

## Parameters

- `url` — The document that the document picker exports or moves.

- `mode` — The type of file-transfer operation that the document picker performs. This argument accepts only the [UIDocumentPickerModeExportToService](../uidocumentpickermode/exporttoservice.md) or [UIDocumentPickerModeMoveToService](../uidocumentpickermode/movetoservice.md) mode.

## Return Value

Returns an initialized `UIDocumentPickerViewController` object, or `nil` if the object could not be successfully initialized.

## Discussion

In iOS 10 and earlier, this method returns the document picker view controller from the most recently used Document Provider extension. If no valid Document Provider can be found, it defaults back to iCloud Drive.

In iOS 11 and later, it returns the standard browser interface. This interface is the same one used by the [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md) class.

## See Also

### Deprecated

- [- initWithDocumentTypes:inMode:](<init(documenttypes_in_).md>) — Creates and returns a document picker that can open or copy the specified file types. _(deprecated)_
- [- initWithURLs:inMode:](<init(urls_in_).md>) — Creates and returns a document picker that can export or move the specified documents. _(deprecated)_
