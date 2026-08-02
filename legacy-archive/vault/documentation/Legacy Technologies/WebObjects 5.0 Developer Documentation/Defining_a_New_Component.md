---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/ComponentCommunication/Defining_a_New_Component.html
archived_at: '2026-07-15T08:12:48.697965Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Custom_Objects.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Modifying_t_n_component.md)

## Defining a New Component

In this section, you'll create a new project and add a component
for displaying and editing a user's information.

Remember that each component has its own Java class. It is
convenient to think of components, as well as the objects representing
them, as self-contained units with specific tasks. The task of the
new component is to allow the user to edit a User object. By encapsulating
behavior this way, you ensure that if you add, remove, or alter
the properties of a user, you need to modify only this component
to allow editing the new attributes.

You begin by creating a new project since you no longer need
the code for tracking the request-response cycle. Then you add the
custom User class and create a component for editing a User object.
Then you will alter the Main component to maintain a list of users rather
than a single user, and add methods to use the new component to
edit any one of them.

1. Create a
   new WebObjects application project and name it ComponentCommunication.
   ![[image: ../Art/componentcommcreate.gif]](../Art/componentcommcreate.gif)
2. Add a `User.java` class.

   Follow
   the steps in ["Adding the Custom Class"](Custom_Objects.md#apple-ijbegqseincuo) to add the file to the project. Then
   edit the file so that it looks like [Listing 6-3](#apple-ijbusqshijdes).

   __Listing
   6-3 User.java__

   ```
   import com.webobjects.foundation.*;
   import com.webobjects.appserver.*;
   import com.webobjects.eocontrol.*;

   public class User extends Object {
       protected String personName;
       protected String favoriteFood;

       public String personName() {
           return personName;
       }
       public void setPersonName(String newPersonName) {
           personName = newPersonName;
       }
       public String favoriteFood() {
           return favoriteFood;
       }
       public void setFavoriteFood(String newFavoriteFood) {
           favoriteFood = newFavoriteFood;
       }

       public boolean entryIncomplete() {
           if (personName == null || favoriteFood == null || personName.equals("")  || favoriteFood.equals(""))  {
               return true;
           }
           else {
               return false;
           }
       }
   }
   ```
3. Add a component to the project.
   1. Select Web Components
      from the Groups & Files list.
   2. Choose File > New File.
   3. Under WebObjects, select Component in the New File pane of
      the assistant and click Next.
   4. Enter `UserEdit` in
      the File Name text field.
       ![[image: ../Art/pbaddcomponent.gif]](../Art/pbaddcomponent.gif)
   5. Make sure Application Server is selected in the Targets list
      and click Finish.

You'll notice that the new component is added to the project's
Web Components group.

 ![[image: ../Art/compcommcompadded.gif]](../Art/compcommcompadded.gif)

You're now ready to customize the component used for editing
a User object, UserEdit. The user edits one User object at a time,
so `UserEdit.java` needs
to have one instance variable of type User. The UserEdit component
will have fields similar to those defined in the Main component
of the UserEntry project (see ["User Interface"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/iUser_Interface.html))
and buttons to submit and cancel the changes.

1. Open `UserEdit.wo` in
   WebObjects Builder.
2. Add a User instance variable named `user` to
   the component.

   Select the options that create an instance variable
   and provide accessor methods. This variable holds the particular
   User object being edited.

    ![[image: ../Art/wobcompcommaddvar.gif]](../Art/wobcompcommaddvar.gif)
3. Add a WOForm element to the UserEdit component.
4. Add and bind the WOTextFields as shown in [Figure 6-1](#apple-krifqusfiyytcmi).
5. Add an action method called `submitChanges` to
   the component. Choose Main as the page returned by the method. This
   means that when the user is done editing, she's returned to the
   Main component rather than the UserEdit component.
    ![[image: ../Art/compcommaddsubmit.gif]](../Art/compcommaddsubmit.gif)
6. Use the Forms menu to add a WOResetButton and a WOSubmitButton,
   and bind the `submitChanges` method
   to the WOSubmitButton's `action` attribute.

   The
   WOResetButton resets the form fields.
7. Save `UserEdit.wo`.
8. Edit the `submitChanges` method
   in `UserEdit.java` so that
   it looks like [Listing 6-4](#apple-ijbusqsjincuo).

   __Listing
   6-4 EditUser.java's submitChanges method__

   ```
   public Main submitChanges() {
       Main nextPage = (Main)pageWithName("Main");
       // Initialize your component here
       nextPage.setUser(user); // send user object to the Main page
       return nextPage;
   }
   ```
9. Save `UserEdit.java`.

__Figure
6-1 UserEdit.wo__

![[image: ../Art/compcommcomplt.gif]](../Art/compcommcomplt.gif)

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Custom_Objects.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Modifying_t_n_component.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
