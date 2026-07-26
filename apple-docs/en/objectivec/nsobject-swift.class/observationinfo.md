---
title: observationInfo
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/observationinfo
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observationinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/observationinfo.json'
content_hash: 'sha256:ad538dc355b74aa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# observationInfo

<sub>Instance Property</sub>

Returns a pointer that identifies information about all of the observers that are registered with the observed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var observationInfo: UnsafeMutableRawPointer? { get set }
```

## Return Value

A pointer that identifies information about all of the observers that are registered with the observed object, the options that were used at registration-time, and so on.

## Discussion

The default implementation of this method retrieves the information from a global dictionary of observed objects keyed by memory addresses.

For improved performance, both this property and [observationInfo](observationinfo.md) can be overridden to store the opaque data pointer in an instance variable. Overrides of this property must not attempt to send messages to the stored data.

## See Also

### Observing Customization

- [+ automaticallyNotifiesObserversForKey:](<automaticallynotifiesobservers(forkey_).md>) — Returns a Boolean value that indicates whether the observed object supports automatic key-value observation for the given key.
- [+ keyPathsForValuesAffectingValueForKey:](<keypathsforvaluesaffectingvalue(forkey_).md>) — Returns a set of key paths for properties whose values affect the value of the specified key.
- [NSKeyValueObservingCustomization](../../foundation/nskeyvalueobservingcustomization.md) — Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys
