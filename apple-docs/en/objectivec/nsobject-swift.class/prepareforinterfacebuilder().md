---
title: prepareForInterfaceBuilder()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/prepareforinterfacebuilder()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/prepareforinterfacebuilder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/prepareforinterfacebuilder%28%29.json'
content_hash: 'sha256:600b4887efdad6fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# prepareForInterfaceBuilder()

<sub>Instance Method</sub>

Called when a designable object is created in Interface Builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func prepareForInterfaceBuilder()
```

## Discussion

When Interface Builder instantiates a class with the `IB_DESIGNABLE` attribute, it calls this method to let the resulting object know that it was created at design time. You can implement this method in your designable classes and use it to configure their design-time appearance. For example, you might use the method to configure a custom text control with a default string. The system does not call this method; only Interface Builder calls it.

Interface Builder waits until all objects in a graph have been created and initialized before calling this method. So if your object’s runtime configuration relies on subviews or parent views, those objects should exist by the time this method is called.

Your implementation of this method must call `super` at some point so that parent classes can perform their own custom setup.
