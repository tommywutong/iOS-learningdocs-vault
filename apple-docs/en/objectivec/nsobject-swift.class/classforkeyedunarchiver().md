---
title: classForKeyedUnarchiver()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/classforkeyedunarchiver()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classforkeyedunarchiver()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/classforkeyedunarchiver%28%29.json'
content_hash: 'sha256:2224ff7d29f930d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# classForKeyedUnarchiver()

<sub>Type Method</sub>

Overridden by subclasses to substitute a new class during keyed unarchiving.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func classForKeyedUnarchiver() -> AnyClass
```

## Return Value

The class to substitute for the receiver during keyed unarchiving.

## Discussion

During keyed unarchiving, instances of the receiver will be decoded as members of the returned class. This method overrides the results of the decoder’s class and instance name to class encoding tables.

## See Also

### Archiving

- [- awakeAfterUsingCoder:](<awakeafter(using_).md>) — Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.
- [classForArchiver](classforarchiver.md) — The class to substitute for the receiver’s own class during archiving.
- [classForCoder](classforcoder.md) — Overridden by subclasses to substitute a class other than its own during coding.
- [classForKeyedArchiver](classforkeyedarchiver.md) — Subclasses to substitute a new class for instances during keyed archiving.
- [+ classFallbacksForKeyedArchiver](<classfallbacksforkeyedarchiver().md>) — Overridden to return the names of classes that can be used to decode objects if their class is unavailable.
- [- replacementObjectForArchiver:](<replacementobject(for_)-8ih2x.md>) — Overridden by subclasses to substitute another object for itself during archiving. _(deprecated)_
- [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) — Overridden by subclasses to substitute another object for itself during encoding.
- [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) — Overridden by subclasses to substitute another object for itself during keyed archiving.
- [+ setVersion:](<setversion(__).md>) — Sets the receiver’s version number.
- [+ version](<version().md>) — Returns the version number assigned to the class.
