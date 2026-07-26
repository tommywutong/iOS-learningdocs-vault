---
title: 'present(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 16.1+, macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedeskviewapplication/present(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/present(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeskviewapplication/present%28completionhandler%3A%29.json'
content_hash: 'sha256:cf8c33538c1b8787'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeskViewApplication](../avcapturedeskviewapplication.md)

# present(completionHandler:)

<sub>Instance Method</sub>

Launches Desk View with no additional configuration and then performs a completion handler if you specify it.

<sub>Mac Catalyst, macOS</sub>

```swift
func present(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>Mac Catalyst, macOS</sub>

```swift
func present() async throws
```

## Parameters

- `completionHandler` — The code to perform after the system displays Desk View.

## Discussion

If the Desk View app is already running, this method brings it to the front. If Desk View is in the Dock, this method opens it and brings it to the front.

Desk View launches in setup mode. This mode shows the full field of view of an ultrawide camera with a superimposed trapezoid that indicates the cropped desk region to display. The system displays this region after the user completes setup and starts Desk View.

## See Also

### Presenting the Desk View app

- [- presentWithLaunchConfiguration:completionHandler:](<present(launchconfiguration_completionhandler_).md>) — Launches Desk View with the configuration and completion handler that you specify.
- [LaunchConfiguration](launchconfiguration.md) — An object that configures how to present Desk View.
