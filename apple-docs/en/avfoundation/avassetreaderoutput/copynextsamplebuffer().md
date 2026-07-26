---
title: copyNextSampleBuffer()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetreaderoutput/copynextsamplebuffer()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/copynextsamplebuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/copynextsamplebuffer%28%29.json'
content_hash: 'sha256:22a83021b8d25062'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutput](../avassetreaderoutput.md)

# copyNextSampleBuffer()

<sub>Instance Method</sub>

Copies the next sample buffer from the output.

> [!warning] Deprecated
> Use AVAssetReaderOutput.Provider.next() instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copyNextSampleBuffer() -> CMSampleBuffer?
```

## Return Value

The output sample buffer, or `nil` if you’ve read all samples or an error occurs.

## Discussion

This method returns `nil` when you’ve read all available sample buffers, or if there’s an error. Check the value of the asset reader’s [status](../avassetreader/status-swift.property.md) property to determine the reason.

The order of returned sample buffers depends on the output’s configuration. For a track output with a `nil` [outputSettings](../avassetreadertrackoutput/outputsettings.md) dictionary, the output skips decoding and returns sample buffers in decode order. Preserve that order when working with the encoded samples directly, such as when passing them to [AVAssetWriter](../avassetwriter.md). When the output decodes the samples, it returns them in presentation order. Playback and downstream processing operate in presentation order, so decode order no longer matters after decoding.

## See Also

### Copying sample buffers

- [Provider](provider.md) — An object that reads a collection of samples of a common media type from an asset reader.
- [RandomAccessController](randomaccesscontroller.md) — Object used to reset an output provider to read specified time ranges.
- [SupportedPayload](supportedpayload.md)
