---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/User_Interface.html
archived_at: '2026-07-15T08:13:36.307448Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Request_Processing.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Tracing_the_sponse_Loop.md)

## User Interface

Input elements are bound to variables in a way very similar
to the way display elements are. In fact, input elements are essentially
bidirectional display elements—they get a value from the object
when the response is generated and send a value back to the object
when a request is received. See ["Request Processing"](Request_Processing.md#apple-ijbegssbinduq) for more
information.

For this example, you display a bit of information about the
user. You'll use text input fields to get data from the user,
and once she's entered it, you'll use a WOConditional to hide
the text fields and display the data. Then you'll encapsulate
the user data into a custom object so you can generate an array
of them.

First, create a new project named UserEntry. Edit the Main
component with WebObjects Builder. The first step is to add variables
for the data the user enters. Then, you add WOTextFields and bind
them to the variables.

1. Add two variables
   named `personName` and `favoriteFood` to
   the Main component using the Edit Source menu. These variables should
   be of type `java.lang.String`.
   Make sure the three options below "Generate source code for"
   are selected so that an instance variable and accessor methods are
   generated.
    ![[image: ../Art/wobuserinterfaceaddvars.gif]](../Art/wobuserinterfaceaddvars.gif)

|  |
| --- |
| __Note:__ Avoid calling a variable `name`. This name is used by WebObjects and using it for your own purposes will lead to unexpected results! |
2. Use the Edit Source menu to add an action method named `addUser`.
   Accept the default of `null` for
   the component's return value.

   In a later step, you'll
   customize this method to set some additional variables.
3. Add a WOForm, labels, WOTextFields, and a WOSubmitButton to
   capture data from the user.
   1. Add the WOForm by
      choosing Forms > WOForm.

      All form elements, including submit
      buttons, must be within a WOForm to function.
   2. Add the WOForm's elements.

      Add two labels "`Name:` "
      and "`Favorite Food:` "
      in separate lines.

      Add a WOTextField next to the Name
      label by choosing Forms > WOTextField.

      Add a second
      WOTextField next to the Favorite Food label.

      Place the
      cursor at the end of last text field and press Shift-Enter.

      Choose
      Forms > WOSubmitButton to add a button to use to submit the form.
4. Bind the variables to the `value` attribute
   of the appropriate text fields, just as with the WOString. See [Figure 5-3](#apple-ijauur2fjbbuq).

   __Figure
   5-3 Binding the Favorite Food text field
   to personName__

   ![[image: ../Art/userinputbindfields.gif]](../Art/userinputbindfields.gif)
5. Bind the `addUser` action
   to the `action` attribute
   of the WOSubmitButton.
6. Save `Main.wo`.

All the user interface elements are connected. The WOTextFields
set the properties bound to them during request processing. The
Java method bound to the WOSubmitButton's `action` attribute
is called when the user clicks the submit button.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Request_Processing.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Tracing_the_sponse_Loop.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
