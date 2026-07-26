---
title: NSKeyValueObservingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvalueobservingoptions
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvalueobservingoptions.json'
content_hash: 'sha256:df07ed95a0db9402'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyValueObservingOptions

<sub>Structure</sub>

The values that can be returned in a change dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSKeyValueObservingOptions
```

## Overview

These constants are passed to [addObserver(_:forKeyPath:options:context:)](<../objectivec/nsobject-swift.class/addobserver(__forkeypath_options_context_).md>) and determine the values that are returned as part of the change dictionary passed to an [observeValue(forKeyPath:of:change:context:)](<../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>). You can pass `0` if you require no change dictionary values.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [NSKeyValueObservingOptionNew](nskeyvalueobservingoptions/new.md) — Indicates that the change dictionary should provide the new attribute value, if applicable.
- [NSKeyValueObservingOptionOld](nskeyvalueobservingoptions/old.md) — Indicates that the change dictionary should contain the old attribute value, if applicable.
- [NSKeyValueObservingOptionInitial](nskeyvalueobservingoptions/initial.md) — If specified, a notification should be sent to the observer immediately, before the observer registration method even returns.
- [NSKeyValueObservingOptionPrior](nskeyvalueobservingoptions/prior.md) — Whether separate notifications should be sent to the observer before and after each change, instead of a single notification after the change.

### Initializers

- [init(rawValue:)](<nskeyvalueobservingoptions/init(rawvalue_).md>)

## See Also

### Enumerations

- [NSGrammaticalCase](nsgrammaticalcase.md)
- [NSGrammaticalDefiniteness](nsgrammaticaldefiniteness.md)
- [NSGrammaticalDetermination](nsgrammaticaldetermination.md)
- [NSGrammaticalPerson](nsgrammaticalperson.md)
- [NSGrammaticalPronounType](nsgrammaticalpronountype.md)
- [NSKeyValueChange](nskeyvaluechange.md) — The kinds of changes that can be observed.
- [NSKeyValueSetMutationKind](nskeyvaluesetmutationkind.md)
