---
title: 'present(launchConfiguration:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 16.1+, macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedeskviewapplication/present(launchconfiguration:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/present(launchconfiguration:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeskviewapplication/present%28launchconfiguration%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:ca5e38cd91412227'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeskViewApplication](../avcapturedeskviewapplication.md)

# present(launchConfiguration:completionHandler:)

<sub>Instance Method</sub>

Launches Desk View with the configuration and completion handler that you specify.

<sub>Mac Catalyst, macOS</sub>

```swift
func present(launchConfiguration: AVCaptureDeskViewApplication.LaunchConfiguration, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>Mac Catalyst, macOS</sub>

```swift
func present(launchConfiguration: AVCaptureDeskViewApplication.LaunchConfiguration) async throws
```

## Parameters

- `launchConfiguration` — A configuration that specifies how to present Desk View.

- `completionHandler` — The code to perform after the system displays Desk View or the user transitions to Desk View after setup, depending on the configuration.

## Discussion

If Desk View is already running, this method brings it to the front. If Desk View is in the Dock, this method opens it and brings it to the front.

Desk View launches in setup mode. This mode shows the full field of view of an ultrawide camera with a superimposed trapezoid that indicates the cropped desk region to display. The system displays this region after the user completes setup and starts Desk View.

Create an instance of [LaunchConfiguration](launchconfiguration.md) and set it for `launchConfiguration` to specify the frame for Desk View and when to perform the `completionHandler`.

## See Also

### Presenting the Desk View app

- [- presentWithCompletionHandler:](<present(completionhandler_).md>) — Launches Desk View with no additional configuration and then performs a completion handler if you specify it.
- [LaunchConfiguration](launchconfiguration.md) — An object that configures how to present Desk View.
