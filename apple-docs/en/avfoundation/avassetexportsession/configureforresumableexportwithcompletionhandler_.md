---
title: 'configureForResumableExportWithCompletionHandler:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/configureforresumableexportwithcompletionhandler:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/configureforresumableexportwithcompletionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/configureforresumableexportwithcompletionhandler%3A.json'
content_hash: 'sha256:7626cedcf7187571'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# configureForResumableExportWithCompletionHandler:

<sub>Instance Method</sub>

Attempt to configure the exportSession into resumption mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) configureForResumableExportWithCompletionHandler:(void (^)(AVAssetExportSessionResumptionState *resumptionState)) completionHandler;
```

## Discussion

For select encoders, an export can be performed in temporal segments, and then stitched together at the end.

The client is responsible for configuring the export session identically for subsequent sessions, if the export is to be resumed from partial results from a previous run.

IMPORTANT: directoryForTemporaryFiles MUST be specified for resumable exports. This directory holds the temporary files for resumable exports which allows the export to resume on a subsequent instantiation. The client is responsible for making the directoryForTemporaryFiles unique and deterministic across app launches or device reboots if the session is intended to be resumable after such events. The client must ensure that it does not re-use a temporary directory corresponding to a different resumable export session, or the contents between different exports may be erroneously combined.

This method validates that the currently configured export properties allow resumption, and interrogates the contents of directoryForTemporaryFiles to determine if this is a resuming session or a new one. As such, this should be called after all settings are finalized for this export session, i.e. just prior to exportAsynchronouslyWithCompletionHandler.

resumptionState details the currently configured resumption state of the export session. Even if resumptionState indicates not all conditions for resumption are met, a client may still call exportAsynchronouslyWithCompletionHandler using the current session, and the export will be performed in the default (non-resuming) manner.

This method cannot be called after the export has started.

cancelExport may be called if an in-flight export needs to be interrupted. The partial results will be maintained.

The client is responsible for deleting the temporary directory if the export will never be resumed in the future.

Since intermediate files are written to support the resume functionality, resumable exports will typically double the NAND accesses, since the samples need to be written to disk twice.

## See Also

### Configuring resumable export

- [AVAssetExportSessionResumptionState](../avassetexportsessionresumptionstate.md) — AVAssetExportSessionResumptionState details the current resumption state of the export session. A resumable export session is configured via configureForResumableExportWithCompletionHandler:. _(beta)_
- [ResumptionFailureReason](resumptionfailurereason.md) — An enum that identifies various reasons why resumable export configuration has failed. _(beta)_
