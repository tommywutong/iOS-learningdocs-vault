---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/Introduction/Introduction.html
archived_at: '2026-07-27T06:57:07.550221Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](Extensions%20Overview.md)

# About Safari Extensions

Safari extensions provide a way for you to add features to the Safari browser. You can add custom buttons to the Safari toolbar, create bars of your own, add contextual menu items, display full-page content, add menus or popovers to toolbar items, and inject scripts and apply style sheets into webpages.

__Important:__ In this book, Safari extensions refers to the legacy `.safariextz`-style Safari extensions. Developer-signed Safari extensions are not supported in Safari 12. Safari extensions distributed in the Safari Extension Gallery are deprecated, and Safari 12 is the last release to support them. Safari by default will turn off Safari extensions using `canLoad`. Instead, use Content Blocker extensions. New submissions to the Safari Extensions Gallery will be accepted until the end of 2018.

Use Safari app extensions to add features to the Safari browser. To convert your Safari extension to a Safari app extension, or to start developing Safari app extensions, see [Safari App Extensions](https://developer.apple.com/documentation/safariservices#2191080).

You write Safari extensions using HTML, CSS, and JavaScript. A JavaScript API for extensions allows you to interact with the browser and web content in ways that scripts normally can’t.

__Important:__ To develop extensions for Safari, you need to sign up for the Apple Developer Program online at [https://developer.apple.com](https://developer.apple.com). For more information, see [Developer Certificates](Extensions%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjvfvjvomrw).

## At a Glance

Safari extensions let you add persistent items to Safari—controls, menus and menu items, local or web-based content, and scripts that modify the content Safari presents.

### What’s the Difference Between an Extension and a Plug-in?

A plug-in can add support for media types to a browser. An extension can add many different features.

Extensions and plug-ins both expand a browser’s capabilities. Plug-ins let browsers display media that the browser can’t display natively or provide a particular media player experience. Extensions personalize and enhance the browser itself and can interact with HTML web content.

A plug-in can’t interact with webpages except to display media of specific MIME types. A plug-in cannot add features to Safari, such as toolbar buttons or contextual menu items.

A plug-in is a binary file that interfaces with the browser but is essentially an app in itself—the browser hands off specific media types to the plug-in to handle.

An extension is a collection of HTML, JavaScript, and CSS files that the browser uses to expand its feature set. Extensions allow you to reformat webpages, block unwanted sites or unwanted material, display RSS feeds and other data in a bar or window, and do thousands of other things that plug-ins can’t do.

### Extensions Have Their Own JavaScript API

Extensions have access to a special JavaScript API that lets them access the Safari app and web content. This API is documented in _[Safari Extensions Reference](https://developer.apple.com/documentation/safariextensions)_.

__Relevant Chapter:__ [Extensions Overview](Extensions%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjvfvjvomi)

### Extensions Run in a Sandbox

Safari Extensions run in their own "sandbox" or container area. The designated container area for Safari Extensions is the execution of normal HTML, CSS, and JavaScript within the Safari app, and the specific JavaScript APIs documented here and _[Safari Extensions Reference](https://developer.apple.com/documentation/safariextensions)_.

__Important:__ Launching an installed Safari plug-in from an extension by using the HTML `<object>` or `<embed>` tags is prohibited.

### You Create Extensions Right in Safari

You create extensions using Extension Builder, which is built into Safari. Open Extension Builder, tell it to create an extension folder, drag your HTML, JavaScript, and CSS style sheets into the folder, fill out the fields in Extension Builder, and you’re ready to go.

The main ingredients of an extension are:

- __Global HTML page__—code that’s loaded once, when Safari launches or when your extension is enabled. This is the ideal place to put the code for buttons in the Safari toolbar, extension menus, or contextual menus. This page is never displayed; it’s just for logic.
- __Content__ (HTML, CSS, JavaScript, media)—HTML content and interactive controls that you display in popovers, extension bars, or in tabs as full-page content. Extension bar and popover files have access to the Safari app and can include logic for menus or toolbar items.
- __Menu Items__ (labels, images)—items that appear in extension menus that you define, or are added to Safari’s existing contextual menus.
- __Injected scripts__—scripts to be injected into browser content. These scripts can read, modify, add to, or delete content.
- __Injected style sheets__—user style sheets that can modify the display of web content by overriding or adding to the styles normally applied.
- __Icon image__—the icon for your extension.

__Relevant Chapter:__ [Using Extension Builder](Using%20Extension%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrnknltc)

### You Can Define User Settings in Extension Builder

Your extension can have its own user settings, accessible to the user in the Extensions pane of Safari preferences. You define the settings, user interface items, and default values using Extension Builder.

There is also a settings API similar to HTML5 local storage for accessing and modifying settings programmatically. You can use encrypted settings for security.

__Relevant Chapter:__ [Settings and Local Storage](Settings%20and%20Local%20Storage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjrfvjvomi)

### Debug Your Extension with Safari’s Built-in Tools

You can use the Safari developer tools to help debug your extension. The developer tools report HTML errors and profile JavaScript, log messages to the console, and let you interactively set breakpoints, get variable values, and call functions. The debugging tools are supported for extension bars, global HTML pages, and injected scripts. Each extension bar and global page has its own console.

__Relevant Chapter:__ [Debugging Extensions](Debugging%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqojnknltc)

### Update Your Extension Automatically from the Web

Safari provides a method to support checking for updates to an extension automatically: the Update Manifest. You specify a web address, and Safari periodically compares the installed version of your extension with the latest version on your website. If your website has a newer version, Safari offers the user an update.

__Relevant Chapter:__ [Updating Extensions](Updating%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjsfvjvomi)

## Prerequisites

You need to be familiar with HTML, JavaScript, and the basics of CSS. Familiarity with HTML5 and CSS3 is helpful. To add a button to the toolbar, you need to be able to create an image with an alpha channel (transparency).

## See Also

- _[Safari Extensions Reference](https://developer.apple.com/documentation/safariextensions)_—the JavaScript classes, methods, and properties that only Safari extensions can use.
- _[Safari DOM Additions Reference](https://developer.apple.com/documentation/webkitjs)_—the classes, methods, and properties that Safari exposes to JavaScript that are not available in all browsers.
- _[Safari Web Inspector Guide](../Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_—the built-in web development tools that come with Safari.
- _[Safari Content-Blocking Rules Reference](https://developer.apple.com/library/archive/documentation/Extensions/Conceptual/ContentBlockingRules/Introduction/Introduction.html#//apple_ref/doc/uid/TP40016265)_—a guide to formatting content-blocking rules.

[Next](Extensions%20Overview.md)
