---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBook/GuestBook7.html
archived_at: '2026-07-15T07:53:30.861188Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookTOC.md) [!Previous Section](GuestBook6.md)

## Using the Inspector

You use the Inspector window to set properties of the elements in your component. The Inspector's title and contents reflect the element you've selected in the component window.

- Click !.

A window titled Heading Inspector appears. It allows you to set the level of the heading.

!- Click "1".

The text is now part of an <H1> tag, and it is displayed in a larger font.

- Click the ! icon at the top of the window.

The top of the window shows the _element path_to the selected element. Any element can be contained in a hierarchy of several levels of elements and can in turn contain other elements. Here, the element path shows that the heading element is contained in the page element, which is the top level of the hierarchy. By clicking the icons in the element path, you can easily choose different elements in the hierarchy.

Each element has its own Inspector that allows you to set properties appropriate for the element. The Page Attributes Inspector allows you to set properties such as the page's title and its text color.

!- Enter a title (such as My Guest Book, or something else of your choosing) in the Title text field. This is the title of the window that appears in your web browser when you run the application.
- Close the Inspector window.
- Choose File!Save to save the Main component.

__Note:__ Version 3.5 of WebObjects Builder doesn't allow you to undo actions you take when editing your component. Therefore, it is a good idea to save frequently. That way, if you make a mistake, you can revert to your previously saved version.

[!Table of Contents](GuestBookTOC.md) [!Next Section](GuestBook8.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
