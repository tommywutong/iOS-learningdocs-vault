---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/StoredProcs1.html
archived_at: '2026-07-15T08:04:31.728841Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

!Table of Contents [!Previous Section](Working%20with%20Stored%20Procedures.md)

# Adding Stored Procedures

If your stored procedure is defined in the database at the time you create your model, you don't have to do anything to define it in your model. When you create a new model with EOModeler, the application reads stored procedure definitions from the database's data dictionary and stores them in the model's __.eomodeld__ file. You can also add a stored procedure definition to an existing model.
To add a stored procedure:

- Select the Stored Procedures icon in the tree view.
- Choose Property ! Add Stored Procedure.
- Specify a name and external name for the stored procedure.

!

Figure 38. Adding a Stored Procedure

You must also define an _argument_ for a stored procedure's return value and for each of its parameters. Add arguments to a stored procedure the same way you add attributes to an entity. In fact, the arguments of a stored procedure are represented with EOAttribute objects.
__Note:__  The Advanced Attribute Inspector isn't applicable to stored procedure arguments. As a result, you can't access it while editing a stored procedure argument.
To define and display the attributes of a stored procedure:

- Select the stored procedure in the tree view.

Alternatively, you can double-click the __!__ icon to the left of a stored procedure in the Model Editor's stored procedure table.

- Choose Property ! Add Argument.
- Specify the argument's characteristics in the Model Editor's table.

Minimally, you must provide values for the Name, Column, Direction, External Type, and Value Class characteristics.

Each table column corresponds to a single characteristic of a stored procedure argument. By default, the columns included in the table only represent a subset of the possible characteristics you can set for a given entity. To add columns for additional characteristics, use the Add Column menu in the lower left corner of the table.
The following table describes the characteristics you can set for a stored procedure argument.

|  Characteristic |  What it is |
|  Allows Null |  Indicates whether the argument's value can be NULL. |
|  Column |  The name of a parameter as it is defined in the database (doesn't apply to a "returnValue" argument). |
|  Direction |  In, InOut, Out, or Void. Don't choose Void; it's reserved for future use. |
|  External Type |  The data type of the argument as it's defined in the database. |
|  Name |  The name your application uses for the argument. |
|  Precision |  The number of significant digits (applies to number data only). |
|  Scale |  The number of digits to the right of the decimal point (applies to number data only). |
|  Value Class (Java) |  The Java type to which the argument value will be coerced in your application. |
|  Value Class (Obj-C) |  The Objective-C type to which the argument value will be coerced in your application. |
|  Value Type |  The format type for NSNumber classes such as "i" or "d". |
|  Width |  The maximum width (applies to string, raw, and binary data). |

```
```


For example, to add arguments for the Sybase stored procedure defined as:

```
create proc movie_by_date (@begin datetime, @end
datetime) as
begin
    select
        CATEGORY, DATE_RELEASED, LANGUAGE, MOVIE_ID, RATING,
        REVENUE, STUDIO_ID, TITLE
    from MOVIES
    where DATE_RELEASED > @begin and DATE_RELEASED < @end
end
```


you would add an argument for __@begin__ and __@end__ with column names "begin" and "end", respectively.
Tip: If you're using Oracle, you can define a stored procedure to represent a function. Add an argument named "returnValue" and use the EOAdaptorChannel method __returnValuesForLastStoredProcedureInvocation__ to get the function's result.
If the Framework invokes your stored procedure automatically, the argument names of a stored procedure must match the name of a corresponding EOAttribute object. For example, if you want to invoke a stored procedure whenever the Framework fetches a Movie object by its primary key, the stored procedure's argument names must correspond to the primary key attributes of the Movie entity. The following section discusses this requirement more thoroughly.

!Table of Contents [!Next Section](Assigning%20a%20Stored%20Procedure%20to%20an%20Entity.md)
