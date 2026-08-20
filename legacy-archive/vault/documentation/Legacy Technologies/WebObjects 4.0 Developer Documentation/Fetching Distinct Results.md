---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/distinct.html
archived_at: '2026-07-15T08:01:38.392397Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Fetching Distinct Results

##  Synopsis

Describes how to use the EOFetchSpecification _setUsesDistinct_
method to omit duplicate records during a fetch.

##  Discussion

Duplicate records sometimes appear in database fetches, usually when the fetch involves joining multiple tables to satisfy the fetch qualifier. The EOFetchSpecification allows you to specify whether you want these duplicate records with the _setUsesDistinct_
method.The EOF adaptor modifies its query based on this setting. The standard relational database adaptors add the SQL keyword _DISTINCT_
to the SQL _Select_
statement when _usesDistinct_
is set to YES.

!EOFetchSpecification's default is _setUsesDistinct(NO)_
, meaning `don't use the
DISTINCT keyword' and, therefore, allow duplicates.!

The simplest way to fetch with no duplicate records is to explicitly create the EOFetchSpecification.

As an example, assume you want to fetch all of the movies from the Movies example database whose titles begin with "S" having one or more talents whose lastNames begin with "F").

#####  Figure 1. Java Code

```
public NSArray movies;
```



```
public WOComponent fetch() {
```



```
    EOEditingContext ec=session().defaultEditingContext();
```



```
    EOQualifier qual=EOQualifier.qualifierWithQualifierFormat
```



```
        ("title like 'S*' AND roles.talent.lastName like 'F*'", null);
```



```
    EOFetchSpecification fs=new EOFetchSpecification("Movie", qual, null);
```



```
    fs.setUsesDistinct(true);
```



```
    movies=ec.objectsWithFetchSpecification(fs);
```



```
    return null;
```



```
}
```


#####  Figure 2. Objective-C Code

```
NSArray *movies=nil;
```



```objc
- (WOComponent  *) fetch {
```



```
    EOEditingContext *ec=[[self session] defaultEditingContext];
```



```
    EOQualifier *qual=[EOQualifier qualifierWithQualifierFormat:
```



```
        @"title like 'S*' AND roles.talent.lastName like 'F*'"];
```



```
    EOFetchSpecification *fs=[EOFetchSpecification
```



```
        fetchSpecificationWithEntityName: @"Movie"
```



```
        qualifier: qual sortOrderings: nil];
```



```
    [fs setUsesDistinct: YES];
```



```
    movies =[ec objectsWithFetchSpecification: fs];
```



```
    return nil;
```



```
}
```


#####  Figure 3. SQL Log

```
[<ODBCChannel: 0xa416a0> evaluateExpression: <ODBCSQLExpres
sion: "SELECT DISTINCT  t0.`CATEGORY`, t0.`DATE_RELEASED`,
t0.`LANGUAGE`, t0.`MOVIE_ID`, t0.`POSTER_NAME`, t0.`REVENUE
`, t0.`STUDIO_ID`, t0.`TITLE`, t0.`TRAILER_NAME` FROM `TALE
NT` t2 , `MOVIE_ROLE` t1 , `MOVIE` t0  WHERE (t0.`TITLE` li
ke ? AND t2.`LAST_NAME` like ?) AND t1.`TALENT_ID` = t2.`TA
LENT_ID` and t0.`MOVIE_ID` = t1.`MOVIE_ID`" withBindings:(1
:S%(title), 2:F%(lastName))>]
```


####  Using DISTINCT with Large Data Types

Many databases do not allow the _DISTINCT_
keyword on fetches that contain columns of large data types. These data types include _BLOB,_
_LONG RAW_
, _LONG_
, and _MEMO_
columns.

One technique to solve this problem is to split up the large data type columns into another table, and set up a to-one relationship from the master row to the row containing the large data types. This allows you to fetch using _DISTINCT_
on all the columns except the large data type column. Once you have the desired master records, you can walk the to-one relationship and get the extra large data. This technique may also save time-very large data is not retrieved until it's needed.

##  See Also

· EOFetchSpecification

· Working with Unnormalized Tables

· Fetching with an Editing Context

##  Questions

· How can I eliminate duplicate records from my fetch?

· How can I fetch from the database?

· What is the EOF equivalent of the SQL _DISTINCT_
keyword?

· How do I fetch distinct records with entities that contain _BLOB_
s?

· How do I fetch distinct records using an EOFetchSpecification that I did not create?

##  Keywords

· _DISTINCT_

· SQL

· _DUPLICATE RECORDS_

· _usesDistinct_

· _SetUsesDistinct_

· Fetch

· Fetch Specification

##  Revision History

20 July, 1998. David Scheck. First Draft.

19 November, 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
