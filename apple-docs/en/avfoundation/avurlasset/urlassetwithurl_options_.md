---
title: 'URLAssetWithURL:options:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avurlasset/urlassetwithurl:options:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/urlassetwithurl:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/urlassetwithurl%3Aoptions%3A.json'
content_hash: 'sha256:70890fe8cd2e90aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# URLAssetWithURL:options:

<sub>Type Method</sub>

Returns an asset that models the media resource found at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) URLAssetWithURL:(NSURL *) URL options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `URL` — A URL that references the media for the asset to model.

- `options` — A dictionary that contains options used to customize the initialization of the asset. For possible keys and values, see [Initialization options](../initialization-options.md).

## Return Value

An asset that models the media resource found at `URL`.

## See Also

### Creating an asset

- [- initWithURL:options:](<init(url_options_)-2x8uu.md>) — Creates an asset that models the media resource at the specified URL.
- [Initialization options](../avurlasset-initialization-options.md) — Specify options to configure the initialization of a media asset.
