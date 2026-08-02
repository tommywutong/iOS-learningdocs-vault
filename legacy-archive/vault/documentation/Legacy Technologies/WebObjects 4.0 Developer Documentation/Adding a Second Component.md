---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBookPlus/GuestBookPlus11.html
archived_at: '2026-07-18T01:21:20.146883Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Enhancing%20Your%20Application.md) [!Previous Section](GuestBookPlus10.md)

# Adding a Second Component

In this section, you'll create a new component. Instead of Java, you'll implement its code using WebScript. This section demonstrates the quick turn around between development cycles when using WebScript.

- In Project Builder's browser, click Web Components in the first column.
- Choose File !New in Project.

Note that the Web Components suitcase is selected.

- Type GuestList as the name of the new component, then click OK.

The WebObjects Component Wizard appears.

- Choose None for Available Assistance and WebScript for Component Language.
- Click Finish.
- In the second column of the browser, double-click __GuestList.wo__ to bring up the component window in WebObjects Builder.
- Create a heading for this page, as you did for the Main component. Call it "Guest List" (or something else of your choosing), then press Enter twice.
- Add a WOString below the heading. After the WOString, type the text " guests have signed this guestbook."

You're going to bind this WOString so that it reflects the number of guests who have submitted this form (see screen shot on next page).

- In the object browser, click __application__.

There is an entry in the second column for the __allGuests__ application variable you created. This entry appears in the Main component as well, since application variables are accessible from anywhere in the code.

If you click __allGuests__, you'll see in the third column an entry for __count__. This is a standard method that returns the number of objects in the array.

- Make a connection from __count__ to the center rectangle to bind it to the WOString's __value__ attribute.

!

- Save the GuestList component.

You need to do one more thing so that the GuestList page now displays when the user submits the form.

- Go back to Project Builder and view the source code for __Main.java__. Replace the return statement in the __submit__ method with the following code:

```
return pageWithName("GuestList");
```


__pageWithName__ is a standard WebObjects method (defined in the WOApplication class) that allows you to specify a new page to display.

At this point, the code for __Main.java__ looks like this:

!

- Save __Main.java__.
- Build and run your application.

Each time you submit the form, the number of guests displayed in the WOString should increase.

To return to the Main page, you'll have to use your browser's backtrack button. Later in the tutorial, you'll add a hyperlink to return to the Main page.

[!Table of Contents](Enhancing%20Your%20Application.md) [!Next Section](Using%20a%20Repetition.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
