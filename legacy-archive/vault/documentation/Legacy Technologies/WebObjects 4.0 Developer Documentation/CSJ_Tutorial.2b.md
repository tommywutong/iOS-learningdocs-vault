---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.2b.html
archived_at: '2026-07-15T07:59:55.745947Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.2a.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.2c.md)

## Enterprise Objects Framework Concepts

### Note to Oracle Users

The Oracle login panel is designed to work with SQL\*Net v2, which gets the host machine name from the file __tnsnames__
__.__
__ora__
. If you're using
SQL\*Net v1, you must explicitly supply the host machine name along with the server ID in the Server ID field by using a string of the following format:

_T:hostMachine:serverID_

For example, if you are using a host machine called "tahoe" and your database's server ID is "eof," you can connect the database by typing the following in the Server ID field:

T:tahoe:eof

###   What is an Enterprise Object?

An enterprise object is like any other object, in that it couples data with the methods for operating on that data. However, an enterprise object class has certain characteristics that distinguish it from other classes:

- It has properties that map to stored data; an enterprise object instance typically corresponds to a single row or record in a database.

- It knows how to interact with other parts of the Framework to give and receive values for its properties.

The ingredients that make up an enterprise object are its class definition and the data values from the database row or record with which the object is instantiated. An enterprise object also has a corresponding model that defines the mapping between the class' object model and the database schema.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.2a.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.2c.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
