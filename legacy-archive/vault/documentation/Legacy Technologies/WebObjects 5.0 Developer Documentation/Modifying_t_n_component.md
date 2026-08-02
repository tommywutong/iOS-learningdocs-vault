---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/ComponentCommunication/Modifying_t_n_component.html
archived_at: '2026-07-15T08:12:51.696275Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Defining_a_New_Component.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Running_the_Application.md)

## Modifying the Main component

In this section you'll add elements to the Main component
so that it displays the user information after it has been edited.
The component needs a WOConditional element so that user information
is displayed only if the user entered data in the UserEdit page.
After the modifications are made, `Main.wo` should
look similar to [Figure 6-2](#apple-ijbusrkhifbuo).

1. Add a method
   called `noDataEntered` to `Main.java`,
   as shown in [Listing 6-5](#apple-ijbusq2bjjfee).

   __Listing
   6-5 The noDataEntered method of the Main.java
   class__

   ```
   public boolean noDataEntered() {
       if (user == null || user.entryIncomplete()) {
           return true;
       }
       else {
           return false;
       }
   }
   ```
2. Open `Main.wo` in
   WebObjects Builder.
3. Add a `user` instance
   variable of type User, including accessor methods.
4. Add informational text displayed when no data has been entered.
   1. Add a WOConditional
      element.
   2. Enter the following text inside the WOConditional: `User
      data has not been entered`.
   3. Bind the WOConditional's `condition` attribute
      to `noDataEntered`.
5. Add display fields and a caption displayed when data has been
   entered.
   1. Add
      another WOConditional element below the first one.
   2. Inside the second WOConditional, add a WOString, enter the
      text " `likes to eat` " after
      it, and add another WOString.
   3. Bind the first WOString's `value` attribute
      to `user.personName` and
      the second's to `user.favoriteFood`.
   4. Bind the WOConditional's `condition` attribute
      to `noDataEntered`.

      Click
      "+" in the WOConditional so that it changes to "-". This
      makes it so that only one of the WOConditional elements's content
      is displayed at a time. See ["Conditional Display With WOConditional Elements"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/iConditional_al_Elements.html) for more information.
6. Add an action called `editUser`,
   which returns a UserEdit component.
    ![[image: ../Art/wobaddedituseractn.gif]](../Art/wobaddedituseractn.gif)
7. Add a link that displays the UserEdit page.
   1. Add a WOHyperlink
      below the second WOConditional, and enter `Edit` as
      its caption.
   2. Bind the WOHyperlink's `action` attribute
      to the `editUser` action.
8. Save `Main.wo`.
9. Edit the `editUser` method
   in `Main.java` so that
   it looks like [Listing 6-6](#apple-ijbusqsgi5auc).

   __Listing
   6-6 Main component's editUser action method__

   ```
   public UserEdit editUser() {
       UserEdit nextPage = (UserEdit)pageWithName("UserEdit");
       // Initialize your component here
       if (user == null) {
           user = new User();
       }
       nextPage.setUser(user); // send the user object to the UserEdit page
       return nextPage;
   }
   ```
10. Save `Main.java`.

__Figure
6-2 Main.wo__

![[image: ../Art/compcommmainwo.gif]](../Art/compcommmainwo.gif)

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Defining_a_New_Component.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Running_the_Application.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
