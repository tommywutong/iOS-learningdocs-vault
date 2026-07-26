---
title: 'shouldArchiveValue(forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/caemittercell/shouldarchivevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/shouldarchivevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/shouldarchivevalue%28forkey%3A%29.json'
content_hash: 'sha256:685c1264a391d580'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# shouldArchiveValue(forKey:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the value for a given key should be archived.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func shouldArchiveValue(forKey key: String) -> Bool
```

## Parameters

- `key` — The name of one of the receiver’s properties.

## Return Value

[true](../../swift/true.md) if the specified property should be archived, otherwise [false](../../swift/false.md).

## Discussion

The default implementation returns [true](../../swift/true.md). This method is called by the object’s implementation of `encodeWithCoder:`.

## See Also

### Using Key-Value Coding Extensions

- [+ defaultValueForKey:](<defaultvalue(forkey_).md>) — Returns the default value of the property with the specified key.
