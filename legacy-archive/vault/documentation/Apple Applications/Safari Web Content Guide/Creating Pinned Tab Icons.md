---
title: Safari Web Content Guide
apple_id: TP40002051
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/pinnedTabs/pinnedTabs.html
archived_at: '2026-07-15T05:19:23.414722Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Web Content Guide](Developing%20Web%20Content%20for%20Safari.md)


[Next](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/PromotingAppswithAppBanners/PromotingAppswithAppBanners.html)[Previous](Handling%20Events.md)

# Creating Pinned Tab Icons

Pinned Sites allow your users to keep their favorite websites open, running, and easily accessible. You can set the icon that the user sees when they pin your site by providing a vector image.

Use 100% black for all vectors with a transparent background in SVG format and add the following markup to all webpages that the icon should represent (replacing `"website_icon"` with your own file's name).

```
<link rel="mask-icon" href="website_icon.svg" color="red">
```

In the example, the `color` attribute sets the display color of the image. That attribute can specify a single color with a hexadecimal value (`#990000`), an RGB value (`rgb(153, 0, 0)`), or a recognized color-keyword, such as: `red`, `lime`, or `navy`.

[Next](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/PromotingAppswithAppBanners/PromotingAppswithAppBanners.html)[Previous](Handling%20Events.md)

