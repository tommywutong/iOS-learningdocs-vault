---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBook/UsingInspector.html
archived_at: '2026-07-18T01:21:15.621617Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Previous Section](EnterStaticText.md)

## Using the Inspector

You use the Inspector panel to set properties of the elements in your component. The Inspector's title and contents reflect the element you've selected in the component window.

- Click !.

A panel titled Heading Inspector appears. It allows you to set the level of the heading.

!

- Click "1".

The text is now part of an <H1> tag, and it is displayed in a larger font.

- Click the ! icon at the top of the panel.

The top of the panel shows the _element path_to the selected element. Any element can be contained in a hierarchy of several levels of elements and can in turn contain other elements. Here, the element path shows that the heading element is contained in the page element, which is the top level of the hierarchy. By clicking the icons in the element path, you can easily choose different elements in the hierarchy.

Each element has its own Inspector that allows you to set properties appropriate for the element. The Page Attributes Inspector allows you to set properties such as the page's title and its text color.

!

- Choose "Full document" from the "Partial document" pull-down menu.
- Enter a title (such as "My Guest Book", or something else of your choosing) in the Title text field. This is the title of the window that appears in your web browser when you run the application.
- Close the Inspector panel.
- Choose File!Save to save the Main component.

Although WebObjects Builder supports undo, it is always a good idea to save your work frequently.

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Next Section](FormBasedElements.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
