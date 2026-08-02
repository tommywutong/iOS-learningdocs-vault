---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/StoredProcs2.html
archived_at: '2026-07-18T01:18:54.220444Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Adding%20Stored%20Procedures.md) [!Previous Section](Adding%20Stored%20Procedures.md)

# Assigning a Stored Procedure to an Entity

You can assign stored procedures to entities to be used to perform the following operations:

- Insert a new object.
- Delete an object.
- Fetch all the objects for an entity.
- Fetch an object by its primary key.
- Generate a primary key value for a new object.

If you associate a stored procedure with an entity's operation, the Framework invokes it automatically when the operation occurs. For example, if you want to use a stored procedure to insert new Customer objects:

- Define the stored procedure in the database.
- Define the stored procedure in the model as described in the previous section.
- Associate the stored procedure with the Customer entity's insert operation.

You can associate a stored procedure with an entity using EOModeler or you can do it programmatically (see the chapter "Answers to Common Design Questions" in the book _Enterprise Objects Framework Developer's Guide_).
To assign a stored procedure to an entity in EOModeler:

- Select the entity with which you want to associate a stored procedure.
- Open the inspector.
- Click the Stored Procedures Inspector icon.

!

- Type the name of the stored procedure in the field associated with the appropriate database operation.

!

Figure 39. The Stored Procedure Inspector

### Requirements for Framework-Invoked Stored Procedures

When Enterprise Objects Framework invokes a stored procedure for an operation, the procedure must behave in an expected way. The Framework specifies what a stored procedure's arguments, results, and return values should be. For more information on these requirements, see the chapter "Answers to Common Design Questions" in the book _Enterprise Objects Framework Developer's Guide_.
[!Table of Contents](Adding%20Stored%20Procedures.md) [!Next Section](Working%20with%20Fetch%20Specifications.md)
