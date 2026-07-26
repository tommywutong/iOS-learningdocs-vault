---
title: AVAssetExportSession
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession.json'
content_hash: 'sha256:d92c4190546c49b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetExportSession

<sub>Class</sub>

An object that exports assets in a format that you specify using an export preset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetExportSession
```

## Overview

You configure this object to export an instance of [AVAsset](avasset.md) by setting an export preset, an output file type, and an output URL.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an export session

- [- initWithAsset:presetName:](<avassetexportsession/init(asset_presetname_).md>) — Creates an export session with a preset configuration.
- [Export presets](export-presets.md) — Configure an export session to output media in standard sizes and formats.

### Accessing export presets

- [presetName](avassetexportsession/presetname.md) — The name of the preset that the asset export session uses.
- [- determineCompatibleFileTypesWithCompletionHandler:](<avassetexportsession/determinecompatiblefiletypes(completionhandler_).md>) — Determines the output file types an asset export session supports writing in its current configuration.
- [+ allExportPresets](<avassetexportsession/allexportpresets().md>) — Returns all available export preset names.
- [+ determineCompatibilityOfExportPreset:withAsset:outputFileType:completionHandler:](<avassetexportsession/determinecompatibility(ofexportpreset_with_outputfiletype_completionhandler_).md>) — Determines an export preset’s compatibility to export the asset in a container of the output file type.

### Configuring output

- [supportedFileTypes](avassetexportsession/supportedfiletypes.md) — An array containing the types of files the session can write.
- [allowsParallelizedExport](avassetexportsession/allowsparallelizedexport.md) — A Boolean value that indicates whether the session can parallelize its export operation.
- [shouldOptimizeForNetworkUse](avassetexportsession/shouldoptimizefornetworkuse.md) — A Boolean value that indicates whether to optimize the movie for network use.
- [canPerformMultiplePassesOverSourceMediaData](avassetexportsession/canperformmultiplepassesoversourcemediadata.md) — A Boolean value that indicates whether the export session can perform multiple passes over the source media to achieve better results.
- [timeRange](avassetexportsession/timerange.md) — The time range of the source asset to export.
- [fileLengthLimit](avassetexportsession/filelengthlimit.md) — The file length that the output of the session must not exceed.
- [directoryForTemporaryFiles](avassetexportsession/directoryfortemporaryfiles.md) — A directory suitable to store temporary files that the export process generates.

### Configuring metadata

- [metadata](avassetexportsession/metadata.md) — The metadata an export session writes to the output container file.
- [metadataItemFilter](avassetexportsession/metadataitemfilter.md) — An object the export session uses to filter the metadata items it transfers to the output asset.

### Configuring video output

- [videoComposition](avassetexportsession/videocomposition.md) — An optional object that provides instructions for how to composite frames of video.
- [customVideoCompositor](avassetexportsession/customvideocompositor.md) — An optional custom object to use when compositing video frames.

### Configuring track groups

- [audioTrackGroupHandling](avassetexportsession/audiotrackgrouphandling.md) — A policy that defines how the session exports alternate audio tracks.
- [AVAssetTrackGroupOutputHandling](avassettrackgroupoutputhandling.md) — A type that specifies policies for how an export session processes alternate tracks in a track group.

### Configuring audio output

- [audioMix](avassetexportsession/audiomix.md) — The parameters for audio mixing and an indication of whether to enable nondefault audio mixing for export.
- [audioTimePitchAlgorithm](avassetexportsession/audiotimepitchalgorithm.md) — A processing algorithm for managing audio pitch for scaled audio edits.

### Exporting media

- [export(to:as:isolation:)](<avassetexportsession/export(to_as_isolation_).md>) — Exports the asset to the output location in the specified file type.

### Monitoring export progress

- [states(updateInterval:)](<avassetexportsession/states(updateinterval_).md>) — Monitors the progress state of an export operation.
- [State](avassetexportsession/state.md) — Constants that indicate the state of an export operation.
- [Status](avassetexportsession/status-swift.enum.md) — Values that indicate the state of an export session.

### Estimating file length and duration

- [- estimateOutputFileLengthWithCompletionHandler:](<avassetexportsession/estimateoutputfilelength(completionhandler_).md>) — Starts estimating the output file length of the export while considering the asset, preset, and time range configuration of the export session.

### Estimating duration

- [- estimateMaximumDurationWithCompletionHandler:](<avassetexportsession/estimatemaximumduration(completionhandler_).md>) — Starts estimating the maximum duration of the export while considering the asset, preset, and time range configuration of the export session.

### Accessing the asset

- [asset](avassetexportsession/asset.md) — An asset that a session exports.

### Configuring resumable export

- [configureForResumableExport()](<avassetexportsession/configureforresumableexport().md>) — Configures the export session for resumable export.
- [ResumptionState](avassetexportsession/resumptionstate.md) — Represents the resumption state of the export session.
- [ResumptionFailureReason](avassetexportsession/resumptionfailurereason.md) — An enum that identifies various reasons why resumable export configuration has failed. _(beta)_

### Deprecated

- [Deprecated symbols](avassetexportsession-deprecated-symbols.md) — Review unsupported symbols and their replacements.

## See Also

### Media export

- [Exporting video to alternative formats](exporting-video-to-alternative-formats.md) — Convert an existing movie file to a different format.
