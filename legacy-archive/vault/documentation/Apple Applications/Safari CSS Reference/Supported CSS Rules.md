---
title: Safari CSS Reference
apple_id: TP40002050
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: WebKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/OtherStandardCSS3Features.html
archived_at: '2026-07-15T05:19:02.163163Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari CSS Reference](Introduction%20to%20Safari%20CSS%20Reference.md)


[Next](CSS%20Property%20Functions.md)[Previous](Supported%20CSS%20Properties.md)

# Supported CSS Rules

This chapter describes selected CSS rules supported by Safari. This is not intended to be an exhaustive list. The CSS rules described here are limited to rules that are either new or are not broadly supported by other browsers (including some specific to WebKit).

Enables the use of downloadable web fonts (among other things).

____Syntax____: |  |
```
@font-face {
    font-family: "MyFamilyname", cursive [, ...];
    font-style: normal [, ...];
    font-variant: normal[, ...];
    font-weight: bold[, ...];
    font-stretch: condensed[, ...]; /* Not supported */
    font-size: 12pt;[, ...] /* Not supported */
    src: local("Font Family Name"),
        url(http://..../fontfile.ttf) format("truetype"),
        url(http://..../fontfile.ttf) [, ...];
}
```

____Constants____: __`all`__: The font will match for all possible values of the corresponding property.

____Discussion____: The only required properties are `font-family` and `src`. For each of these properties, you can specify either a single value or a comma-separated list containing multiple values.

In the `src` property, you can specify any number of local font family names and any number of URLs (provided that you include at least one local name or URL, of course).

For each URL, you can also specify a format hint if desired. This hint is intended to help the browser avoid downloading fonts in formats that it does not support.

The remaining properties tell the browser how to choose between multiple variants in the same font family. For example:

```
<style><!--
@font-face {
        font-family: Geo, sans-serif;
        font-style: normal;
        src: url(fonts/geo_sans_light/GeosansLight.ttf);
}

@font-face {
        font-family: Geo, sans-serif;
        font-style: oblique;
        src: url(fonts/geo_sans_light/GeosansLight-Oblique.ttf);
}

.ingeo {
        font-family: Geo, sans-serif;
}
--></style>
<div class='ingeo'>This is a test.</div>
```

Because the `font-style` property is specified for both font definitions, the browser uses the first entry for normal text and the second entry for oblique text, and thus, the text “This is a test.” is displayed normally (vertically). If you remove these properties, the last font definition is used and the text appears in an oblique font (slanted).

For a list of specific values allowed for each of these properties, see the description for the property in question.

____Availability____: Safari 3.1 and later.

____Support Level____: CSS 2

Specifies CSS properties specific to a given output medium. For example, you might have styles specific to print media. Here is the syntax for these queries:

____Syntax____: |  |
```
@media print {
    div.chapternumber {
        /* A new chapter should begin at the top of a
           printed page, slightly below normal text.
         */
        page-break-before: always;
        margin-top: .25 in;
    }
}
```

____Discussion____: Safari supports the following media types:

| Media Type | Description |
| --- | --- |
| `all` | Applies to all devices, regardless of medium. Equivalent to listing no media type.  Available in Safari 1.0 and later.  Available in iOS 1.0 and later. |
| `print` | Applies only to printed copies of the document.  Available in Safari 4.0 and later.  Available in iOS 1.0 and later. |
| `screen` | Applies only to content displayed on a screen.  Available in Safari 4.0 and later.  Available in iOS 1.0 and later. |

__Note:__ The `aural` media type is deprecated in CSS 2.1. The CSS 2.1 specification reserves the `speech` media type, but does not define which properties do or do not apply to it.

The following media query extensions can be added to a `@media` rule to indicate that the rule only applies to display formats with certain properties:

