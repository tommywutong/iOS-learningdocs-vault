---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/Attributes1.html
archived_at: '2026-07-15T08:03:30.707214Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Working%20with%20Attributes.md) [!Previous Section](Working%20with%20Attributes.md)

# Changing an Attribute's Characteristics

EOModeler provides three mechanisms for viewing and modifying an entity's attributes: the table mode of the Model Editor, the diagram view of the Model Editor, and the Attribute Inspector. You can use any of the mechanisms to examine the characteristics of your model's attributes and to make refinements. Each has advantages over the others and is useful in different circumstances.

- The Model Editor in table mode is most convenient for most attribute editing, because you have access to all of but a few of the possible attribute characteristics.
- Use the diagram view of the Model Editor for very limited attribute editing when you're already using the diagram view. Because you can modify only a few of an attribute's characteristics in diagram view, you have to switch to another mechanism for many tasks.
- Use the Attribute Inspector for editing attribute characteristics that you can't access in the Model Editor's table mode. Additionally, some attribute characteristics are easier to set in the inspector.

The following sections provide more detail on what attribute characteristics you can set with each mechanism.

## Using Table Mode

To display an entity's attributes in table mode, select the entity in the tree view.

!

Figure 19. Displaying an Entity's Attributes

Each table column corresponds to a single characteristic of the attribute, such as its name or its external type (that is, the type by which it's represented in the database). By default, the columns included in this view only represent a subset of the possible characteristics you can set for a given attribute. To add columns for additional characteristics, you use the Add Column menu in the lower left corner of the table.
The following table describes the characteristics you can set for an attribute. Unless otherwise specified, the instructions are for editing the characteristic in the Model Editor's table mode.

|  Characteristic |  What it is |  How you modify it |
|  Allows Null |  Indicates whether the attribute can have a NULL value. |  Click in the column to toggle the check on and off. (The column for Allows Null is labeled "A".) |
|  Class Property |  Indicates a property that meets both of these criteria: you want to include it in your class definition, and it can be fetched from the database. |  Click in the  column to toggle class property off and on.  You can also edit this characteristic in diagram view. |
|  Client-Side Class Property |  Declares whether a property is a class property in the entity's client-side class. Only applicable for Java Client applications. |  Click in the  column to toggle locking off and on. |
|  Column |  The database name of the column that corresponds to the attribute. |  Edit the table cell. |
|  Definition |  The definition for a derived attribute. Note that Column and Definition are mutually exclusive; you can't set both. Setting one clears the other. |  Edit the table cell. |
|  External Type |  The data type of the attribute as it's understood by the database. |  Choose a value from the pull-down list |
|  Locking |  Indicates whether an attribute should be used for locking when an update is performed. |  Click in the  column (shown in [Figure 19](#apple-geydaoa)) to toggle locking off and on.  You can also edit this characteristic in diagram view. |
|  Name |  The name your application uses for the attribute. EOModeler supplies default names derived from the name of the corresponding column in the database. You can edit these names if desired. |  Edit the table cell.  You can also edit this characteristic in diagram view. |
|  Precision |  The number of significant digits. |  Edit the table cell.  Or use the Attribute Inspector as described in [Using the Attribute Inspector](#apple-guydmmy). |
|  Primary Key |  Declares whether a property is, or is part of, the primary key for the entity. |  Click in the  column to toggle the primary key off and on.  You can also edit this characteristic in diagram view. |
|  Prototype |  A prototype attribute from which this attribute derives its characteristics. |  Choose a value from the pull-down list |
|  Read Format |  The format string that's used to format the attribute's value for SELECT statements. In the string, %P is replaced by the attribute's external name. This string is used whenever the attribute is referenced in a select list or qualifier. |  Edit the table cell. |
|  Read Only |  Indicates whether the attribute is read only. |  Use the Advanced Attribute Inspector. You can't set this characteristic in the Model Editor. |
|  Scale |  The number of digits to the right of the decimal point. Can be negative. |  Edit the table cell.  Or use the Attribute Inspector as described in [Using the Attribute Inspector](#apple-guydmmy). |
|  Value Class (Java) |  If your enterprise object is a Java class, the Java type to which the attribute will be coerced in your application. |  Edit the table cell.  Or use the Attribute Inspector as described in [Using the Attribute Inspector](#apple-guydmmy). |
|  Value Class (Obj-C) |  If your enterprise object is an Objective-C class, the Objective-C type to which the attribute will be coerced in your application. |  Edit the table cell.  Or use the Attribute Inspector as described in [Using the Attribute Inspector](#apple-guydmmy). |
|  Value Type |  The conversion character (such as "i" or "d") for the data type a NSNumber attribute is converted to and from in your application. |  Edit the table cell.  Or use the Attribute Inspector as described in [Using the Attribute Inspector](#apple-guydmmy). |
|  Width |  The maximum width (applies to string and raw data only). |  Edit the table cell.  Or use the Attribute Inspector as described in [Using the Attribute Inspector](#apple-guydmmy). |
|  Write Format |  The format string that's used to format the attribute's value for INSERT or UPDATE expressions. In the string, %P is replaced by the attribute's external name. |  Edit the table cell. |

```
```


## Using the Attribute Inspector

The Attribute Inspector is most useful for setting characteristics of an attribute that are related to how the attribute is represented inside your application. These characteristics are:

- Precision
- Scale
- Value Class (Java)
- Value Class (Obj-C)
- Value Type
- Width

The Attribute Inspector is particularly useful for editing these characteristics because it manages the dependencies between them. For example, EOModeler supplies a default mapping between an attribute's external type and internal type, both for Java and Objective-C. If you change the Java value class, the Objective-C value class is automatically updated correspondingly, and vice versa. Also, some of the attribute characteristics are only applicable to attributes whose internal type is set to a particular value class. For example, Precision and Scale are only applicable to decimal number value classes-BigDecimal in Java and NSDecimalNumber in Objective-C.
The Attribute Inspector helps you keep track of these dependencies by changing its user interface to match whatever internal data type you choose (shown in [Figure 20](#apple-ge2dembz)).

!

Figure 20. Setting Internal Data Type Characteristics with he Attribute Inspector

To view an attribute in the Attribute Inspector, select the attribute in the Model Editor and open the inspector, either by clicking the ! button in the toolbar or by choosing Tools ! Inspector.

### Using Custom Data Types

Some attributes, such as TalentPhoto's __photo__ attribute, use custom value classes to represent them inside your application. When you use a custom data type, you are responsible for specifying how the data is read from and written to the database. You can use the Attribute Inspector to specify a custom data type. For a description of how to do this, see the chapter Advanced Enterprise Object Modeling in the book _Enterprise Objects Framework Developer's Guide_. See the class specification for EOAttribute in the _Enterprise Objects Framework Reference_ for more discussion of custom data types.

## Using the Advanced Attribute Inspector

The main reason you use the Advanced Attribute Inspector is to set an attribute's Read Only characteristic. By default, and attribute is read-write. You only need to set it if you want it to be read-only. To do this, you have to use the Advanced Attribute Inspector. Open the inspector panel, and select the Advanced Attribute Inspector as shown in [Figure 21](#apple-ge2denzt).

!

Figure 21. Displaying the Advanced Attribute Inspector

[!Table of Contents](Working%20with%20Attributes.md) [!Next Section](Prototype%20Attributes.md)
