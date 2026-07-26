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
doc_path: '/documentation/foundation/userdefaults/set(_:forkey:)-2w22f'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/set(_:forkey:)-2w22f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/set%28_%3Aforkey%3A%29-2w22f.json'
content_hash: 'sha256:6cd6cfe19cb97c64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# set(_:forKey:)

<sub>Instance Method</sub>

Sets the value of the specified key to a double.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func set(_ value: Double, forKey defaultName: String)
```

## Parameters

- `value` — The double value to store in the defaults database.

- `defaultName` — The key that contains the setting’s name.

## Discussion

This method places the double value in an [NSNumber](../nsnumber.md) type before writing the key and value to the defaults database. After you call this method, the system generates a [NSUserDefaultsDidChangeNotification](didchangenotification.md) for registered observers.

## See Also

### Setting the value for a key

- [- setBool:forKey:](<set(__forkey_)-3nn5m.md>) — Sets the value of the specified key to a Boolean value.
- [- setInteger:forKey:](<set(__forkey_)-3v852.md>) — Sets the value of the specified key to an integer.
- [- setFloat:forKey:](<set(__forkey_)-1t5ec.md>) — Sets the value of the specified key to a floating-point number.
- [- setURL:forKey:](<set(__forkey_)-2bqjt.md>) — Sets the value of the specified key to a URL.
- [- setObject:forKey:](<set(__forkey_)-8ab6d.md>) — Sets the value of the specified key to a property list object.
