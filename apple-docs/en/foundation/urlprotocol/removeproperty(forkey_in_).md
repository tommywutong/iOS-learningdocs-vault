---
title: 'removeProperty(forKey:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/removeproperty(forkey:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/removeproperty(forkey:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/removeproperty%28forkey%3Ain%3A%29.json'
content_hash: 'sha256:a4e28538183baeed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# removeProperty(forKey:in:)

<sub>Type Method</sub>

Removes the property associated with the specified key in the specified request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func removeProperty(forKey key: String, in request: NSMutableURLRequest)
```

## Parameters

- `key` — The key whose value should be removed.

- `request` — The request from which to remove the property value.

## Discussion

This method is used to provide an interface for protocol implementors to customize protocol-specific information associated with [URLRequest](../urlrequest.md) objects, or [NSMutableURLRequest](../nsmutableurlrequest.md) objects in Objective-C.

## See Also

### Getting and setting request properties

- [+ propertyForKey:inRequest:](<property(forkey_in_).md>) — Fetches the property associated with the specified key in the specified request.
- [+ setProperty:forKey:inRequest:](<setproperty(__forkey_in_).md>) — Sets the property associated with the specified key in the specified request.
