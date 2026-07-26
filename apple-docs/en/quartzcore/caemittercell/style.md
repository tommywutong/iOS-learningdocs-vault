---
title: style
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/style
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/style'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/style.json'
content_hash: 'sha256:c868f27fb7ff15c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# style

<sub>Instance Property</sub>

An optional dictionary containing additional style values that are not explicitly defined by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var style: [AnyHashable : Any]? { get set }
```

## Discussion

This dictionary may in turn have a `style` key, forming a hierarchy of default values. In the case of hierarchical style dictionaries the shallowest value for a property is used. For example, the value for “style.someValue” takes precedence over “style.style.someValue”.

If the style dictionary doesn’t define a value for an attribute, the cell’s [+ defaultValueForKey:](<defaultvalue(forkey_).md>) class method is called.

The style dictionary is not consulted for the following keys: `bounds`, `frame`.

The default value of this property is `nil`.

> [!warning] Warning
> If the style dictionary or any of its ancestors are modified, the values of the cell’s properties are undefined until the `style` property is reset.

## See Also

### Setting Emitter Cell Visual Attributes

- [enabled](isenabled.md) — A Boolean value indicating whether or not cells from this emitter are rendered.
- [color](color.md) — The color of each emitted object. Animatable.
- [redRange](redrange.md) — The amount by which the red color component of the cell can vary. Animatable.
- [greenRange](greenrange.md) — The amount by which the green color component of the cell can vary. Animatable.
- [blueRange](bluerange.md) — The amount by which the blue color component of the cell can vary. Animatable.
- [alphaRange](alpharange.md) — The amount by which the alpha component of the cell can vary. Animatable.
- [redSpeed](redspeed.md) — The speed, in seconds, at which the red color component changes over the lifetime of the cell. Animatable.
- [greenSpeed](greenspeed.md) — The speed, in seconds, at which the green color component changes over the lifetime of the cell. Animatable.
- [blueSpeed](bluespeed.md) — The speed, in seconds, at which the blue color component changes over the lifetime of the cell. Animatable.
- [alphaSpeed](alphaspeed.md) — The speed, in seconds, at which the alpha component changes over the lifetime of the cell. Animatable.
- [magnificationFilter](magnificationfilter.md) — The filter used when increasing the size of the content.
- [minificationFilter](minificationfilter.md) — The filter used when reducing the size of the content.
- [minificationFilterBias](minificationfilterbias.md) — The bias factor used by the minification filter to determine the levels of detail.
- [scale](scale.md) — Specifies the scale factor applied to the cell. Animatable.
- [scaleRange](scalerange.md) — Specifies the range over which the scale value can vary. Animatable.
