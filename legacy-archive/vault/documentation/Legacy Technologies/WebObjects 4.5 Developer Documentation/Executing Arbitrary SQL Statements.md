---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.32.html
archived_at: '2026-07-15T08:09:59.481816Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Creating%20Adaptor%20Sublayer%20Objects%20and%20Connecting%20Them%20to%20the%20Server.md) [!](Accessing%20Schema%20Information%20from%20the%20Database%20Server.md)

#   Executing Arbitrary SQL Statements

##  Synopsis

Describes how to execute arbitrary SQL statements, including statements with
GROUP BY
and
HAVING
.

##  Description

Enterprise Objects Framework (EOF) allows you to send arbitrary SQL statements using the adaptor sublayer. This topic presents two methods for sending arbitrary SQL: sending it with the EOAdaptorChannel or using the EOUtilities abstract class convenience API. EOUtilities is a category on EOEditingContext in Objective-C.

###   Executing Arbitrary SQL Using the Adaptor Sublayer

The EOAdaptorChannel
evaluateExpression
method is used to send the SQL to the database server. Thus, you need access or create an adaptor channel. See the programming topics [Accessing Adaptor Sublayer Objects](Accessing%20Adaptor%20Sublayer%20Objects.md#apple-gi3tanbu)
, [Creating Adaptor Sublayer Objects and Connecting Them to the Server](Creating%20Adaptor%20Sublayer%20Objects%20and%20Connecting%20Them%20to%20the%20Server.md#apple-ge3tknrv)
, and [Accessing Schema Information from the Database Server](Accessing%20Schema%20Information%20from%20the%20Database%20Server.md#apple-gi2denrx)
for more information about getting the adaptor channel.

The sample Java code below shows how to use the
evaluateExpression
method for a SQL statement that returns rows. If the statement doesn't return rows, omit the
do...while
loop.

```

EOAdaptorChannel myChannel; // assume this exists
String sqlString;           // assume exists
NSDictionary row;

EOSQLExpression expression = EOSQLExpression.expressionForString(sqlString);

myChannel.openChannel();
try {
    myChannel.evaluateExpression(expression);
    do {
        myChannel.setAttributesToFetch(myChannel.describeResults());
        while ((row = myChannel.fetchRow()) != null) {
            // Process the row
        }
    } while (myChannel.isFetchInProgress()); // Process next result set
} catch (Exception exception) {
    // Handle the exception
}
```


The code first converts the SQL string to an EOSQLExpression object needed by the
evaluateExpression
method. Note that the SQL expression must be valid on the database server. EOF performs no substitution or formatting on the SQL expression.

The code invokes
openChannel
method to establish a connection to the database. You must open the adaptor channel before you perform any database operations with it. The
evaluateExpression
invocation sends the SQL expression to the server. The outer
do
loop iterates over result sets (what?). In order to form raw row dictionaries, the channel sets the attributes that it will fetch using the
setAttributesToFetch
method. The
describeResults
method determines these attributes from the
evaluteExpression
results. the inner
while
loop iterates over the raw rows returned from the database server.

Each row returned is an NSDictionary whose keys are Strings (NSStrings in Objective-C) containing adaptor-dependent attribute names. For example, in Oracle, the keys are generated sequentially starting with "Attribute0" corresponding to the first value that is returned in your SQL
SELECT
statement, "Attribute1" corresponding to the second, and so on. The types of the values depend on the corresponding database types and the adaptor's default type mapping. For example, VARCHAR types are mapped to Strings (NSStrings in Objective-C). For more information about type mapping, see the documentation about the specific adaptor you are using.

###  Executing Arbitrary SQL Using EOUtilities

EOUtilities allows you to execute raw SQL when you are working with the control layer. To use EOUtilities, you need to have an EOEditingContext and an EOModel. The following code uses EOUtilities to send raw SQL to the database server.

```

String sqlString; // Assume exists
String modelName; // Assume exists
NSArray results;
try {
    results = EOUtilities.rawRowsForSQL
        (this.session().defaultEditingContext(),sqlString,modelName);
} catch (Exception exception) {
    // Handle exception
}
return results;
```


The results array is an array of NSDictionary objects. Each NSDictionary has the same form as the raw row when you fetch using the EOAdaptorChannel. See [Executing Arbitrary SQL Using the Adaptor Sublayer](#apple-geydoojs)
above.

###  SQL Topics

The following are some SQL statements that are useful to send directly to the database server:

GROUP BY
allows the user to group several rows sharing a particular pattern and compute some statistics on the aggregate (such as the total number of rows, the average, or the variance). For example, the following statement selects the number of movies produced by a given studio:

```

Select count(*), t1.name from movie t0, studio t1 where t0.studio_id=t1.studio_id GROUP BY t1.name
```


You can also compute the average and variance of a particular column. The following returns the list of the averages of revenue for each studio_id:

```

Select avg(revenue), studio_id from movie GROUP BY studio_id
```


HAVING
allows you to select rows based on the result of an aggregate function such as
count
or
avg
. This example selects only the number of movies from studios that have produced more than three movies.

```

Select count(*), t1.name from movie t0, studio t1 where t0.studio_id=t1.studio_id GROUP BY t1.name HAVING count(*)>=3
```


Oracle has a feature called sequences. Suppose movie_seq is a name of a sequence. To get the value of a sequence, you send the following statement:

```

Select movie_seq.nextval from dual
```

##  See Also

- 

  [Fetching with an Editing Context](Fetching%20with%20an%20Editing%20Context.md#apple-ge2tsmzt)
- 

  [Inserting with the Adaptor Sublayer](Inserting%20with%20the%20Adaptor%20Sublayer.md#apple-gm3dgnbu)
- 

  [Updating with the Adaptor Sublayer](Updating%20with%20the%20Adaptor%20Sublayer.md#apple-geydcnju)
- 

  [Deleting with the Adaptor Sublayer](Deleting%20with%20the%20Adaptor%20Sublayer.md#apple-gi2donjr)
- 

  [Accessing Adaptor Sublayer Objects](Accessing%20Adaptor%20Sublayer%20Objects.md#apple-gi3tanbu)
- 

  [Creating Adaptor Sublayer Objects and Connecting Them to the Server](Creating%20Adaptor%20Sublayer%20Objects%20and%20Connecting%20Them%20to%20the%20Server.md#apple-ge3tknrv)
- 

  [Accessing Schema Information from the Database Server](Accessing%20Schema%20Information%20from%20the%20Database%20Server.md#apple-gi2denrx)
- 

  EOAdaptor class specification in the _Enterprise Objects Framework Reference_

##  Questions

- 

  How do I compute statistics on my data?
- 

  How do I use
  GROUP BY
  statement?
- 

  How do I use the
  HAVING
  statement?
- 

  How do I fetch a sequence value?
- 

  How do I execute raw SQL statements using EOF?

##  Keywords

- 

  SQL
- 

  Grouping

##  Revision History

21 July, 1998. Jean-Luc Marsolier. First Draft.
12 November, 1998. Clif Liu. Second Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Creating%20Adaptor%20Sublayer%20Objects%20and%20Connecting%20Them%20to%20the%20Server.md) [!](Accessing%20Schema%20Information%20from%20the%20Database%20Server.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
