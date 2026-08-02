---
title: Safari Image Delivery Best Practices
apple_id: TP40012449
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-10-03'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/SafariImageDeliveryBestPractices/ServingImagestoRetinaDisplays/ServingImagestoRetinaDisplays.html
archived_at: '2026-07-15T08:19:12.181515Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Image Delivery Best Practices](About%20Proper%20Image%20Delivery%20on%20the%20Web.md)


[Next](Substituting%20Raster%20Images%20for%20Vector%20Alternatives.md)[Previous](About%20Proper%20Image%20Delivery%20on%20the%20Web.md)

# Serving Images Efficiently to Displays of Varying Pixel Density

Safari draws text, form controls, shadows, gradients, and borders crisply right out of the box, regardless of screen resolution. Images, on the other hand, require special attention. Safari stretches images to maintain a relative size to other elements, and must interpolate pixel values based on a mathematical average. This often results in a blurry image. To correct this, you must supply a pair of image files for each image you wish to present: one for standard-resolution displays, and one for Retina displays. Do not discard your standard-resolution images, because if you only supplied high-resolution images to all your visitors, bandwidth would be wasted on those with non-Retina displays.

Create images that are twice the width and height of your current image resources. A common file-naming convention for high-resolution images on the web is to prepend `_2x` before the file extension; for example, `myImage_2x.jpg`. Don’t use `@2x` in the filename, since the `@` character in a URL is reserved as the delimiter separating the username and password from the host in authentication URL schemes.

The easiest method of implementing high-resolution graphics on your website differs on a case-by-case basis. To help you find the best solution for your website, this chapter outlines four common practices:

- [Serving Images With Image Sets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdinbzfvbuqmznknltk)
- [Serving Images With Media Queries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdinbzfvbuqmznknltg)
- [Serving Images With JavaScript](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdinbzfvbuqmznknlti)
- [Serving Images With Icons](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdinbzfvbuqmznknlts)

Choose one or many of these ways to retrofit your image content to support displays of all resolutions.

An image set is a comma-separated list of image paths and their respective resolutions. You denote the image URL and image scale in your CSS file, as shown in Listing 1-1. Safari figures out the device’s pixel density automatically, so standard- and high-resolution images load on their respective displays.

__Listing 1-1__  Delivering images of proper resolution with image sets

```
header {
    background: -webkit-image-set( url(images/header.jpg)    1x,
                                   url(images/header_2x.jpg) 2x);
    height: 150px; /* height in CSS pixels */
    width: 800px; /* width in CSS pixels */
}
```

In the `-webkit-image-set` function, `1x` correlates to standard-resolution and `2x` correlates to high-resolution.

The pixel values you supply for the width and height properties should match the standard-resolution image’s dimensions. This is because __CSS pixels are not the same as device pixels__. On standard-resolution displays, CSS pixels and device pixels are 1:1. On Retina displays, however, there are four device pixels inside every CSS pixel.

Safari will automatically discover the target resolution and load the appropriate image specified in the `url()` function, even if the user is browsing on a dual-monitor setup. If the image is loaded on a standard-resolution display and more than 50% of the window is dragged to a Retina display, the high-resolution image will automatically download and replace the standard-resolution image, and vice-versa.

Repeat this process for each image on your website for a consistent user experience.

Media queries are blocks of rules that you include in your CSS to specify which properties are to be set under which conditions. You may be familiar with the `screen` and `print` media queries, which allow web developers to set different CSS properties to elements based on the medium in which they are presented, either onscreen or on paper.

Media queries can also detect the pixel density of the device. If the device’s pixel ratio is 1, the display is standard. If the device’s pixel ratio is 2, the display is high-resolution. All Retina displays have a pixel ratio of 2.

__Listing 1-2__  Delivering images of proper resolution with media queries

```
header {
    background-image: url(images/header.jpg);
    background-size: cover;
    height: 150px;
    width: 800px;
}
/* ... more 1x CSS rules ... */
@media screen and (-webkit-min-device-pixel-ratio: 2) {
    header {
        background-image: url(images/header_2x.jpg);
    }
    /* ... more 2x CSS rules ... */
}
```

Instead of `-webkit-min-device-pixel-ratio`, you could specify `-webkit-device-pixel-ratio`, but the former future-proofs the site so higher-resolution displays will load the higher-resolution image.

Media queries handle resolution changes automatically.

The third method of delivering high-resolution images is with JavaScript. On a large-scale project, JavaScript is a practical solution because you can tackle image delivery logic programatically. It degrades gracefully to support older browsers. There are, however, a few downsides of relying on JavaScript to choose which resolution image to load:

- Image downloads are delayed until JavaScript execution begins, which occurs later in the pageload lifetime.
- You are placing code relating to visual data in your logic, a faux pas according to the Model-View-Controller design pattern.
- The user may have JavaScript disabled, in which case neither your standard- nor high-resolution image would appear.

Code similar to what’s shown in Listing 1-3 should be called when your page initializes:

__Listing 1-3__  Delivering images of proper resolution with JavaScript

```
function loadImages() {
    var header = document.querySelector('header');
    if(window.devicePixelRatio >= 2) {
        header.style.background = 'url(images/header_2x.jpg)';
    }
    else {
        header.style.background = 'url(images/header.jpg)';
    }
}
```

The code in Listing 1-3 detects the display pixel density and delivers the appropriate image accordingly. Take heed that on large sites, manually listing every version of an image inflates your script and is error prone. You could instead adhere to a strict file-naming convention, or specify the path of the 2x version in a `data-*` attribute of your HTML element, and use the same `if/else` condition to load the high-resolution image.

Another possibility that may be beneficial to you would be to specify the standard-resolution image in CSS, then check the device pixel ratio in JavaScript. If JavaScript determines that the user is on a Retina display, overwrite the image with the high-resolution version. While this causes users on Retina displays to download both the standard- _and_ high-resolution version of every image, the user perceives the downloading to occur faster, as high-resolution images will replace their standard-resolution counterparts as soon as they are ready (similar to how progressive JPEGs load).

You also must set up an event listener in case the window moves to a screen with a different device pixel ratio, as JavaScript does not handle resolution changes automatically:

```
window.matchMedia('(-webkit-device-pixel-ratio:1)').addListener(loadImages);
```


A final consideration for your high-resolution images is icon size. The icon image appears in the Safari address bar, bookmarks list, and history. Standard resolution displays prefer 16 x 16 pixel icons. Retina displays stretch the standard icons just as they would other web images. To avoid any blurring of your icons, you can provide both a 16 x 16 and a 32 x 32 icon image. Include icons of multiple sizes with a single `.ico` image file. Safari chooses the most appropriate resolution from the `.ico` file. Use a link element, with the `rel=icon` attribute to deliver the image file. The markup similar to what’s shown in Listing 1-4 should be in the `head` of your HTML files. See the [HTML5 specification](http://www.w3.org/html/wg/drafts/html/master/links.html#rel-icon) for more on link type “icon”.

__Listing 1-4__  Delivering images of proper resolution with icons

```
<link rel="icon" href="myIcon.ico" sizes="16x16 32x32" type="image/x-icon">
```

[Next](Substituting%20Raster%20Images%20for%20Vector%20Alternatives.md)[Previous](About%20Proper%20Image%20Delivery%20on%20the%20Web.md)

