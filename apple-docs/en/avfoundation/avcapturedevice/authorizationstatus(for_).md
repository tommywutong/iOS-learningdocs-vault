---
title: 'authorizationStatus(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/authorizationstatus(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/authorizationstatus(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/authorizationstatus%28for%3A%29.json'
content_hash: 'sha256:39636662677beaa5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# authorizationStatus(for:)

<sub>Type Method</sub>

Returns an authorization status that indicates whether the user grants the app permission to capture media of a particular type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func authorizationStatus(for mediaType: AVMediaType) -> AVAuthorizationStatus
```

## Parameters

- `mediaType` — A media type for which to check the authorization status. The supported media types are [AVMediaTypeVideo](../avmediatype/video.md) and [AVMediaTypeAudio](../avmediatype/audio.md).

## Return Value

An authorization status value.

## Discussion

A user must explicitly grant your app access to record audio or video. Call this method to determine your app’s current authorization status. If it returns a value of [AVAuthorizationStatusNotDetermined](../avauthorizationstatus/notdetermined.md), call [+ requestAccessForMediaType:completionHandler:](<requestaccess(for_completionhandler_).md>) to prompt the user for capture permission.

After the user grants permission, the system remembers their choice and doesn’t prompt them again. However, a user can change their choice at any time in the Settings app.

> [!note] Note
> If a user has denied your app recording permission, or hasn’t yet responded to the permission prompt, audio recordings contain only silence and video recordings contain only black frames.

## See Also

### Authorizing device access

- [+ requestAccessForMediaType:completionHandler:](<requestaccess(for_completionhandler_).md>) — Requests the user’s permission to allow the app to capture media of a particular type.
- [AVAuthorizationStatus](../avauthorizationstatus.md) — Constants that indicate the status of an app’s authorization to capture media.
