---
title: Safari Extensions Conversion Guide
apple_id: TP40009993
resource_type: Guide
platform: Safari
topic: User Experience
technology: Safari Extensions
published: '2011-07-20'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SafariExtensionsConversionGuide/Chapters/Greasemonkey.html
archived_at: '2026-07-27T06:57:07.823600Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Extensions Conversion Guide](About%20Safari%20Extensions.md)


[Next](Document%20Revision%20History.md)[Previous](Converting%20Firefox%20Extensions.md)

# Converting Greasemonkey Scripts

Safari extensions can inject JavaScript and CSS, so bringing Greasemonkey scripts to Safari is generally quite straightforward. You need to add your injected content to your extension’s bundle and add these files to your extension’s list of injected scripts and style sheets using the Extension Builder. You can also inject scripts and style sheets at runtime using methods on the `SafariExtension` object. For more information, see [Injecting Scripts](../../Safari%20Extensions%20Development%20Guide/Injecting%20Scripts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnq) and [Injecting Styles](../../Safari%20Extensions%20Development%20Guide/Injecting%20Styles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqny).

One important difference is how you access your extension’s settings. The settings API isn’t directly available to injected scripts because they are run as part of the web content layer. To access settings, dispatch a message from the injected script to the global page via the [SafariContentBrowserTabProxy](https://developer.apple.com/documentation/safariextensions/safaricontentbrowsertabproxy) object. Because the global page is part of the application layer, scripts running in it can access your extension’s settings. Then dispatch a message that contains the settings information from the global page back to the injected script.

Safari extensions must be digitally signed before they can be installed. To get your signing certificate, visit the Safari Dev Center.

[Next](Document%20Revision%20History.md)[Previous](Converting%20Firefox%20Extensions.md)
