---
title: Safari CSS Visual Effects Guide
apple_id: TP40008032
resource_type: Guide
platform: iAd System JS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/SafariVisualEffectsProgGuide/UsingCSSFilters/UsingCSSFilters.html
archived_at: '2026-07-15T07:44:13.002590Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari CSS Visual Effects Guide](Introduction.md)


[Next](Animating%20CSS%20Transitions.md)[Previous](Using%20Reflections.md)

# Using CSS Filters

Safari 6 and later supports CSS filters, or special visual effects, that you can apply to many elements, including videos (see [Figure 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damzsfvbuqmjxfvjvomi)). These hardware-accelerated filters (such as brightness, contrast, saturation, and blur) can be stacked on top of and animated against one another. Read [CSS Property Functions](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/Functions.html#//apple_ref/doc/uid/TP40007955) in _[Safari CSS Reference](../../Apple%20Applications/Safari%20CSS%20Reference/Introduction%20to%20Safari%20CSS%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjq)_ to find out more about CSS filters.

__Figure 4-1__  CSS filters on a video

!!

To add a CSS filter to an HTML element, include the -webkit-filter property in the element’s CSS declaration, as shown in [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damzsfvbuqmjxfvjvomq). You can list as many of the functions found in [CSS Property Functions](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/Functions.html#//apple_ref/doc/uid/TP40007955) in _[Safari CSS Reference](../../Apple%20Applications/Safari%20CSS%20Reference/Introduction%20to%20Safari%20CSS%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjq)_ as you’d like.

__Listing 4-1__  Applying CSS filters to HTML elements

```
<!doctype html>
<html>
<head>
    <title>Filters</title>
    <style>
        video {
            float: left;
            width: 50%;
        }
        .filtered {
            -webkit-filter: hue-rotate(180deg)
                            saturate(200%);
        }
    </style>
</head>
<body>
    <h1>Video with and without CSS filters</h1>
    <p>The video on the left does not have CSS filters applied, while the video on the right does.</p>
    <p>These videos are playing from the same source file.</p>
    <video src="shuttle.m4v" autoplay></video>
    <video src="shuttle.m4v" autoplay class="filtered"></video>
</body>
</html>
```


[Next](Animating%20CSS%20Transitions.md)[Previous](Using%20Reflections.md)

