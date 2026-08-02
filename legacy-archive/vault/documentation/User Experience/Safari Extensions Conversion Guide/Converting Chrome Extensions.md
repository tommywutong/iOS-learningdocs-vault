---
title: Safari Extensions Conversion Guide
apple_id: TP40009993
resource_type: Guide
platform: Safari
topic: User Experience
technology: Safari Extensions
published: '2011-07-20'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SafariExtensionsConversionGuide/Chapters/Chrome.html
archived_at: '2026-07-27T06:57:07.816470Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Extensions Conversion Guide](About%20Safari%20Extensions.md)


[Next](Converting%20Firefox%20Extensions.md)[Previous](About%20Safari%20Extensions.md)

# Converting Chrome Extensions

Extensions in Chrome and Safari have similar functionality, so you should find the API quite familiar. There are, of course, some key differences.

Use Extension Builder to create a new extension, to provide metadata such as your name, website, and a description of the extension, and to set up the user interface for your extension. You can also modify some parts of your UI at runtime—for example, you can disable toolbar items and add contextual menu items.

If your Chrome extension used browser or page actions, you should use toolbar items in Safari. If you used popups in Chrome, use a popover in Safari. If you used a background page, use the global page in Safari.

The event system is based on the DOM event system. To set up an event listener, call the [addEventListener](https://developer.apple.com/documentation/safariextensions/safarieventtarget/1635408-addeventlistener) method on the object that should listen for the event. Any instance of `SafariEventTarget` or its subclasses can register event listeners. For security reasons, you can dispatch messages only within your own extension.

The API is divided into two parts: the web content layer, which runs inside the web content area, and the application layer, which runs outside of it. To communicate between scripts running in different layers, use messages. In Safari, there is no difference between short-term message passing and long-term connections; you use the same methods for both.

You can submit your extension to the gallery from the Safari Dev Center. Safari extensions are always hosted by their developer, regardless of whether they are posted to the gallery.

Safari extensions must be digitally signed before they can be installed. To get your signing certificate, visit the Safari Dev Center.

[Next](Converting%20Firefox%20Extensions.md)[Previous](About%20Safari%20Extensions.md)
