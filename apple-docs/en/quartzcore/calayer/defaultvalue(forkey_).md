---
title: 'defaultValue(forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/defaultvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/defaultvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/defaultvalue%28forkey%3A%29.json'
content_hash: 'sha256:0649eb4e76c43c98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# defaultValue(forKey:)

<sub>Type Method</sub>

Specifies the default value associated with the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func defaultValue(forKey key: String) -> Any?
```

## Parameters

- `key` — The name of one of the receiver’s properties.

## Return Value

The default value for the named property. Returns `nil` if no default value has been set.

## Discussion

If you define custom properties for a layer but do not set a value, this method returns a suitable “zero” default value based on the expected value of the `key`. For example, if the value for `key` is a [CGSize](../../corefoundation/cgsize.md) struct, the method returns a size struct containing (0.0,0.0) wrapped in an [NSValue](../../foundation/nsvalue.md) object. For a [CGRect](../../corefoundation/cgrect.md) an empty rectangle is returned. For [CGAffineTransform](../../corefoundation/cgaffinetransform.md) and [CATransform3D](../catransform3d.md), the appropriate identity matrix is returned.

### Special Considerations

If `key` is not a known for property of the class, the result of the method is undefined.

## See Also

### Key-value coding extensions

- [- shouldArchiveValueForKey:](<shouldarchivevalue(forkey_).md>) — Returns a Boolean indicating whether the value of the specified key should be archived.
