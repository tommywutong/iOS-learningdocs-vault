---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies6.html
archived_at: '2026-07-15T07:55:02.966115Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies5.md)

## Specifying Primary Keys

If you are using a database that stores primary key information in its database server's schema information, the wizard skips this step. The wizard has already successfully read primary key information from the schema information and assigned primary keys to your model.
However, if primary key information isn't specified in your database server's schema information (as with Microsoft Access), the wizard now asks you to specify a primary key for each entity.!

- Select __movieId__ as the primary key for the Movie entity.
- Click Next.
- Select both __movieId__ and __talentId__ as the primary key for the MovieRole entity.

MovieRole's primary key is _compound_; that is, it's composed of more than one attribute. Use a compound primary key when any single attribute isn't sufficient to uniquely identify a row. For MovieRole, the combination of the __movieId__ and __talentId__ attributes is guaranteed to uniquely identify a row.

- Click Next.
- Select __talentId__ as the primary key for the Talent entity.
- Click Next.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies7.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
