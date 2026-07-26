---
title: 'setProperty(_:forKey:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/setproperty(_:forkey:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/setproperty(_:forkey:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/setproperty%28_%3Aforkey%3Ain%3A%29.json'
content_hash: 'sha256:b2f5632494a0b3e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# setProperty(_:forKey:in:)

<sub>Type Method</sub>

Sets the property associated with the specified key in the specified request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setProperty(_ value: Any, forKey key: String, in request: NSMutableURLRequest)
```

## Parameters

- `value` — The value to set for the specified property.

- `key` — The key for the specified property.

- `request` — The request for which to create the property.

## Discussion

Use this method to provide an interface for protocol implementors to customize protocol-specific information associated with [URLRequest](../urlrequest.md) objects.

## See Also

### Getting and setting request properties

- [+ propertyForKey:inRequest:](<property(forkey_in_).md>) — Fetches the property associated with the specified key in the specified request.
- [+ removePropertyForKey:inRequest:](<removeproperty(forkey_in_).md>) — Removes the property associated with the specified key in the specified request.
