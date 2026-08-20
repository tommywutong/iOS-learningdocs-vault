---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/GuestBook/BindAbstract.html
archived_at: '2026-07-15T07:48:37.001528Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBook.book.md) [!Previous Section](AbstractElements.md)

## Bind the WORepetition element

Just as you had to bind the input elements to variables so that the input values could be captured in the script, you now have to bind the output elements to script variables so that the page displays the correct information.

- Click the first field inside the WORepetition, and double-click __guests__ under __application__ in the object browser.

This binds the __guests__ array to the __list__ attribute of WORepetition. WebObjects Builder automatically creates a variable called __guest__ and binds it to the __item__ attribute (the second field in the repetition).

!- Bind each item in the variable __guest__ (__name__, __email__, and __comments__) to the three WOStrings inside the WORepetition by selecting the WOString and double-clicking the variable.
!- Save the Main component.

### A closer look

You just bound the WORepetition's __list__ attribute to the application script's __guests__ array, which you created earlier. A WORepetition displays its contents for each item contained in its __list__ attribute. When you created the WORepetition, you defined its contents as three WOStrings. Then, you bound those WOStrings to the information in the newly created variable __guest__, which is updated to contain the current item in the list as WORepetition moves through the list.!
Creating a WORepetition and binding it in this manner is the equivalent of saying "for each guest item in the guests array, display the name, e-mail, and comments."
WORepetition is an example of a dynamic element that requires bindings to two different variables. The __list__ attribute is bound to the __guests__ array, and the __item__ attribute is bound to the variable __guest__. WOString, on the other hand, is like the WOTextFields and WOText that you bound earlier: WOString defines multiple attributes, but you only need to bind to one attribute, the __value__ attribute, for the string to work properly. The other attributes are assigned default values.
You can learn more about WORepetitions, WOStrings, and the other dynamic elements in this example by looking them up in the [Dynamic Elements section of the _WebObjects Reference_](../../Reference/DynamicElements/DynamicElements.book.md). To learn more about how to use WebObjects Builder to create dynamic elements, see "[Using Dynamic Elements in WebObjects Builder](../../WOBuilder/DynElem/DynElem.book.md)."

[!Table of Contents](GuestBook.book.md) [!Next Section](AwakeSleep.md)
