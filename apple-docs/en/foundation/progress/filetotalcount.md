---
title: fileTotalCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/filetotalcount
source_url: 'https://developer.apple.com/documentation/foundation/progress/filetotalcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/filetotalcount.json'
content_hash: 'sha256:d1db108780ee7855'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# fileTotalCount

<sub>Instance Property</sub>

The total number of files for a file progress object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileTotalCount: Int? { get set }
```

## Discussion

If the current progress is operating on a set of files, set this property to the total number of files in the operation.

If present, [Progress](../progress.md) presents additional information in its localized description by setting a value in the `userInfo` dictionary.

## See Also

### Inspecting File Operation Progress Information

- [fileOperationKind](fileoperationkind-swift.property.md) — The kind of file operation for the progress object.
- [fileURL](fileurl.md) — A URL that represents the file for the current progress object.
- [fileCompletedCount](filecompletedcount.md) — The number of completed files for a file progress object.
- [FileOperationKind](fileoperationkind-swift.struct.md) — The kind of file operation.
