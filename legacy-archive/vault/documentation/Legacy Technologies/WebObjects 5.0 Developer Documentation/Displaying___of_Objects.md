---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/SessionStateMaintenance/Displaying___of_Objects.html
archived_at: '2026-07-15T08:13:26.783307Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](The_Session.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Running_the_Application.md)

## Displaying and Editing Lists of Objects

Before you begin, you should make a copy of the ComponentCommunication
project and name it SessionState. See ["Duplicating the UserEntry Project"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/ComponentCommunication/iCustom_Objects.html).

You'll now edit the Main component to show a list of users
instead of just one. For that, you'll need to use the NSArray
and NSMutableArray classes.

### The NSArray and NSMutableArray Classes

The NSArray represents an ordered collection of objects, much
like a Java array (java.lang.Array). NSArray
objects are not changeable after being instantiated. (The array itself
is not changeable, but the items it contains can be changed if their
types are mutable.) The NSMutableArray class (a subclass of NSArray)
is intended for arrays that need to grow and shrink dynamically.

The following sections list the NSArray and NSMutableArray
methods that you may find useful when manipulating arrays.

#### NSArray

**`objectAtIndex(int
index)`**
: Returns the object at the given integer index. The first
object in an NSArray is at index zero. Objects are returned as generic
Java Objects. Your Java code may need to cast objects to a specific
class to use them.

**`count`**
: Returns an integer indicating the number of objects
in the NSArray.

#### NSMutableArray

**`addObject(Object
anObject)`**
: Adds the given object to the end of the array, increasing
its size by one.

**`removeObjectAtIndex(int
index)`**
: Removes the indicated object from the array, causing
it to shrink in size.

In addition to these methods, the NSArray and NSMutableArray
classes have other methods you may find useful. You can examine
them using Java Browser.

### Adding the NSMutableArray to the Session

You can use WebObjects Builder to add an array to the Session
class.

1. Open `Main.wo` in
   WebObjects Builder.
2. Add the `userList` instance
   variable to `session`.
   1. Select `session` in
      the Main list.
   2. Control-click in the Session list.
       ![[image: ../Art/wobsessionaddkey.gif]](../Art/wobsessionaddkey.gif)
   3. Choose Add Key to Session from the pop-up menu.
   4. Name the variable `userList`.
   5. Select the "Mutable array of" option and then User from
      the pup-up menu.
   6. Under "Generate source code for," make sure only "An
      instance variable" is selected and click Add.
       ![[image: ../Art/compcommaddarray.gif]](../Art/compcommaddarray.gif)
3. Initialize the new array in `Session.java`.

   The
   NSMutableArray needs to be instantiated when the Session object
   is created. It will initially be empty, but you will provide methods
   to add objects to it.

   Edit the constructor of the `Session.java` class
   and add the `addToUserList` and `removeFromUserList` methods.
   When you're done the file should look like [Listing 7-1](#apple-ijbusskhjjeei).

   __Listing
   7-1 Session.java__

   ```
   import com.webobjects.foundation.*;
   import com.webobjects.appserver.*;
   import com.webobjects.eocontrol.*;

   public class Session extends WOSession {
       /** @TypeInfo User */
       protected NSMutableArray userList;

       public Session() {
           super();

           /* ** Put your per-session initialization code here ** */
           userList = new NSMutableArray();
       }
       public void addToUserList(User newUser) {
           userList.addObject(newUser);
       }
       public void removeFromUserList(User aUser) {
           userList.removeObject(aUser);
       }
   }
   ```

### Adding the WORepetition to Main

A WORepetition element is an element designed to iterate over
each item in an NSArray, repeating a set of HTML code (possibly
including WebObjects elements) once for each item.

A WORepetition has bindings for a list to iterate over (the `list` attribute)
and for a variable to use to hold each item temporarily as it iterates
over the list (the `item` attribute).
As the contents of a WORepetition are displayed, the current item
in the list is stored in the placeholder. WebObjects elements within
the WORepetition can refer to this placeholder variable, and the
value of each item is substituted in turn.

