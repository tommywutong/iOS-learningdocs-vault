---
title: fileCompletedCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsprogress/filecompletedcount
source_url: 'https://developer.apple.com/documentation/foundation/nsprogress/filecompletedcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsprogress/filecompletedcount.json'
content_hash: 'sha256:809de1778d35477a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# fileCompletedCount

<sub>Instance Property</sub>

The number of completed files for a file progress object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (copy, nullable) NSNumber * fileCompletedCount;
```

## Discussion

If the current progress is operating on a set of files, set this property to the number of completed files in the operation.

If present, [Progress](../progress.md) presents additional information in its localized description by setting a value in the `userInfo` dictionary.

## See Also

### Inspecting File Operation Progress Information

- [fileOperationKind](../progress/fileoperationkind-swift.property.md) — The kind of file operation for the progress object.
- [fileURL](../progress/fileurl.md) — A URL that represents the file for the current progress object.
- [fileTotalCount](filetotalcount.md) — The total number of files for a file progress object.
- [FileOperationKind](../progress/fileoperationkind-swift.struct.md) — The kind of file operation.
