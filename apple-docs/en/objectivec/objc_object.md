---
title: objc_object
framework: Objective-C Runtime
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_object
source_url: 'https://developer.apple.com/documentation/objectivec/objc_object'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_object.json'
content_hash: 'sha256:970ed665091a62f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_object

<sub>Structure</sub>

Represents an instance of a class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct objc_object
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init(isa:)](<objc_object/init(isa_).md>)

### Instance Properties

- [isa](objc_object/isa.md) — A pointer to the class definition of which this object is an instance. _(deprecated)_

## See Also

### Instance Data Types

- [objc_super](objc_super-swift.struct.md) — Specifies the superclass of an instance.
