---
title: 'export(to:as:isolation:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/export(to:as:isolation:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/export(to:as:isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/export%28to%3Aas%3Aisolation%3A%29.json'
content_hash: 'sha256:a476fa67a8d28456'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# export(to:as:isolation:)

<sub>Instance Method</sub>

Exports the asset to the output location in the specified file type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@backDeployed(before: macOS 26.0, iOS 26.0, tvOS 26.0, visionOS 26.0)
final func export(to url: URL, as fileType: AVFileType, isolation: isolated (any Actor)? = #isolation) async throws
```

## Parameters

- `url` — An output location to write the exported media. You can use the [preferredFilenameExtension](../../uniformtypeidentifiers/uttype-swift.struct/preferredfilenameextension.md) property of [UTType](../../uniformtypeidentifiers/uttype-swift.struct.md) to determine an appropriate file extension for the specified file type.

- `fileType` — The type of file for the session to write.

- `isolation` — The isolation context.

## Discussion

This method throws an error if you cancel the export or you specify a file type value that isn’t contained in the session’s [supportedFileTypes](supportedfiletypes.md).

You can monitor the status of an export by calling the [states(updateInterval:)](<states(updateinterval_).md>) method.

> [!note] Note
> You can cancel an in-progress export by calling [cancel()](<../../swift/task/cancel().md>) on the [Task](../../swift/task.md) or parent task that initiated the operation.
