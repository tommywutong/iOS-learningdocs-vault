---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.2d.html
archived_at: '2026-07-15T08:07:37.689227Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Designing%20the%20Main%20Page.md) [!](Choosing%20the%20Tables%20to%20Include.md) [!](Specifying%20Referential%20Integrity%20Rules.md)

---

#  Specifying Primary Keys

If you are using a database that stores primary key information in its database server's schema information, the wizard skips this step. The wizard has already successfully read primary key information from the schema information and assigned primary keys to your model.

However, if primary key information isn't specified in your database server's schema information (as with Microsoft Access), the wizard now asks you to specify a primary key for each entity.!

1. 

   Select __movieId__ as the primary key for the Movie entity.
2. 

   Click Next.
3. 

   Select both __movieId__ and __talentId__ as the primary key for the MovieRole entity.

   MovieRole's primary key is compound; that is, it's composed of more than one attribute. Use a compound primary key when any single attribute isn't sufficient to uniquely identify a row. For MovieRole, the combination of the __movieId__ and __talentId__ attributes is guaranteed to uniquely identify a row.
4. 

   Click Next.
5. 

   Select __talentId__ as the primary key for the Talent entity.
6. 

   Click Next.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Designing%20the%20Main%20Page.md) [!](Choosing%20the%20Tables%20to%20Include.md) [!](Specifying%20Referential%20Integrity%20Rules.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
