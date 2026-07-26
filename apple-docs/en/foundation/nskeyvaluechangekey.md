---
title: NSKeyValueChangeKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvaluechangekey
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvaluechangekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvaluechangekey.json'
content_hash: 'sha256:44116b3aac4f1bc5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyValueChangeKey

<sub>Structure</sub>

The keys that can appear in the change dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSKeyValueChangeKey
```

## Discussion

These constants are used as keys in the change dictionary passed to [observeValue(forKeyPath:of:change:context:)](<../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [NSKeyValueChangeIndexesKey](nskeyvaluechangekey/indexeskey.md) — If the value of the [NSKeyValueChangeKindKey](nskeyvaluechangekey/kindkey.md) entry is [NSKeyValueChangeInsertion](nskeyvaluechange/insertion.md), [NSKeyValueChangeRemoval](nskeyvaluechange/removal.md), or [NSKeyValueChangeReplacement](nskeyvaluechange/replacement.md), the value of this key is an `NSIndexSet` object that contains the indexes of the inserted, removed, or replaced objects.
- [NSKeyValueChangeKindKey](nskeyvaluechangekey/kindkey.md) — An `NSNumber` object that contains a value corresponding to one of the [NSKeyValueChange](nskeyvaluechange.md) enums, indicating what sort of change has occurred.
- [NSKeyValueChangeNewKey](nskeyvaluechangekey/newkey.md) — If the value of the [NSKeyValueChangeKindKey](nskeyvaluechangekey/kindkey.md) entry is [NSKeyValueChangeSetting](nskeyvaluechange/setting.md), and [NSKeyValueObservingOptionNew](nskeyvalueobservingoptions/new.md) was specified when the observer was registered, the value of this key is the new value for the attribute.
- [NSKeyValueChangeNotificationIsPriorKey](nskeyvaluechangekey/notificationispriorkey.md) — If the [NSKeyValueObservingOptionPrior](nskeyvalueobservingoptions/prior.md) option was specified when the observer was registered this notification is sent prior to a change.
- [NSKeyValueChangeOldKey](nskeyvaluechangekey/oldkey.md) — If the value of the [NSKeyValueChangeKindKey](nskeyvaluechangekey/kindkey.md) entry is [NSKeyValueChangeSetting](nskeyvaluechange/setting.md), and [NSKeyValueObservingOptionOld](nskeyvalueobservingoptions/old.md) was specified when the observer was registered, the value of this key is the value before the attribute was changed.

### Initializers

- [init(rawValue:)](<nskeyvaluechangekey/init(rawvalue_).md>)

## See Also

### Structures

- [AsyncCharacterSequence](asynccharactersequence.md) — An asynchronous sequence of characters.
- [AsyncLineSequence](asynclinesequence.md) — An asynchronous sequence of lines of text.
- [AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md) — An asychronous sequence of Unicode scalar values.
- [Expression](expression.md)
- [NSAttributedStringFormattingContextKey](nsattributedstringformattingcontextkey.md) — A type that represents a key in the formatting context dictionary.
- [NSKeyValueObservedChange](nskeyvalueobservedchange.md)
- [NSKeyValueOperator](nskeyvalueoperator.md) — These constants define the available array operators. See [Using Collection Operators](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
- [PresentationIntent](presentationintent.md) — A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.
