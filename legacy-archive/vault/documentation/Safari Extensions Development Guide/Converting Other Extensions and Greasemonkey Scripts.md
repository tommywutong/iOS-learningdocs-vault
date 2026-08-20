---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/ConvertingToSafari/ConvertingToSafari.html
archived_at: '2026-07-27T06:57:07.789458Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Distributing%20Your%20Extension.md)[Previous](Debugging%20Extensions.md)

# Converting Other Extensions and Greasemonkey Scripts

Safari extensions provide similar functionality to extensions for other browsers, but there are some important differences detailed in this chapter. If you have already written Google Chrome extensions, Firefox extensions, or Greasemonkey scripts, then this chapter will help you convert them to Safari extensions.

## Converting Chrome Extensions

Use Extension Builder to create a new Safari extension, as described in [Using Extension Builder](Using%20Extension%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrnknltc). In the Extension Builder interface provide metadata such as your name, website, and a description of the extension.

Next, set up the user interface for your extension in Extension Builder. If your Chrome extension used browser or page actions, use toolbar items in Safari. If you used popups in Chrome, use a popover in Safari. If you used a background page, use the global page in Safari. You can also modify some parts of your UI at runtime—for example, you can disable toolbar items and add contextual menu items.

The events that occur in Safari are based on the DOM event system, described in [Document Object Model Events](http://www.w3.org/TR/DOM-Level-2-Events/events.html) and [UIEvents](http://www.w3.org/TR/DOM-Level-3-Events/#event-types). To set up an event listener, call the [addEventListener](https://developer.apple.com/documentation/safariextensions/safarieventtarget/1635408-addeventlistener) method on the object that should listen for the event. Any instance of `SafariEventTarget` or its subclasses can register event listeners. For security reasons, you can dispatch messages only within your own extension.

The Safari API is divided into two parts: the web content layer, which runs inside the web content area, and the application layer, which runs outside of it. To communicate between scripts running in different layers, use messages. In Safari, there is no difference between short-term message passing and long-term connections; you use the same methods for both.

## Converting Firefox Extensions

Both Firefox and Safari provide an extensions API, but the two APIs have substantially different functionality. As you bring your extension to Safari, you may find that some of the features you used in Firefox are in a different place in Safari, or are not available. You may still be able to bring your extension to Safari—consider the core functionality of your extension and determine how you can expose that functionality using the API that is provided. You should also examine the functionality provided in Safari that you didn’t have in Firefox, to understand how you might use it to improve your extension.

To start developing Safari extensions, just enable extensions from the Develop menu; there is no special setup procedure. Safari extensions are written using HTML5, CSS3, and JavaScript. The information stored in RDF and XUL files for Firefox extensions is stored in the `Info.plist` file for Safari Extensions. This file, which you create and edit using Extension Builder, contains all the metadata about your extension and a description of its user interface. See [Using Extension Builder](Using%20Extension%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrnknltc).

## Converting Greasemonkey Scripts

Safari extensions can inject JavaScript and CSS, so bringing Greasemonkey scripts to Safari is generally quite straightforward. You need to add your Greasemonkey injected content to your Safari extension’s bundle. Use Extension Builder to add these files to your Safari extension’s list of injected scripts and style sheets, described in [Injecting Scripts](Injecting%20Scripts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnrnknltc) and [Injecting Styles](Injecting%20Styles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqnznknltc). You can also inject scripts and style sheets at runtime using methods on the [SafariExtension](https://developer.apple.com/documentation/safariextensions/safariextension) object.

Safari differs from Greasemonkey in how you access your extension’s settings. The Safari settings API isn’t directly available to injected scripts because they are run as part of the web content layer. To access settings, dispatch a message from the injected script to the global page by using the [SafariContentBrowserTabProxy](https://developer.apple.com/documentation/safariextensions/safaricontentbrowsertabproxy) object. Because the global page is part of the application layer, scripts running in it can access your Safari extension’s settings. Then dispatch a message that contains the settings information from the global page back to the Safari extension injected script. For more information on messaging, see [Messages and Proxies](Messages%20and%20Proxies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjufvjvomi).

[Next](Distributing%20Your%20Extension.md)[Previous](Debugging%20Extensions.md)
