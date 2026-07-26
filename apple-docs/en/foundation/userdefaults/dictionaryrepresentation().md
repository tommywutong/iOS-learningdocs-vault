---
title: dictionaryRepresentation()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults/dictionaryrepresentation()
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/dictionaryrepresentation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/dictionaryrepresentation%28%29.json'
content_hash: 'sha256:0468c00add2c25ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# dictionaryRepresentation()

<sub>Instance Method</sub>

Returns a dictionary with the union of all key-value pairs found from all domains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dictionaryRepresentation() -> [String : Any]
```

## Return Value

A dictionary with the combined set of keys and values from all domains.

## Discussion

Use this method to retrieve a union of the keys and values available to your app. The dictionary contains the data from all of the available domains. If multiple domains contain a value for the same key, the dictionary includes the value from the earliest occurrence of that key and discards the values in subsequent domains.

The values in the dictionary are one of the property list object types, such as [NSNumber](../nsnumber.md), [NSString](../nsstring.md), [Data](../data.md), [Date](../date.md), [NSArray](../nsarray.md), or [NSDictionary](../nsdictionary.md).

## See Also

### Getting the value of a key

- [- boolForKey:](<bool(forkey_).md>) — Returns the Boolean value associated with the specified key.
- [- integerForKey:](<integer(forkey_).md>) — Returns the integer value associated with the specified key.
- [- floatForKey:](<float(forkey_).md>) — Returns the floating-point value associated with the specified key.
- [- doubleForKey:](<double(forkey_).md>) — Returns the double value associated with the specified key.
- [- URLForKey:](<url(forkey_).md>) — Returns the URL associated with the specified key.
- [- stringForKey:](<string(forkey_).md>) — Returns the string associated with the specified key.
- [- stringArrayForKey:](<stringarray(forkey_).md>) — Returns the array of strings associated with the specified key.
- [- dataForKey:](<data(forkey_).md>) — Returns the data object associated with the specified key.
- [- objectForKey:](<object(forkey_).md>) — Returns the object associated with the specified key.
- [- arrayForKey:](<array(forkey_).md>) — Returns the array associated with the specified key.
- [- dictionaryForKey:](<dictionary(forkey_).md>) — Returns the dictionary object associated with the specified key.
