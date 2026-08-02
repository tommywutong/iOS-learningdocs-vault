---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.1c.html
archived_at: '2026-07-15T08:07:17.617279Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Creating%20a%20Custom%20Guest%20Class.md) [!](Binding%20the%20Dynamic%20Elements%20in%20the%20Table.md) [!](Keeping%20Track%20of%20Multiple%20Guests.md)

---

#  Creating the Guest Object

Earlier in this chapter, you created a Java class of type Guest and wrote a constructor for it. You also added a variable of that class, __currentGuest__, to the Main component. However, adding a variable to the component doesn't actually create a new Guest object; you need to create one explicitly at some point in your code.

You'll create the Guest object in the constructor method for your component. This method is called when the component is first created; that is, the first time the user accesses the component.

__Note:__ In WebScript or Objective-C, you use a method called __init__ for this purpose.

1. 

   Choose View Source File from the pull-down list at the bottom of the window.

   Project Builder becomes active and displays the code for __Main.java__. Notice the following declaration that was added to your code when you added the __currentGuest__ variable:

   protected Guest currentGuest;
2. 

   Delete the declarations of __guestName__, __email__, and __comments__ since you aren't using them anymore.
3. 

   Add the constructor method inside the Main class definition:

   public Main() {
      super();
      currentGuest = new Guest();
    }

   The first statement calls the constructor of Main's superclass (which is __com.apple.yellow.webobjects.WOComponent__). The second statement allocates a new empty Guest object and calls Guest's constructor to initialize its instance variables.
4. 

   Save __Main.java__.
5. 

   Build and run your application.

   The application should work similarly to that in the first chapter, except that the guest's data is displayed in a table at the bottom of the page instead of as plain text.

   !

   At this point, your application still handles information from a single guest only; in the next section, you'll modify the application so that it can keep track of multiple guests.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Creating%20a%20Custom%20Guest%20Class.md) [!](Binding%20the%20Dynamic%20Elements%20in%20the%20Table.md) [!](Keeping%20Track%20of%20Multiple%20Guests.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
