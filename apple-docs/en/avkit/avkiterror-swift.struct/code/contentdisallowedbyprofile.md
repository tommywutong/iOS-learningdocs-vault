---
title: AVKitError.Code.contentDisallowedByProfile
framework: AVKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [tvOS 13.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avkiterror-swift.struct/code/contentdisallowedbyprofile
source_url: 'https://developer.apple.com/documentation/avkit/avkiterror-swift.struct/code/contentdisallowedbyprofile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avkiterror-swift.struct/code/contentdisallowedbyprofile.json'
content_hash: 'sha256:55f6448e06b84660'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVKitError](../../avkiterror-swift.struct.md) · [Code](../code.md)

# AVKitError.Code.contentDisallowedByProfile

<sub>Case</sub>

An installed profile restricts access to this content.

<sub>tvOS</sub>

```swift
case contentDisallowedByProfile
```

## Discussion

The user can’t override this restriction by entering the device passcode, but they may be able to override it in the Settings app.

## See Also

### Error Codes

- [AVKitErrorUnknown](unknown.md) — An unknown error.
- [AVKitErrorContentRatingUnknown](contentratingunknown.md) — The media content rating is missing or unrecognized.
- [AVKitErrorContentDisallowedByPasscode](contentdisallowedbypasscode.md) — A restriction disallows access to this content, but the user can override the restriction by entering the device passcode.
- [AVKitErrorPictureInPictureStartFailed](pictureinpicturestartfailed.md) — The system failed to start Picture in Picture.
