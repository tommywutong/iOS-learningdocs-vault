---
title: AVKitError.Code
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avkiterror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/avkit/avkiterror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avkiterror-swift.struct/code.json'
content_hash: 'sha256:f52952ead0e9d98d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVKitError](../avkiterror-swift.struct.md)

# AVKitError.Code

<sub>Enumeration</sub>

Constants that identify framework error codes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating an error code

- [init(rawValue:)](<code/init(rawvalue_).md>)

### Error Codes

- [AVKitErrorUnknown](code/unknown.md) — An unknown error.
- [AVKitErrorContentRatingUnknown](code/contentratingunknown.md) — The media content rating is missing or unrecognized.
- [AVKitErrorContentDisallowedByPasscode](code/contentdisallowedbypasscode.md) — A restriction disallows access to this content, but the user can override the restriction by entering the device passcode.
- [AVKitErrorPictureInPictureStartFailed](code/pictureinpicturestartfailed.md) — The system failed to start Picture in Picture.
- [AVKitErrorContentDisallowedByProfile](code/contentdisallowedbyprofile.md) — An installed profile restricts access to this content.

## See Also

### Errors

- [AVKitErrorDomain](../avkiterrordomain.md) — The domain of errors the framework generates.
- [AVKitError](../avkiterror-swift.struct.md) — A structure that represents a framework error.
