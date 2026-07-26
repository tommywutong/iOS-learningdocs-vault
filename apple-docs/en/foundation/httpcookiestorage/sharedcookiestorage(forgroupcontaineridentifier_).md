---
title: 'sharedCookieStorage(forGroupContainerIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookiestorage/sharedcookiestorage(forgroupcontaineridentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestorage/sharedcookiestorage(forgroupcontaineridentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestorage/sharedcookiestorage%28forgroupcontaineridentifier%3A%29.json'
content_hash: 'sha256:a21b7d4166c0c4fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStorage](../httpcookiestorage.md)

# sharedCookieStorage(forGroupContainerIdentifier:)

<sub>Type Method</sub>

Returns the cookie storage instance for the container associated with the specified app group identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func sharedCookieStorage(forGroupContainerIdentifier identifier: String) -> HTTPCookieStorage
```

## Parameters

- `identifier` — The app group identifier.

## Discussion

By default, apps and associated app extensions will have different data containers. As a result, the value of the [HTTPCookieStorage](../httpcookiestorage.md) class’s [sharedHTTPCookieStorage](shared.md) property will refer to different persistent cookie stores when called by the app and by its extensions.You can use this method to create a persistent cookie storage available to all apps and extensions with access to the same app group.

Subsequent calls to the this method with the same identifier will return the same storage instance.

## See Also

### Getting the shared cookie storage object

- [sharedHTTPCookieStorage](shared.md) — The shared cookie storage instance.
