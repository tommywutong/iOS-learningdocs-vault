---
title: UIApplication.OpenExternalURLOptionsKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/openexternalurloptionskey
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/openexternalurloptionskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/openexternalurloptionskey.json'
content_hash: 'sha256:7911472597d076ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# UIApplication.OpenExternalURLOptionsKey

<sub>Structure</sub>

Options for opening a URL.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct OpenExternalURLOptionsKey
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### URL options

- [UIApplicationOpenURLOptionUniversalLinksOnly](openexternalurloptionskey/universallinksonly.md) — URLs must be universal links and have an app configured to open them.

### Measuring ad taps

- [UIApplicationOpenExternalURLOptionsEventAttributionKey](openexternalurloptionskey/eventattribution.md) — An object you use to send tap event attribution data to the browser for Private Click Measurement.

### Initializers

- [init(rawValue:)](<openexternalurloptionskey/init(rawvalue_).md>) — Creates a new instance with the specified raw value.

## See Also

### Opening a URL resource

- [- openURL:options:completionHandler:](<open(__options_completionhandler_).md>) — Attempts to asynchronously open the resource at the specified URL.
- [- canOpenURL:](<canopenurl(__).md>) — Returns a Boolean value that indicates whether an app is available to handle a URL scheme. _(deprecated)_
