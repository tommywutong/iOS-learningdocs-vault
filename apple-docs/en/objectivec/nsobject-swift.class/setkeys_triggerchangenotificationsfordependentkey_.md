---
title: 'setKeys:triggerChangeNotificationsForDependentKey:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/setkeys:triggerchangenotificationsfordependentkey:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setkeys:triggerchangenotificationsfordependentkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setkeys%3Atriggerchangenotificationsfordependentkey%3A.json'
content_hash: 'sha256:fa2cc0f023e0e1a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setKeys:triggerChangeNotificationsForDependentKey:

<sub>Type Method</sub>

Configures the observed object to post change notifications for a given property if any of the properties specified in a given array changes.

> [!warning] Deprecated
> Use the method [+ keyPathsForValuesAffectingValueForKey:](<keypathsforvaluesaffectingvalue(forkey_).md>) instead.

<sub>macOS</sub>

```objc
+ (void) setKeys:(NSArray *) keys triggerChangeNotificationsForDependentKey:(NSString *) dependentKey;
```

## Parameters

- `keys` — The names of the properties upon which the value of the property identified by `dependentKey` depends.

- `dependentKey` — The name of a property whose value depends on the properties specified by `keys`.

## Discussion

Invocations of will- and did-change KVO notification methods for any key in `keys` automatically invokes the corresponding change notification methods for `dependentKey`. The observed object does not receive `willChange` or `didChange` messages to generate the notifications.

Dependencies should be registered before any instances of the receiving class are created, so you typically invoke this method in a class’s [+ initialize](<initialize().md>) method, as illustrated in the following example.

```objc
+ (void)initialize {
    [self setKeys:@[@"firstName", @"lastName"] triggerChangeNotificationsForDependentKey:@"fullName"];
}
```

## See Also

### Deprecated Class Methods

- [+ defaultPlaceholderForMarker:withBinding:](<defaultplaceholder(for_with_).md>) — Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified. _(deprecated)_
- [+ setDefaultPlaceholder:forMarker:withBinding:](<setdefaultplaceholder(__for_with_).md>) — Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified. _(deprecated)_
- [+ useStoredAccessor](<usestoredaccessor().md>) — Returns `true` if the stored value methods [- storedValueForKey:](<storedvalue(forkey_).md>) and [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) should use private accessor methods in preference to public accessors. _(deprecated)_
