---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/Conditional_al_Elements.html
archived_at: '2026-07-15T08:13:31.409649Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Tracing_the_sponse_Loop.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Derived_Properties.md)

## Conditional Display With WOConditional Elements

A WOConditional element provides a means of conditionally
displaying part of a component. This part could include text, elements,
and other components.

The WOConditional element has two attributes: `condition` and `negate`.
The `condition` attribute
is required. While it is syntactically correct to use the values `YES` or `NO` for
this binding, the element is only useful when `condition` is
bound to a Java method that returns `true` or `false` (you
can also bind it to integer objects, in which case nonzero values
are interpreted as `true` and
zero values as `false`).
If the method evaluates to `true`,
the contents of the conditional are displayed; otherwise, they are
not. If the `negate` attribute
it set to `true`, this
arrangement is reversed: the contents are displayed only if the `condition` attribute
evaluates to `false`.

You can use a pair of WOConditionals to ask the user for input
and then display the information she entered. This is the method
you'll use to capture and display user data.

1. Add an instance
   variable you can use to indicate whether the user has entered the necessary
   information.

   Add the following variable to `Main.java`:

   ```
   protected boolean entryIncomplete;
   ```

   You
   can use WebObjects Builder's Edit Source menu or add the variable
   directly to the class file. (If you use WebObjects Builder, be sure
   to deselect the options under "Create source code for" in the
   Add Key dialog.)

   This variable should be initialized
   to `true` because the variables
   are empty when the page is first displayed, so the entry is incomplete.
   Otherwise, the fields would not be displayed the first time the
   page is shown. Initialize the variable in the component's constructor.

   ```
   public Main(WOContext context) {
       super(context);
       entryIncomplete = true;
   }
   ```

   Also
   modify the `addUser` method
   to check the form properties and update the value of `entryIncomplete`.

   ```
   public WOComponent addUser() {
       System.out.println("'addUser' button was clicked.");
       if (personName.equals("") || favoriteFood.equals("") {
           entryIncomplete = true;
       }
       else {
           entryIncomplete = false; // the entry is now complete
       }
       return null;
   }
   ```
2. Save `Main.java`.
3. Open `Main.wo` in
   WebObjects Builder
4. Make the form element conditional by wrapping it in a WOConditional.

   The
   fields and the submit button should be displayed only while `entryIncomplete` is `true`.
   Select the form and choose WOConditional from the WebObjects menu.
   (You can select the form by clicking inside it and then clicking
   the `<WOForm>` tag
   in the path pane, located below the content editor.)
5. Bind the `condition` attribute
   of the WOConditional to the `entryIncomplete` instance variable.

   As
   long as `entryIncomplete` evaluates
   to `true`, WebObjects displays
   the WOConditional's content.
6. Create elements to display the data once it has been entered.
   1. Make a new line below
      the WOConditional.
   2. Add two WOStrings.
   3. Add the text " `prefers to eat` "
      between the WOStrings (note the leading and trailing spaces).
   4. Bind the first WOString's `value` attribute
      to `personName`,
      and the second's to `favoriteFood`.
7. Select the new items and create a WOConditional around them.
8. Bind the new WOConditional's `condition` to `entryIncomplete`.
   Click "+" on the WOConditional to invert its meaning. It changes
   to a "-" and the contents of the second WOConditional are displayed
   only when the value of the `entryIncomplete` variable
   is `false`.

   __Figure
   5-4 WOConditional elements__

   ![[image: ../Art/userinputwocond2.gif]](../Art/userinputwocond2.gif)
9. Build and run the application.

The first time the Main component is generated, you see the
same page as the last version of the application, because `entryIncomplete` is `true` and
the contents of the first WOConditional are displayed.

Once the user enters data and clicks the submit button, the `addUser` method
determines if she entered text in both text fields and, if you so,
sets `entryIncomplete` to `false`.
Since the `addUser` method
returns `null`, the page
is redrawn with the new variable settings, and this time the contents
of the other WOConditional are displayed because the variable changed.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Tracing_the_sponse_Loop.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Derived_Properties.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
