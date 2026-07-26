---
title: indexesKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvaluechangekey/indexeskey
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvaluechangekey/indexeskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvaluechangekey/indexeskey.json'
content_hash: 'sha256:5ada45406b71e99d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyValueChangeKey](../nskeyvaluechangekey.md)

# indexesKey

<sub>Type Property</sub>

If the value of the [NSKeyValueChangeKindKey](kindkey.md) entry is [NSKeyValueChangeInsertion](../nskeyvaluechange/insertion.md), [NSKeyValueChangeRemoval](../nskeyvaluechange/removal.md), or [NSKeyValueChangeReplacement](../nskeyvaluechange/replacement.md), the value of this key is an `NSIndexSet` object that contains the indexes of the inserted, removed, or replaced objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let indexesKey: NSKeyValueChangeKey
```

## See Also

### Type Properties

- [NSKeyValueChangeKindKey](kindkey.md) — An `NSNumber` object that contains a value corresponding to one of the [NSKeyValueChange](../nskeyvaluechange.md) enums, indicating what sort of change has occurred.
- [NSKeyValueChangeNewKey](newkey.md) — If the value of the [NSKeyValueChangeKindKey](kindkey.md) entry is [NSKeyValueChangeSetting](../nskeyvaluechange/setting.md), and [NSKeyValueObservingOptionNew](../nskeyvalueobservingoptions/new.md) was specified when the observer was registered, the value of this key is the new value for the attribute.
- [NSKeyValueChangeNotificationIsPriorKey](notificationispriorkey.md) — If the [NSKeyValueObservingOptionPrior](../nskeyvalueobservingoptions/prior.md) option was specified when the observer was registered this notification is sent prior to a change.
- [NSKeyValueChangeOldKey](oldkey.md) — If the value of the [NSKeyValueChangeKindKey](kindkey.md) entry is [NSKeyValueChangeSetting](../nskeyvaluechange/setting.md), and [NSKeyValueObservingOptionOld](../nskeyvalueobservingoptions/old.md) was specified when the observer was registered, the value of this key is the value before the attribute was changed.
