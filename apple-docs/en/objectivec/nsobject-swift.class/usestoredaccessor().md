---
title: useStoredAccessor()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/usestoredaccessor()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/usestoredaccessor()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/usestoredaccessor%28%29.json'
content_hash: 'sha256:4a6400e5d697bf06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# useStoredAccessor()

<sub>Type Method</sub>

Returns `true` if the stored value methods [- storedValueForKey:](<storedvalue(forkey_).md>) and [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) should use private accessor methods in preference to public accessors.

> [!warning] Deprecated
> This method has no direct replacement, although see [accessInstanceVariablesDirectly](accessinstancevariablesdirectly.md).

<sub>tvOS, visionOS, watchOS</sub>

```swift
class func useStoredAccessor() -> Bool
```

## Discussion

Returning [NO](../no.md) causes the stored value methods to use the same accessor method or instance variable search order as the corresponding basic key-value coding methods ([- valueForKey:](<value(forkey_).md>) and [- takeValue:forKey:](<takevalue(__forkey_).md>)). The default implementation returns [YES](../yes.md).

Applications should use the `valueForKey:` and `setValue:forKey:` methods instead of `storedValueForKey:` and `takeStoredValue:forKey:`.

## See Also

### Deprecated Class Methods

- [+ defaultPlaceholderForMarker:withBinding:](<defaultplaceholder(for_with_).md>) — Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified. _(deprecated)_
- [+ setDefaultPlaceholder:forMarker:withBinding:](<setdefaultplaceholder(__for_with_).md>) — Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified. _(deprecated)_
