---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/ApA_ERMd3.html
archived_at: '2026-07-15T08:02:32.382311Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Entity-Relationship%20Modeling.md) [!Previous Section](Entities%20and%20Attributes.md)

# Relationships

Your employee database might have, in addition to the Employee entity, a JobTitle entity that identifies the various job titles that an employee can have and whether each title represents a salaried or an hourly position. A _relationship_ between the Employee entity and the JobTitle entity expresses the affinity between employees and titles, and allows you to access the title information for a given employee. Graphically, a relationship can be shown as a named arrow that points from one entity (the _source entity_) to another (the _destination entity_); the Employee-JobTitle relationship (which is named toJobTitle) is depicted in [Figure 57](#apple-gmytomy).

__Note:__  To support the toJobTitle relationship, the Employee entity has been altered-the titleID attribute has been added to it. This is explained in the section["Relationship Keys"](#apple-gqzdm).

The table that's represented by the source entity is referred to as the _source table_; the source table contains _source records_. Similarly, the table that's represented by the destination entity is referred to as the _destination table_; it contains _destination records_.
Be aware that you can't just randomly create relationships between your entities. Relationships that you add to your entities must reflect real relationships between the tables in the database. For more information, see the section["Relationship Keys"](#apple-gqzdm).

!

Figure 57. The toJobTitle Relationship

## Relationship Directionality

Relationships are _unidirectional_. In a unidirectional relationship, the path that leads from the source to the destination can't be traveled in the opposite direction-you can't use a relationship to go from the destination to the source. For example, although you can use the toJobTitle relationship to find the title for a particular employee, you can't use it to get a list of the employees that share a particular title.
Unidirectionality is enforced by the way a relationship is resolved. Specifically, the source record is a given. Resolving a relationship means finding the correct destination record (or records) given a specific source record.
Bidirectional relationships-in which you can look up records in either direction-can be created by adding a separate "return-trip" relationship. This is demonstrated in the section["Bidirectional Relationships"](#apple-gmzdonq).

## Naming Relationships

Most of the relationships described in this manual use a simple naming convention: relationships are named after the destination entity. For example, a Movie entity can have a studio relationship to a Studio entity, and a roles relationship to a MovieRoles entity. Note that singular names are typically used for to-one relationships, and plural names are used for to-many relationships. However, you're not bound by this convention-EOModeler lets you give relationships any names you like.
In the figures throughout this book, the entity that is adjacent to the relationship's label is said to _own_ the relationship. For example, in [Figure 57](#apple-gm4tamq) the Employee entity owns the toJobTitle relationship, as indicated by the proximity of the "toJobTitle" label to the entity.

### Relationships and the Data Dictionary

Unlike entities and attributes, relationships don't correspond to names in the server's data dictionary. In general, most servers don't define structural elements for relationships, so their data dictionaries don't contain names to which E-R relationships can correspond. But relationships aren't completely disassociated from the data dictionary: A relationship's definition, as explained in the next section, depends on the existence of particular entities and attributes (which, as described earlier, must correspond to data dictionary names).

## Relationship Keys

The construction of a relationship involves more than just two entities. You also have to designate at least one attribute from each entity as a _relationship key_. In the toJobTitle relationship, for instance, the Employee.titleID and JobTitle.titleID are so designated; this is indicated in [Figure 57](#apple-gm4tamq) as the two attributes that lie at either end of the relationship arrow. Just as the tables are called source and destination tables, so are the relationship keys named. In the source entity, the relationship key is called the _source key_. The destination entity's relationship key is called the _destination key_.

__Note:__  As in the case of the toJobTitle relationship, the source and destination keys often have the same name, although this isn't a requirement of model design.
The reason you need to designate relationship keys is so the relationship can be used to create cross-references between specific instances of the related entities (this is called "resolving" the relationship). For example, let's say you fetch an employee object. The Enterprise Objects Framework takes the value for the employee's titleID attribute and compares it to the value for titleID in each JobTitle instance. A match locates the desired job title record.
For this cross-referencing scheme to work, the source and destination keys must characterize the same data-you couldn't find an employee's job title by comparing, for example, Employee.empID to JobTitle.titleID. This is why the titleID attribute was added to the Employee entity.

### An Example with Data

To further illustrate how a relationship is resolved, consider the "EMPLOYEE" and "JOB_TITLE" tables presented in [Figure 58](#apple-gqydi) (for the purpose of this example, only the essential columns are shown).

Here we see that the value for the titleID attribute for James Winton is 1. Looking in the "JOB_TITLE" table, we see that 1 is the ID of the President. Thus, James Winton is the company president. Similarly, we can determine that Kai Veasey is a manager.

!

Figure 58. The "EMPLOYEE" and "JOB_TITLE" Tables

### Choosing Relationship Keys

Any attribute can be used as a relationship key, but some are better suited than others. In general, of the two relationship keys for a particular relationship, the destination key will be a primary key for its entity (or, otherwise, an attribute that characterizes unique data) and the source key is manufactured to emulate the destination key. In traditional E-R modeling, the emulating attribute is called a _foreign key_. The toJobTitle relationship demonstrates this: The destination key in the JobTitle entity is titleID, the primary key for that entity. The titleID attribute is added to Employee as foreign key.
Note that if empID had been used as the relationship key for the toJobTitle relationship, a given title could only be assigned to a single employee.

### Compound Relationship Keys

A relationship's keys needn't be single attributes from the related entities; any number of attributes can be paired as relationship keys within the same relationship to form a _compound relationship key_. A relationship that designates more than one pair of keys is called a _compound relationship_.
For example, consider an entity (empPhoto) containing the employee's picture that uses the attributes firstName and lastName as a compound relationship key. (Using people's names for unique identification is generally a bad idea, but it serves the purpose for illustration. In actual practice, this relationship would likely use empID as its relationship key.) This relationship is depicted in [Figure 59](#apple-gq3tm).

!

Figure 59. A Compound Relationship

The algorithm used to resolve a compound relationship is similar to that for a simple relationship. The only difference is the number of pairs of relationship key values that are compared. For two records to correspond, all of the comparisons must be successful.
__Note:__  The keys in a compound relationship can be a combination of _any_ attributes-not just a compound primary key (or foreign keys to a compound primary key). Conversely, you can use a single attribute from a compound primary key as a relationship key in a simple
(non-compound) relationship.

### Joins

Relationships are made up of source-destination key pairs. A _join_ is the pairing of one source attribute and one destination attribute for purposes of establishing a relationship. Thus, simple relationships consist of one join. Compound relationships are composed of two or more joins. In [Figure 59](#apple-gq3ti), for example, the toEmpPhoto relationship is composed of two joins: one linking Employee.lastName to EmpPhoto.lastName, and one linking Employee.firstName to EmpPhoto.firstName.

The Enterprise Objects Framework requires you to declare the join in a relationship as either an _inner join_, a _right outer join_, a _left outer join_, or a _full outer join_. These four _join semantics_ are defined as follows:

- In an inner join, if a destination record can't be found for a given source record, that source record isn't included in the result of the join. Destination records that don't match up to any records in the source table are not included in the result of an inner join, either.
- In a right outer join, destination records for which no source record can be found are included, but not the reverse.
- In a left outer join, source records for which no destination record can be found are included, but not the reverse.
- In a full outer join, _all_ source records from both tables are included in the result of the join.

## Relationship Cardinality

Every relationship has a _cardinality_; the cardinality tells you how many destination records can (potentially) resolve the relationship. The Enterprise Objects Framework defines two cardinalities, _to-one_ and
_to-many_:

- In a to-one relationship, for each source record there's _exactly one_ corresponding destination record.
- In a to-many relationship, for each source record there may be zero, one, or more corresponding destination records.

The toJobTitle relationship is an example of a to-one relationship: An employee can only have one title. The converse relationship, from JobTitle to Employee, would be to-many: a single title can be shared by more than one employee, or there may be no employees with a given title. This relationship, which is owned by JobTitle and called toEmployee, is shown in [Figure 60](#apple-gq2do) (for clarity, the source and destination components are pointed out). That the relationship is to-many is indicated by the double arrowhead.

Notice that the relationship keys for the toEmployee relationship are the same as for toJobTitle. However, the source and destination key assignments are reversed. In other words, whereas Employee.titleID is the source key for the toJobTitle relationship, it's the destination key for toEmployee; similarly, JobTitle.titleID changes destination and source key roles between the two relationships.
This switch does more than demonstrate that the same attributes can be used as relationship keys in more than one relationship; it also exemplifies the typical orientation of the primary key with regard to the relationship keys in to-one and to-many relationships:

- In a to-one relationship, the destination key is always the primary key for its entity.
- In a to-many relationship, the source key is usually a primary key.

!

Figure 60. A To-Many Relationship

## Bidirectional Relationships

Since relationships, as defined by the Enterprise Objects Framework, are unidirectional, it's natural to assume that to simulate a bidirectional relationship-in other words, to express the natural relationship between two entities without regard for direction-all you need is two relationships: One that leads from entity A to entity B, and one that leads from entity B to entity A. Unfortunately, it isn't always that easy.
Consider, for example, the actual relationship between employees and projects. A project can involve many employees, and a single employee can contribute to more than one project.

!

Figure 61. The Project Entity

Forming a to-many relationship between Employee and Project (toProject) and a to-many relationship between Project and Employee (toEmployee) doesn't work, because it's impossible to assign relationship keys that would support this set-up. For example, in the toProject relationship you can't use the empID attribute as a source key because the destination key, Project.empID (added as a foreign key), wouldn't be atomic (since a project may consist of more than one employee). Importing projectID as a foreign key into Employee has the same problem: The attribute wouldn't be atomic (since an employee may be involved with more than one project).
The most common way to establish this "many-to-many" relationship (as it's called in traditional E-R modeling) is to insert an auxiliary entity between Employee and Project, and form a network of relationships to and from it. This is depicted in [Figure 62](#apple-gq2di).

!

Figure 62. A Many-to-Many Relationship

The compound primary key used in EmpProject indicates that the entity characterizes unique combinations of employees and projects. The table that the entity represents would hold a different record for each employee of every project. For example, if three employees were involved with a single project, there would be three EmpProject instances with the same value for the projectID attribute, but each record would have a different value for its empID attribute.

### The Tables Behind the Many-to-Many Model

To better understand how the many-to-many model works, it helps to see an example of the tables that store the data. Sample "EMPLOYEE" and "PROJECT" tables that are filled with this information are shown in [Figure 63](#apple-gqzta) (for clarity, only relevant attributes are shown).

!

Figure 63. "EMPLOYEE" and "PROJECT" Tables

The "EMP_PROJECT" table is shown in [Figure 64](#apple-gu4ti) (for clarity, the last names and project names are shown in the margins).

!

Figure 64. The "EMP_PROJECT" Table

As expected, some values appear more than once for the empID attribute; similarly, some values for projectID are repeated. But since empID and projectID form a compound primary key for the EmpProject entity, no two records may possess the same combination of values for these two attributes. This fact-that no two records can have the same empID and the same ProjectID-signifies that a given employee cannot be assigned to a single project more than once.

## Reflexive Relationships

The source and destination entities in a relationship needn't be different. Where the entities in a relationship are the same, a _reflexive relationship_ is created. Reflexive relationships are important in characterizing a system in which an instance of an entity points to another instance of the same entity.
For example, to show who a given employee reports to, you could create a separate Manager entity. It would be easier, however, to just create a reflexive relationship, as shown in [Figure 65](#apple-gq3ds).

!

Figure 65. A Reflexive Relationship

__Note:__  The name of the relationship, managerOf, doesn't follow the relationship naming convention suggested earlier in this chapter. However, it follows from the meaning of the relationship, and meaning takes precedence over form.
The managerID attribute acts as the relationship's source key; empID is the destination key. Where an employee's managerID matches another employee's empID, the first employee reports to the second. If an employee doesn't have a manager, the value for the managerID attribute is NULL in that employee's record.
Reflexive relationships can represent arbitrarily deep recursions. Thus, from the model above, an employee can report to another employee who reports to yet another employee, and so on. This could go on until an employee who's managerID is NULL is reached, denoting an employee who reports to no one (probably the company president!).

## Flattened Attributes

At the beginning of this chapter, it was stated that an entity maps to a table in the database. This is not strictly true, however, because the Enterprise Objects Framework allows you to add _flattened attributes_ (and _flattened relationships_) to your entity, effectively extending the entity's mapping to more than one table in a database.
A flattened attribute is an attribute that you effectively add from one entity to another by traversing a relationship. You can't add arbitrary attributes from various entities, however. To add an attribute from one entity to another, there must be a to-one relationship between those entities.
For example, by traversing the toJobTitle relationship, you can determine a given employee's title. If you add the title attribute from the JobTitle entity to the Employee entity as a flattened attribute, the Enterprise Objects Framework will automatically traverse the relationship and locate the employee's title when the employee is fetched from the database.
To your code, the flattened attribute looks like any other. After adding the title attribute to the Employee entity as a flattened attribute (which has no effect on the "EMPLOYEE" table in the database), for instance, your application's view of the Employee table would look like [Figure 66](#apple-gq2da):

!

Figure 66. A View of the "EMPLOYEE" Table After Adding a Flattened Attribute

You are not limited to flattening attributes across a single relationship; any number of relationship traversals can be employed. Thus, if there was a relationship between the JobTitle entity and a SalaryRange entity, you could include an employee's maximum salary with the rest of the employee information by flattening a toJobTitle.toSalaryRange.maxSalary attribute into the Employee entity.

### Flattened Relationships

Just as you can flatten an attribute to add it to another entity, so can you flatten a relationship. This gives a source entity access to relationships that a destination entity has with other entities. It is equivalent to performing a multi-table join.
As an example, suppose you need department information for corporate assets that are assigned to employees, using the entities and relationships shown in [Figure 67](#apple-guyts). One way to obtain the needed information is to flatten the relevant attributes (deptName and location, perhaps) across the toEmployee and toDepartment relationships. A simpler way would be to flatten the toDepartment relationship itself, so that it appears to your code as if the Department entity is a part of the Equipment entity.

!

Figure 67. Equipment Allocated by Department

[Figure 68](#apple-gq4dg) shows how the Equipment entity might look after the flattened relationship had been added. In it, toDepartment is a relationship defined as toEmployee.toDepartment. When your code asks an Equipment object for the value of its __toDepartment__ property, it receives the corresponding Department object. Your code can then query the Department object for the needed properties.

!

Figure 68. A Flattened Relationship

While the entities involved in a flattened relationship must be related, those relationships can either be to-one or to-many. If any of the relationships are to-many and your code requests the value for a flattened relationship, it will receive an array of objects corresponding to the flattened relationship's destination entity.

#

---
