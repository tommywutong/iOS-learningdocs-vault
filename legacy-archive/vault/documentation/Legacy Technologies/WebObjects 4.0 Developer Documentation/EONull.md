---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EONull.html
archived_at: '2026-07-18T01:28:36.683828Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EONotQualifier-2.md)
[!](EOObjectStore-2.md)

---

# EONull

__Inherits From:__
NSObject

__Conforms To:__ NSCoding
NSCopying
NSObject (NSObject)

__Declared in:__ EOControl/EONull.h

The EONull class defines a unique object used to represent null values in collection objects (which don't allow __nil__ values). For example, NSDictionaries fetched by an EOAdaptorChannel contain an EONull instance for such values. EONull is automatically translated to __nil__ in enterprise objects, however, so most applications should rarely need to account for this class. See the NSObject Additions class specification for details on where this translation is performed.

EONull has exactly one instance, returned by the __null__ class method. This object isn't reference-counted, can't be copied (__copyWithZone:__ returns __self__ ), and is never deallocated. You can thus safely cache this instance and use pointer comparison to test for the presence of a null value:

> ```
> static id NULL_VALUE;
>
> - (void)applicationDidFinishLaunching:(NSNotification *)aNotification
> {
>     /* ... */
>     NULL_VALUE = [EONull null];
>     return;
> }
> if (value == NULL_VALUE) {
>     /* ... */
> }
> ```

---

## Adopted Protocols

**NSCoding**

**- encodeWithCoder:

**- initWithCoder:****

**EOSortOrderingComparison**

**[- compareAscending:](EOSortOrderingComparison.md)

**[- compareCaseInsensitiveAscending:](EOSortOrderingComparison.md)

**[- compareCaseInsensitiveDescending:](EOSortOrderingComparison.md)

**[- compareDescending:](EOSortOrderingComparison.md)********

****NSCopying****

**- copyWithZone:**

---

#### null

+ (EONull \*)__null__

Returns the unique instance of EONull.

---

[!](EONotQualifier-2.md)
[!](EOObjectStore-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
