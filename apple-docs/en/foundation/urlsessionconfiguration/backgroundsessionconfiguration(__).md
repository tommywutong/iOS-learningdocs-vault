---
title: 'backgroundSessionConfiguration(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+（8.0 起废弃）, iPadOS 7.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/urlsessionconfiguration/backgroundsessionconfiguration(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/backgroundsessionconfiguration(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/backgroundsessionconfiguration%28_%3A%29.json'
content_hash: 'sha256:1c6b674e8b4672d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# backgroundSessionConfiguration(_:)

<sub>Type Method</sub>

Returns a session configuration object that allows HTTP and HTTPS uploads or downloads to be performed in the background.

> [!warning] Deprecated
> Use [+ backgroundSessionConfigurationWithIdentifier:](<background(withidentifier_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func backgroundSessionConfiguration(_ identifier: String) -> URLSessionConfiguration
```

## Parameters

- `identifier` — The unique identifier for the configuration object. This parameter must not be `nil` or an empty string.

## Return Value

A URL session configuration object that causes upload and download tasks to be performed by the system in a separate process.
