---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBookPlus/GuestBookPlus10.html
archived_at: '2026-07-18T01:21:20.077526Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Enhancing%20Your%20Application.md) [!Previous Section](GuestBookPlus9.md)

## Adding Guests to the Guest List

Now, when the user submits the form, you'll add the information to the __allGuests__ array rather than displaying it directly.

- Switch to the code for __Main.java__.
- In the __submit__ method, add the following code before the return statement:

```
((Application)application()).addGuest(currentGuest);
currentGuest = new Guest();
```


This code calls the application's __addGuest__ method, which adds an object (in this case, __currentGuest__) to the end of the array. Then it creates a new Guest object to hold the next guest's data.

__Note:__ The __addGuest__ method is defined in the class Application, which is a subclass of WOApplication. The component's __application__ method (called in the above statement) returns an object of type WOApplication, so you must cast it to Application in order to access its __addGuest__ method.

Your next step is to create a new component to display the list of guests that __allGuests__ stores.

[!Table of Contents](Enhancing%20Your%20Application.md) [!Next Section](Adding%20a%20Second%20Component.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
