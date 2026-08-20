---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/Editing16.html
archived_at: '2026-07-18T01:26:56.345917Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Editing15.md)

# Creating Hyperlinks

There are two types of hyperlinks that you can use in a WebObjects application:

- A static hyperlink (which uses the HTML <A> tag), whose destination is constant.
- A dynamic hyperlink (WOHyperlink), whose destination can be specified at run time. See ["Dynamic Hyperlinks"](DynamicElements14.md#apple-gy2dimi)for more information about these.

To create a static hyperlink:

- Click ! on the toolbar.
- Type the text that the hyperlink should contain. As you type, the text is underlined.
- Click ! again.

Alternatively, you can select existing text and then click ! once to convert the text to a hyperlink.

- Use the Inspector to set the destination of the link.

!

__Note__: While the destination of a static link cannot change, it's possible to vary its text at run time by using a dynamic string (see ["Dynamic Strings"](DynamicElements13.md#apple-gyztmna)) inside the hyperlink.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Setting%20Page%20Attributes.md)
