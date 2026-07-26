---
title: NSKeyValueObserving
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nskeyvalueobserving
source_url: 'https://developer.apple.com/documentation/objectivec/nskeyvalueobserving'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nskeyvalueobserving.json'
content_hash: 'sha256:e01f4840b044f834'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# NSKeyValueObserving

<sub>API Collection</sub>

An informal protocol that objects adopt to be notified of changes to the specified properties of other objects.

## Overview

You can observe any object properties including simple attributes, to-one relationships, and to-many relationships. Observers of to-many relationships are informed of the type of change made — as well as which objects are involved in the change.

[NSObject](nsobject-swift.class.md) provides an implementation of the [NSKeyValueObserving](nskeyvalueobserving.md) protocol that provides an automatic observing capability for all objects. You can further refine notifications by disabling automatic observer notifications and implementing manual notifications using the methods in this protocol.

## Topics

### Change Notification

- [- observeValueForKeyPath:ofObject:change:context:](<nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>) — Informs the observing object when the value at the specified key path relative to the observed object has changed.

### Registering for Observation

- [- addObserver:forKeyPath:options:context:](<nsobject-swift.class/addobserver(__forkeypath_options_context_).md>) — Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.
- [- removeObserver:forKeyPath:](<nsobject-swift.class/removeobserver(__forkeypath_).md>) — Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.
- [- removeObserver:forKeyPath:context:](<nsobject-swift.class/removeobserver(__forkeypath_context_).md>) — Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message, given the context.

### Notifying Observers of Changes

- [- willChangeValueForKey:](<nsobject-swift.class/willchangevalue(forkey_).md>) — Informs the observed object that the value of a given property is about to change.
- [- didChangeValueForKey:](<nsobject-swift.class/didchangevalue(forkey_).md>) — Informs the observed object that the value of a given property has changed.
- [- willChange:valuesAtIndexes:forKey:](<nsobject-swift.class/willchange(__valuesat_forkey_).md>) — Informs the observed object that the specified change is about to be executed at given indexes for a specified ordered to-many relationship.
- [- didChange:valuesAtIndexes:forKey:](<nsobject-swift.class/didchange(__valuesat_forkey_).md>) — Informs the observed object that the specified change has occurred on the indexes for a specified ordered to-many relationship.
- [- willChangeValueForKey:withSetMutation:usingObjects:](<nsobject-swift.class/willchangevalue(forkey_withsetmutation_using_).md>) — Informs the observed object that the specified change is about to be made to a specified unordered to-many relationship.
- [- didChangeValueForKey:withSetMutation:usingObjects:](<nsobject-swift.class/didchangevalue(forkey_withsetmutation_using_).md>) — Informs the observed object that the specified change was made to a specified unordered to-many relationship.

### Observing Customization

- [+ automaticallyNotifiesObserversForKey:](<nsobject-swift.class/automaticallynotifiesobservers(forkey_).md>) — Returns a Boolean value that indicates whether the observed object supports automatic key-value observation for the given key.
- [+ keyPathsForValuesAffectingValueForKey:](<nsobject-swift.class/keypathsforvaluesaffectingvalue(forkey_).md>) — Returns a set of key paths for properties whose values affect the value of the specified key.
- [NSKeyValueObservingCustomization](../foundation/nskeyvalueobservingcustomization.md) — Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys
- [observationInfo](nsobject-swift.class/observationinfo.md) — Returns a pointer that identifies information about all of the observers that are registered with the observed object.

### Constants

- [NSKeyValueObservation](../foundation/nskeyvalueobservation.md)
- [NSKeyValueObservedChange](../foundation/nskeyvalueobservedchange.md)
- [NSKeyValueChange](../foundation/nskeyvaluechange.md) — The kinds of changes that can be observed.
- [NSKeyValueObservingOptions](../foundation/nskeyvalueobservingoptions.md) — The values that can be returned in a change dictionary.
- [NSKeyValueChangeKey](../foundation/nskeyvaluechangekey.md) — The keys that can appear in the change dictionary.
- [NSKeyValueSetMutationKind](../foundation/nskeyvaluesetmutationkind.md)

## See Also

### Related Documentation

- [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)
