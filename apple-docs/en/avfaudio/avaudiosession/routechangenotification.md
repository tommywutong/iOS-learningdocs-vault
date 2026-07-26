---
title: routeChangeNotification
framework: AVFAudio
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudiosession/routechangenotification
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudiosession/routechangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudiosession/routechangenotification.json'
content_hash: 'sha256:0f8b30955867eb13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFAudio](../../avfaudio.md) · [AVAudioSession](../avaudiosession.md)

# routeChangeNotification

<sub>Type Property</sub>

A notification the system posts when its audio route changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class let routeChangeNotification: NSNotification.Name
```

## Discussion

The [userInfo](../../foundation/nsnotification/userinfo.md) dictionary of this notification contains the [AVAudioSessionRouteChangeReasonKey](../avaudiosessionroutechangereasonkey.md) and [AVAudioSessionRouteChangePreviousRouteKey](../avaudiosessionroutechangepreviousroutekey.md) keys, which provide information about the route change.

See [Responding to audio route changes](../responding-to-audio-route-changes.md) for more information on using this notification.

The system posts this notification on a secondary thread.

## Topics

### User Info Keys

- [AVAudioSessionRouteChangeReasonKey](../avaudiosessionroutechangereasonkey.md) — A user info key that’s used to retrieve the route change reason.
- [AVAudioSessionRouteChangePreviousRouteKey](../avaudiosessionroutechangepreviousroutekey.md) — A user info key that’s used to retrieve the previously active audio session route.

### User Info Values

- [RouteChangeReason](routechangereason.md) — Constants that indicate the reason for an audio route change.

## See Also

### Inspecting the current route

- [currentRoute](currentroute.md) — A description of the current audio route’s input and output ports.
- [AVAudioSessionRouteDescription](../avaudiosessionroutedescription.md) — An object that describes the input and output ports associated with a session’s audio route.
- [AVAudioSessionPortDescription](../avaudiosessionportdescription.md) — Information about the capabilities of the port and the hardware channels it supports.
