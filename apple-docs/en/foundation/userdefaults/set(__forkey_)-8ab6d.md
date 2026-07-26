---
title: 'set(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/set(_:forkey:)-8ab6d'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/set(_:forkey:)-8ab6d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/set%28_%3Aforkey%3A%29-8ab6d.json'
content_hash: 'sha256:f75226eca289fc3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# set(_:forKey:)

<sub>Instance Method</sub>

Sets the value of the specified key to a property list object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func set(_ value: Any?, forKey defaultName: String)
```

## Parameters

- `value` — The property-list type to store in the defaults database. If you specify an array or dictionary type, those collections must similarly contain only property list types.

- `defaultName` — The key that contains the setting’s name.

## Discussion

Use this method to write property list object types to the defaults store. To store types that aren’t property list objects, archive them to a [Data](../data.md) object and use this method to save that data object to the defaults store.

After you call this method, the system generates a [NSUserDefaultsDidChangeNotification](didchangenotification.md) for registered observers.

## See Also

### Setting the value for a key

- [- setBool:forKey:](<set(__forkey_)-3nn5m.md>) — Sets the value of the specified key to a Boolean value.
- [- setInteger:forKey:](<set(__forkey_)-3v852.md>) — Sets the value of the specified key to an integer.
- [- setFloat:forKey:](<set(__forkey_)-1t5ec.md>) — Sets the value of the specified key to a floating-point number.
- [- setDouble:forKey:](<set(__forkey_)-2w22f.md>) — Sets the value of the specified key to a double.
- [- setURL:forKey:](<set(__forkey_)-2bqjt.md>) — Sets the value of the specified key to a URL.
