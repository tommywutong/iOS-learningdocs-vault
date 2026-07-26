---
title: 'setClass(_:forClassName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/setclass(_:forclassname:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/setclass(_:forclassname:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/setclass%28_%3Aforclassname%3A%29-swift.type.method.json'
content_hash: 'sha256:6e4be59eed5bb5d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# setClass(_:forClassName:)

<sub>Type Method</sub>

Sets a global translation mapping to decode objects encoded with a given class name as instances of a given class instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setClass(_ cls: AnyClass?, forClassName codedName: String)
```

## Parameters

- `cls` — The class with which to replace instances of the class named `codedName`.

- `codedName` — The ostensible name of a class in an archive.

## Discussion

When decoding, the class’s translation mapping is used only if no translation is found first in an instance’s separate translation map.

## See Also

### Managing Class Names

- [+ classForClassName:](<class(forclassname_)-swift.type.method.md>) — Returns the class from which this unarchiver instantiates an encoded object with a given class name.
- [- setClass:forClassName:](<setclass(__forclassname_)-swift.method.md>) — Sets a translation mapping on this unarchiver to decode objects encoded with a given class name as instances of a given class instead.
- [- classForClassName:](<class(forclassname_)-swift.method.md>) — Returns the class from which this unarchiver instantiates an encoded object with a given class name.
