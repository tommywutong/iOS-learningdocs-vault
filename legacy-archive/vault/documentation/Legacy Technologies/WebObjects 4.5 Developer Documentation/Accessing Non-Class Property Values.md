---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.34.html
archived_at: '2026-07-15T08:09:59.539923Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Accessing%20Schema%20Information%20from%20the%20Database%20Server.md) [!](Refreshing%20Data%20by%20Refetching%20from%20the%20Database%20or%20Invalidating%20an%20Object.md)

#   Accessing Non-Class Property Values

##  Synopsis

While anything that is not marked as a class property should be regarded simply as a database artifact (and not something to be accessed), you might need to read a non-class property value on rare occasions. One such example would be the need to obtain a foreign key for the generation of a qualifier. This discussion explains how to read a non-class property value, and provides an example of obtaining the primary key for an object when the object's primary key is not a class property.

##  Discussion

Any attribute marked as a class property in EOModeler is included in a class definition when you generate source files for a class. In addition, any attributes marked as class properties are fetched and passed to your enterprise objects when you create instances from the database. Anything you mark as a class property should have a meaningful value in the object graph created when you fetch data from the database. Attributes that are essentially database artifacts you do not want to include in the user interface such as primary keys should not be marked as class properties. Anything you do not mark as a class property will not be part of your enterprise object, nor will it be inserted into an editing context, so you cannot use normal accessor methods to obtain their values.

However, you might need access to a primary or foreign key, such as when you are writing a restricting qualifier in single-table inheritance and you must use the value of the foreign key. How do you go about getting this information? How do you gain access to the raw data of the database before it gets pushed into the enterprise object.

EOUtilities provides a set of convenience methods for accessing raw rows of data, for accessing primary and foreign keys, and for accessing other attributes that are not class properties. (EOUtilities is an EOAccess class in Java and, in Objective-C, a category of methods on EOEditingContext.) The following EOUtilities methods are useful for accessing primary and foreign keys:

```

public static com.apple.yellow.foundation.NSDictionary
    primaryKeyForObject(EOEditingContext ec, EOEnterpriseObject eo);
public static com.apple.yellow.foundation.NSDictionary
    destinationKeyForSourceObject(EOEditingContext ec,
    EOEnterpriseObject eo, String relationship);
```


The second method returns the foreign key for the rows at the destination entity of the specified relationship.

You can also access other items of data from the database that are not marked as class properties by using the following EOUtilities methods to fetch raw rows at the adaptor level.

```

public static com.apple.yellow.foundation.NSArray
    rawRowsWithQualifierFormat(com.apple.yellow.eocontrol.EOEditingContext
    ec, String entityName, String qualifierFormat,
    com.apple.yellow.foundation NSArray arguments);
public static com.apple.yellow.foundation.NSArray
    rawRowsMatchingKeyAndValue (com.apple.yellow.eocontrol.EOEditingContext
    ec, String entityName, String key, Object value);
public static com.apple.yellow.foundation.NSArray
    rawRowsMatchingValues (com.apple.yellow.eocontrol.EOEditingContext ec,
    String entityName,
    com.apple.yellow.foundation.NSDictionary matchingValues);
public static com.apple.yellow.foundation.NSArray
    rawRowsForSQL (com.apple.yellow.eocontrol.EOEditingContext ec,
    String modelName, String sql);
public static com.apple.yellow.foundation.NSArray
    rawRowsForStoredProcedureNamed (
    com.apple.yellow.eocontrol.EOEditingContext ec, String procedureName,
    com.apple.yellow.foundation.NSDictionary arguments);
```



```

Here is a code example that gets a foreign key and uses it to qualify a fetchEOEditingContext ec;
EOEnterpriseObject studio;
NSDictionary foreignKeyToStudio;
NSArray moviesMGM;
ec = session().defaultEditingContext();
studio = EOUtilities.objectMatchingKeyAndValues(ec, "Studio", "name",
     "MGM");
// destinationKeyForSourceObject returns the foreign key in a
// form that can be used to qualify the destination
foreignKeyToStudio = EOUtilities.destinationKeyForSourceObject(ec. studio,
     "movies");
// You can use non-class properties to qualify a database fetch
moviesMGM = EOUtilities.objectsMatchingValues(ec, "Movie",
    foreignKeyToStudio);
```


##  See Also

- 

  EOUtilities class specification (Java) in the _Enterprise Objects Framework Reference_
- 

  EOUtilities category specification (Objective-C) in the _Enterprise Objects Framework Reference_

##  Questions

- 

  How do I access a non-class property of an object?
- 

  How do I get a row's primary key?
- 

  How do I get a destination object's foreign key?
- 

  How do I fetch at the adaptor level?
- 

  How do I get column data that are not instance variables of an enterprise object?

##  Keywords

- 

  EOUtilities
- 

  Property
- 

  Fetch
- 

  Specification
- 

  Key
- 

  Primary
- 

  Foreign
- 

  Entity

##  Revision History

24 July 1998. Virginia McCulloh. First Draft.

18 November 1988. Terry Donoghue. Second Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Accessing%20Schema%20Information%20from%20the%20Database%20Server.md) [!](Refreshing%20Data%20by%20Refetching%20from%20the%20Database%20or%20Invalidating%20an%20Object.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
