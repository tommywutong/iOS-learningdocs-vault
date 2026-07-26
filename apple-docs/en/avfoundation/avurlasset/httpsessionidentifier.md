---
title: httpSessionIdentifier
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlasset/httpsessionidentifier
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/httpsessionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/httpsessionidentifier.json'
content_hash: 'sha256:f214efa307458bf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# httpSessionIdentifier

<sub>Instance Property</sub>

A session identifier that the asset sends in HTTP requests that it makes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpSessionIdentifier: UUID { get }
```

## Discussion

The asset uses this value to set as the `X-Playback-Session-Id` header of HTTP requests that it creates.

> [!note] Note
> Copies of an [AVURLAsset](../avurlasset.md) have the same session identifier as the original asset.
