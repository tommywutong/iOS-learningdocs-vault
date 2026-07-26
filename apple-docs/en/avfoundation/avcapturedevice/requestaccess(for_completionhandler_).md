---
title: 'requestAccess(for:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/requestaccess(for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/requestaccess(for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/requestaccess%28for%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:c9e3b7a8066e1ce6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# requestAccess(for:completionHandler:)

<sub>Type Method</sub>

Requests the user’s permission to allow the app to capture media of a particular type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func requestAccess(for mediaType: AVMediaType, completionHandler handler: @escaping @Sendable (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func requestAccess(for mediaType: AVMediaType) async -> Bool
```

## Parameters

- `mediaType` — A media type for which to check the authorization status. The supported media types are [AVMediaTypeVideo](../avmediatype/video.md) and [AVMediaTypeAudio](../avmediatype/audio.md).

- `handler` — A callback the system invokes with a Boolean value that indicates whether the user granted or denied access to your app. Return control to the main queue or [MainActor](../../swift/mainactor.md) before performing user interface updates.

## Discussion

Capturing media requires explicit permission from the user. An app’s default authorization status is [AVAuthorizationStatusNotDetermined](../avauthorizationstatus/notdetermined.md), which means the user hasn’t yet granted it permission to capture media. The first time you create an [AVCaptureDeviceInput](../avcapturedeviceinput.md) object for a media type that requires permission, the system automatically displays an alert to request recording permission. Alternatively, call this method to prompt the user at a time of your choosing. The system saves the user’s selection so that it doesn’t have to prompt the user again. A user can change their authorization status in the Settings app.

> [!important] Important
> Your app must provide an explanation for its use of capture devices using the [NSCameraUsageDescription](../../bundleresources/information-property-list/nscamerausagedescription.md) and [NSMicrophoneUsageDescription](../../bundleresources/information-property-list/nsmicrophoneusagedescription.md) Info.plist keys. The system presents the strings you set for these keys when prompting the user for permission, and thereafter in the Settings app. Calling this method or attempting to start a capture session without a usage description raises an exception.

Calling this method doesn’t block the thread while the system is prompting the user for access. However, until the grants permission, the system only vends black video frames and silent audio samples.

> [!note] Note
> Calling this method with a media type of [AVMediaTypeAudio](../avmediatype/audio.md) is equivalent to calling the [requestRecordPermission(_:)](<../../avfaudio/avaudiosession/requestrecordpermission(__).md>) method on [AVAudioSession](../../avfaudio/avaudiosession.md).

## See Also

### Authorizing device access

- [+ authorizationStatusForMediaType:](<authorizationstatus(for_).md>) — Returns an authorization status that indicates whether the user grants the app permission to capture media of a particular type.
- [AVAuthorizationStatus](../avauthorizationstatus.md) — Constants that indicate the status of an app’s authorization to capture media.
