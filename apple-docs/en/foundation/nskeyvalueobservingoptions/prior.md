---
title: prior
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvalueobservingoptions/prior
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/prior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvalueobservingoptions/prior.json'
content_hash: 'sha256:4f9d65142f3e0406'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyValueObservingOptions](../nskeyvalueobservingoptions.md)

# prior

<sub>Type Property</sub>

Whether separate notifications should be sent to the observer before and after each change, instead of a single notification after the change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var prior: NSKeyValueObservingOptions { get }
```

## Discussion

The change dictionary in a notification sent before a change always contains an [NSKeyValueChangeNotificationIsPriorKey](../nskeyvaluechangekey/notificationispriorkey.md) entry whose value is an `NSNumber` object that contains the Boolean value [true](../../swift/true.md), but never contains an [NSKeyValueChangeNewKey](../nskeyvaluechangekey/newkey.md) entry. When this option is specified the change dictionary in a notification sent after a change contains the same entries that it would contain if this option were not specified. You can use this option when the observer’s own key-value observing-compliance requires it to invoke one of the `-willChange...` methods for one of its own properties, and the value of that property depends on the value of the observed object’s property. (In that situation it’s too late to easily invoke `-willChange...` properly in response to receiving an [observeValue(forKeyPath:of:change:context:)](<../../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>) message after the change.)

## See Also

### Constants

- [NSKeyValueObservingOptionNew](new.md) — Indicates that the change dictionary should provide the new attribute value, if applicable.
- [NSKeyValueObservingOptionOld](old.md) — Indicates that the change dictionary should contain the old attribute value, if applicable.
- [NSKeyValueObservingOptionInitial](initial.md) — If specified, a notification should be sent to the observer immediately, before the observer registration method even returns.
