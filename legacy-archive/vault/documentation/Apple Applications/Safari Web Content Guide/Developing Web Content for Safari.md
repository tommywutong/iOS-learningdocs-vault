---
title: Safari Web Content Guide
apple_id: TP40002051
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/Introduction/Introduction.html
archived_at: '2026-07-15T05:19:15.875533Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Creating%20Compatible%20Web%20Content.md)

# Developing Web Content for Safari

Safari is a full-featured Web browser for macOS and iOS. You don't need to add any Safari-specific tweaks to make your website work with Safari or to make your website work on iOS-based devices. If you design your website using W3C standards for HTML, CSS, and JavaScript, and don't rely on third-party plug-ins, users can view and interact with your website using Safari on all supported platforms.

Making websites work with Safari is just a first step, however. It should be your goal to optimize websites to create the best experience for all users, including people using Safari on handheld devices with touch screens. Use CSS with responsive design techniques to change the layout of your website for multiple viewport screen sizes and multitasking split-screen, add touch and gesture support, animate changes in CSS properties, and so on.

There are three main areas to focus on when creating web content for Safari:

- Make sure your website is compatible with Safari.
- Enhance the user experience in Safari, particularly on mobile devices.
- Make the best use of dynamically changing network bandwidth to deliver content.

### Making It Work

Safari has an array of built-in tools for quickly spotting incompatibilities and debugging problems. If you have a website up and running, and are getting complaints that the site doesn't work with Safari, it is usually because of one of the following problems:

- The site includes media compressed in a format that Safari doesn't support.
- The site relies on plug-ins to handle audio, video, or animation.

Use the Web Inspector to identify errors and warnings, making them easy to correct.

There are Safari-compatible media formats and embedding techniques for every job. Safari supports audio media in AAC, MP3, AIFF, and WAVE formats on all platforms. Safari supports video media encoded using H.264 compression, commonly used in MPEG-4 format, on all platforms. Handheld devices support a somewhat more limited set of MPEG-4 profiles than desktop devices.

Use the HTML5 `<audio>` and `<video>` tags to embed audio and video files in supported formats, with fallback to a plug-in for older browsers on the desktop. Safari on iOS does not support plug-ins. Therefore, to make your website accessible using handheld devices, do not rely on plug-ins to display content. Safari on the desktop does support plug-ins. and there are Safari-compatible versions of all common plug-ins, including QuickTime, Flash, and SilverLight. When possible, avoid plug-ins and use CSS or Canvas to embed animation and create special effects.

### Enhancing the User Experience

Enhance the user's experience with responsive design to provide different page layouts for varying viewport sizes on handheld and desktop devices. Responsive design can handle CSS and JavaScript detection as well as select the appropriate CSS layout for a device. Responsive design can react to portrait and landscape orientation and multitasking split-screen, automatically switching between layouts with CSS and JavaScript syntax.

It's easy to add touch and gesture support by adding a few event handlers to your site. Make navigation easier for touchscreen users by making links large enough to reliably hit with a finger, and by surrounding links with enough whitespace to avoid accidentally hitting the wrong link. Leave a blank gutter or border on the page as well, so the user can easily scroll the screen with a finger without touching a link.

iOS-specific enhancements can turn your website into a web app that behaves like a native iOS app. Optimize websites for iOS by providing an icon for the user's home screen, by making your website into a fullscreen web app, and by including links that dial a phone number, open the Maps app, or open other built-in iOS apps.

Use caching and client-side storage to make your website work even when the user is offline or the user’s device loses network connectivity. Safari supports HTML5 client-side storage and caching, "lazy" caching for offline reading, and techniques for allowing web-based games to work offline.

You need a solid understanding of HTML, familiarity with JavaScript, and a basic understanding of CSS in order to make the best use of this document.

- _[Safari Web Inspector Guide](../Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_—How to use Safari’s built-in tools for debugging and optimization.
- _[Safari HTML5 Audio and Video Guide](../../Audio%20Video/Safari%20HTML5%20Audio%20and%20Video%20Guide/About%20HTML5%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrt)_—How to embed audio and video without using plug-ins, or by using a plug-in as a fallback.
- _[Safari HTML5 Canvas Guide](../../Audio%20Video/Safari%20HTML5%20Canvas%20Guide/About%20Canvas.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbs)_—How to add sophisticated animation and interactive games to a website without using plug-ins.
- _[Safari CSS Visual Effects Guide](../../Internet%20Web/Safari%20CSS%20Visual%20Effects%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damzs)_—How to enhance websites using WebKit extensions for masks, gradients, reflections, CSS animation, and 3D transformations.
- _[Safari Client-Side Storage and Offline Applications Programming Guide](../../iPhone/Safari%20Client-Side%20Storage%20and%20Offline%20Applications%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjw)_—How to create websites that work when the user is offline, or that contain HTML5 client-side databases.
- _[HTTP Live Streaming Overview](../../Networking%20Internet/HTTP%20Live%20Streaming%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzs)_—How to optimize network bandwidth for streaming audio and video from a standard web server.
- _[Safari HTML Reference](../Safari%20HTML%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanbz)_—HTML elements and attributes supported in Safari.
- _[Safari CSS Reference](../Safari%20CSS%20Reference/Introduction%20to%20Safari%20CSS%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjq)_—CSS properties and classes supported in Safari.
- _[Safari DOM Additions Reference](https://developer.apple.com/documentation/webkitjs)_—Events and other DOM additions supported in Safari.
[Next](Creating%20Compatible%20Web%20Content.md)

