---
title: Progress.FileOperationKind
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/fileoperationkind-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/progress/fileoperationkind-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/fileoperationkind-swift.struct.json'
content_hash: 'sha256:7ed4bdded65ce006'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# Progress.FileOperationKind

<sub>Structure</sub>

The kind of file operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FileOperationKind
```

## Discussion

When tracking file operations with the progress [kind](kind.md) set to [NSProgressKindFile](../progresskind/file.md), provide a value for the [NSProgressFileOperationKindKey](../progressuserinfokey/fileoperationkindkey.md) in the user info dictionary.

To specify the kind of file operation, provide one of the following values:

- [NSProgressFileOperationKindCopying](fileoperationkind-swift.struct/copying.md)
- [NSProgressFileOperationKindDecompressingAfterDownloading](fileoperationkind-swift.struct/decompressingafterdownloading.md)
- [NSProgressFileOperationKindDownloading](fileoperationkind-swift.struct/downloading.md)
- [NSProgressFileOperationKindUploading](fileoperationkind-swift.struct/uploading.md)
- [NSProgressFileOperationKindReceiving](fileoperationkind-swift.struct/receiving.md)

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Kinds of File Operation

- [init(_:)](<fileoperationkind-swift.struct/init(__).md>) — Creates a new kind of file operation using the specified string.
- [init(rawValue:)](<fileoperationkind-swift.struct/init(rawvalue_).md>) — Creates a new kind of file operation using the raw value of a string you specify.

### Recognizing Kinds of File Operations

- [NSProgressFileOperationKindCopying](fileoperationkind-swift.struct/copying.md) — The progress is tracking the copying of a file from source to destination.
- [NSProgressFileOperationKindDecompressingAfterDownloading](fileoperationkind-swift.struct/decompressingafterdownloading.md) — The progress is tracking file decompression after a download.
- [NSProgressFileOperationKindDownloading](fileoperationkind-swift.struct/downloading.md) — The progress is tracking a file download operation.
- [NSProgressFileOperationKindUploading](fileoperationkind-swift.struct/uploading.md) — The progress is tracking a file upload operation.
- [NSProgressFileOperationKindReceiving](fileoperationkind-swift.struct/receiving.md) — The progress is tracking the receipt of a file from another source.

## See Also

### Inspecting File Operation Progress Information

- [fileOperationKind](fileoperationkind-swift.property.md) — The kind of file operation for the progress object.
- [fileURL](fileurl.md) — A URL that represents the file for the current progress object.
- [fileTotalCount](filetotalcount.md) — The total number of files for a file progress object.
- [fileCompletedCount](filecompletedcount.md) — The number of completed files for a file progress object.
