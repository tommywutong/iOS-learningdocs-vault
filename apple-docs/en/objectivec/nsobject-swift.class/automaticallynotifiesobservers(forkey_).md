---
title: 'automaticallyNotifiesObservers(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/automaticallynotifiesobservers(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/automaticallynotifiesobservers(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/automaticallynotifiesobservers%28forkey%3A%29.json'
content_hash: 'sha256:4aebb3522bdc7028'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# automaticallyNotifiesObservers(forKey:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the observed object supports automatic key-value observation for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func automaticallyNotifiesObservers(forKey key: String) -> Bool
```

## Return Value

[YES](../yes.md) if the key-value observing machinery should automatically invoke [- willChangeValueForKey:](<willchangevalue(forkey_).md>)/[- didChangeValueForKey:](<didchangevalue(forkey_).md>) and [- willChange:valuesAtIndexes:forKey:](<willchange(__valuesat_forkey_).md>)/[- didChange:valuesAtIndexes:forKey:](<didchange(__valuesat_forkey_).md>) whenever instances of the class receive key-value coding messages for the `key`, or mutating key-value-coding-compliant methods for the `key` are invoked; otherwise [NO](../no.md).

## Discussion

The default implementation returns [YES](../yes.md). Starting in OS X 10.5, the default implementation of this method searches the receiving class for a method whose name matches the pattern `+automaticallyNotifiesObserversOf<Key>`, and returns the result of invoking that method if it is found. Any found methods must return `BOOL`. If no such method is found [YES](../yes.md) is returned.

## See Also

### Observing Customization

- [+ keyPathsForValuesAffectingValueForKey:](<keypathsforvaluesaffectingvalue(forkey_).md>) — Returns a set of key paths for properties whose values affect the value of the specified key.
- [NSKeyValueObservingCustomization](../../foundation/nskeyvalueobservingcustomization.md) — Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys
- [observationInfo](observationinfo.md) — Returns a pointer that identifies information about all of the observers that are registered with the observed object.
