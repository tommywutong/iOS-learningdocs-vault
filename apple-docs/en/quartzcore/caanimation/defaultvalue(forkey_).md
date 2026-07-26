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
doc_path: '/documentation/quartzcore/caanimation/defaultvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimation/defaultvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimation/defaultvalue%28forkey%3A%29.json'
content_hash: 'sha256:ec8f0344d2d586db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimation](../caanimation.md)

# defaultValue(forKey:)

<sub>Type Method</sub>

Specifies the default value of the property with the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func defaultValue(forKey key: String) -> Any?
```

## Parameters

- `key` — The name of one of the receiver’s properties.

## Return Value

The default value for the named property. Returns `nil` if no default value has been set.

## Discussion

If this method returns `nil` a suitable “zero” default value for the property is provided, based on the declared type of the `key`. For example, if `key` is a `CGSize` object, a size of (0.0,0.0) is returned. For a `CGRect` an empty rectangle is returned. For `CGAffineTransform` and `CATransform3D`, the appropriate identity matrix is returned.

### Special Considerations

If `key` is not a known for property of the class, the result of the method is undefined.
