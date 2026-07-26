---
title: 'set(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/set(_:forkey:)-2bqjt'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/set(_:forkey:)-2bqjt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/set%28_%3Aforkey%3A%29-2bqjt.json'
content_hash: 'sha256:6d10bae248c07c26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# set(_:forKey:)

<sub>Instance Method</sub>

Sets the value of the specified key to a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func set(_ url: URL?, forKey defaultName: String)
```

## Parameters

- `url` — The value to store in the defaults database.

- `defaultName` — The key that contains the setting’s name.

## Discussion

This method handles file URLs differently than other types of URLs. For most URLs, the method stores the URL object as the root object of a [Data](../data.md) archive. If `url` contains a path to a file in the home directory, this method replaces the home directory portion of the path with a tilde (~) character before generating the data object. When you read the value back, the system expands the tilde character to the current home directory path.

If the location of a file might change, don’t use a file URL to specify its location. Instead, create a bookmark URL using the [+ bookmarkDataWithContentsOfURL:error:](<../nsurl/bookmarkdata(withcontentsof_).md>) method and save that URL instead. Bookmark URLs store additional information about the file so the system can locate the file later, even if the path to that file changes.

After you call this method, the system generates a [NSUserDefaultsDidChangeNotification](didchangenotification.md) for registered observers.

## See Also

### Setting the value for a key

- [- setBool:forKey:](<set(__forkey_)-3nn5m.md>) — Sets the value of the specified key to a Boolean value.
- [- setInteger:forKey:](<set(__forkey_)-3v852.md>) — Sets the value of the specified key to an integer.
- [- setFloat:forKey:](<set(__forkey_)-1t5ec.md>) — Sets the value of the specified key to a floating-point number.
- [- setDouble:forKey:](<set(__forkey_)-2w22f.md>) — Sets the value of the specified key to a double.
- [- setObject:forKey:](<set(__forkey_)-8ab6d.md>) — Sets the value of the specified key to a property list object.
