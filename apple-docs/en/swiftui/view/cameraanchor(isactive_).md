---
title: 'cameraAnchor(isActive:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/cameraanchor(isactive:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/cameraanchor(isactive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/cameraanchor%28isactive%3A%29.json'
content_hash: 'sha256:fb824449f50b0675'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# cameraAnchor(isActive:)

<sub>Instance Method</sub>

Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.

<sub>visionOS</sub>

```swift
@MainActor func cameraAnchor(isActive: Bool = true) -> some View

```

## Parameters

- `isActive` — Whether or not the camera anchor is active. You can use this value to ensure that only one camera anchor is active at a time if you want to create multiple views that could act as the anchor in your app.

## Discussion

This modifier can be used by visionOS apps to specify the placement of the virtual camera used to create a 2D stream of the user’s Persona. For example, a video conferencing app might add this modifier to the view that shows the other participants during a call. Then when the participant on visionOS looks at that view their Persona will make eye contact with the other participants on the call. The anchor will be at the center of the modified View.

```swift
ExampleAppVideoView()
    .cameraAnchor()
```

You might want to create multiple views with an anchor and then only activate the one that has focus.

```swift
struct ExampleSelfPreviewWhenFocusedView: View {
   @Environment(\.isFocused) var isFocused: Bool

   var body: some View {
       ExampleAppVideoView()
        #if os(visionOS)
            .cameraAnchor(isActive: isFocused)
        #endif
   }
}
```

> [!important] Important
> You should avoid creating multiple views with simultaneously active camera anchors. If multiple views with active camera anchors are found, the first created will have its parent View be used as the camera anchor, and a runtime error will be emitted.

## See Also

### Displaying media

- [CameraView](../../homekit/cameraview.md) — A SwiftUI view into which a video stream or an image snapshot is rendered.
- [NowPlayingView](../../watchkit/nowplayingview.md) — A view that displays the system’s Now Playing interface so that the user can control audio.
- [VideoPlayer](../../avkit/videoplayer.md) — A view that displays content from a player and a native user interface to control playback.
- [continuityDevicePicker(isPresented:onDidConnect:)](<continuitydevicepicker(ispresented_ondidconnect_).md>) — A `continuityDevicePicker` should be used to discover and connect nearby continuity device through a button interface or other form of activation. On tvOS, this presents a fullscreen continuity device picker experience when selected. The modal view covers as much the screen of `self` as possible when a given condition is true.
- [foveatedStreamingPauseSheet(session:)](<foveatedstreamingpausesheet(session_).md>) — Tells the system to present a sheet with controls for resuming or ending the foveated streaming session when it pauses.
