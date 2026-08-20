---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/ComponentCommunication/Custom_Objects.html
archived_at: '2026-07-15T08:12:47.218974Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Component_Communication.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Defining_a_New_Component.md)

## Custom Objects

Right now, you're storing the name and food information
in variables of the Main component, abandoning the benefits of an
object-oriented system.

In the case that you wanted to pass the information the user
enters to other components, you'd have pass both values. If you
had more information about a particular person, you'd have to
pass each datum separately. It would be much more convenient to
encapsulate all the information about a user into one object and
pass that from component to component. Since WebObjects is fully
object-oriented, you can define a custom object to contain the user-entered
data.

For now, you'll just encapsulate the same data into an object.
Later, though, this kind of encapsulation is exactly what will allow
you to use a database as your persistent data storage system.

Once you've defined the User class with the appropriate
properties, you'll add a variable of type User to the Main component
and modify the WOTextFields on `Main.wo` to
use that variable's properties instead of the `personName` and `favoriteFood` instance
variables.

### Duplicating the UserEntry Project

Before proceeding with the custom class example, you should
create a copy of the UserEntry project.

1. Duplicate
   the UserEntry directory and name it UserEntryCustomObject.
2. Rename the `UserEntry.pbproj` file
   inside the UserEntryCustomObject directory
   to `UserEntryCustomObject.pbproj`.
3. Open the UserEntryCustomObject project in Project Builder.
4. Rename the UserEntry target to UserEntryCustomObject.
   1. Click the Targets
      tab.
   2. Select the UserEntry target in the Targets list.
   3. Choose Project > Rename.
   4. Replace UserEntry with UserEntryCustomObject.
   5. Click the Files tab.
5. Choose Build > Clean.

### Adding the Custom Class

In this section you'll create the custom class User.java and
add it to your project.

1. Make sure
   the UserEntryCustomObject project is open in Project Builder.
2. Select the group and target for the new file.
   1. Select Classes in
      the Groups & Files list.
   2. Choose Application Server from the target menu, located on
      the toolbar.
       ![[image: ../Art/pbaddcustomclassprep.gif]](../Art/pbaddcustomclassprep.gif)
3. Add the class file.
   1. Choose File > New
      File.
       ![[image: ../Art/pbaddcustomclass.gif]](../Art/pbaddcustomclass.gif)
   2. Under WebObjects, select Java Class and click Next.
   3. Enter `User.java` in
      the File Name text field and click Finish.
       ![[image: ../Art/pbaddedcustomclass.gif]](../Art/pbaddedcustomclass.gif)
4. Move the variables and methods relating to the person name
   and favorite food properties from `Main.java` to
   the new class.

   Select the `personName` and `favoriteFood` variables,
   as well as their accessor methods, from `Main.java` and
   choose Cut on the Edit menu. Then paste them into the `User.java` file.
5. Save `Main.java` and `User.java`.
6. Add a variable of type User to the Main component.
   1. Open the Main component
      in WebObjects Builder.
   2. Choose Add Key from the Edit Source menu.
   3. Name the variable `user` and
      choose User from the Type pop-up menu. Do not include accessor methods.
7. Instantiate the `user` variable
   in the Main class.

   You need to create a User object in the
   Main component. Make the constructor method of the Main class look
   like [Listing 6-1](#apple-ijbusqsbjbeeu).

   __Listing 6-1 Instantiating
   the user instance variable in the constructor of the Main.java class__

   ```
   public Main(WOContext context) {
       super(context);
       user = new User();
   }
   ```

   Save `Main.java`.
8. Change the bindings on the dynamic elements to use the new
   variable.

   Click `user` in
   the variable browser of WebObjects Builder's main window. Just
   as with creating other bindings, drag a connection from the variable `favoriteFood` to
   the WOTextField that is currently bound to `favoriteFood`.
   When you release the mouse button, a pop-up menu lists the bindings
   available.

   Notice that `value` has
   a checkmark next to it, indicating that it currently has a binding. Selecting `value` replaces `favoriteFood` with `user.favoriteFood`.

   Replace
   the `personName` binding
   in a similar fashion. Be sure to change both the WOStrings and the
   WOTextFields.
9. Update the `entryIncomplete` method.

   The `entryIncomplete` method
   in Main can no longer directly access the `personName` and `favoriteFood` instance
   variables because they are protected elements of the User class. It
   has to use the accessor methods that User provides. Make the changes
   necessary so that the method looks like [Listing 6-2](#apple-ijbusqsdjfees).

   __Listing
   6-2 Main.java's entryIncomplete method
   using the user instance variable__

   ```
   public boolean entryIncomplete() {
       if (user.personName() == null || user.favoriteFood() == null ||  user.personName().equals("") || user.favoriteFood().equals(""))  {
           return true;
       }
       else {
           return false;
       }
   }
   ```
10. Choose UserEntryCustomObject from the target pop-up menu.
11. Build and run the application.

    The behavior is the same
    as the one displayed by the UserEntry project, defined in ["Managing User Input"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/iManaging_User_Input.html),
    but the data is now being accessed via the new custom object.

### Following a Keypath

You'll notice that the bindings for the dynamic elements
are in a slightly different format. Rather than simply naming the
variable or method to call, they specify a more specific path to
the property in question: in this case, the `userName` variable
from the `user` object.
This is called a keypath.

Encapsulating data into objects, as in this example, is a
very important part of object-oriented development. Access to this
data is defined by a keypath that specifies the objects, methods,
or variables that can provide the data in question.

A keypath is a set of keys separated by periods. When WebObjects
requires access to data specified in a keypath, it follows the keypath
by evaluating the first key from the list.

This first key is evaluated within the scope of the instance
representing the component—the class file in the component is
examined for the method or variable. In this case, the `user` instance
variable found in the `Main.java` class.

At this point, if there is another key in the keypath, it
is evaluated the same way, but this time using the result of the
first keypath as the source object for the method or variable. Now,
the `personName` method
is called. Since there are no more keys in the keypath, the value
from the `personName` method
is returned as the value for the binding.

In this way, you can access the data you need, as long as
it can be reached by some method from the current component. In
the simplest case, you store variables in the component itself.
As your data becomes more complex, you may need to store it in custom
objects and pass them between components.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Component_Communication.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Defining_a_New_Component.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
