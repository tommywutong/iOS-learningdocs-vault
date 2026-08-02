---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/GuestBook/StaticHTML.html
archived_at: '2026-07-15T07:48:49.341592Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBook.book.md) [!Previous Section](ImplementMethod.md)

# Create the application's output

So far, you have a way for the guest to enter information, a way for the application to add that information to the guest list, and a way to store the guest list. Now, you need a way for the application to display the list of guests. To do this, you'll add more dynamic elements to the main page. But first, create a heading for the output.

## Create static HTML elements

When you created the heading at the top of the page, you just typed directly into the Main component's window. To create the heading for the page's output section, you could just do the same thing, but it's more common to drag elements from the palette so that you can better control what HTML tags are used.

- Place the cursor at the bottom of the Main page, below the horizontal line.
- In the palette window, click the first icon to display the Static Elements palette.
- Drag a heading element to the page.
- Select the text inside the heading and type __Guests__.
!

You just added a static HTML element, a heading, to the page. As an optional step, you can modify the heading's appearance using the inspector panel. Click the inspector button (the button labeled with an "i") to display the inspector panel. Select the heading element, and you'll see the properties you can set for the heading. You can change the heading to any one of the six levels supported in HTML (H1 through H6). To learn more about adding elements to the page, see "HTML Editing in WebObjects Builder" in _Using WebObjects Builder_.!

[!Table of Contents](GuestBook.book.md) [!Next Section](AbstractElements.md)
