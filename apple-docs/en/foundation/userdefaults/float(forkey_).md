---
title: 'float(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/float(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/float(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/float%28forkey%3A%29.json'
content_hash: 'sha256:a1148bb22882d694'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# float(forKey:)

<sub>Instance Method</sub>

Returns the floating-point value associated with the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func float(forKey defaultName: String) -> Float
```

## Parameters

- `defaultName` — The key to retrieve from the defaults database.

## Return Value

The floating-point value associated with `defaultName`, or `0.0` if the key isn’t present in the defaults database.

## Discussion

This method automatically coerces certain types to their equivalent integer values. The Boolean value `true` becomes `1.0` and `false` becomes `0.0`. An integer becomes the equivalent floating-point number –– for example, `2` becomes `2.0`. A string that contains a numerical value contains the equivalent floating-point value — for example, “123.4” becomes `123.4`.

## See Also

### Getting the value of a key

- [- boolForKey:](<bool(forkey_).md>) — Returns the Boolean value associated with the specified key.
- [- integerForKey:](<integer(forkey_).md>) — Returns the integer value associated with the specified key.
- [- doubleForKey:](<double(forkey_).md>) — Returns the double value associated with the specified key.
- [- URLForKey:](<url(forkey_).md>) — Returns the URL associated with the specified key.
- [- stringForKey:](<string(forkey_).md>) — Returns the string associated with the specified key.
- [- stringArrayForKey:](<stringarray(forkey_).md>) — Returns the array of strings associated with the specified key.
- [- dataForKey:](<data(forkey_).md>) — Returns the data object associated with the specified key.
- [- objectForKey:](<object(forkey_).md>) — Returns the object associated with the specified key.
- [- arrayForKey:](<array(forkey_).md>) — Returns the array associated with the specified key.
- [- dictionaryForKey:](<dictionary(forkey_).md>) — Returns the dictionary object associated with the specified key.
- [- dictionaryRepresentation](<dictionaryrepresentation().md>) — Returns a dictionary with the union of all key-value pairs found from all domains.
