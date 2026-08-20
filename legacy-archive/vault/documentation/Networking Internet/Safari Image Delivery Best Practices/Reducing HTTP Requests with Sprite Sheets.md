---
title: Safari Image Delivery Best Practices
apple_id: TP40012449
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: null
published: '2013-10-03'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/SafariImageDeliveryBestPractices/ReducingHTTPRequestswithSprites/ReducingHTTPRequestswithSprites.html
archived_at: '2026-07-15T08:19:11.369600Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Image Delivery Best Practices](About%20Proper%20Image%20Delivery%20on%20the%20Web.md)


[Next](Document%20Revision%20History.md)[Previous](Substituting%20Raster%20Images%20for%20Vector%20Alternatives.md)

# Reducing HTTP Requests with Sprite Sheets

A sprite sheet, more commonly known as _sprites_ or _spriting_, contains multiple image files in one file. While the bandwidth of one large image versus many smaller images are relatively equal, only one HTTP connection is required to transfer the sprite sheet. Even if your images are cached in the browser to prevent subsequent redownloads, the user’s initial visit requires one HTTP connection per resource. Every resource suffers a delay, or latency, while trying to reach the server. If you have fifteen separate images, each one of those images experiences latency. Although the latency may be brief, it can quickly add up depending on the numbers of images to download. Sprite sheets enable you to speed up the download time of your website by reducing the overall latency to your servers. Users will also save battery power and CPU cycles by requesting one resource instead of fifteen.

The best candidates to elect for spriting are small images that appear globally throughout your website, such as small UI decorations, icons, social buttons, background tiles, and so on, as shown in Figure 3-1. Large images are not worth spriting.

__Figure 3-1__  A sprite sheet of different app icons

![A sprite sheet containing four rows and 12 columns of different sprite images.](attachments/Art/7up_2x.png)

Implementing sprites in your webpages is easy. Once you have composed a sprite sheet in an image editor of your choice, apply it to every element you desire by setting its path as the `background-image` property. Then adjust the `background-position` property to line up with the sprite, as shown in Listing 3-1. The `width` and `height` properties act as mask dimensions and should be set to the width and height of the individual sprite.

__Listing 3-1__  A sprite sheet as defined in CSS

```
.spritesheet {
    background-image: url(images/spritesheet.png);
    background-size: 324px 88px;
    height: 22px;
    width: 27px;
}
/* pseudo-states for the closed-caption button */
#cc { background-position: 0 0; }
#cc:hover { background-position: 0 22px; }
#cc:active { background-position: 0 44px; }
```


Memory, especially on mobile devices, is a precious commodity. You should do everything in your power to reduce the amount of memory required to load your page so that the interface remains smooth and responsive. It is important to understand how displaying images affects memory usage.

Every pixel of an image produces 4 bytes in memory, 1 for each color channel (red, green, blue, and alpha). So for a 500 x 800 pixel image, you have 500 x 800 x 4 = 1,600,000 bytes, just over 1.5 MB, taking up memory. This is not the same as file size. A 500 x 800 pixel transparent PNG could be mere kilobytes on disk, but when displayed on screen it occupies 1.5 MB of memory!

For this reason, you should try to make your sprite sheets as dense as possible. Eliminate unused transparent or white space and pack your images tightly together to shrink the memory footprint of your web content.

Because the `background-position` property is defined in CSS pixel units, you do not need to do anything special regarding sprites on a Retina display. If the screen viewing your web content is a Retina display, and a high-resolution sprite is supplied, Safari will automatically position the 2x sprite correctly.

[Next](Document%20Revision%20History.md)[Previous](Substituting%20Raster%20Images%20for%20Vector%20Alternatives.md)

