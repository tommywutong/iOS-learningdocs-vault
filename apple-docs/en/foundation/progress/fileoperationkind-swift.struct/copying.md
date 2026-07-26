---
title: copying
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/progress/fileoperationkind-swift.struct/copying
source_url: 'https://developer.apple.com/documentation/foundation/progress/fileoperationkind-swift.struct/copying'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/fileoperationkind-swift.struct/copying.json'
content_hash: 'sha256:fe2295a09f33c8fc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Progress](../../progress.md) · [FileOperationKind](../fileoperationkind-swift.struct.md)

# copying

<sub>Type Property</sub>

The progress is tracking the copying of a file from source to destination.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let copying: Progress.FileOperationKind
```

## See Also

### Recognizing Kinds of File Operations

- [NSProgressFileOperationKindDecompressingAfterDownloading](decompressingafterdownloading.md) — The progress is tracking file decompression after a download.
- [NSProgressFileOperationKindDownloading](downloading.md) — The progress is tracking a file download operation.
- [NSProgressFileOperationKindUploading](uploading.md) — The progress is tracking a file upload operation.
- [NSProgressFileOperationKindReceiving](receiving.md) — The progress is tracking the receipt of a file from another source.
