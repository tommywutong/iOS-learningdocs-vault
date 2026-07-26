---
title: version()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/version()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/version()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/version%28%29.json'
content_hash: 'sha256:490dffe75d80b481'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# version()

<sub>Type Method</sub>

Returns the version number assigned to the class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func version() -> Int
```

## Return Value

The version number assigned to the class.

## Discussion

If no version has been set, the default is `0`.

Version numbers are needed for decoding or unarchiving, so older versions of an object can be detected and decoded correctly.

Caution should be taken when obtaining the version from within an `NSCoding` protocol or other methods. Use the class name explicitly when getting a class version number:

```objc
version = [MyClass version];
```

Don’t simply send `version` to the return value of class—a subclass version number may be returned instead.

### Special Considerations

The version number applies to `NSArchiver`/`NSUnarchiver`, but not to `NSKeyedArchiver`/`NSKeyedUnarchiver`.  A keyed archiver does not encode class version numbers.

## See Also

### Related Documentation

- [version(forClassName:)](<../../foundation/nscoder/version(forclassname_).md>) — This method is present for historical reasons and is not used with keyed archivers.

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
- [+ setVersion:](<setversion(__).md>) — Sets the receiver’s version number.
