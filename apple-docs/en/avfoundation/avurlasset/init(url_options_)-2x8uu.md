---
title: 'init(url:options:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avurlasset/init(url:options:)-2x8uu'
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/init(url:options:)-2x8uu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/init%28url%3Aoptions%3A%29-2x8uu.json'
content_hash: 'sha256:b54b8d1e155685d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# init(url:options:)

<sub>Initializer</sub>

Creates an asset that models the media resource at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(url URL: URL, options: [String : Any]? = nil)
```

## Parameters

- `URL` — A URL that references the media for the asset to model.

- `options` — A dictionary that contains options used to customize the initialization of the asset. For supported keys and values, see [Initialization options](../initialization-options.md).

## Return Value

An asset that models the media resource found at `URL`.

## See Also

### Creating an asset

- [init(url:)](<init(url_).md>) — Creates an asset that models the media at the specified URL.
- [Initialization options](../avurlasset-initialization-options.md) — Specify options to configure the initialization of a media asset.
