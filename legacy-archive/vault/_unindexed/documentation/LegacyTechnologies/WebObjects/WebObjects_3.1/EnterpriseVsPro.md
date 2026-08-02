---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/EnterpriseVsPro.html
archived_at: '2026-07-15T07:48:09.955520Z'
---
> 导航：[总目录](../../../../../README.md) · 未编入索引的页面


__### Differences Between WebObjects Enterprise and Pro__
WebObjects Enterprise and WebObjects Pro are very similar products. They provide the same tools for generating dynamic, web-based database applications and are based on the same database integration technology, Enterprise Objects Framework. However, the two products are suited for different sets of requirements. WebObjects Enterprise is intended for enterprise intranet and popular internet sites. As such, the Enterprise product has advantages over WebObjects Pro in the following areas:

- Performance and Scalability
- Database Access
- Application Architecture

The following sections describe the differences in more detail.

__Performance and Scalability__
WebObjects Enterprise provides essentially unlimited scalability. WebObjects Pro, on the other hand, is intended for workgroup intranet and smaller internet sites. Specifically, the Enterprise product provides the following performance and scalability advantages over Pro:

**_Multiple Application Instances_**
: With the Enterprise product, you can deploy WebObjects application servers on multiple hardware servers. You can also run multiple instances of an application on each server. In contrast, WebObjects Pro limits your deployment to running a single instance of each WebObjects application on a single hardware server.

**_Separate Application and HTTP Server Systems_**
: With WebObjects Pro, WebObjects applications must execute on the same hardware system as the web server. There is no such restriction in the Enterprise product.

**_NSAPI and ISAPI Adaptors_**
: With WebObjects Enterprise, you can choose to use native interfaces for Netscape (NSAPI) and Microsoft (ISAPI) web servers instead of the Common Gateway Interface. With WebObjects Pro, you are limited to the lower-performance CGI adaptor.

**_Native Database Client Libraries_**
: WebObjects Enterprise supports native database client libraries for Sybase, Oracle, and Informix. On Windows NT, WebObjects Pro only supports ODBC database access.

__Database Access__Both WebObjects Enterprise and Pro provide NeXT's Enterprise Objects Framework for integrating databases with your web-based applications, but WebObjects Enterprise offers the following database access advantages over WebObjects Pro:

**_Adaptors_**
: WebObjects Pro for UNIX platforms includes adaptors for Informix, Oracle and Sybase. WebObjects Pro for Windows NT includes the ODBC adaptor instead. WebObjects Enterprise includes the Informix, Oracle and Sybase adaptors on all platforms, and the ODBC adaptor on the Windows NT platform only. In addition, WebObjects Enterprise applications can use third party or custom adaptors (such as those from Yrrid and Connextions) to access legacy database systems. WebObjects Pro only supports the adaptors included with the product.

**_Optimized relationship access_**
: WebObjects Enterprise provides mechanisms (_prefetching relationships_ and _batch faulting_) for optimizing relationship resolution. WebObjects Pro doesn't provide the same mechanisms.

**_Stored procedure support_**
: WebObjects Enterprise provides support for invoking stored procedures, while WebObjects Pro does not.

__Application Architecture__Enterprise Objects Framework establishes the major portion of a database application's architecture by specifying how data is fetched from the database into objects and back. While WebObjects Enterprise provides all the functionality of Enterprise Objects Framework, the functionality is limited in WebObjects Pro. The primary difference is that in the Enterprise product, you can create custom classes to couple business logic with data from a database. WebObjects and Enterprise Objects Framework automatically create instances of your custom classes and invoke their logic (data validation, for example). In WebObjects Pro, you can't use custom enterprise object classes. Instead, you are restricted to using EOGenericRecords.

Enterprise Objects Framework is also limited in other ways in WebObjects Pro. As a result, the WebObjects product you choose determines some details of application architecture. The following list summarizes the architectural advantages of WebObjects Enterprise:

**_Custom business objects_**
: With WebObjects Enterprise, you can create custom classes to couple business logic with data from a database. In WebObjects Pro, you are restricted to using EOGenericRecords as described above.

**_Entity inheritance_**
: In WebObjects Enterprise, you can model inheritance relationships. For example, you can specify that a Customer entity is the parent of the Guest and Member entities. Then Guest and Member objects can get some of their data from their parent CUSTOMER table and the rest of their data from the GUEST and MEMBER tables, respectively. WebObjects Pro does not support such _deep fetching_. (See the chapter "Designing Enterprise Objects" in _Enterprise Objects Framework Developer's Guide_ for a discussion about using inheritance.)

**_Multiple model files_**
: With WebObjects Enterprise, you can access multiple model files in a single application. With WebObjects Pro, you can only access one. As a result, a WebObjects Pro application can't access multiple databases. In contrast, a WebObjects Enterprise application can fetch some of its data from an Oracle database and the rest from an Informix database, for example. In addition, WebObjects Enterprise applications can define cross-database relationships.

**_Multi-table mapping_**
: With WebObjects Enterprise, you can populate an object's instance variables from data in more than one database table by _flattening_ attributes. In WebObjects Pro, an object's instance variables each must map to a column in one root table.

**_Referential integrity_**
: With WebObjects Enterprise, you can specify referential integrity rules on relationships. For example, you can specify that the deletion of a Customer is denied if the customer has any Rentals. Similarly, you can specify that the deletion of a Customer should _cascade_ to delete all the customer's Guests as well. WebObjects Pro doesn't enforce referential integrity rules. In a WebObjects Pro application, deleting an object always has the side-effect of inserting NULL values in the foreign key fields of related objects.
