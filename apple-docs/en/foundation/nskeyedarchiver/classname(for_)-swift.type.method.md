---
title: 'className(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiver/classname(for:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/classname(for:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/classname%28for%3A%29-swift.type.method.json'
content_hash: 'sha256:f40500555cca02e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# className(for:)

<sub>Type Method</sub>

Returns the class name with which the archiver class encodes instances of a given class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func className(for cls: AnyClass) -> String?
```

## Parameters

- `cls` — The class for which to determine the translation mapping.

## Return Value

The class name with which [NSKeyedArchiver](../nskeyedarchiver.md) encodes instances of `cls`. Returns `nil` if [NSKeyedArchiver](../nskeyedarchiver.md) does not have a translation mapping for `cls`.

## See Also

### Managing Classes and Class Names

- [+ setClassName:forClass:](<setclassname(__for_)-swift.type.method.md>) — Sets a global translation mapping to encode instances of a given class with the provided name, rather than their real name.
- [- setClassName:forClass:](<setclassname(__for_)-swift.method.md>) — Sets a mapping for this archiver to encode instances of a given class with the provided name, rather than their real name.
- [- classNameForClass:](<classname(for_)-swift.method.md>) — Returns the class name with which this archiver encodes instances of a given class.
