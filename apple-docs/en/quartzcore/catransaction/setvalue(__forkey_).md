---
title: 'setValue(_:forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransaction/setvalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/setvalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/setvalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:38e81b1ac4f5f8c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# setValue(_:forKey:)

<sub>Type Method</sub>

Sets the arbitrary keyed-data for the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func setValue(_ anObject: Any?, forKey key: String)
```

## Parameters

- `anObject` — The value for the key identified by `key`.

- `key` — The name of one of the receiver’s properties.

## Discussion

Nested transactions have nested data scope; setting a key always sets it in the innermost scope.

## See Also

### Getting and Setting Transaction Properties

- [+ valueForKey:](<value(forkey_).md>) — Returns the arbitrary keyed-data specified by the given key.
