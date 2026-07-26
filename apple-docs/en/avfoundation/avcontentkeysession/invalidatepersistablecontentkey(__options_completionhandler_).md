---
title: 'invalidatePersistableContentKey(_:options:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/invalidatepersistablecontentkey(_:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/invalidatepersistablecontentkey(_:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/invalidatepersistablecontentkey%28_%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:7d3ad7e220db53c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# invalidatePersistableContentKey(_:options:completionHandler:)

<sub>Instance Method</sub>

Invalidates the persistable content key and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invalidatePersistableContentKey(_ persistableContentKeyData: Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]? = nil, completionHandler handler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invalidatePersistableContentKey(_ persistableContentKeyData: Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]? = nil) async throws -> Data
```

## Parameters

- `persistableContentKeyData` — The persistable content key data to invalidate.

- `options` — Additional options to use when generating the server playback context. Pass `nil` to indicate no additional options.

- `handler` — The completion handler callback.

## See Also

### Invalidating content keys

- [- invalidateAllPersistableContentKeysForApp:options:completionHandler:](<invalidateallpersistablecontentkeys(forapp_options_completionhandler_).md>) — Invalidates all of an app’s persistable content keys and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [AVContentKeySessionServerPlaybackContextOption](../avcontentkeysessionserverplaybackcontextoption.md) — Options for specifying additional information for generating server playback context (SPC).
