---
title: 'filter(withName:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilterconstructor/filter(withname:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilterconstructor/filter(withname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilterconstructor/filter%28withname%3A%29.json'
content_hash: 'sha256:0736235dcc604706'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterConstructor](../cifilterconstructor.md)

# filter(withName:)

<sub>Instance Method</sub>

Returns a filter object specified by name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func filter(withName name: String) -> CIFilter?
```

## Parameters

- `name` — The name of the requested custom filter.

## Return Value

A [CIFilter](../cifilter-swift.class.md) object implementing the custom filter.

## Discussion

Core Image calls this method when a filter is requested by name using the [CIFilter](../cifilter-swift.class.md) class method [+ filterWithName:](<../cifilter-swift.class/init(name_).md>) method (or related methods). Your implementation of this method should provide a new instance of the [CIFilter](../cifilter-swift.class.md) subclass for your custom filter.

## See Also

### Related Documentation

- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
