---
title: fileURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/fileurl
source_url: 'https://developer.apple.com/documentation/foundation/progress/fileurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/fileurl.json'
content_hash: 'sha256:b5d45f314368668e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# fileURL

<sub>Instance Property</sub>

A URL that represents the file for the current progress object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileURL: URL? { get set }
```

## Discussion

Set this value for a progress that you [- publish](<publish().md>) to subscribers that register for updates using [+ addSubscriberForFileURL:withPublishingHandler:](<addsubscriber(forfileurl_withpublishinghandler_).md>).

If present, [Progress](../progress.md) presents additional information in its localized description by setting a value in the `userInfo` dictionary.

## See Also

### Inspecting File Operation Progress Information

- [fileOperationKind](fileoperationkind-swift.property.md) — The kind of file operation for the progress object.
- [fileTotalCount](filetotalcount.md) — The total number of files for a file progress object.
- [fileCompletedCount](filecompletedcount.md) — The number of completed files for a file progress object.
- [FileOperationKind](fileoperationkind-swift.struct.md) — The kind of file operation.