You'll wrap the dynamic elements in `Main.wo` in
a WORepetition. You can use the `user` instance
variable as the WORepetition's placeholder. After performing the
following steps, `Main.wo` should
look similar to [Figure 7-2](#apple-ijbusssfjbbuc).

1. In `Main.wo`,
   delete the first WOConditional element (the one that contains the
   text "User information has not been entered."
2. Cut the internal contents of the remaining WOConditional.
3. Select the WOConditional and delete it.
4. Paste the content after the Edit WOHyperlink.
5. Add a `deleteUser` method
   that returns `null`.
6. Add a WOHyperlink to delete users.
   1. Add a WOHyperlink
      element after the second WOString.
   2. Enter `Delete` as
      the WOHyperlink's caption.
   3. Add a carriage return after the WOHyperlink by pressing Shift-Enter.
   4. Bind the WOHyperlink's `action` attribute
      to the `deleteUser` method.
7. Wrap the dynamic elements in `Main.wo` with
   a WORepetition.
   1. Select all the elements in the page.
   2. Choose WebObjects > WORepetition.

      The elements are
      enclosed in a WORepetition element.
8. Bind the WORepetition's `list` attribute
   to `session.userList`.

   Drag
   from `session.userList` to
   the first square of the WORepetition.
9. Bind the WORepetition's `item` attribute
   to `user`.

   Drag from `user` to
   the second square of the WORepetition.
10. Add an `addUser` action
    that returns a UserEdit page.
11. Add a WOHyperlink to add new users.
    1. Add a WOHyperlink
       below the WORepetition.
    2. Enter `Add User` as
       the WOHyperlink's caption.
    3. Bind the WOHyperlink's `action` attribute
       to the `addUser` method.

__Figure
7-2 Main.wo with a WORepetition__

![[image: ../Art/wobsessionmainwo.gif]](../Art/wobsessionmainwo.gif)

### Editing the Users

You can use the UserEdit component to edit an arbitrary user.
To do so, you'll use the `editUser` method
in `Main.java`. The method
has additional logic that is not needed in this application. Edit
the `editUser` method so
that it looks like [Listing 7-2](#apple-krifqusfiyytcmy).

__Listing
7-2 The editUser method of the Main.java
class__

```
public UserEdit editUser() {
    UserEdit nextPage = (UserEdit)pageWithName("UserEdit");

    // Initialize your component here
    nextPage.setUser(user);
    return nextPage;
}
```

The `editUser` method
creates an instance of UserEdit and calls its `setUser` method
with `user` as the argument.
The `user` variable contains
the appropriate object because, when the user clicks Edit, WebObjects
stores the `session.userList` item
corresponding to the row on which the Edit link is located in the `user` instance
variable. Remember that the WORepetition's `item` attribute
is bound to `user`.

The UserEdit component requires a minor change. The `submitChanges` method
in `UserEdit.java` no longer
needs to invoke the `setUser` method
of the `Main.java` class
(user information is stored at the session level, which Main can
access through the `session` object).
Edit the `submitChanges` method
so that it looks like [Listing 7-3](#apple-infeercbinduq).

__Listing
7-3 The submitChanges method of the UserEdit.java
class__

```
public Main submitChanges() {
    Main nextPage = (Main)pageWithName("Main");

    // Initialize your component here
    return nextPage;
}
```

### Adding Users

This is where it all ties together. Right now, you have a
means of editing a specific user (the UserEdit component); a list
of users, which starts out empty (`session.userList)`;
and a WORepetition that displays your list (in the Main component).
All you need to add is a way to build the list!

You need to edit the `addUser` method
in `Main.java` so that
it creates a new User object, adds it to the session's list of
users, and also passes it to the UserEdit page before it is sent
to the Web browser to be edited. Edit `addUser` so
that it matches [Listing 7-4](#apple-infeessgirces). Notice in particular the code that retrieves the
Session object. The `addToUserList` method
of that object is then invoked with the newly created User object
as the argument.

__Listing
7-4 The addUser method of the Main.java
class__

```
public UserEdit addUser() {
    UserEdit nextPage = (UserEdit)pageWithName("UserEdit");

    // Initialize your component here
    Session session = (Session)session();  // get session for current user
    User newUser = new User();             // create a new user object
    session.addToUserList(newUser);  // add new user to session's userList
    nextPage.setUser(newUser);       // send the new user to UserEdit
    return nextPage;
}
```


### Deleting Users

The last step is to edit the `deleteUser` method
in `Main.java` so that
it removes a user from the list. The method is very similar to the `addUser` method
described in ["Displaying and Editing Lists of Objects"](#apple-krifqusfiyytany). The only difference
is that, instead of creating a new user object and invoking the `Session.addToUserList` method,
it only invokes the `Session.removeFromUserList` method
with the User object in the `user` instance
variable (updated by WebObjects when the user clicks Delete).

Edit the `deleteUser` method
in `Main.java` so that
it looks like [Listing 7-5](#apple-infeeq2cifdui).

__Listing
7-5 The deleteUser method of the Main.java
class__

```
public WOComponent deleteUser() {
    Session session = (Session)session();// get session for current user
    session.removeFromUserList(user);// remove user from session's userList
    return null;
}
```

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](The_Session.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Running_the_Application.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
