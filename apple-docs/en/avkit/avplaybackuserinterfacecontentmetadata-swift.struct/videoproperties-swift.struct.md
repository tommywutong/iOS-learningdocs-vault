---
title: AVPlaybackUserInterfaceContentMetadata.VideoProperties
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.struct
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacecontentmetadata-swift.struct/videoproperties-swift.struct.json'
content_hash: 'sha256:2cd8800753a7dc42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceContentMetadata](../avplaybackuserinterfacecontentmetadata-swift.struct.md)

# AVPlaybackUserInterfaceContentMetadata.VideoProperties

<sub>Structure</sub>

Properties specific to video content.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct VideoProperties
```

## Overview

The presence of a `VideoProperties` instance indicates the content contains video. Use [VideoProperties](videoproperties-swift.struct.md) to provide the natural presentation size for video content.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(presentationSize:)](<videoproperties-swift.struct/init(presentationsize_).md>) — Creates a new video properties instance. _(beta)_

### Instance Properties

- [presentationSize](videoproperties-swift.struct/presentationsize.md) — The natural pixel dimensions of the video content, used for aspect ratio calculations and layout. _(beta)_
