---
title: kindKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvaluechangekey/kindkey
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvaluechangekey/kindkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvaluechangekey/kindkey.json'
content_hash: 'sha256:b4846f8ecb00696c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyValueChangeKey](../nskeyvaluechangekey.md)

# kindKey

<sub>Type Property</sub>

An `NSNumber` object that contains a value corresponding to one of the [NSKeyValueChange](../nskeyvaluechange.md) enums, indicating what sort of change has occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let kindKey: NSKeyValueChangeKey
```

## Discussion

A value of [NSKeyValueChangeSetting](../nskeyvaluechange/setting.md) indicates that the observed object has received a [setValue(_:forKey:)](<../../objectivec/nsobject-swift.class/setvalue(__forkey_).md>) message, or that the key-value-coding-compliant set method for the key has been invoked, or that one of the [willChangeValue(forKey:)](<../../objectivec/nsobject-swift.class/willchangevalue(forkey_).md>) or [didChangeValue(forKey:)](<../../objectivec/nsobject-swift.class/didchangevalue(forkey_).md>) methods has otherwise been invoked.

A value of [NSKeyValueChangeInsertion](../nskeyvaluechange/insertion.md), [NSKeyValueChangeRemoval](../nskeyvaluechange/removal.md), or [NSKeyValueChangeReplacement](../nskeyvaluechange/replacement.md) indicates that mutating messages have been sent a key-value observing compliant collection proxy, or that one of the key-value-coding-compliant collection mutation methods for the key has been invoked, or a collection will change or did change method has been otherwise been invoked.

You can use the [unsignedIntegerValue](../nsnumber/uintvalue.md) method on the `NSNumber` object to retrieve the value of the change kind.

## See Also

### Type Properties

- [NSKeyValueChangeIndexesKey](indexeskey.md) — If the value of the [NSKeyValueChangeKindKey](kindkey.md) entry is [NSKeyValueChangeInsertion](../nskeyvaluechange/insertion.md), [NSKeyValueChangeRemoval](../nskeyvaluechange/removal.md), or [NSKeyValueChangeReplacement](../nskeyvaluechange/replacement.md), the value of this key is an `NSIndexSet` object that contains the indexes of the inserted, removed, or replaced objects.
- [NSKeyValueChangeNewKey](newkey.md) — If the value of the [NSKeyValueChangeKindKey](kindkey.md) entry is [NSKeyValueChangeSetting](../nskeyvaluechange/setting.md), and [NSKeyValueObservingOptionNew](../nskeyvalueobservingoptions/new.md) was specified when the observer was registered, the value of this key is the new value for the attribute.
- [NSKeyValueChangeNotificationIsPriorKey](notificationispriorkey.md) — If the [NSKeyValueObservingOptionPrior](../nskeyvalueobservingoptions/prior.md) option was specified when the observer was registered this notification is sent prior to a change.
- [NSKeyValueChangeOldKey](oldkey.md) — If the value of the [NSKeyValueChangeKindKey](kindkey.md) entry is [NSKeyValueChangeSetting](../nskeyvaluechange/setting.md), and [NSKeyValueObservingOptionOld](../nskeyvalueobservingoptions/old.md) was specified when the observer was registered, the value of this key is the value before the attribute was changed.
