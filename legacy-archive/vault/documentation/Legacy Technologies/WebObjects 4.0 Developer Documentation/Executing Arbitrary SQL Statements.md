---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/RawSQL.html
archived_at: '2026-07-15T08:01:27.830358Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Executing Arbitrary SQL Statements

##  Synopsis

Describes how to execute arbitrary SQL statements, including statements with _GROUP BY_
and _HAVING_
.

##  Description

Enterprise Objects Framework (EOF) allows you to send arbitrary SQL statements using the EOUtilities category on EOEditingContext in Objective C. EOUtilities is an abstract class in Java.

####  Executing Arbitrary SQL Using EOUtilities

To execute the SQL, use the code listed below and make sure that the objects are cached in memory by

· checking the Cache in Memory option in the Advanced Entity Inspector for the entity using EOModeler.

· setting it programmatically using the EOEntity method setCachesObjects.

#####  Figure 1. Objective-C Code

```objc
- (NSArray *)evaluateSQLString:(NSString *)sqlString
```



```
    withModel:(NSString *)modelName
```



```
{
```



```
    NSArray *results;
```



```
    NS_DURING
```



```
        results = [[[self session] defaultEditingContext]
```



```
             rawRowsWithSQL:sqlString modelNamed:modelName];
```



```
    NS_HANDLER
```



```
        results = nil;
```



```
        NSLog(@"Exception: %@", localException);
```



```
    NS_ENDHANDLER
```



```
    return results;
```



```
}
```


·

The result is returned as an array of rows. The rows are NSDictionaries whose keys are NSStrings and whose values correspond to the values returned in the SQL statement. The keys are database dependent. In Oracle, the keys are generated sequentially starting with "Attribute0_"_
corresponding to the first value that is returned in your SQL _SELECT_
statement, "Attribute1" corresponding to the second, and so on. The types of the values are defined in the model using EOModeler.

####  SQL Topics

The following are some SQL statements that are useful to send directly to the database server:

_GROUP BY_
allows the user to group several rows sharing a particular pattern and compute some statistics on the aggregate (such as the total number of rows, the average, or the variance). For example, the following statement selects the number of movies produced by a given studio:

```
Select count(*), t1.name from movie t0, studio t1 where t0.studio_id=t1.studio_id GROUP BY t1.name
```


You can also compute the average and variance of a particular column. The following returns the list of the averages of revenue for each studio_id:

```
Select avg(revenue), studio_id from movie GROUP BY studio_id
```


_HAVING_
allows you to select rows based on the result of an aggregate function such as _count_
or _avg_
. This example selects only the number of movies from studios that have produced more than three movies.

```
Select count(*), t1.name from movie t0, studio t1 where t0.studio_id=t1.studio_id GROUP BY t1.name HAVING count(*)>=3
```


Oracle has a feature called sequences. Suppose movie_seq is a name of a sequence. To get the value of a sequence, you send the following statement:

```
Select movie_seq.nextval from dual
```


##  See Also

· When to Choose the Adaptor Level to Improve Performance

· Fetching with an Editing Context

· Updating with the Adaptor Level

· Inserting with the Adaptor Level

· Deleting with the Adaptor Level

· EOAdaptor

##  Questions

· How do I compute statistics on my data?

· How do I use _GROUP BY_
statement?

· How do I use the _HAVING_
statement?

· How do I fetch a sequence value?

· How do I execute raw SQL statements using EOF?

##  Keywords

· SQL statements

· Grouping

##  Revision History

21 July, 1998. Jean-Luc Marsolier. First Draft.
12 November, 1998. Clif Liu. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
