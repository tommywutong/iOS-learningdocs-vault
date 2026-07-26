---
title: unusedTrackID()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasset/unusedtrackid()
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/unusedtrackid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/unusedtrackid%28%29.json'
content_hash: 'sha256:3e6b0f0aa8cd1990'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# unusedTrackID()

<sub>Instance Method</sub>

Returns an identifier that no other tracks in the asset use.

> [!warning] Deprecated
> Use [- findUnusedTrackIDWithCompletionHandler:](<findunusedtrackid(completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func unusedTrackID() -> CMPersistentTrackID
```

## Return Value

An unused [CMPersistentTrackID](../../coremedia/cmpersistenttrackid.md) value.
