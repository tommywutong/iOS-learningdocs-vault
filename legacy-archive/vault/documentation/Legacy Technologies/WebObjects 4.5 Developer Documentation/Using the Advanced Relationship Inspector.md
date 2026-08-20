---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.47.html
archived_at: '2026-07-15T08:08:11.464397Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Refining%20Your%20Model.md) [!](Adding%20Relationships%20to%20Your%20Model.md) [!](Where%20Do%20Primary%20Keys%20Come%20From.md)

---

#  Using the Advanced Relationship Inspector

There are several additional settings you use to configure a relationship's referential integrity rules. For these, use the Advanced Relationship Inspector.

1. 

   Inspect Movie's __toMovieRole__ relationship.
2. 

   In the Inspector, click the Advanced Relationship button.!
3. 

   Ensure that the delete rule is set to Cascade.

   If the wizard created relationships for you, the relationship's delete rule should already be set to Cascade. You specified this in the wizard. If you created your relationships by hand, you'll have to set the delete rule yourself.
4. 

   Ensure that the Owns Destination box is checked.

   As with the delete rule, if the wizard created relationships for you, the relationship's Owns Destination box should already be checked. If you created your relationships by hand, you'll have to check this box yourself.
5. 

   Check the Propagate Primary Key box.

   A relationship that propagates its primary key _propagates_ its key value to newly inserted objects in the destination of the relationship. In this case, checking the Propagate Primary Key box means that if you create a new MovieRole and add it to a Movie's list of MovieRoles, the Movie object automatically assigns its __movieId__ value as the value for the new MovieRole's __movieId__ property.

   This option is usually used with relationships that own their destination. For more information on propagating primary keys, see [Where Do Primary Keys Come From?](Where%20Do%20Primary%20Keys%20Come%20From.md#apple-gi2dmnbw)
   .
6. 

   Ensure that Talent's __toMovieRole__ relationship has its delete rule set to Deny.
7. 

   Ensure that Talent's __toMovieRole__ relationship owns its destination.
8. 

   Set Talent's __toMovieRole__ relationship to propagate its primary key.
9. 

   Choose Model !
   Save (File !
   Save on Windows NT) to save your model.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Refining%20Your%20Model.md) [!](Adding%20Relationships%20to%20Your%20Model.md) [!](Where%20Do%20Primary%20Keys%20Come%20From.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
