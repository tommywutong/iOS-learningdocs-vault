---
title: next()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreaderoutput/provider/next()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/provider/next%28%29.json'
content_hash: 'sha256:f9ad70f81750dc4d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetReaderOutput](../../avassetreaderoutput.md) · [Provider](../provider.md)

# next()

<sub>Instance Method</sub>

Returns the next piece of media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated(nonsending) func next() async throws -> Payload?
```

## Return Value

Returns the next piece of media data with the specified Payload type. If no more media data is available, this method returns nil.

## Discussion

> [!danger] Throws
> If the underlying reader encountered an error.

## See Also

### Reading media data

- [captionsNotPresentInPreviousGroups(in:)](<captionsnotpresentinpreviousgroups(in_).md>) — Returns the set of captions that are present in the given group but were not present in any group previously vended by calls to next().
