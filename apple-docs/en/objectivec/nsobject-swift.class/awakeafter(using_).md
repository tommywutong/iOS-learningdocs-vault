---
title: 'awakeAfter(using:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/awakeafter(using:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/awakeafter(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/awakeafter%28using%3A%29.json'
content_hash: 'sha256:25c4c794cf1a794d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# awakeAfter(using:)

<sub>Instance Method</sub>

Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func awakeAfter(using coder: NSCoder) -> Any?
```

## Parameters

- `coder` — The decoder used to decode the receiver.

## Return Value

The receiver, or another object to take the place of the object that was decoded and subsequently received this message.

## Discussion

You can use this method to eliminate redundant objects created by the coder. For example, if after decoding an object you discover that an equivalent object already exists, you can return the existing object. If a replacement is returned, your overriding method is responsible for releasing the receiver.

This method is invoked by `NSCoder`. `NSObject`’s implementation simply returns `self`.

## See Also

### Related Documentation

- [init(coder:)](<../../foundation/nscoding/init(coder_).md>) — Initializes the receiver from data in a given unarchiver.

### Archiving

- [classForArchiver](classforarchiver.md) — The class to substitute for the receiver’s own class during archiving.
- [classForCoder](classforcoder.md) — Overridden by subclasses to substitute a class other than its own during coding.
- [classForKeyedArchiver](classforkeyedarchiver.md) — Subclasses to substitute a new class for instances during keyed archiving.
- [+ classFallbacksForKeyedArchiver](<classfallbacksforkeyedarchiver().md>) — Overridden to return the names of classes that can be used to decode objects if their class is unavailable.
- [+ classForKeyedUnarchiver](<classforkeyedunarchiver().md>) — Overridden by subclasses to substitute a new class during keyed unarchiving.
- [- replacementObjectForArchiver:](<replacementobject(for_)-8ih2x.md>) — Overridden by subclasses to substitute another object for itself during archiving. _(deprecated)_
- [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) — Overridden by subclasses to substitute another object for itself during encoding.
- [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) — Overridden by subclasses to substitute another object for itself during keyed archiving.
- [+ setVersion:](<setversion(__).md>) — Sets the receiver’s version number.
- [+ version](<version().md>) — Returns the version number assigned to the class.
