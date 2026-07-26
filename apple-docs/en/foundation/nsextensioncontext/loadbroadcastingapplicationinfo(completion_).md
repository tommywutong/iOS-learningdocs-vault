---
title: 'loadBroadcastingApplicationInfo(completion:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsextensioncontext/loadbroadcastingapplicationinfo(completion:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/loadbroadcastingapplicationinfo(completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/loadbroadcastingapplicationinfo%28completion%3A%29.json'
content_hash: 'sha256:a77ef1279c950184'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# loadBroadcastingApplicationInfo(completion:)

<sub>Instance Method</sub>

> [!warning] Deprecated
> No longer supported

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func loadBroadcastingApplicationInfo(completion handler: @escaping @Sendable (String, String, UIImage?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func loadBroadcastingApplicationInfo() async -> (String, String, UIImage?)
```

<sub>macOS</sub>

```swift
func loadBroadcastingApplicationInfo(completion handler: @escaping @Sendable (String, String, NSImage?) -> Void)
```

<sub>macOS</sub>

```swift
func loadBroadcastingApplicationInfo() async -> (String, String, NSImage?)
```

## Discussion

## See Also

### Supporting broadcasting

- [- completeRequestWithBroadcastURL:setupInfo:](<completerequest(withbroadcast_setupinfo_).md>) _(deprecated)_
