---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies33.html
archived_at: '2026-07-15T07:54:43.259440Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies32.md)

## Using the Advanced Relationship Inspector

There are several additional settings you use to configure a relationship's referential integrity rules. For these, use the Advanced Relationship Inspector.

- Inspect Movie's __movieRoles__ relationship.
- In the Inspector, click the Advanced Relationship button.
!- Ensure that the delete rule is set to Cascade.

If the wizard created relationships for you, the relationship's delete rule should already be set to Cascade. You specified this in the wizard. If you created your relationships by hand, you'll have to set the delete rule yourself.

- Ensure that the Owns Destination box is checked.

As with the delete rule, if the wizard created relationships for you, the relationship's Owns Destination box should already be checked. If you created your relationships by hand, you'll have to check this box yourself.

- Check the Propagate Primary Key box.

A relationship that propagates its primary key _propagates_ its key value to newly inserted objects in the destination of the relationship. In this case, checking the Propagate Primary Key box means that if you create a new MovieRole and add it to a Movie's list of MovieRoles, the Movie object automatically assigns its __movieId__ value as the value for the new MovieRole's __movieId__ property.

This option is usually used with relationships that own their destination. For more information on propagates primary keys, see ["Where Do Primary Keys Come From?"](Movies34.md#apple-ge2tmobx).

- Ensure that Talent's __movieRoles__ relationship has its delete rule set to Deny.
- Ensure that Talent's __movieRoles__ relationship owns its destination.
- Set Talent's __movieRoles__ relationship to propagate its primary key.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies34.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
