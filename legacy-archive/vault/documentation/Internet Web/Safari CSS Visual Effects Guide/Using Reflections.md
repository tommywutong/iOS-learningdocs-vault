---
title: Safari CSS Visual Effects Guide
apple_id: TP40008032
resource_type: Guide
platform: iAd System JS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/SafariVisualEffectsProgGuide/Reflections/Reflections.html
archived_at: '2026-07-15T07:43:59.399862Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari CSS Visual Effects Guide](Introduction.md)


[Next](Using%20CSS%20Filters.md)[Previous](Using%20Masks.md)

# Using Reflections

A reflection is a mirror image, optionally with its own mask. You can add a reflection to any visible HTML element. Reflections update automatically as the element’s appearance changes. If you hover over a link with a reflection, for example, you see the hover effect in the reflection. If you add a reflection to a [video](../../Apple%20Applications/Safari%20HTML%20Reference/Supported%20HTML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi3dellwnfsgk3y), the video plays in the reflection as well. Resize the element and the reflection is resized. Reflections are not interactive elements, however—clicking or touching a reflection does not generate any events.

Reflections have no effect on layout other than being part of a container’s overflow, and are similar to box shadows in this respect. In other words, you must position elements explicitly to allow space for reflections; if you add a reflection below an image, and follow the image with a paragraph of text, the reflection may cover the text (depending on the size of the image, padding, margins, and so on).

Use the `-webkit-box-reflect` property to add a reflection to an element. The first, mandatory, parameter is the direction in which the reflection projects, which can be `above`, `below`, `left`, or `right`. For example, the following snippet adds a reflection below an `h1` element, as Figure 3-1 illustrates:

```
<h1 style="-webkit-box-reflect: below;">
Reflection in Blue
</h1>
```


__Figure 3-1__  Reflection below a heading

!

The reflection is the same visible size as the element. The element border and padding are included in the reflection.

The first argument of the `-webkit-box-reflect` property specifies the direction of the reflection. An optional second argument specifies the offset or space between the original image and the reflection.

By default, the reflection begins with no separation from the element’s bounding box. To change this behavior, add an offset parameter. A positive offset causes the reflection to be separated from the element by additional space; a negative offset causes the reflection to overlap the element. For example, the bounding box of an `h1` element includes substantial white space; to tuck the reflection in closer to the text, add a negative offset. The following example adds an offset of `-15px` to the reflection. The result is shown in Figure 3-1:

`<h1 style = "-webkit-box-reflect: below -15px;">`

__Figure 3-2__  Reflection with negative offset

!

An optional third argument to `-webkit-box-reflect` specifies a mask to apply to the reflection.

A mask renders part of the reflection transparent or translucent. The mask is either an image file, specified as a URL, or a gradient. A mask image file can be a `.png`, an `.svg`, or a `.gif` with transparent areas. The alpha value of the mask is applied to the reflection on a pixel-by-pixel basis. Only the alpha value of the mask’s color values has any effect on the reflection.

When creating a mask, shape it to mask the target element itself, not to mask the reflection. The reflection shows a mirror image of the masked element, even though the element does not appear masked. The following snippet adds a mask image to a reflection. Figure 3-3 shows the resulting masked reflection side-by-side with the mask image.

`style="-webkit-box-reflect: below 0px url(mask.png);"`

__Figure 3-3__  Reflection with image as mask

!!

The following snippet adds a reflection below an image, using a gradient as a mask. Figure 3-4 shows the result.

`<img src = "sunrise.png" style = " border-radius: 20px;`

`-webkit-box-reflect: below 0px`

`-webkit-linear-gradient(transparent, transparent 50%, white 90%);">`

__Figure 3-4__  Image with reflection and gradient mask

!

Note that the reflection includes the rounded borders of the `img` element. Notice also that the gradient goes from transparent at the top to opaque at the bottom—the opposite of its appearance in the reflection; this is because the reflection shows a mirror image of the masked element.

For more about masks, see [Using Masks](Using%20Masks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damzsfvbuqmjrfvjvomi); for more about gradients, see [Using Gradients](Using%20Gradients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damzsfvbuqmjqfvjvomi).

When you reflect an element, all of the element’s descendants are displayed in the reflection. If you add a reflection to a child element, the child’s reflection is rendered first; this inner reflection is included in the parent element’s reflection. The following snippet adds a reflection to a `div` element containing an `img` element that has its own reflection. Figure 3-5 shows the result:

```
<div style="-webkit-box-reflect: below;">
   <img src = "sunrise.png" height="177" width="339" style = " border-radius: 20px;          -webkit-box-reflect: below 0px
        -webkit-linear-gradient(transparent,transparent 80%,white);">
   <P>
   <P>Text...
   <P>Text...
</div>
```


__Figure 3-5__  Inner reflection, reflected

!

[Next](Using%20CSS%20Filters.md)[Previous](Using%20Masks.md)

