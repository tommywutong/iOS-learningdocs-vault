---
title: 'shouldArchiveValue(forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/shouldarchivevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/shouldarchivevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/shouldarchivevalue%28forkey%3A%29.json'
content_hash: 'sha256:df032d43e37197e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# shouldArchiveValue(forKey:)

<sub>Instance Method</sub>

Returns a Boolean indicating whether the value of the specified key should be archived.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func shouldArchiveValue(forKey key: String) -> Bool
```

## Parameters

- `key` — The name of one of the receiver’s properties.

## Return Value

[true](../../swift/true.md) if the specified property should be archived or [false](../../swift/false.md) if it should not.

## Discussion

The default implementation returns [true](../../swift/true.md).

## See Also

### Key-value coding extensions

- [+ defaultValueForKey:](<defaultvalue(forkey_).md>) — Specifies the default value associated with the specified key.
