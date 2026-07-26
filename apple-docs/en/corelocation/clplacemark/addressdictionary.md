---
title: addressDictionary
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（11.0 起废弃）, iPadOS 5.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.8+（10.13 起废弃）, tvOS 9.0+（11.0 起废弃）, watchOS 1.0+（4.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clplacemark/addressdictionary
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark/addressdictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark/addressdictionary.json'
content_hash: 'sha256:eb03c73a756d5bed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLPlacemark](../clplacemark.md)

# addressDictionary

<sub>Instance Property</sub>

A dictionary containing the Address Book keys and values for the placemark.

> [!warning] Deprecated
> Use [CLPlacemark](../clplacemark.md) instead of Address Book.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var addressDictionary: [AnyHashable : Any]? { get }
```

## Discussion

The keys in this dictionary are those defined by the Address Book framework and used to access address information for a person. For a list of the strings that can be in this dictionary, see the “Address Property” constants in `ABPerson`.

You can format the contents of this dictionary to get a full address string as opposed to building the address yourself. To format the dictionary, use the [ABCreateStringWithAddressDictionary(_:_:)](<../../addressbookui/abcreatestringwithaddressdictionary(____).md>) function as described in `AddressBookUI Functions`.

## See Also

### Getting the associated contact details

- [postalAddress](postaladdress.md) — The postal address associated with the location, formatted for use with the Contacts framework. _(deprecated)_