| Media Query | Description |
| --- | --- |
| `animation` | Applies only to browsers that support animations specified with `[-webkit-animation](StandardCSSProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvpxozlcnnuxix3bnzuw2ylunfxw4)`.  Available in Safari 4.0 and later. |
| `max-device-height` | Applies only to devices with the specified maximum height. |
| `max-device-width` | Applies only to devices with the specified maximum width. |
| `min-device-height` | Applies only to devices with the specified minimum height. |
| `min-device-width` | Applies only to devices with the specified minimum width. |
| `transition` | Applies only to browsers that support transitions specified with `[-webkit-transition](StandardCSSProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvomjs)`.  Available in Safari 4.0 and later. |
| `-webkit-device-pixel-ratio` | Applies only to devices with the specified ratio where a value of 2 indicates Retina displays and 1 indicates standard displays.  Available in Safari 4.0 and later. |
| `-webkit-max-device-pixel-ratio` | Applies only to devices with the specified maximum ratio where 2 indicates Retina displays and 1 indicates standard displays.  Available in Safari 4.0 and later. |
| `-webkit-min-device-pixel-ratio` | Applies only to devices with the specified minimum ratio where 2 indicates Retina displays and 1 indicates standard displays.  Available in Safari 4.0 and later. |

____Availability____: Available in Safari 1.0 and later.

Available in iOS 1.0 and later.

____Support Level____: CSS 3

Specifies keyframes for CSS visual effect animation properties.

____Syntax____: |  |
```
keyframes-rule: '@-webkit-keyframes' [ IDENT | STRING ] '{' keyframes-blocks '}';
keyframes-blocks: [ keyframe-selectors block ]* ;
keyframe-selectors: [ 'from' | 'to' | PERCENTAGE ] [ ',' [ 'from' | 'to' | PERCENTAGE ] ]*;
```

____Discussion____: The `@-webkit-keyframes` keyword is followed by the name of the target animation and a set of style rules following the syntax above. You set the animation name using the `-webkit-animation-name` property.

The keyframes selector consists of a list of percentage values or the keywords `from` or `to`. The selector is used to specify the percentage along the duration of the animation or transition that the keyframes represent. The keyframes are specified by the block of property values declared for the selector. The keyword `from` is equivalent to the value `0`. The keyword `to` is equivalent to the value `100`.

The keyframe declaration consists of properties and values. Properties that are not animating are ignored in this rule, with the exception of the `-webkit-animation-timing-function` property.

This rule is the last rule encountered in sorted rules order that matches the name of the transition. This rule does not cascade; therefore, an animation never derives keyframes from more than one `@-webkit-keyframes` rule.

All of the values in selectors are sorted in increasing order by time. If there are any duplicates, the last keyframe specified inside the `@-webkit-keyframes` rule is used to provide the keyframe information for that time. There is no cascading within a `@-webkit-keyframes` rule if multiple keyframes specify the same keyframe selector value.

For example, the following `@-webkit-keyframes` rule contains keyframes for a transition or animation named "wobble." In the first keyframe, shown at the beginning of the animation cycle, the `left` value of the animation is 100 pixels. After 40% of the animation duration, the value of `left` is 150 pixels. After 60% of the animation duration, the `left` value is 75 pixels. At the end of the animation cycle, the `left` value returns to 100 pixels.

```
@-webkit-keyframes 'wobble' {

      0 {
        left: 100px;
      }

      40% {
        left: 150px;
      }

      60% {
        left: 75px;
      }

      100% {
        left: 100px;
      }

    }
```

You can also use a keyframes rule to set a timing function to animate or transition from one keyframe to another. You set the timing function for a keyframe within its block using the `-webkit-animation-timing-function` property.

For example, the following `@-webkit-keyframes` rule defines keyframes for a transition or animation named "bounce." Between the first and second keyframes—between 0 and 25%—an `ease-out` timing function is used. Between the second and third keyframes—between 25% and 50%—an `ease-in` timing function is used. As a result, the element moves up the page by 50 pixels, slowing down as it reaches its highest point, then speeds up as it falls back to 100 pixels. The second half of the animation behaves in a similar manner, but moves the element only 25 pixels up the page.

```
@-webkit-keyframes 'bounce' {

      from {
        top: 100px;
        -webkit-animation-timing-function: ease-out;
      }

      25% {
        top: 50px;
        -webkit-animation-timing-function: ease-in;
      }

      50% {
        top: 100px;
        -webkit-animation-timing-function: ease-out;
      }

      75% {
        top: 75px;
        -webkit-animation-timing-function: ease-in;
      }

      to {
        top: 100px;
      }

    }
```

____Availability____: Available in Safari 4.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension

[Next](CSS%20Property%20Functions.md)[Previous](Supported%20CSS%20Properties.md)

