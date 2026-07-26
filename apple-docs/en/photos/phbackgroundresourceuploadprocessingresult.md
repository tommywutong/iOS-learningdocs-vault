---
title: PHBackgroundResourceUploadProcessingResult
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phbackgroundresourceuploadprocessingresult
source_url: 'https://developer.apple.com/documentation/photos/phbackgroundresourceuploadprocessingresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phbackgroundresourceuploadprocessingresult.json'
content_hash: 'sha256:c598eb6defa515f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHBackgroundResourceUploadProcessingResult

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum PHBackgroundResourceUploadProcessingResult
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md)

## Topics

### Processing results

- [PHBackgroundResourceUploadProcessingResult.completed](phbackgroundresourceuploadprocessingresult/completed.md) — the extension has completed all processing required and is up to date with the photos library
- [PHBackgroundResourceUploadProcessingResult.failure](phbackgroundresourceuploadprocessingresult/failure.md) — the extension failed the processing task with an error
- [PHBackgroundResourceUploadProcessingResult.processing](phbackgroundresourceuploadprocessingresult/processing.md) — the extension has only partially completed its processing and still requires more time

## See Also

### Processing upload requests

- [process()](<phbackgroundresourceuploadextension/process().md>) — Request to initiate processing background upload jobs. _(deprecated)_
