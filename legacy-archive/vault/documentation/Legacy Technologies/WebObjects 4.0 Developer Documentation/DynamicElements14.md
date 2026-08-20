---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements14.html
archived_at: '2026-07-18T01:25:38.669615Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DynamicElements13.md)

## Dynamic Hyperlinks

Dynamic hyperlinks (WOHyperlink) allow you to specify the link's destination at run time rather than at compile time. There are several ways to do this:

- You can specify the name of a page in your application as the destination of the link. To do this, bind the name to the WOHyperlink's __pageName__attribute. This is useful since pages in a WebObjects application don't have predictable URLs that you can specify in an HTML hyperlink.
- You can specify an action to be performed when the hyperlink is clicked by binding WOHyperlink's __action__ attribute to an action method in your code. This method can perform any sort of action, as well as returning a page as the destination.
- You can also specify a URL as the destination by binding to the __href__ __attribute.__

To create a dynamic hyperlink:

- Click ! in the toolbar.
- Replace the word `Hyperlink` with the text of the link.
- Create the element's bindings.

To learn how to create a static hyperlink, see ["Creating Hyperlinks"](Creating%20Hyperlinks.md#apple-gu3tcoa).

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DynamicElements15.md)
