---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/Entities2.html
archived_at: '2026-07-15T08:03:57.128687Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Changing%20an%20Entity%27s%20Characteristics.md) [!Previous Section](Changing%20an%20Entity%27s%20Characteristics.md)

# Using the Entity Inspector

You use the Entity Inspector to set an entity's characteristics and specify a mapping between the entity and an enterprise object class. You can also accomplish the same tasks using the table mode of the Model Editor, but this section focuses on the Entity Inspector.
To inspect an entity, select the entity in the Model Editor and open the inspector (either with the ! button on the tool bar or by choosing Tools ! Inspector).
[Figure 35](#apple-geytgnq) shows the Entity Inspector for the Movie entity.

!

Figure 35. The Entity Inspector

Name and Table Name
The Name field lists the name your application uses for the entity. The Table Name field contains the name of the root table in the database. You can change the internal name (that is, the name as it appears in the application), but you shouldn't change the database table name unless you have also changed the name in your database server.
Class
The Class field initially contains the text "EOGenericRecord". This is because the default enterprise object class is an EOGenericRecord. To specify a custom class, type the name of the class in this field. For more information on creating custom classes, see[Specifying an Enterprise Object Class](Specifying%20an%20Enterprise%20Object%20Class.md#apple-geytkna).

Properties
The Properties area lets you specify the properties you want to include in your enterprise object class and set characteristics for them.
There are three columns in this area. Each column displays the status of a particular setting: Primary Key, Used For Locking, and Class Property. Icons are used to indicate that a setting is enabled for a particular property; the dash icon indicates that a setting is not applicable to a property. You add and delete icons by clicking the appropriate column next to the property.
!The Primary Key column is used to declare whether a property is, or is part of, the primary key for the enterprise object class. To specify a compound primary key, you simply add a Primary Key icon to the column for each property you want to include in the primary key.
Specifying a primary key for your enterprise object class is mandatory; the primary key is the means by which an enterprise object is uniquely identified within your application and mapped to the appropriate database row.
__Note:__  Enterprise Objects Framework doesn't support modifiable primary key values. You shouldn't design your application so that users can change a primary key's value.
!The Class Property column is used to indicate properties that meet both of these criteria: You want to include them in your class definition, and they can be fetched from the database. By default, the Entity Inspector sets all of an entity's properties as belonging to your class. You can remove a property by clicking its Class Property icon. If you define an attribute that doesn't exist in the database but is used by your application (such as a computed value), you should remove its Class Property icon. Note that generated source files won't include instance variable declarations for these attributes-you'll have to type those in by hand (this is a rare case). You also should not include primary and foreign keys as class properties unless you need to display their values in the user interface. If you don't remove the Class Property icon for an attribute that has no corresponding database value, it will result in a server error when your application attempts to fetch the property from the database.
!The Used For Locking column indicates whether an attribute should be checked for changes before an update is allowed. This setting applies when you're using Enterprise Object Framework's default update strategy, optimistic locking. Under optimistic locking, the state of a row is saved as a _snapshot_ when you fetch it from the database. When you perform an update, the snapshot is checked against the row to make sure the row hasn't changed. If you set Used For Locking for an attribute whose data is a BLOB type, it can have an adverse effect on system performance. By default, the Entity Inspector sets all of an entity's attributes to be used for locking.
In [Figure 35](#apple-geytgni), note that:

- In the Inspector, the property __movieID__ has been designated as the enterprise object class's primary key.
- For the entity's relationships, the Inspector automatically displays the Not applicable icons in the Primary Key and Used For Locking columns.

[!Table of Contents](Changing%20an%20Entity%27s%20Characteristics.md) [!Next Section](Specifying%20an%20Enterprise%20Object%20Class.md)
