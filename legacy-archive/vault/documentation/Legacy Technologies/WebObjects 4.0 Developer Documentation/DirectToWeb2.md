---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb2.html
archived_at: '2026-07-18T01:24:43.684361Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Creating%20a%20Direct%20to%20Web%20Project.md)

## The Different Looks for WebObjects Applications

In this release, Direct to Web offers two different user-interface styles, or "looks," for WebObjects applications: Basic and WebObjects. More looks will be added in future releases. Currently the only simple way to change the look of an application is to re-create a project using Project Builder and then redefine the project with the WebObjects application wizard. Therefore it is advisable to know which look you want in advance.
The essential difference between the Basic look and the WebObjects look is that the latter look uses more graphics, particularly the spider-web image. But there are also differences in the style and placement of user-interface elements. The HTML in the Basic look is simple and straightforward, which makes the Basic look more suitable if you intend to freeze your pages and then customize them..
The login page for the Basic look has a panel-like submit form for the entry of user name and password:

!

The login page for the WebObjects look presents the submit form without the enclosing panel:

!

In the dynamically-generated pages (query, list, inspect, and so on), the differences between the Basic look and the WebObjects look are even more striking. In the Basic look the control header runs across the top of the page whereas in the WebObjects look it appears on the left side of the page. In addition, the Basic look is more tabular while the WebObjects look tends to present records in visual "blocks." For example, the following is an example of a list page in the Basic look:

!

The following illustrates what a list page looks like in the WebObjects look.

!

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](The%20Structure%20of%20a%20Direct%20to%20Web%20Project.md)
