---
title: NSKeyValueChange
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvaluechange
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvaluechange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvaluechange.json'
content_hash: 'sha256:19740c3c2a8f624a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyValueChange

<sub>Enumeration</sub>

The kinds of changes that can be observed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSKeyValueChange
```

## Overview

These constants are returned as the value for a [NSKeyValueChangeKindKey](nskeyvaluechangekey/kindkey.md) key in the change dictionary passed to [observeValue(forKeyPath:of:change:context:)](<../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>) indicating the type of change made.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSKeyValueChangeSetting](nskeyvaluechange/setting.md) — Indicates that the value of the observed key path was set to a new value. This change can occur when observing an attribute of an object, as well as properties that specify to-one and to-many relationships.
- [NSKeyValueChangeInsertion](nskeyvaluechange/insertion.md) — Indicates that an object has been inserted into the to-many relationship that is being observed.
- [NSKeyValueChangeRemoval](nskeyvaluechange/removal.md) — Indicates that an object has been removed from the to-many relationship that is being observed.
- [NSKeyValueChangeReplacement](nskeyvaluechange/replacement.md) — Indicates that an object has been replaced in the to-many relationship that is being observed.

### Initializers

- [init(rawValue:)](<nskeyvaluechange/init(rawvalue_).md>)

## See Also

### Enumerations

- [NSGrammaticalCase](nsgrammaticalcase.md)
- [NSGrammaticalDefiniteness](nsgrammaticaldefiniteness.md)
- [NSGrammaticalDetermination](nsgrammaticaldetermination.md)
- [NSGrammaticalPerson](nsgrammaticalperson.md)
- [NSGrammaticalPronounType](nsgrammaticalpronountype.md)
- [NSKeyValueObservingOptions](nskeyvalueobservingoptions.md) — The values that can be returned in a change dictionary.
- [NSKeyValueSetMutationKind](nskeyvaluesetmutationkind.md)
