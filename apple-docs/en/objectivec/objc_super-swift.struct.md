---
title: objc_super
framework: Objective-C Runtime
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_super-swift.struct
source_url: 'https://developer.apple.com/documentation/objectivec/objc_super-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_super-swift.struct.json'
content_hash: 'sha256:e714df29a72dd3b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_super

<sub>Structure</sub>

Specifies the superclass of an instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct objc_super
```

## Discussion

The compiler generates an `objc_super` data structure when it encounters the `super` keyword as the receiver of a message. It specifies the class definition of the particular superclass that should be messaged.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Fields

- [receiver](objc_super-swift.struct/receiver.md) — A pointer of type [objc_object](objc_object.md). Specifies an instance of a class.
- [super_class](objc_super-swift.struct/super_class.md) — A pointer to a [Class](class.md) data structure. Specifies the particular superclass of the instance to message.

### Instance Properties

- [receiver](objc_super-swift.struct/receiver.md) — A pointer of type [objc_object](objc_object.md). Specifies an instance of a class.
- [super_class](objc_super-swift.struct/super_class.md) — A pointer to a [Class](class.md) data structure. Specifies the particular superclass of the instance to message.

### Initializers

- [init(receiver:super_class:)](<objc_super-swift.struct/init(receiver_super_class_).md>)

## See Also

### Instance Data Types

- [objc_object](objc_object.md) — Represents an instance of a class.
