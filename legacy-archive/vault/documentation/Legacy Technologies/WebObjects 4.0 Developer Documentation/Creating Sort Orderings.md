---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/EOSortOrdering.html
archived_at: '2026-07-15T08:01:09.213835Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Creating Sort Orderings

##  Synopsis

Describes how to create EOSortOrderings used either to specify fetch order or to sort an array in memory.

##  Discussion

An array of EOSortOrderings is used within EOF to specify the sort order for a fetch, as well as to specify a sort order to sort an array of Enterprise Objects already in memory. An EOSortOrdering consists of a key (for example, "lastName") and a sort direction (for example, _caseInsensitiveAscending_
). For database fetches, the key can be either an attribute of the object, or an attribute
path such as _studio.name_
. When sorting an array in memory, the key can be any key that the object can respond to via _valueForKey_
or _valueForKeyPath_
. This allows you to sort on values returned from methods of the object. For example, you can sort on a derived attribute like fullName, even though it is a method.

Creating an array of EOSortOrdering objects defines a complete sort specification. Since a sort ordering is completely generic, it can be used with EOFetchSpecifications and in-memory filters.

####  Sorting During Fetches

An EOFetchSpecification object can be given an array of EOSortOrderings to be applied during the fetch. It is the database adaptor's responsibility to use the array of sort orderings and return rows in the specified sorted order. The standard relational database adaptors included with EOF convert the array of EOSortOrdering objects into a SQL _ORDER BY_
clause.

The following example fetches all movies that have a title starting with S, and requests the database to sort them first by the category (case-insensitive ascending) and then by the title (case-insensitive descending).

#####  Figure 1. Java Code

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
         ("title like 'S*'", null);
```



```
    Object orderings[]={
```



```
        EOSortOrdering.sortOrderingWithKey("category",
```



```
            EOSortOrdering.CompareCaseInsensitiveAscending),
```



```
        EOSortOrdering.sortOrderingWithKey("title",
```



```
            EOSortOrdering.CompareCaseInsensitiveDescending)};
```



```
    EOFetchSpecification fs=new EOFetchSpecification
```



```
        ("Movie", qual, new NSArray(orderings));
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


!Note
WebScript does not know about the names describing sort direction, since they are just #defines in EOSortOrdering.h. Since WebScript will convert a string object into an ObjC selector when necessary, uncomment the definitions for sort direction when using WebScript.!

#####  Figure 2. Objective-C & WebScript Code

```
- fetch {
```



```
    /* Uncomment these definitions for WebScript
```



```
    id EOCompareAscending=@"compareAscending:";
```



```
    id EOCompareDescending=@"compareDescending:";
```



```
    id EOCompareCaseInsensitiveAscending=@"compareCaseInsensitiveAscending:";
```



```
    id EOCompareCaseInsensitiveDescending=
```



```
        @"compareCaseInsensitiveDescending:";
```



```
    */
```



```
    EOEditingContext *ec=[[self session] defaultEditingContext];
```



```
    EOQualifier *qual=[EOQualifier qualifierWithQualifierFormat:
```



```
        @"title like 'S*'"];
```



```
    NSArray *orderings=[NSArray arrayWithObjects:
```



```
        [EOSortOrdering sortOrderingWithKey:@"category"
```



```
             selector: EOCompareCaseInsensitiveAscending],
```



```
        [EOSortOrdering sortOrderingWithKey:@"title"
```



```
             selector: EOCompareCaseInsensitiveDescending], nil];
```



```
    EOFetchSpecification *fs=[EOFetchSpecification
```



```
        fetchSpecificationWithEntityName: @"Movie"
```



```
        qualifier: qual sortOrderings: orderings];
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
[<ODBCChannel: 0xae0f70> evaluateExpression: <ODBCSQLExpres
sion: "SELECT  t0.`CATEGORY`, t0.`DATE_RELEASED`, t0.`LANGU
AGE`, t0.`MOVIE_ID`, t0.`POSTER_NAME`, t0.`REVENUE`, t0.`ST
UDIO_ID`, t0.`TITLE`, t0.`TRAILER_NAME` FROM `MOVIE` t0  WH
ERE t0.`TITLE` like ? ORDER BY UCASE(t0.`CATEGORY`) asc, UC
ASE(t0.`TITLE`) desc" withBindings:(1:S%(title))>]
```

####  Sorting Arrays in Memory

An NSArray or NSMutableArray can use an array of EOSortOrderings to perform an in-memory sort of the contents of the array. Remember that when sorting an array in-memory, the sort ordering key can be any key that the object can respond to via valueForKey or valueForKeyPath. This allows you to even sort on values returned from methods on the object. For example, you can sort on a calculated fullName, even though it is only a method and not an attribute.

The following creates a new sorted array from a given original unsorted array. It then resorts a different mutable array within itself using the same sortOrderings. The sort will be first by the category (case-insensitive ascending) and then by the title (case-insensitive descending).

#####  Figure 4. Java Code

```
Object orderings[]={
```



```
    EOSortOrdering.sortOrderingWithKey("category",
```



```
        EOSortOrdering.CompareCaseInsensitiveAscending),
```



```
    EOSortOrdering.sortOrderingWithKey("title",
```



```
        EOSortOrdering.CompareCaseInsensitiveDescending)};
```



```

```



```
// This returns a new array in sorted order.
```



```
NSArray newSortedArray=sortedArrayUsingKeyOrderArray
```



```
    (originalArray, new NSArray(orderings));
```



```

```



```
// This resorts the mutableArray itself.
```



```
sortArrayUsingKeyOrderArray
```



```
    (originalMutableArray, new NSArray(orderings));
```



```

```


!Note
WebScript does not know about the names describing sort direction, since they are just #defines in EOSortOrdering.h. Since WebScript will convert a string object into an ObjC selector whenever needed, uncomment the definitions for sort direction when in WebScript.!

#####  Figure 5. Objective-C Code

```
/* Uncomment these definitions for WebScript
```



```
id EOCompareAscending=@"compareAscending:";
```



```
id EOCompareDescending=@"compareDescending:";
```



```
id EOCompareCaseInsensitiveAscending=@"compareCaseInsensitiveAscending:";
```



```
id EOCompareCaseInsensitiveDescending=@"compareCaseInsensitiveDescending:";
```



```
*/
```



```

```



```
NSArray *orderings=[NSArray arrayWithObjects:
```



```
    [EOSortOrdering sortOrderingWithKey:@"category"
```



```
        selector: EOCompareCaseInsensitiveAscending],
```



```
    [EOSortOrdering sortOrderingWithKey:@"title"
```



```
        selector: EOCompareCaseInsensitiveDescending], nil];
```



```

```



```
// This returns a new array in sorted order.
```



```
NSArray *newSortedArray=[originalArray
```



```
    sortedArrayUsingKeyOrderArray: orderings];
```



```

```



```
// This resorts the mutableArray itself.
```



```
[originalMutableArray  sortUsingKeyOrderArray: orderings];
```


##  See Also

· Fetching Distinct Results

· Fetching with an Editing Context

· EOSortOrdering

· EOFetchSpecification

· EOEditingContext

##  Questions

· How do I fetch records in sorted order?

· What is the EOF equivalent of the SQL _ORDER BY_
clause?

· How do I sort an array in memory?

· How do I get case-insensitive sort to work with MSAccess?

##  Keywords

· Sort

· ORDER BY

· EOSortOrdering

· UPPER

· UCASE

##  Revision History

21 July, 1998. David Scheck. First Draft.
19 November 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
