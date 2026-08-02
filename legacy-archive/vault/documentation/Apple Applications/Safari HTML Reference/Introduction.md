---
title: Safari HTML Reference
apple_id: TP40002049
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: WebKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariHTMLRef/Introduction.html
archived_at: '2026-07-15T05:19:06.503612Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Explanation%20of%20Terms.md)

# Introduction

This document details every HTML element and property supported by WebKit and Safari on all platforms, which include Mac OS X, iOS, and Windows. You should read this if you are developing web content that will be displayed in Safari or within a WebKit-based application.

This document is not intended as a comprehensive specification. The HTML5 specification is available at [http://dev.w3.org/html5/spec/Overview.html](http://dev.w3.org/html5/spec/Overview.html).

The following articles describe key aspects of Safari HTML support:

- [Explanation of Terms](Explanation%20of%20Terms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danjsfvjvomi) explains terminology used in this reference.
- [Supported HTML](Supported%20HTML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi3delktk4za) describes all the HTML elements supported by Safari. This includes standard elements (as defined by the World Wide Web Consortium, or W3C), common elements that are not part of a standard, and Apple extensions.
- [Supported Attributes](Supported%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danjyfvjvomi) describes the HTML attributes supported by Safari.
- [Supported Input Values](Supported%20Input%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danjvfvjvomi) describes supported types for the `input` element.
- [Supported Meta Tags](Supported%20Meta%20Tags.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojtfvjvomi) describes additional keys for the `meta` element.
- [Supported Accessibility Roles](Supported%20Accessibility%20Roles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqga4tqnzwfvjvomi) describes supported accessibility roles defined in the WAI-ARIA specification.

You'll find a variety of other resources for Safari web content developers in the [Safari Developer Library](https://developer.apple.com/library/safari/navigation/).

If you are creating web content for Safari platforms, then you should read:

- _[Safari Web Content Guide](../Safari%20Web%20Content%20Guide/Developing%20Web%20Content%20for%20Safari.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjr)_, which describes how to create content that is compatible with, optimized for, and customized for Safari on any platform.

If you are designing web content for Safari on iOS, then you should also read:

- _iOS Human Interface Guidelines_, which provides user interface guidelines for designing webpages and web applications for Safari on iOS.
- _[Apple URL Scheme Reference](../../../featuredarticles/Apple%20URL%20Scheme%20Reference/About%20Apple%20URL%20Schemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqojz)_, which describes how to use the Phone, Mail, Text, YouTube, iTunes, and Maps applications from your webpages.

If you want to learn more about visual effects, then you should read:

- _[Safari CSS Visual Effects Guide](../../Internet%20Web/Safari%20CSS%20Visual%20Effects%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damzs)_, which describes how to use the CSS visual effects properties—the transition, animation, and transforms properties. It also covers the JavaScript APIs for handling visual effects events.

If you want to learn more about the JavaScript multitouch event support, then you should read:

- _[Safari DOM Additions Reference](https://developer.apple.com/documentation/webkitjs)_, which describes the touch event classes that you use to handle multitouch gestures in JavaScript.

If you want to use the JavaScript media APIs, then you should read:

- _[Safari HTML5 Audio and Video Guide](../../Audio%20Video/Safari%20HTML5%20Audio%20and%20Video%20Guide/About%20HTML5%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrt)_, which describes how to use the HTML5 audio and video elements.

If you want to learn more about which Cascading Style Sheets (CSS) properties are supported in Safari, then read:

- _[Safari CSS Reference](../Safari%20CSS%20Reference/Introduction%20to%20Safari%20CSS%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjq)_, which describes the CSS properties supported by Safari and WebKit applications.

If you are using JavaScript and want access to the DOM or use the canvas object, then read:

- _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_, which describes how to use JavaScript in web content for WebKit-based applications.
- _[Safari HTML5 Canvas Guide](../../Audio%20Video/Safari%20HTML5%20Canvas%20Guide/About%20Canvas.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbs)_, which provides information about the `canvas` HTML5 element.

If you are developing web content for Safari on the desktop and iOS, then you should read:

- _[Safari Web Inspector Guide](../Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_, which describes how to use the Debug menu in Safari.
- _[Dashcode User Guide](../Dashcode%20User%20Guide/Introduction%20to%20Dashcode%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojs)_, which describes how to use Dashcode to create web applications.

If you want to learn more about WebKit or contribute to the open source project, then go to [The WebKit Open Source Project](http://webkit.org/).

If you want to read the WebKit W3C proposals, then go to: [http://www.webkit.org/specs](http://www.webkit.org/specs).

[Next](Explanation%20of%20Terms.md)

