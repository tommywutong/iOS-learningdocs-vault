---
title: 'continuityDevicePicker(isPresented:onDidConnect:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 17.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/continuitydevicepicker(ispresented:ondidconnect:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/continuitydevicepicker(ispresented:ondidconnect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/continuitydevicepicker%28ispresented%3Aondidconnect%3A%29.json'
content_hash: 'sha256:f6613bf0d5ac653d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# continuityDevicePicker(isPresented:onDidConnect:)

<sub>Instance Method</sub>

A `continuityDevicePicker` should be used to discover and connect nearby continuity device through a button interface or other form of activation. On tvOS, this presents a fullscreen continuity device picker experience when selected. The modal view covers as much the screen of `self` as possible when a given condition is true.

<sub>tvOS</sub>

```swift
@MainActor @preconcurrency func continuityDevicePicker(isPresented: Binding<Bool>, onDidConnect: ((AVContinuityDevice?) -> Void)? = nil) -> some View

```

## Parameters

- `isPresented` — A `Binding` to whether the modal view is presented.

- `onDidConnect` — A closure executed when the picker successfully, connects AVContinuityDevice or nil if cancelled by a user.

## See Also

### Displaying media

- [CameraView](../../homekit/cameraview.md) — A SwiftUI view into which a video stream or an image snapshot is rendered.
- [NowPlayingView](../../watchkit/nowplayingview.md) — A view that displays the system’s Now Playing interface so that the user can control audio.
- [VideoPlayer](../../avkit/videoplayer.md) — A view that displays content from a player and a native user interface to control playback.
- [cameraAnchor(isActive:)](<cameraanchor(isactive_).md>) — Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.
- [foveatedStreamingPauseSheet(session:)](<foveatedstreamingpausesheet(session_).md>) — Tells the system to present a sheet with controls for resuming or ending the foveated streaming session when it pauses.
