---
title: 'invalidateAllPersistableContentKeys(forApp:options:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/invalidateallpersistablecontentkeys(forapp:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/invalidateallpersistablecontentkeys(forapp:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/invalidateallpersistablecontentkeys%28forapp%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:f77aee89135191c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# invalidateAllPersistableContentKeys(forApp:options:completionHandler:)

<sub>Instance Method</sub>

Invalidates all of an app’s persistable content keys and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invalidateAllPersistableContentKeys(forApp appIdentifier: Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]? = nil, completionHandler handler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invalidateAllPersistableContentKeys(forApp appIdentifier: Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]? = nil) async throws -> Data
```

## Parameters

- `appIdentifier` — An opaque identifier for the app.

- `options` — Additional data necessary to generate the server playback context. Pass `nil` to indicate no additional options. See [AVContentKeySessionServerPlaybackContextOption](../avcontentkeysessionserverplaybackcontextoption.md) for supported options.

- `handler` — The completion handler callback.

## See Also

### Invalidating content keys

- [- invalidatePersistableContentKey:options:completionHandler:](<invalidatepersistablecontentkey(__options_completionhandler_).md>) — Invalidates the persistable content key and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [AVContentKeySessionServerPlaybackContextOption](../avcontentkeysessionserverplaybackcontextoption.md) — Options for specifying additional information for generating server playback context (SPC).
