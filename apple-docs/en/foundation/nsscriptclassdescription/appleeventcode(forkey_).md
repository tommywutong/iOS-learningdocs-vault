---
title: 'appleEventCode(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptclassdescription/appleeventcode(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/appleeventcode(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/appleeventcode%28forkey%3A%29.json'
content_hash: 'sha256:6e2126e116ae7a05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# appleEventCode(forKey:)

<sub>Instance Method</sub>

Returns the Apple event code for the specified attribute or relationship in the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func appleEventCode(forKey key: String) -> FourCharCode
```

## Parameters

- `key` — The identifying key for an attribute or relationship of the receiver.

## Return Value

The four-character Apple event code associated with the attribute or relationship identified by `key` in the receiver or, if none exists, in the class description for the receiver’s superclass. Returns `0` if no such attribute or relationship is found.

## See Also

### Getting and comparing Apple event codes

- [appleEventCode](appleeventcode.md) — Returns the Apple event code associated with the receiver’s class.
- [- matchesAppleEventCode:](<matchesappleeventcode(__).md>) — Returns a Boolean value indicating whether a primary or secondary Apple event code in the receiver matches the passed code.
