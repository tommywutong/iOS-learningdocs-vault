---
title: AVCaptionGrouper
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptiongrouper
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptiongrouper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptiongrouper.json'
content_hash: 'sha256:1b87f3595d1bbd85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionGrouper

<sub>Class</sub>

An object that analyzes the temporal overlaps of caption objects to create caption groups for each span of concurrent captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVCaptionGrouper
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Adding captions

- [- addCaption:](<avcaptiongrouper/add(__).md>) — Adds a caption to the pending group.

### Generating captions groups

- [- flushAddedCaptionsIntoGroupsUpToTime:](<avcaptiongrouper/flushaddedcaptions(upto_).md>) — Creates caption groups for the captions you enqueue up to the time.

## See Also

### Groups

- [AVCaptionGroup](avcaptiongroup.md) — An object that represents zero or more captions that intersect in time.
