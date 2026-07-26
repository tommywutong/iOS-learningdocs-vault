---
title: AVContentKeySessionServerPlaybackContextOption
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption.json'
content_hash: 'sha256:82a6ee102ce3d0b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentKeySessionServerPlaybackContextOption

<sub>Structure</sub>

Options for specifying additional information for generating server playback context (SPC).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVContentKeySessionServerPlaybackContextOption
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Server playback context options

- [AVContentKeySessionServerPlaybackContextOptionProtocolVersions](avcontentkeysessionserverplaybackcontextoption/protocolversions.md) — Specifies the versions of the content protection protocols supported by the application.
- [AVContentKeySessionServerPlaybackContextOptionServerChallenge](avcontentkeysessionserverplaybackcontextoption/serverchallenge.md) — Specifies a nonce to include in the secure server playback context (SPC) to prevent replay attacks.

### Initializing an options structure

- [init(rawValue:)](<avcontentkeysessionserverplaybackcontextoption/init(rawvalue_).md>) — Creates a playback context options structure with the specified raw value.

## See Also

### Invalidating content keys

- [- invalidatePersistableContentKey:options:completionHandler:](<avcontentkeysession/invalidatepersistablecontentkey(__options_completionhandler_).md>) — Invalidates the persistable content key and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [- invalidateAllPersistableContentKeysForApp:options:completionHandler:](<avcontentkeysession/invalidateallpersistablecontentkeys(forapp_options_completionhandler_).md>) — Invalidates all of an app’s persistable content keys and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
