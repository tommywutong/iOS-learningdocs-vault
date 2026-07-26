---
title: Contents Gravity Values
framework: Core Animation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/contents-gravity-values
source_url: 'https://developer.apple.com/documentation/quartzcore/contents-gravity-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/contents-gravity-values.json'
content_hash: 'sha256:b11ae760ed9555b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md) · [CALayer](calayer.md)

# Contents Gravity Values

<sub>API Collection</sub>

The contents gravity constants specify the position of the content object when the layer bounds is larger than the bounds of the content object. They are used by the [contentsGravity](calayer/contentsgravity.md) property.

## Topics

### Constants

- [kCAGravityCenter](calayercontentsgravity/center.md) — The content is horizontally and vertically centered in the bounds rectangle.
- [kCAGravityTop](calayercontentsgravity/top.md) — The content is horizontally centered at the top-edge of the bounds rectangle.
- [kCAGravityBottom](calayercontentsgravity/bottom.md) — The content is horizontally centered at the bottom-edge of the bounds rectangle.
- [kCAGravityLeft](calayercontentsgravity/left.md) — The content is vertically centered at the left-edge of the bounds rectangle.
- [kCAGravityRight](calayercontentsgravity/right.md) — The content is vertically centered at the right-edge of the bounds rectangle.
- [kCAGravityTopLeft](calayercontentsgravity/topleft.md) — The content is positioned in the top-left corner of the bounds rectangle.
- [kCAGravityTopRight](calayercontentsgravity/topright.md) — The content is positioned in the top-right corner of the bounds rectangle.
- [kCAGravityBottomLeft](calayercontentsgravity/bottomleft.md) — The content is positioned in the bottom-left corner of the bounds rectangle.
- [kCAGravityBottomRight](calayercontentsgravity/bottomright.md) — The content is positioned in the bottom-right corner of the bounds rectangle.
- [kCAGravityResize](calayercontentsgravity/resize.md) — The content is resized to fit the entire bounds rectangle.
- [kCAGravityResizeAspect](calayercontentsgravity/resizeaspect.md) — The content is resized to fit the bounds rectangle, preserving the aspect of the content. If the content does not completely fill the bounds rectangle, the content is centered in the partial axis.
- [kCAGravityResizeAspectFill](calayercontentsgravity/resizeaspectfill.md) — The content is resized to completely fill the bounds rectangle, while still preserving the aspect of the content. The content is centered in the axis it exceeds.

## See Also

### Modifying the layer’s appearance

- [contentsGravity](calayer/contentsgravity.md) — A constant that specifies how the layer’s contents are positioned or scaled within its bounds.
- [opacity](calayer/opacity.md) — The opacity of the receiver. Animatable.
- [hidden](calayer/ishidden.md) — A Boolean indicating whether the layer is displayed. Animatable.
- [masksToBounds](calayer/maskstobounds.md) — A Boolean indicating whether sublayers are clipped to the layer’s bounds. Animatable.
- [mask](calayer/mask.md) — An optional layer whose alpha channel is used to mask the layer’s content.
- [doubleSided](calayer/isdoublesided.md) — A Boolean indicating whether the layer displays its content when facing away from the viewer. Animatable.
- [cornerRadius](calayer/cornerradius.md) — The radius to use when drawing rounded corners for the layer’s background. Animatable.
- [maskedCorners](calayer/maskedcorners.md)
- [CACornerMask](cacornermask.md)
- [borderWidth](calayer/borderwidth.md) — The width of the layer’s border. Animatable.
- [borderColor](calayer/bordercolor.md) — The color of the layer’s border. Animatable.
- [backgroundColor](calayer/backgroundcolor.md) — The background color of the receiver. Animatable.
- [shadowOpacity](calayer/shadowopacity.md) — The opacity of the layer’s shadow. Animatable.
- [shadowRadius](calayer/shadowradius.md) — The blur radius (in points) used to render the layer’s shadow. Animatable.
- [shadowOffset](calayer/shadowoffset.md) — The offset (in points) of the layer’s shadow. Animatable.
