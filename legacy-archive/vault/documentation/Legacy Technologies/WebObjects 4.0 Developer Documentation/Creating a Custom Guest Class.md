---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBookPlus/GuestBookPlus2.html
archived_at: '2026-07-18T01:21:36.301038Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__ [WebObjects
4.0 Documentation](../../../../../../webobjects.md)
__>__ [Getting
Started With WebObjects](../GettingStartedTOC.md)

 [!Table
of Contents](GuestBookPlus.md) [!Previous
Section](GuestBookPlus1.md) 

# Creating a Custom Guest Class

 In the first chapter, you created individual
variables to store a guest's name, e-mail address, and comments. When
keeping track of multiple guests, it's more useful to encapsulate all
the data for a guest as a single entity. You'll do this by creating a
Java class that contains the data for a single guest.

1.  In Project Builder's browser, select Classes
   in the first column. 
2. Choose File !
   New in Project. 
   !

3. Type Guest.java as the name of the file. 
4. Click OK. 

   The newly created file contains a skeleton for a class called
   Guest.

5. Modify the code so it looks like this:

   ```
   import com.apple.yellow.foundation.*;
   import com.apple.yellow.eocontrol.*;
   import com.apple.yellow.webobjects.*;

   public class Guest extends EOCustomObject {
      protected String guestName;
      protected String email;
      protected String comments;

      Guest() {
         guestName = "";
         email = "";
         comments = "";
      }
   }
   ```
6.  A class stores information in its
   _instance variables_ (also referred to as _data
   members_). Here you're declaring three instance variables for
   Guest: __guestName__, __email__, and
   __comments__. Note that these declarations are the
   same as those that appeared in the code for
   __Main.java__ when you added the three variables
   using WebObjects Builder. In WebObjects, a component is also a
   class, specifically a subclass of the class WOComponent.

   Java classes require a _constructor_ to initialize an
   instance (or _object_) of a particular class whenever one
   is created. A constructor has the same name as the class and
   returns no value.

   Whenever your application creates a new Guest class, its
   instance variables are initialized with empty strings, which is
   the default value if the user enters no data. (If you prefer, you
   can use different strings for these initial values.)

7. Save __Guest.java__ by choosing Save from the
   File menu. 

   Saving the file lets WebObjects Builder know about your newly
   created Guest class.

[!Table
of Contents](GuestBookPlus.md) [!Next
Section](GuestBookPlus3.md)

|  |
| --- |
| --- |
|         Choose Area to Search ------------------------------- Macintosh Documentation QuickTime Documentation Java Documentation Hardware Documentation WebObjects Documentation Mac OS X Server Documentation ------------------------------- Apple Technical Publications Apple Developer Connection     __Find:__       Copyright © 1998 Apple Computer, Inc. [All rights reserved.](http://www.apple.com/legal/) |
