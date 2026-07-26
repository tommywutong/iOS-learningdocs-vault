---
title: 'property(forKey:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/property(forkey:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/property(forkey:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/property%28forkey%3Ain%3A%29.json'
content_hash: 'sha256:d915965e1ca89201'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# property(forKey:in:)

<sub>Type Method</sub>

Fetches the property associated with the specified key in the specified request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func property(forKey key: String, in request: URLRequest) -> Any?
```

## Parameters

- `key` — The key of the desired property.

- `request` — The request whose properties are to be queried.

## Return Value

The property associated with `key`, or `nil` if no property has been stored for `key`.

## Discussion

Use this method to access protocol-specific information associated with [URLRequest](../urlrequest.md) objects.

## See Also

### Getting and setting request properties

- [+ setProperty:forKey:inRequest:](<setproperty(__forkey_in_).md>) — Sets the property associated with the specified key in the specified request.
- [+ removePropertyForKey:inRequest:](<removeproperty(forkey_in_).md>) — Removes the property associated with the specified key in the specified request.
