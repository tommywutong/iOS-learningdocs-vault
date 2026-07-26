---
title: style
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/style
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/style'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/style.json'
content_hash: 'sha256:0ac3574d33239d73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# style

<sub>Instance Property</sub>

An optional dictionary used to store property values that aren’t explicitly defined by the layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var style: [AnyHashable : Any]? { get set }
```

## Discussion

This dictionary may in turn have a `style` key, forming a hierarchy of default values. In the case of hierarchical style dictionaries the shallowest value for a property is used. For example, the value for “style.someValue” takes precedence over “style.style.someValue”.

If the style dictionary does not define a value for an attribute, the receiver’s [+ defaultValueForKey:](<defaultvalue(forkey_).md>) method is called. The default value of this property is `nil`.

The style dictionary is not consulted for the following keys: `bounds`, `frame`.

> [!warning] Warning
> If the style dictionary or any of its ancestors are modified, the values of the layer’s properties are undefined until the `style` property is reset.

## See Also

### Modifying the layer’s appearance

- [contentsGravity](contentsgravity.md) — A constant that specifies how the layer’s contents are positioned or scaled within its bounds.
- [Contents Gravity Values](../contents-gravity-values.md) — The contents gravity constants specify the position of the content object when the layer bounds is larger than the bounds of the content object. They are used by the [contentsGravity](contentsgravity.md) property.
- [opacity](opacity.md) — The opacity of the receiver. Animatable.
- [hidden](ishidden.md) — A Boolean indicating whether the layer is displayed. Animatable.
- [masksToBounds](maskstobounds.md) — A Boolean indicating whether sublayers are clipped to the layer’s bounds. Animatable.
- [mask](mask.md) — An optional layer whose alpha channel is used to mask the layer’s content.
- [doubleSided](isdoublesided.md) — A Boolean indicating whether the layer displays its content when facing away from the viewer. Animatable.
- [cornerRadius](cornerradius.md) — The radius to use when drawing rounded corners for the layer’s background. Animatable.
- [maskedCorners](maskedcorners.md)
- [CACornerMask](../cacornermask.md)
- [borderWidth](borderwidth.md) — The width of the layer’s border. Animatable.
- [borderColor](bordercolor.md) — The color of the layer’s border. Animatable.
- [backgroundColor](backgroundcolor.md) — The background color of the receiver. Animatable.
- [shadowOpacity](shadowopacity.md) — The opacity of the layer’s shadow. Animatable.
- [shadowRadius](shadowradius.md) — The blur radius (in points) used to render the layer’s shadow. Animatable.
