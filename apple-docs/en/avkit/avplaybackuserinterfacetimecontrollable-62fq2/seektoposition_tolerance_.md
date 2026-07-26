---
title: 'seekToPosition:tolerance:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/seektoposition:tolerance:'
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/seektoposition:tolerance:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/seektoposition%3Atolerance%3A.json'
content_hash: 'sha256:64c4abd54a8b7b50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceTimeControllable](../avplaybackuserinterfacetimecontrollable-62fq2.md)

# seekToPosition:tolerance:

<sub>Instance Method</sub>

Requests a seek to the specified position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
- (void) seekToPosition:(CMTime) position tolerance:(CMTime) tolerance;
```

## Parameters

- `position` — The position to seek to.

- `tolerance` — How close to `position` the actual seek must land. Pass `kCMTimeZero` for exact frame-accurate seeking or `kCMTimePositiveInfinity` for fast approximate seeking.
