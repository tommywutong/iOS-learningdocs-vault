---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/More/SQLStatementFormats.html
archived_at: '2026-07-18T01:28:23.387026Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](Mapping%20Attributes-2.md)
[!](EODatabase-3.md)

---

# SQL Statement Formats

In addition to mapping database values to object values, an EOAttribute can alter the way values are selected, inserted, and updated in the database by defining special format strings. These format strings allow a client application to extend its reach right down to the server for certain operations. For example, you might want to view an employee's salary on a yearly basis, without defining a derived attribute as in a previous example. In this case, you could set the salary attribute's SELECT statement format to "salary \* 12" (with [`setReadFormat:`](../EOAttribute.md#apple-heztc)) and the INSERT and UPDATE statement formats to "salary / 12" ([`setWriteFormat:`](../EOAttribute.md#apple-he3ds)). Thus, whenever your application retrieves values for the salary attribute they're multiplied by 12, and when it writes values back to the database they're divided by 12.

Your application can use any legal SQL value expression in a format string, and can even access server-specific features such as functions and stored procedures (see EOEntity's [`setStoredProcedure:forOperation:`](../EOEntity.md#apple-hezti) method description for more information). Accessing server-specific features can offer your application great flexibility in dealing with its server, but does limit its portability. You're responsible for ensuring that your SQL is well-formed and will be understood by the database server.

Format strings for the [`setReadFormat:`](../EOAttribute.md#apple-heztc) and [`setWriteFormat:`](../EOAttribute.md#apple-he3ds) methods should use "%P" as the substitution character for the value that is being formatted. "%@" will not work. For example:

> ```
> [myAttribute setReadFormat:@"TO_UPPER(%P)"];[myAttribute setWriteFormat:@"TO_LOWER(%P)"];
> ```

Instead of setting the read and write formats programmatically, you can set them in EOModeler, which is more common. For more information, see the chapter "Using EOModeler" in _WebObjects Tools and Techniques_.

---

[!](Mapping%20Attributes-2.md)
[!](EODatabase-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
