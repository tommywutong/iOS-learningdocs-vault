---
title: recommendedMediaTimeScaleForAssetWriter
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideodataoutput/recommendedmediatimescaleforassetwriter
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/recommendedmediatimescaleforassetwriter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/recommendedmediatimescaleforassetwriter.json'
content_hash: 'sha256:68ec290a15783e17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# recommendedMediaTimeScaleForAssetWriter

<sub>Instance Property</sub>

Indicates the recommended media timescale for the video track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var recommendedMediaTimeScaleForAssetWriter: CMTimeScale { get }
```

## Return Value

The recommended media timescale based on the active capture session’s inputs. It is never less than 600. It may or may not be a multiple of 600.

## See Also

### Configuring video capture

- [videoSettings](videosettings.md) — A dictionary that contains the compression settings for the output.
- [Video settings](../video-settings.md) — Configure video processing settings using standard key and value constants.
- [alwaysDiscardsLateVideoFrames](alwaysdiscardslatevideoframes.md) — Indicates whether to drop video frames if they arrive late.
- [automaticallyConfiguresOutputBufferDimensions](automaticallyconfiguresoutputbufferdimensions.md) — A Boolean value that indicates whether the output automatically configures the size of output buffers.
- [deliversPreviewSizedOutputBuffers](deliverspreviewsizedoutputbuffers.md) — A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.
- [preparesCellularRadioForNetworkConnection](preparescellularradiofornetworkconnection.md) — Indicates whether the receiver should prepare the cellular radio for imminent network activity.
- [preservesDynamicHDRMetadata](preservesdynamichdrmetadata.md) — Indicates whether the receiver should preserve dynamic HDR metadata as an attachment on the output sample buffer’s underlying pixel buffer.
- [- recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:](<recommendedmoviemetadata(forvideocodectype_assetwriteroutputfiletype_).md>) — Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_).md>) — Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [- recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:outputFileURL:](<recommendedvideosettings(forvideocodectype_assetwriteroutputfiletype_outputfileurl_).md>) — Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [- recommendedVideoSettingsForAssetWriterWithOutputFileType:](<recommendedvideosettingsforassetwriter(writingto_).md>) — Specifies the recommended settings for use with an AVAssetWriterInput.
