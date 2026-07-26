---
title: 'foveatedStreamingPauseSheet(session:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.4+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/foveatedstreamingpausesheet(session:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/foveatedstreamingpausesheet(session:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/foveatedstreamingpausesheet%28session%3A%29.json'
content_hash: 'sha256:e8526078b4e78dcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# foveatedStreamingPauseSheet(session:)

<sub>Instance Method</sub>

Tells the system to present a sheet with controls for resuming or ending the foveated streaming session when it pauses.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency func foveatedStreamingPauseSheet(session: Binding<FoveatedStreamingSession?>) -> some View

```

## Parameters

- `session` — A binding to the foveated streaming session to display the pause sheet for. If `nil`, the system never displays the pause sheet.

## Discussion

Add this view modifier to inform the system that it should display UI for resuming the foveated streaming session when the person pauses the session. Otherwise, build your own UI that allows the person to resume the session by calling the `FoveatedStreamingSession/resume()` function.

## See Also

### Displaying media

- [CameraView](../../homekit/cameraview.md) — A SwiftUI view into which a video stream or an image snapshot is rendered.
- [NowPlayingView](../../watchkit/nowplayingview.md) — A view that displays the system’s Now Playing interface so that the user can control audio.
- [VideoPlayer](../../avkit/videoplayer.md) — A view that displays content from a player and a native user interface to control playback.
- [continuityDevicePicker(isPresented:onDidConnect:)](<continuitydevicepicker(ispresented_ondidconnect_).md>) — A `continuityDevicePicker` should be used to discover and connect nearby continuity device through a button interface or other form of activation. On tvOS, this presents a fullscreen continuity device picker experience when selected. The modal view covers as much the screen of `self` as possible when a given condition is true.
- [cameraAnchor(isActive:)](<cameraanchor(isactive_).md>) — Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.
