---
title: process()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.1+（27.0 起废弃）, iPadOS 26.1+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phbackgroundresourceuploadextension/process()
source_url: 'https://developer.apple.com/documentation/photos/phbackgroundresourceuploadextension/process()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phbackgroundresourceuploadextension/process%28%29.json'
content_hash: 'sha256:85bac4a25efe4e68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHBackgroundResourceUploadExtension](../phbackgroundresourceuploadextension.md)

# process()

<sub>Instance Method</sub>

Request to initiate processing background upload jobs.

> [!warning] Deprecated
> Adopt PHBackgroundResourceUploadJobExtension instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func process() -> PHBackgroundResourceUploadProcessingResult
```

## Return Value

A result type of [PHBackgroundResourceUploadProcessingResult](../phbackgroundresourceuploadprocessingresult.md) based on the state of the processing task.

## See Also

### Processing upload requests

- [PHBackgroundResourceUploadProcessingResult](../phbackgroundresourceuploadprocessingresult.md)
