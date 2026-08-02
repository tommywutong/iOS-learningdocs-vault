---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/GuestBook/AbstractElements.html
archived_at: '2026-07-15T07:48:33.034226Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBook.book.md) [!Previous Section](StaticHTML.md)

## Add abstract dynamic elements to the page

To display the list of guests that have visited the page, you'll use abstract dynamic elements. Unlike the form elements you added earlier, abstract elements have no true equivalent in HTML. Instead, your application determines what these elements look like.

- Place the cursor at the bottom of the page.
- In the palette window, click the third icon to display the Abstract Elements palette.
- Drag a Repetition element onto the page.
!- Select the word "Repetition" inside the Repetition object, and press the Delete key twice to delete the word and the carriage return before it.
- Drag three String elements from the Abstract Elements palette. After each String element, enter a carriage return so that each string is on a separate line.
- Place the cursor below the third String element inside the Repetition, choose the Static Elements palette, and drag a horizontal line onto the page.
!

You're done adding elements to the page now, so you can close the palette window and save the __Main.wo__ component.

### A closer look

You just added several abstract dynamic elements: a WORepetition and three WOStrings. The WOStrings are simply dynamic strings. The application decides what text the strings should display at run time. WORepetition is an object with two parts: contents and a list. You just defined the contents. They are the three WOStrings and the horizontal rule. The list you define when you bind the WORepetition, which you'll do next. WORepetition is a complex element. You'll read about how it works after you make its bindings.
Although this example uses WORepetition and WOString only to display output, you could also use them to display input. To learn more about these elements, see the [Dynamic Elements section of the _WebObjects Reference_.](../../Reference/DynamicElements/DynamicElements.book.md)

[!Table of Contents](GuestBook.book.md) [!Next Section](BindAbstract.md)
