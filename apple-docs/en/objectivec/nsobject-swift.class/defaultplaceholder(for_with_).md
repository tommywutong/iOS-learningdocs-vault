---
title: 'defaultPlaceholder(for:with:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/defaultplaceholder(for:with:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/defaultplaceholder(for:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/defaultplaceholder%28for%3Awith%3A%29.json'
content_hash: 'sha256:682d86e4273eab3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# defaultPlaceholder(for:with:)

<sub>Type Method</sub>

Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.

<sub>macOS</sub>

```swift
class func defaultPlaceholder(for marker: Any?, with binding: NSBindingName) -> Any?
```

## Discussion

The `marker` can be `nil` or one of the constants described in [Selection Markers](../../appkit/selection-markers.md).

## See Also

### Deprecated Class Methods

- [+ setDefaultPlaceholder:forMarker:withBinding:](<setdefaultplaceholder(__for_with_).md>) — Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified. _(deprecated)_
- [+ useStoredAccessor](<usestoredaccessor().md>) — Returns `true` if the stored value methods [- storedValueForKey:](<storedvalue(forkey_).md>) and [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) should use private accessor methods in preference to public accessors. _(deprecated)_
