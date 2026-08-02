---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToJavaClient/Tutorial/Configuring_Entities.html
archived_at: '2026-07-15T08:12:20.961730Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](The_Assistant.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Configuring_Properties.md)

## Configuring Entities

The default set of rules that Direct to Java Client uses to
identify main, enumeration, and _other_ entities
are a pretty good start. However, you might need to make some changes
to the way Direct to Java Client classifies your application's
entities. For example, this tutorial application doesn't use the
User entity, so you need to remove it from the list of main entities.

1. Specify the
   User entity as an "Other" entity.

   In the Assistant window,
   ensure that the "Entities" tab is selected. In the Main Entities list,
   select User. Click the arrow pointing to the left to move the User
   entity from the Main Entities list to the Other Entities list.
2. Rearrange the entities.

   By default, the entities are
   ordered alphabetically. For example, in the Query Window, the Customer
   tab is first, then Movie, and so on. In this application, it makes
   more sense to group Movie, Talent, and Studio together and group
   Customer, Unit, and Video.

   In the Main Entities list,
   select Movie. Click the arrow pointing up to move the Movie entity
   to the top of the list. Move Talent so it's next in the list,
   then Studio. Customer, Unit, and Video, in that order, should be
   last in the list.
3. Apply the changes.

   Click Apply. This updates the Assistant's
   in-memory set of rules. The new rules don't affect existing windows,
   but they are applied when Direct to Java Client generates new user-interfaces
   in the running client application.

   To see that your
   changes have been recorded in the Assistant's set of rules, choose
   Tools > New Query Window. The new Query Window that opens doesn't
   have a tab for User, and the window's tabs are ordered as you
   specified in step 2.
4. Restart the application.

   Click Restart. This restarts
   the client application using the Assistant's in-memory set of rules.
   In the new instance of the application, the Query Window immediately
   displays the changes you specified.

   Since you can't
   update an application's existing user interface by applying changes, you
   can use Restart to reflect your changes throughout the entire application.
   If you don't like the changes, you can revert them by clicking
   Revert.
5. Save your changes.

   Click Save. This updates the set of
   rules saved in your project. Once you have saved the changes, you
   can no longer revert.

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](The_Assistant.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Configuring_Properties.md)

© 2001 Apple Computer, Inc.
