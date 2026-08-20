---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/ComponentCommunication/Running_the_Application.html
archived_at: '2026-07-15T08:12:52.660078Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Modifying_t_n_component.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/SessionStateMaintenance/index.html)

## Running the Application

Make sure the ComponentCommunication target is selected. Build
and run the application. When the Main page is first displayed,
there is no user data to show (the `user` instance
variable is `null`), therefore
the message "User information has not been entered" appears
instead. When the user clicks Edit, the Main component invokes its `userEdit` action,
which returns a UserEdit page. If the user enters data into the
Name and Favorite Food text fields in the UserEdit page and clicks
submit, UserEdit's `submitChanges` action, which
returns a new Main page, is invoked.

There is only one instance of User during the application's
execution. The User object is instantiated in Main's `editUser` method
if it does not already exist (see [Listing 6-6](Modifying_t_n_component.md#apple-ijbusqsgi5auc). Main then sends this
object to the newly created UserEdit page. Similarly, UserEdit sends
the User object to a new Main instance in its `submitChanges` method.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Modifying_t_n_component.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/SessionStateMaintenance/index.html)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
