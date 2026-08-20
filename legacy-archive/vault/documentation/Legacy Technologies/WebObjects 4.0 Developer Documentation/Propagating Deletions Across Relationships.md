---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/PropogateDeleteRule.html
archived_at: '2026-07-15T08:01:26.756643Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Propagating Deletions Across Relationships

##  Synopsis

Describes the different delete rules for relationships specified in the EOModel.

##  Description

EOModeler allows the user to set the delete rules for a relationship in the advanced relationship inspector. The different delete rules are discussed here.

####  Nullify Delete Rule

When the object is deleted and one of the relationships has a nullify delete rule, EOF traverses through the object graph to the relationship object(s) and sets any back pointer to the deleted object to nil. For example, if a department has employees, the employees relationship in the department has a nullify delete rule, and the department is deleted, EOF removes any back pointer from the employee(s) to the department.

######  Advantages

· Maintains database consistency; back pointers to deleted rows are nulled.

######  Disadvantages

· EOF performs expensive round trips to the database to get the objects at the other side of the relationship and reset their back pointers.

· EOF must resolve faults for the objects on the other side of the relationship.

####  Cascade Delete Rule

When the parent object is deleted, EOF deletes all the objects at the end of a relationship with the cascade delete rule. For example, a department has employees. If the department's employee relationship's delete rule is set as a cascade delete and the department object is deleted, it also deletes the employee objects.

######  Advantages

· Maintains database consistency; back pointers are eliminated along with the objects that contain them.

######  Disadvantages

· EOF performs expensive round trips to the database to access and delete the objects on the other side of the relationship.

· EOF must resolve faults for the objects on the other side of the relationship.

####  Deny Delete Rule

EOF will refuse to delete an object, that has an object at the other end of a relationship with the deny delete rule. For example, the department cannot be deleted if there are employees in the department.

######  Advantages

· Maintains database consistency; prevents rows that are destinations of back pointers from being deleted.

######  Disadvantages

· EOF performs expensive round trips to the database to determine if there are objects on the other side of the relationship.

· EOF must resolve faults for the objects on the other side of the relationship.

####  No Action Delete Rule

When the parent object is deleted, it does not do any checks to the objects at the other end of a relationship with the no action delete rule. Referring to the department/employee example, when the department is deleted, the employees are left with back pointers pointing to the nonexistent department.

######  Advantages

· EOF performs no expensive database round trips.

######  Disadvantages

· Does not maintain database consistency; back pointers can point to deleted rows.

##  See Also

· Adding Referential Integrity Rules in Enterprise Objects Framework Tools and Techniques

##  Questions

· How do I prevent the deletion or an EO which has other EOs in its relationships?

· How do I prevent EOF from doing anything when an EO is deleted?

· How do I delete all the EOs associated with the parent EO when the parent is deleted?

##  Keywords

· Delete Rules

· Cascade

· Nullify

· Deny

· No Action

##  Revision History

22 July, 1998. Seejo Pylappan. First Draft.
19 November, 1998. Clif Liu. Second Draft.

##### 

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
