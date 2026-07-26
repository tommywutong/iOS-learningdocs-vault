---
title: CFRunLoopMode
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopmode
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopmode.json'
content_hash: 'sha256:3c4e48454092198c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopMode

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFRunLoopMode
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) — Objects added to a run loop using this value as the mode are monitored by all run loop modes that have been declared as a member of the set of “common” modes with [CFRunLoopAddCommonMode](<cfrunloopaddcommonmode(____).md>).
- [kCFRunLoopDefaultMode](cfrunloopmode/defaultmode.md) — Run loop mode that should be used when a thread is in its default, or idle, state, waiting for an event. This mode is used when the run loop is started with [CFRunLoopRun](<cfrunlooprun().md>).

### Initializers

- [init(_:)](<cfrunloopmode/init(__).md>)
- [init(rawValue:)](<cfrunloopmode/init(rawvalue_).md>)

## See Also

### Data Types

- [CFAllocatorTypeID](cfallocatortypeid.md)
- [CFCalendarIdentifier](cfcalendaridentifier.md)
- [CFDateFormatterKey](cfdateformatterkey.md)
- [CFErrorDomain](cferrordomain.md)
- [CFLocaleIdentifier](cflocaleidentifier.md)
- [CFLocaleKey](cflocalekey.md)
- [CFNotificationName](cfnotificationname.md)
- [CFNumberFormatterKey](cfnumberformatterkey.md)
- [CFStreamPropertyKey](cfstreampropertykey.md)
- [CFTypeRef](cftyperef.md) — An untyped “generic” reference to any Core Foundation object.
