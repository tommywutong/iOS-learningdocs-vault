---
title: 'requestPlaybackRestrictionsAuthorization(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/requestplaybackrestrictionsauthorization(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/requestplaybackrestrictionsauthorization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/requestplaybackrestrictionsauthorization%28_%3A%29.json'
content_hash: 'sha256:1ab01482fd7663fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# requestPlaybackRestrictionsAuthorization(_:)

<sub>Instance Method</sub>

Determines whether this item is subject to parental restrictions, and, if so, prompts the user to enter the restrictions passcode.

<sub>tvOS</sub>

```swift
func requestPlaybackRestrictionsAuthorization(_ completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

<sub>tvOS</sub>

```swift
func requestPlaybackRestrictionsAuthorization() async throws -> Bool
```

## Parameters

- `completion` — A callback the system invokes after it makes a determination of parental restrictions. - **`isAuthorized`** — A Boolean value that indicates whether the system authorizes the app to play an item. - **`error`** — An optional error that contains error details if the system encountered an error.

## See Also

### Requesting playback authorization in tvOS

- [- cancelPlaybackRestrictionsAuthorizationRequest](<cancelplaybackrestrictionsauthorizationrequest().md>) — Cancels a pending authorization request and dismisses the passcode entry, if displayed.
