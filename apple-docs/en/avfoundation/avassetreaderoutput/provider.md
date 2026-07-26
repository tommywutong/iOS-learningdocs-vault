---
title: AVAssetReaderOutput.Provider
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreaderoutput/provider
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/provider.json'
content_hash: 'sha256:385ad0aa93426d8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutput](../avassetreaderoutput.md)

# AVAssetReaderOutput.Provider

<sub>Class</sub>

An object that reads a collection of samples of a common media type from an asset reader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class Provider<Payload> where Payload : AVAssetReaderOutput.SupportedPayload
```

## Topics

### Reading media data

- [captionsNotPresentInPreviousGroups(in:)](<provider/captionsnotpresentinpreviousgroups(in_).md>) — Returns the set of captions that are present in the given group but were not present in any group previously vended by calls to next().
- [next()](<provider/next().md>) — Returns the next piece of media data.

## See Also

### Copying sample buffers

- [- copyNextSampleBuffer](<copynextsamplebuffer().md>) — Copies the next sample buffer from the output. _(deprecated)_
- [RandomAccessController](randomaccesscontroller.md) — Object used to reset an output provider to read specified time ranges.
- [SupportedPayload](supportedpayload.md)
