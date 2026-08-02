---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/NSStringAdditions.html
archived_at: '2026-07-15T08:11:35.880550Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# NSString Additions

> __Category
> of:__ NSString

> __Declared in:__  EOAccess/EOEntity.h

---

## Category Description

---

The access layer adds two methods to the NSString class, to
enable the conversion of modeling object names to database schema
names, and database schema names to modeling object names.

## Class Methods

---

### externalNameForInternalName:separatorString:useAllCaps:

`+ (NSString *)externalNameForInternalName:(NSString
*)name,
separatorString:(NSString *)separatorString,
useAllCaps:(BOOL)useAllCaps)`

Used by the Framework to convert modeling object
names to database schema names that conform to a standard convention.
A conforming database schema name is upper-case and uses "_"
to separate words. Consequently "name" becomes "NAME" and
"firstName" becomes "FIRST_NAME".

_separatorString_ is
a character that is used to separate words. The Framework uses "_"
by default as in the examples above. _useAllCaps_ indicates
whether to capitalize the name. For example, providing NO converts
"firstName" to "first_name".

---

### nameForExternalName:separatorString:initialCaps:

`+ (NSString *)nameForExternalName:(NSString
*)name,
separatorString:(NSString *)separatorString,
initialCaps:(BOOL)initialCaps)`

Used by name beautification to convert database
schema names to modeling object names that conform to a standard
convention. A conforming attribute, relationship, or stored procedure
name is lower-case except for the initial letter of each embedded
word other than the first. Consequently "NAME" becomes "name"
and "FIRST_NAME" becomes "firstName". A conforming entity
is all lower-case except for the initial letter of each word. Consequently
"CUSTOMER_ACCOUNT" becomes "CustomerAccount".

_separatorString_ is
a character that is used to separate words. The Framework uses "_"
by default as in the examples above. _initialCaps_ indicates
whether to capitalize the first letter of the first word. By default,
the Framework uses YES for entities and NO for everything else.

__See
Also:__  [- beautifyNames](EOModel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2nn5sgk3bpmjswc5lunfthsttbnvsxg) (EOModel), [- beautifyName](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3cmvqxk5djmz4u4ylnmu) ( [EOAttribute](EOAttribute-3.md#apple-incuqq2ijfeue), [EOEntity](EOEntity-3.md#apple-irauuq2ginduu), [EORelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#BFCDGGAG), [EOStoredProcedure](EOStoredProcedure-2.md#apple-inbuuqsdjjeei))

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
