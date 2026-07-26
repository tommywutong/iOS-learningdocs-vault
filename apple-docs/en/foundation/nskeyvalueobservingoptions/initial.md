---
title: initial
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvalueobservingoptions/initial
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/initial'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvalueobservingoptions/initial.json'
content_hash: 'sha256:bed648eb28f2417d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyValueObservingOptions](../nskeyvalueobservingoptions.md)

# initial

<sub>Type Property</sub>

If specified, a notification should be sent to the observer immediately, before the observer registration method even returns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var initial: NSKeyValueObservingOptions { get }
```

## Discussion

The change dictionary in the notification will always contain an [NSKeyValueChangeNewKey](../nskeyvaluechangekey/newkey.md) entry if [NSKeyValueObservingOptionNew](new.md) is also specified but will never contain an [NSKeyValueChangeOldKey](../nskeyvaluechangekey/oldkey.md) entry. (In an initial notification the current value of the observed property may be old, but it’s new to the observer.) You can use this option instead of explicitly invoking, at the same time, code that is also invoked by the observer’s [observeValue(forKeyPath:of:change:context:)](<../../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>) method. When this option is used with[addObserver(_:forKeyPath:options:context:)](<../../objectivec/nsobject-swift.class/addobserver(__forkeypath_options_context_).md>) a notification will be sent for each indexed object to which the observer is being added.

## See Also

### Constants

- [NSKeyValueObservingOptionNew](new.md) — Indicates that the change dictionary should provide the new attribute value, if applicable.
- [NSKeyValueObservingOptionOld](old.md) — Indicates that the change dictionary should contain the old attribute value, if applicable.
- [NSKeyValueObservingOptionPrior](prior.md) — Whether separate notifications should be sent to the observer before and after each change, instead of a single notification after the change.
