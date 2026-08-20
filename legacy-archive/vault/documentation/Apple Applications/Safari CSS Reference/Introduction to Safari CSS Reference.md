---
title: Safari CSS Reference
apple_id: TP40002050
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: WebKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Introduction.html
archived_at: '2026-07-15T05:19:03.244845Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Explanation%20of%20Terms.md)

# Introduction to Safari CSS Reference

You can use Cascading Style Sheets (CSS) in conjunction with HTML-based web content to fine-tune the style of the content. The goal of CSS is to separate the _structure_ provided by HTML from the _style_ provided by CSS. Taking style information out of the structure allows designers to independently tune a page’s style for a variety of audiences and readers (such as desktops, hand-held devices like iPhone, and text-based browsers).

All Safari web browsers use the WebKit engine to display webpages. WebKit is an open source framework in Mac OS X that lets developers embed web browser functionality into applications. This document covers support of cascading style sheets (CSS) in WebKit.

This document is not intended as a comprehensive specification. Specifications for versions of CSS are available at [http://www.w3.org/Style/CSS/](http://www.w3.org/Style/CSS/).

You should read this document if you are creating web content for any version of Safari or any other WebKit-based application such as Dashboard.

This document contains the following articles:

- [Explanation of Terms](Explanation%20of%20Terms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknzyfvjvomi) explains terminology used in this reference.
- [Supported CSS Properties](Supported%20CSS%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvomi) describes all of the CSS properties supported by Safari and provides information about which web standards (as defined by the World Wide Web Consortium, or W3C) include those properties, where applicable.
- [Supported CSS Rules](Supported%20CSS%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tmmbrfvjvomi) describes CSS rules supported by Safari, including media rules, downloadable font rules, and so on.
- [CSS Property Functions](CSS%20Property%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tsnjvfvjvomi) describes functions used by CSS transform properties.

There are a variety of other resources for Safari web content developers in the ADC Reference Library.

If you are creating web content for Safari platforms, then you should read:

- _[Safari Web Content Guide](../Safari%20Web%20Content%20Guide/Developing%20Web%20Content%20for%20Safari.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjr)_ describes how to create content that is compatible with, optimized for, and customized for Safari on any platform.

If you are a designing web content for Safari on iOS, then you should also read:

- _iOS Human Interface Guidelines_ provides user interface guidelines for designing webpages and web applications for Safari on iOS.
- _[Apple URL Scheme Reference](../../../featuredarticles/Apple%20URL%20Scheme%20Reference/About%20Apple%20URL%20Schemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqojz)_ describes how to use the Phone, Mail, Text, YouTube, iTunes, and Maps applications from your webpages.

If you want to learn more about visual effects, then you should read:

- _[Safari CSS Visual Effects Guide](../../Internet%20Web/Safari%20CSS%20Visual%20Effects%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damzs)_ describes how to use the CSS visual effects properties—the transition, animation, and transforms properties. It also covers the JavaScript APIs for handling visual effects events.

If you want to learn more about the JavaScript multi-touch event support, then you should read:

- _[Safari DOM Additions Reference](https://developer.apple.com/documentation/webkitjs)_ describes the touch event classes that you use to handle multi-touch gestures in JavaScript.

If you want to use the JavaScript media APIs, then you should read:

- _[Safari HTML5 Audio and Video Guide](../../Audio%20Video/Safari%20HTML5%20Audio%20and%20Video%20Guide/About%20HTML5%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrt)_ describes how to use the HTML5 audio and video elements.

If you want to learn more about what HyperText Markup Language (HTML) tags are supported in Safari, then read:

- _[Safari HTML Reference](../Safari%20HTML%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanbz)_ describes the HTML elements and attributes supported by different Safari and WebKit applications.

If you are using JavaScript and want access to the DOM or use the canvas object, then read:

- _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_ describes how to use JavaScript in web content for WebKit-based applications.

If you are developing web content for Safari on the desktop and iOS, then you should read:

- _[Safari Web Inspector Guide](../Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_ describes how to use the Debug menu in Safari.
- _[Dashcode User Guide](../Dashcode%20User%20Guide/Introduction%20to%20Dashcode%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojs)_ describes how to use Dashcode to create web applications.

If you want to learn more about WebKit or contribute to the open source project, then go to [The WebKit Open Source Project](http://webkit.org/).

If you want to read the WebKit W3C proposals then go to: [http://www.webkit.org/specs](http://www.webkit.org/specs).

[Next](Explanation%20of%20Terms.md)

