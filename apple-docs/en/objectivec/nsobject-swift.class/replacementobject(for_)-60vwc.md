---
title: 'replacementObject(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/replacementobject(for:)-60vwc'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/replacementobject(for:)-60vwc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/replacementobject%28for%3A%29-60vwc.json'
content_hash: 'sha256:e1f59b318819b2c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# replacementObject(for:)

<sub>Instance Method</sub>

Overridden by subclasses to substitute another object for itself during keyed archiving.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacementObject(for archiver: NSKeyedArchiver) -> Any?
```

## Parameters

- `archiver` — A keyed archiver creating an archive.

## Return Value

The object encode instead of the receiver (if different).

## Discussion

This method is called only if no replacement mapping for the object has been set up in the encoder (for example, due to a previous call of [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) to that object).

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
- [+ setVersion:](<setversion(__).md>) — Sets the receiver’s version number.
- [+ version](<version().md>) — Returns the version number assigned to the class.
