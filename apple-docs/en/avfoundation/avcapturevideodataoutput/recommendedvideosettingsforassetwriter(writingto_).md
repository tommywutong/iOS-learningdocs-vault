---
title: 'recommendedVideoSettingsForAssetWriter(writingTo:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/recommendedvideosettingsforassetwriter%28writingto%3A%29.json'
content_hash: 'sha256:2f1b0e646d857e82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# recommendedVideoSettingsForAssetWriter(writingTo:)

<sub>Instance Method</sub>

Specifies the recommended settings for use with an AVAssetWriterInput.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func recommendedVideoSettingsForAssetWriter(writingTo outputFileType: AVFileType) -> [String : Any]?
```

## Parameters

- `outputFileType` — The Uniform Type Identifier of the file type to write. See `File Format UTIs` for supported types.

## Return Value

A fully populated dictionary of keys and values that are compatible with [AVAssetWriter](../avassetwriter.md).

## Discussion

This dictionary contains keys and values described in [Video settings](../video-settings.md) and is suitable for use when creating an [AVAssetWriterInput](../avassetwriterinput.md) with the [- initWithMediaType:outputSettings:](<../avassetwriterinput/init(mediatype_outputsettings_).md>) initializer. For QuickTime movie and ISO file types, the recommended video settings produce output comparable to that of [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md).

Note that the dictionary of settings is dependent on the current configuration of the output’s [AVCaptureSession](../avcapturesession.md) and its inputs. The settings dictionary may change if the session’s configuration changes. As such, configure your session first, then query the recommended video settings.

> [!note] Note
> This method returns appropriate settings based on the device’s default video recording codec, but that default can differ between devices. Use the [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_).md>) method to obtain video settings appropriate for a specific codec.

## See Also

### Configuring video capture

- [videoSettings](videosettings.md) — A dictionary that contains the compression settings for the output.
- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
- [alwaysDiscardsLateVideoFrames](alwaysdiscardslatevideoframes.md) — Indicates whether to drop video frames if they arrive late.
- [automaticallyConfiguresOutputBufferDimensions](automaticallyconfiguresoutputbufferdimensions.md) — A Boolean value that indicates whether the output automatically configures the size of output buffers.
- [deliversPreviewSizedOutputBuffers](deliverspreviewsizedoutputbuffers.md) — A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.
- [preparesCellularRadioForNetworkConnection](preparescellularradiofornetworkconnection.md) — Indicates whether the receiver should prepare the cellular radio for imminent network activity.
- [preservesDynamicHDRMetadata](preservesdynamichdrmetadata.md) — Indicates whether the receiver should preserve dynamic HDR metadata as an attachment on the output sample buffer’s underlying pixel buffer.
- [recommendedMediaTimeScaleForAssetWriter](recommendedmediatimescaleforassetwriter.md) — Indicates the recommended media timescale for the video track.
- [- recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:](<recommendedmoviemetadata(forvideocodectype_assetwriteroutputfiletype_).md>) — Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_).md>) — Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:outputFileURL:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_outputfileurl_).md>) — Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
