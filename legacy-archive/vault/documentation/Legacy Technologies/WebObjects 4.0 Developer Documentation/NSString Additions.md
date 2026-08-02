---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/NSStringAdditions.html
archived_at: '2026-07-18T01:28:23.564002Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOStoredProcedure-2.md)
[!](EOAdaptorChannelDelegate.md)

---

# NSString Additions

__Inherits From:__
NSObject

__Declared in:__
EOAccess/EOEntity.h

---

## Class Description

The access layer adds two methods to the NSString class, to enable the conversion of modeling object names to database schema names, and database schema names to modeling object names.

---

## Class Methods

---

### externalNameForInternalName:separatorString:useAllCaps:

+ (NSString \*)`externalNameForInternalName:`(NSString \*)_name_,
`separatorString:`(NSString \*)_separatorString_,
`useAllCaps:`(BOOL)_useAllCaps_)

Used by the Framework to convert modeling object names to database schema names that conform to a standard convention. A conforming database schema name is upper-case and uses "_" to separate words. Consequently "name" becomes "NAME" and "firstName" becomes "FIRST_NAME".

_separatorString_ is a character that is used to separate words. The Framework uses "_" by default as in the examples above. _useAllCaps_ indicates whether to capitalize the name. For example, providing NO converts "firstName" to "first_name".

---

### nameForExternalName:separatorString:initialCaps:

+ (NSString \*)`nameForExternalName:`(NSString \*)_name_,
`separatorString:`(NSString \*)_separatorString_,
`initialCaps:`(BOOL)_initialCaps_)

Used by name beautification to convert database schema names to modeling object names that conform to a standard convention. A conforming attribute, relationship, or stored procedure name is lower-case except for the initial letter of each embedded word other than the first. Consequently "NAME" becomes "name" and "FIRST_NAME" becomes "firstName". A conforming entity is all lower-case except for the initial letter of each word. Consequently "CUSTOMER_ACCOUNT" becomes "CustomerAccount".

_separatorString_ is a character that is used to separate words. The Framework uses "_" by default as in the examples above. _initialCaps_ indicates whether to capitalize the first letter of the first word. By default, the Framework uses YES for entities and NO for everything else.

__See also:__
[- `beautifyNames`](EOModel.md#apple-gqzde) (EOModel), - `beautifyName` ([EOAttribute](EOAttribute-2.md), [EOEntity](EOEntity-2.md), [EORelationship](EORelationship-2.md),
[EOStoredProcedure](EOStoredProcedure-2.md))

---

[!](EOStoredProcedure-2.md)
[!](EOAdaptorChannelDelegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
