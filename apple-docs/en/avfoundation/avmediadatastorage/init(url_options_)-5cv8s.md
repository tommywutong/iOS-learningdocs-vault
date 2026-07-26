---
title: 'init(url:options:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmediadatastorage/init(url:options:)-5cv8s'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediadatastorage/init(url:options:)-5cv8s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediadatastorage/init%28url%3Aoptions%3A%29-5cv8s.json'
content_hash: 'sha256:5688ee5af7c66859'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaDataStorage](../avmediadatastorage.md)

# init(url:options:)

<sub>Initializer</sub>

Creates a media data storage object associated with a file URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(url URL: URL, options: [String : Any]? = nil)
```

## Parameters

- `URL` — The URL specifying where sample data added to a movie or track is written.

- `options` — A dictionary object containing keys for specifying initialization options. No keys are currently defined.

## Return Value

An `AVMediaDataStorage` object.
