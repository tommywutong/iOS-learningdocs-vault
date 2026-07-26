---
title: 'view(forUIConfiguration:excludedKeys:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/view(foruiconfiguration:excludedkeys:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/view(foruiconfiguration:excludedkeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/view%28foruiconfiguration%3Aexcludedkeys%3A%29.json'
content_hash: 'sha256:3f901bc5911a3238'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# view(forUIConfiguration:excludedKeys:)

<sub>Instance Method</sub>

Returns a filter view for the filter.

<sub>macOS</sub>

```swift
func view(forUIConfiguration inUIConfiguration: [AnyHashable : Any]!, excludedKeys inKeys: [Any]!) -> IKFilterUIView!
```

## Parameters

- `inUIConfiguration` — A dictionary that contains values for the [IKUISizeFlavor](../../quartz/ikuisizeflavor.md) and [kCIUIParameterSet](../kciuiparameterset.md) keys. For allowed values for the [IKUISizeFlavor](../../quartz/ikuisizeflavor.md) key, see [User Interface Options](../user-interface-options.md). For allowed values for the [kCIUIParameterSet](../kciuiparameterset.md) key, see [User Interface Control Options](../user-interface-control-options.md).

- `inKeys` — An array of the input keys for which you do _not_ want to provide a user interface. Pass `nil` if you want all input keys to be represented in the user interface.

## Return Value

An [IKFilterUIView](../../quartz/ikfilteruiview.md) object.

## Discussion

Calling this method to receive a view for a filter causes the [CIFilter](../cifilter-swift.class.md) class to invoke the [provideView(forUIConfiguration:excludedKeys:)](<../../quartz/ikfiltercustomuiprovider/provideview(foruiconfiguration_excludedkeys_).md>) method. If you override [provideView(forUIConfiguration:excludedKeys:)](<../../quartz/ikfiltercustomuiprovider/provideview(foruiconfiguration_excludedkeys_).md>) the user interface is created by your filter subclass. Otherwise, Core Image automatically generates the user interface based on the filter keys and attributes.

Your app can retrieve a view whose control sizes complement the size of user interface elements already used in the application. It is also possible to choose which filter input parameters appear in the view. Consumer applications, for example, may want to show a small, basic set of input parameters whereas professional applications may want to provide access to all input parameters.

When you request a user interface for a parameter set, all keys for that set and below are included. For example, the advanced set consists of all parameters in the basic, intermediate and advanced sets. The development set should contain parameters that are either experimental or for debugging purposes. You should use them only during the development of filters and client applications, and not in a shipping product.

The controls in the view use bindings to set the values of the filter. See [Cocoa Bindings Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i) if you are unfamiliar with bindings.
