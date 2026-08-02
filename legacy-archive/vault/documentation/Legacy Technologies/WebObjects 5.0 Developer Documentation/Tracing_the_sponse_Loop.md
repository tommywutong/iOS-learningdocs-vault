---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/UserInput/Tracing_the_sponse_Loop.html
archived_at: '2026-07-15T08:13:35.345493Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](User_Interface.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Conditional_al_Elements.md)

## Tracing the Request-Response Loop

Now you'll modify the methods in your Java files to display
a message indicating when they're called, so you can watch the
phases of the request-response loop in action.

Each time the user submits a request, the contents of the
text fields are sent with the request. WebObjects then determines
the properties to update and the methods to invoke using the WOD
file.

Selecting the options under "Generate source code for"
when you added the `favoriteFood` and `personName` keys
to the Main component caused WebObjects Builder to insert not just two
String variables, but also two methods that are used to update those
variables (the accessor methods, a getter method and a setter method).
If you add Java printing statements to those methods and to the `addPerson` action
method, you can watch them being called during the request part
of the request-response loop. If you add the other methods described
in ["Request Processing"](Request_Processing.md#apple-ijbegssbinduq),
you can watch them being called as you use the application, as well.

Edit the Session.java, Application.java,
and Main.java files to add the `awake` method
so you can track the processing of the request. You can use the
Java `System.out.println` method
to log text to the console of your application; it is then displayed
in the Run pane of Project Builder's main window. Add the method
in [Listing 5-4](#apple-ijauursfjfeui) to
all three files.

__Listing
5-4 Tracing the request-response loop—the
awake method__

```
public void awake() {
    super.awake();
    System.out.println(this.getClass().getName() + "'s awake method called");
}
```

This method prints the name of the class followed by a notification
that the `awake` method was
called in each class that you put it in. Notice that it calls `super.awake` to
ensure that the superclass's `awake` method
is called before executing its custom logic.

Edit the `setPersonName`, `setFavoriteFood`,
and `addUser` methods in `Main.java` to
log strings to the console when they are called. Your methods should
look like the ones in [Listing 5-5](#apple-ijauuq2eijduq).

__Listing
5-5 Tracing the request-response loop—the
accessor and action methods__

```
public void setPersonName(String newPersonName) {
    System.out.println("Setting personName to '" + newPersonName + "'");
    personName = newPersonName;
}

public void setFavoriteFood(String newFavoriteFood) {
    System.out.println("Setting favoriteFood to '" + newFavoriteFood + "'");
    favoriteFood = newFavoriteFood;
}

public WOComponent addUser() {
    System.out.println("The submit button was clicked.");
    return null;
}
```

Build and run the new application, correcting any errors revealed
during compilation if necessary.

 ![[image: ../Art/pbuserinputrun.gif]](../Art/pbuserinputrun.gif)

Notice that when the page first loads, the `awake` methods
are called. This is because the request-response loop is run through
the first time the page is generated. Also notice that your `set` methods
are not called. This is because at the time of the first request
the user has not yet filled in any text fields, so the state synchronization
phase does not take place (See ["Processing the Request"](Request_Processing.md#apple-krifqusfiyytaoa)).

Fill in the data fields and click Submit.

 ![[image: ../Art/userentrytracerequest.gif]](../Art/userentrytracerequest.gif)

When you click Submit, you'll be able to watch the request
portion of the request-response loop through Project Builder's
output window as variables are updated.

```
Application:awake method called
Session:awake method called
Main:awake method called
Setting personName to 'Joshua Marker'
Setting favoriteFood to 'Sushi'
The submit button was clicked.
```

Because of the `printLn` method
calls added, you can see that WebObjects calls each `awake` method,
does variable assignment, and then calls the action method you assigned
to the submit button. This means that if code in the `addUser` method
referred to the `favoriteFood` or `personName` variables,
the values provided by the user would be available, rather than old
values, if any. You can take advantage of this to set other variables
in your component. For example, currently the form fields remain
active even after the user has filled them in. You could make the
fields disappear once the necessary data has been entered by checking in
the `addUser` method to
see if both fields are filled in and setting a Boolean property
to indicate whether the entry is still incomplete. You could then
use a WOConditional element to hide some elements of the component.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](User_Interface.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Conditional_al_Elements.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
