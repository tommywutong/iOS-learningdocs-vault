---
title: 'class(forClassName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/class(forclassname:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/class(forclassname:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/class%28forclassname%3A%29-swift.type.method.json'
content_hash: 'sha256:fc708aa7c2b634c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# class(forClassName:)

<sub>Type Method</sub>

Returns the class from which this unarchiver instantiates an encoded object with a given class name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func `class`(forClassName codedName: String) -> AnyClass?
```

## Parameters

- `codedName` — The ostensible name of a class in an archive.

## Return Value

The class from which `NSKeyedUnarchiver` instantiates an object encoded with the class name `codedName`. Returns `nil` if `NSKeyedUnarchiver` does not have a translation mapping for `codedName`.

## See Also

### Managing Class Names

- [+ setClass:forClassName:](<setclass(__forclassname_)-swift.type.method.md>) — Sets a global translation mapping to decode objects encoded with a given class name as instances of a given class instead.
- [- setClass:forClassName:](<setclass(__forclassname_)-swift.method.md>) — Sets a translation mapping on this unarchiver to decode objects encoded with a given class name as instances of a given class instead.
- [- classForClassName:](<class(forclassname_)-swift.method.md>) — Returns the class from which this unarchiver instantiates an encoded object with a given class name.
