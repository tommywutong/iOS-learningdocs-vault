---
title: processJobs()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phbackgroundresourceuploadjobextension/processjobs()
source_url: 'https://developer.apple.com/documentation/photos/phbackgroundresourceuploadjobextension/processjobs()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phbackgroundresourceuploadjobextension/processjobs%28%29.json'
content_hash: 'sha256:a1d9fe3445a4aea4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHBackgroundResourceUploadJobExtension](../phbackgroundresourceuploadjobextension.md)

# processJobs()

<sub>Instance Method</sub>

Request to initiate processing background upload jobs.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func processJobs() async -> PHBackgroundResourceUploadProcessingResult
```

## Return Value

A result type of [PHBackgroundResourceUploadProcessingResult](../phbackgroundresourceuploadprocessingresult.md) based on the state of the processing task.
