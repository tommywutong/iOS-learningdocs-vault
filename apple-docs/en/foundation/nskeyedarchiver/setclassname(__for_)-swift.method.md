---
title: 'setClassName(_:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiver/setclassname(_:for:)-swift.method'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/setclassname(_:for:)-swift.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/setclassname%28_%3Afor%3A%29-swift.method.json'
content_hash: 'sha256:a6175af89d39348d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# setClassName(_:for:)

<sub>Instance Method</sub>

Sets a mapping for this archiver to encode instances of a given class with the provided name, rather than their real name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setClassName(_ codedName: String?, for cls: AnyClass)
```

## Parameters

- `codedName` — The name of the class that the receiver uses uses in place of `cls`.

- `cls` — The class for which to set up a translation mapping.

## Discussion

When encoding, the receiver’s translation map overrides any translation that may also be present in the class’s map.

## See Also

### Managing Classes and Class Names

- [+ setClassName:forClass:](<setclassname(__for_)-swift.type.method.md>) — Sets a global translation mapping to encode instances of a given class with the provided name, rather than their real name.
- [+ classNameForClass:](<classname(for_)-swift.type.method.md>) — Returns the class name with which the archiver class encodes instances of a given class.
- [- classNameForClass:](<classname(for_)-swift.method.md>) — Returns the class name with which this archiver encodes instances of a given class.
