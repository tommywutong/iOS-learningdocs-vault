---
title: fileOperationKind
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/fileoperationkind-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/progress/fileoperationkind-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/fileoperationkind-swift.property.json'
content_hash: 'sha256:009a7bb17d20b16b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# fileOperationKind

<sub>Instance Property</sub>

The kind of file operation for the progress object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileOperationKind: Progress.FileOperationKind? { get set }
```

## Discussion

Set this value when the [kind](kind.md) property is [NSProgressKindFile](../progresskind/file.md) to describe the kind of file operation.

If present, [Progress](../progress.md) presents additional information in its localized description by setting a value in the `userInfo` dictionary.

## See Also

### Inspecting File Operation Progress Information

- [fileURL](fileurl.md) — A URL that represents the file for the current progress object.
- [fileTotalCount](filetotalcount.md) — The total number of files for a file progress object.
- [fileCompletedCount](filecompletedcount.md) — The number of completed files for a file progress object.
- [FileOperationKind](fileoperationkind-swift.struct.md) — The kind of file operation.
