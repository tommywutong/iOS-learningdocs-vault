---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies32.html
archived_at: '2026-07-18T01:22:34.383855Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies31.md)

## Adding Relationships to Your Model

The Movies application uses two pairs of inverse relationships. The first pair defines the relationship between the Movie and MovieRole entities, while the second pair defines the relationship between the MovieRole and Talent entities. An Enterprise Objects Framework relationship is _directed_; that is, a relationship has a source and a destination. Generally models define a relationship for each direction.

- Select the Movie entity.

The right frame of the Model Editor shows the Movie's relationships as well as its attributes.>

!

Your model's Movie entity might have a different name than the __toMovieRole__ relationship shown above. That's because the wizard created your relationship, and the relationship's name is dependent on the adaptor the wizard used. Adaptors don't all have the same naming convention for to-many relationships. For example, the Oracle adaptor names Movie's relationship __movieRoleArray__ instead of __toMovieRole__.

If your Movie entity doesn't have a __toMovieRole__ relationship, it means that the database server's schema information for your database didn't have enough information for the wizard to create them. You need to create them by hand now. The next several steps explain how.

- Choose Property ! Add Relationship.

A new relationship named "Relationship" is added in the table view at the bottom of the Model Editor. The new relationship is already selected.

- With the relationship selected in the right frame of the Model Editor, click the ! button (in the toolbar) to inspect the relationship.

!

- In the Inspector, select the To Many option.
- Select MovieRole as the destination entity.
- Select __movieId__ in the Source Attributes list.
- Select __movieId__ in the Destination Attributes list.
- Click Connect.

EOModeler automatically renames the relationship based on the name of the destination entity. For example, after connecting a
to-many relationship from Movie to MovieRole, EOModeler names the relationship "toMovieRole." To-one relationships are named with the singular form of the destination entity's name. For example, EOModeler names the inverse to-one relationship (from MovieRole to Movie) "toMovie."

If the wizard created your relationship and used a name other than "toMovieRole," consider renaming the relationship. The rest of this tutorial assumes that your relationships are named using EOModeler's naming convention.

- Repeat the steps above to create the following relationships (if they do not already exist):

A to-one relationship named "toMovie" in the MovieRole entity where:

- The destination entity is Movie.
- The source attribute is __movieId__.
- The destination attribute is __movieId__.

A to-one relationship named "toTalent" in the MovieRole entity where:

- The destination entity is Talent.
- The source attribute is __talentId__.
- The destination attribute is __talentId__.

A to-many relationship named "toMovieRole" in the Talent entity where:

- The destination entity is MovieRole.
- The source attribute is __talentId__.
- The destination attribute is __talentId__.

- Choose ! in the toolbar pop-up list to switch the Model Editor to Diagram View.

!

At this point your model has all the relationships it needs. The Diagram View gives you an overview of the entities in the model and their relationships to other entities.

!

You can also use the Diagram View to edit your model. Double-click an attribute or relationship to change its name. To create a relationship and its inverse, Control-drag from the relationship's source attribute to its destination attribute.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies33.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
