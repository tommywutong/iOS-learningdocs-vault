---
title: 'setVersion(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setversion(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setversion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setversion%28_%3A%29.json'
content_hash: 'sha256:73b0a9d89a24fb28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setVersion(_:)

<sub>Type Method</sub>

Sets the receiver’s version number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setVersion(_ aVersion: Int)
```

## Parameters

- `aVersion` — The version number for the receiver.

## Discussion

The version number is helpful when instances of the class are to be archived and reused later. The default version is `0`.

### Special Considerations

The version number applies to `NSArchiver`/`NSUnarchiver`, but not to `NSKeyedArchiver`/`NSKeyedUnarchiver`.  A keyed archiver does not encode class version numbers.

## See Also

### Archiving

- [- awakeAfterUsingCoder:](<awakeafter(using_).md>) — Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.
- [classForArchiver](classforarchiver.md) — The class to substitute for the receiver’s own class during archiving.
- [classForCoder](classforcoder.md) — Overridden by subclasses to substitute a class other than its own during coding.
- [classForKeyedArchiver](classforkeyedarchiver.md) — Subclasses to substitute a new class for instances during keyed archiving.
- [+ classFallbacksForKeyedArchiver](<classfallbacksforkeyedarchiver().md>) — Overridden to return the names of classes that can be used to decode objects if their class is unavailable.
- [+ classForKeyedUnarchiver](<classforkeyedunarchiver().md>) — Overridden by subclasses to substitute a new class during keyed unarchiving.
- [- replacementObjectForArchiver:](<replacementobject(for_)-8ih2x.md>) — Overridden by subclasses to substitute another object for itself during archiving. _(deprecated)_
- [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) — Overridden by subclasses to substitute another object for itself during encoding.
- [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) — Overridden by subclasses to substitute another object for itself during keyed archiving.
- [+ version](<version().md>) — Returns the version number assigned to the class.
