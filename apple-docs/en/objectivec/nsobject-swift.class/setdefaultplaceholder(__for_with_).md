---
title: 'setDefaultPlaceholder(_:for:with:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/setdefaultplaceholder(_:for:with:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setdefaultplaceholder(_:for:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setdefaultplaceholder%28_%3Afor%3Awith%3A%29.json'
content_hash: 'sha256:b42c7baef66cf0b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setDefaultPlaceholder(_:for:with:)

<sub>Type Method</sub>

Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.

<sub>macOS</sub>

```swift
class func setDefaultPlaceholder(_ placeholder: Any?, for marker: Any?, with binding: NSBindingName)
```

## Discussion

The `marker` can be `nil` or one of the constants described in [Selection Markers](../../appkit/selection-markers.md).

## See Also

### Related Documentation

- [Cocoa Bindings Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i)

### Deprecated Class Methods

- [+ defaultPlaceholderForMarker:withBinding:](<defaultplaceholder(for_with_).md>) — Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified. _(deprecated)_
- [+ useStoredAccessor](<usestoredaccessor().md>) — Returns `true` if the stored value methods [- storedValueForKey:](<storedvalue(forkey_).md>) and [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) should use private accessor methods in preference to public accessors. _(deprecated)_
