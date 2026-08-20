---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies8.html
archived_at: '2026-07-18T01:23:08.670657Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies7.md)

## Specifying Referential Integrity Rules

If you're using a database that stores foreign key definitions in its database server's schema information, the wizard reads them and creates corresponding relationships in your model. For example, Movie has a
to-many relationship to MovieRole (that is, a Movie has an array of MovieRoles), and Talent has a to-many relationship to MovieRole. The wizard now asks you to provide additional information about the relationships so it can further configure them.

!

If foreign key definitions aren't specified in your database server's schema information (as with Microsoft Access), the wizard hasn't created any relationships at all, and it skips this step. You'll add relationships to your model using EOModeler later in this tutorial.
In the first relationship configuration page, the wizard asks you about Movie's relationship to MovieRole. The name of the relationship is dependent on the adaptor you're using.

- Check the "Movie owns its MovieRole objects" box.

!

This option specifies that a MovieRole can't exist without its Movie. Consequently, when a MovieRole is removed from its Movie's array of MovieRoles, the MovieRole is deleted-deleted in memory and deleted in the database.

- Choose Cascade.

!

This option specifies what to do when the source object (the Movie) is deleted. The cascade delete rule specifies that when a source object is deleted, the source's destination objects should also be deleted-again, deleted in memory and correspondingly in the database.

- Click Next.

Now the wizard asks you about Talent's relationship to MovieRole.

- Check the "Talent owns its MovieRole objects" box.
- Choose Deny.

The deny delete rule specifies that if the relationship source (a Talent) has any destination objects (MovieRoles), then the source object can't be deleted.

- Click Next.

You're done with the model configuration part of the wizard. The rest of the wizard pages are to help you configure your application's user interface.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies9.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
