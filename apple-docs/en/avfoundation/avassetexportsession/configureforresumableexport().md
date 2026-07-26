---
title: configureForResumableExport()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/configureforresumableexport()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/configureforresumableexport()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/configureforresumableexport%28%29.json'
content_hash: 'sha256:fcb24a6f7dab7197'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# configureForResumableExport()

<sub>Instance Method</sub>

Configures the export session for resumable export.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func configureForResumableExport() async -> AVAssetExportSession.ResumptionState
```

## Return Value

A `ResumptionState` indicating whether resumption is available and whether the export will resume from a previous state.

## Discussion

This method validates that the export session’s current configuration supports resumption and checks the temporary directory for any partial results from previous export attempts.

Call this method after configuring all export settings (preset, output file type, etc.) and before calling `exportAsynchronously()`.

> [!note] Note
> Even if resumption is not available, you can still perform a normal (non-resumable) export by calling `exportAsynchronously()`.

Example usage:

```swift
let exportSession = AVAssetExportSession(asset: asset, presetName: .hevc1920x1080)!
exportSession.outputFileType = .mov
exportSession.outputURL = outputURL
exportSession.directoryForTemporaryFiles = temporaryDirectory

let state = await exportSession.configureForResumableExport()
switch state {
case .resumable(let isResuming):
    print("Export is resumable. Continuing from previous state: \(isResuming)")
case .notResumable(let reason):
    print("Cannot perform resumable export with current configuration: \(reason)")
}

try await exportSession.export(to: outputURL, as: .mov)
```

## See Also

### Configuring resumable export

- [ResumptionState](resumptionstate.md) — Represents the resumption state of the export session.
- [ResumptionFailureReason](resumptionfailurereason.md) — An enum that identifies various reasons why resumable export configuration has failed. _(beta)_
