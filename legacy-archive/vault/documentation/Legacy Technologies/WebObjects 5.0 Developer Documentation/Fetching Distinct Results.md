---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.1f.html
archived_at: '2026-07-15T08:14:51.900756Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.1e.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.20.md)

#   Fetching Distinct Results

##  Synopsis

Describes how to use the EOFetchSpecification
setUsesDistinct
method to omit duplicate records during a fetch.

##  Discussion

Duplicate records sometimes appear in database fetches, usually when the fetch involves joining multiple tables to satisfy the fetch qualifier. The EOFetchSpecification allows you to specify whether you want these duplicate records with the
setUsesDistinct
method. The EOF adaptor modifies its query based on this setting. The standard relational database adaptors add the SQL keyword
DISTINCT
to the SQL
Select
statement when
usesDistinct
is set to
YES
.

!_Note_
EOFetchSpecification's default is
setUsesDistinct(NO)
, which omits the

DISTINCT
keyword in the SQL
Select
statement and therefore allows duplicates.!

The simplest way to fetch with no duplicate records is to explicitly create the EOFetchSpecification.

As an example, assume you want to fetch all of the movies from the Movies example database whose titles begin with "S" having one or more talents whose last names begin with "F".

####  Creating a fetch specification using DISTINCT (Java)

```

public NSArray movies;
public WOComponent fetch() {
    EOEditingContext ec=session().defaultEditingContext();
    EOQualifier qual=EOQualifier.qualifierWithQualifierFormat
        ("title like 'S*' AND roles.talent.lastName like 'F*'", null);
    EOFetchSpecification fs=new EOFetchSpecification("Movie", qual, null);
    fs.setUsesDistinct(true);
    movies=ec.objectsWithFetchSpecification(fs);
    return null;
}
```

####  Creating a fetch specification using DISTINCT (Objective-C)

```objc

NSArray *movies=nil;
- (WOComponent  *) fetch {
    EOEditingContext *ec=[[self session] defaultEditingContext];
    EOQualifier *qual=[EOQualifier qualifierWithQualifierFormat:
        @"title like 'S*' AND roles.talent.lastName like 'F*'"];
    EOFetchSpecification *fs=[EOFetchSpecification
        fetchSpecificationWithEntityName: @"Movie"
        qualifier: qual sortOrderings: nil];
    [fs setUsesDistinct: YES];
    movies =[ec objectsWithFetchSpecification: fs];
    return nil;
}
```

####  SQL log

```

[<ODBCChannel: 0xa416a0> evaluateExpression: <ODBCSQLExpression: "SELECT DISTINCT  t0.`CATEGORY`, t0.`DATE_RELEASED`, t0.`LANGUAGE`, t0.`MOVIE_ID`, t0.`POSTER_NAME`, t0.`REVENUE`, t0.`STUDIO_ID`, t0.`TITLE`, t0.`TRAILER_NAME` FROM `TALENT` t2 , `MOVIE_ROLE` t1 , `MOVIE` t0  WHERE (t0.`TITLE` like ? AND t2.`LAST_NAME` like ?) AND t1.`TALENT_ID` = t2.`TALENT_ID` and t0.`MOVIE_ID` = t1.`MOVIE_ID`" withBindings:(1:S%(title), 2:F%(lastName))>]
```


###  Using DISTINCT with Large Data Types

Many databases do not allow the
DISTINCT
keyword on fetches that contain columns of large data types. These data types include
BLOB,

LONG RAW
,
LONG
, and
MEMO
columns.

One technique to solve this problem is to split up the large data type columns into another table, and set up a to-one relationship from the master row to the row containing the large data types. This allows you to fetch using
DISTINCT
on all the columns except the large data type column. Once you have the desired master records, you can walk the to-one relationship and get the extra large data. This technique may also save time--very large data is not retrieved until it's needed.

##  See Also

- 

  [Creating Fetch Specifications Programmatically](Creating%20Fetch%20Specifications%20Programmatically.md#apple-gm4tsmjz)
- 

  [Fetching with an Editing Context](Fetching%20with%20an%20Editing%20Context.md#apple-ge2tsmzt)
- 

  [Working with Unnormalized Tables](Working%20with%20Unnormalized%20Tables.md#apple-ge4tonrq)

##  Questions

- 

  How can I eliminate duplicate records from my fetch?
- 

  How can I fetch from the database?
- 

  What is the EOF equivalent of the SQL
  DISTINCT
  keyword?
- 

  How do I fetch distinct records with entities that contain the
  BLOB
  data type?
- 

  How do I fetch distinct records using an EOFetchSpecification that I did not create?

##  Keywords

- 

  DISTINCT
- 

  SQL
- 

  Duplicate
- 

  Fetch
- 

  Specification

##  Revision History

20 July, 1998. David Scheck. First Draft.

19 November, 1998. Clif Liu. Second Draft.

```

```

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.1e.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.20.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
