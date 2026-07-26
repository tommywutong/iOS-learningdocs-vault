---
title: 'handleQuery(withUnboundKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/handlequery(withunboundkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/handlequery(withunboundkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/handlequery%28withunboundkey%3A%29.json'
content_hash: 'sha256:554e0e1d027dcbc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# handleQuery(withUnboundKey:)

<sub>Instance Method</sub>

Invoked by [- valueForKey:](<value(forkey_).md>) when it finds no property corresponding to `key`.

> [!warning] Deprecated
> Use [- valueForUndefinedKey:](<value(forundefinedkey_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func handleQuery(withUnboundKey key: String) -> Any?
```

## See Also

### Deprecated Methods

- [+ useStoredAccessor](<usestoredaccessor().md>) — Returns `true` if the stored value methods [- storedValueForKey:](<storedvalue(forkey_).md>) and [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) should use private accessor methods in preference to public accessors. _(deprecated)_
- [- handleTakeValue:forUnboundKey:](<handletakevalue(__forunboundkey_).md>) — Invoked by [- takeValue:forKey:](<takevalue(__forkey_).md>) when it finds no property binding for `key`. _(deprecated)_
- [- storedValueForKey:](<storedvalue(forkey_).md>) — Returns the property identified by a given key. _(deprecated)_
- [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) — Sets the value of the property identified by a given key. _(deprecated)_
- [- takeValuesFromDictionary:](<takevalues(from_).md>) — Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties _(deprecated)_
- [- takeValue:forKeyPath:](<takevalue(__forkeypath_).md>) — Sets the value for the property identified by `keyPath` to `value`. _(deprecated)_
- [- takeValue:forKey:](<takevalue(__forkey_).md>) — Sets the value for the property identified by `key` to `value`. _(deprecated)_
- [- unableToSetNilForKey:](<unabletosetnil(forkey_).md>) — Invoked if `key` is represented by a scalar attribute. _(deprecated)_
- [- valuesForKeys:](<values(forkeys_).md>) — Returns a dictionary containing as keys the property names in `keys`, with corresponding values being the corresponding property values. _(deprecated)_
