---
title: contentDisallowedByProfile
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [tvOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avkiterror-swift.struct/contentdisallowedbyprofile
source_url: 'https://developer.apple.com/documentation/avkit/avkiterror-swift.struct/contentdisallowedbyprofile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avkiterror-swift.struct/contentdisallowedbyprofile.json'
content_hash: 'sha256:c8ce7b21d530869b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVKitError](../avkiterror-swift.struct.md)

# contentDisallowedByProfile

<sub>Type Property</sub>

An installed profile restricts access to this content.

<sub>tvOS</sub>

```swift
static var contentDisallowedByProfile: AVKitError.Code { get }
```

## Discussion

The user can’t override this restriction by entering the passcode, but they may be able to override it in the Settings app.

## See Also

### Error Code Constants

- [unknown](unknown.md) — An unknown error.
- [contentRatingUnknown](contentratingunknown.md) — The media content rating is missing or unrecognized.
- [contentDisallowedByPasscode](contentdisallowedbypasscode.md) — A restriction disallows access to this content, but the user can override the restriction by entering the device passcode.
- [pictureInPictureStartFailed](pictureinpicturestartfailed.md) — The system failed to start Picture in Picture.
