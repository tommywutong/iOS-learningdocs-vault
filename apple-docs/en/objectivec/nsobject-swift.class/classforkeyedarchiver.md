---
title: classForKeyedArchiver
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/classforkeyedarchiver
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classforkeyedarchiver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/classforkeyedarchiver.json'
content_hash: 'sha256:6a7686e064fb8413'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# classForKeyedArchiver

<sub>Instance Property</sub>

Subclasses to substitute a new class for instances during keyed archiving.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var classForKeyedArchiver: AnyClass? { get }
```

## Discussion

The object will be encoded as if it were a member of the class. This property is overridden by the encoder class and instance name to class encoding tables. If this property is `nil`, the result of this property is ignored.

## See Also

### Archiving

- [- awakeAfterUsingCoder:](<awakeafter(using_).md>) — Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.
- [classForArchiver](classforarchiver.md) — The class to substitute for the receiver’s own class during archiving.
- [classForCoder](classforcoder.md) — Overridden by subclasses to substitute a class other than its own during coding.
- [+ classFallbacksForKeyedArchiver](<classfallbacksforkeyedarchiver().md>) — Overridden to return the names of classes that can be used to decode objects if their class is unavailable.
- [+ classForKeyedUnarchiver](<classforkeyedunarchiver().md>) — Overridden by subclasses to substitute a new class during keyed unarchiving.
- [- replacementObjectForArchiver:](<replacementobject(for_)-8ih2x.md>) — Overridden by subclasses to substitute another object for itself during archiving. _(deprecated)_
- [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) — Overridden by subclasses to substitute another object for itself during encoding.
- [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) — Overridden by subclasses to substitute another object for itself during keyed archiving.
- [+ setVersion:](<setversion(__).md>) — Sets the receiver’s version number.
- [+ version](<version().md>) — Returns the version number assigned to the class.
