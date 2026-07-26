---
title: 'className(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiver/classname(for:)-swift.method'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/classname(for:)-swift.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/classname%28for%3A%29-swift.method.json'
content_hash: 'sha256:2fc461c84704cea4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# className(for:)

<sub>Instance Method</sub>

Returns the class name with which this archiver encodes instances of a given class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func className(for cls: AnyClass) -> String?
```

## Parameters

- `cls` — The class for which to determine the translation mapping.

## Return Value

The class name with which the receiver encodes instances of `cls`. Returns `nil` if the receiver does not have a translation mapping for `cls`. The class’s separate translation map is not searched.

## See Also

### Managing Classes and Class Names

- [+ setClassName:forClass:](<setclassname(__for_)-swift.type.method.md>) — Sets a global translation mapping to encode instances of a given class with the provided name, rather than their real name.
- [+ classNameForClass:](<classname(for_)-swift.type.method.md>) — Returns the class name with which the archiver class encodes instances of a given class.
- [- setClassName:forClass:](<setclassname(__for_)-swift.method.md>) — Sets a mapping for this archiver to encode instances of a given class with the provided name, rather than their real name.
