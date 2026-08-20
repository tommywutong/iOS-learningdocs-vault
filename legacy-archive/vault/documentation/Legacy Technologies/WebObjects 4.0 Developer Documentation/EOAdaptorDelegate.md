---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOAdaptorDelegate.html
archived_at: '2026-07-18T01:28:23.877059Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOAdaptorContextDelegate.md)
[!](EOCustomClassArchiving.md)

---

# EOAdaptorDelegate

__Adopted By:__
EOAdaptor delegate objects

__Declared in:__
EOAccess/EOAdaptor.h

# Protocol Description

The delegate for EOAdaptor can implement the method [`adaptor:fetchedValueForValue:attribute:`](#apple-heydcoi) to perform a database-specific transformations on a value.

---

## Instance Methods

---

### adaptor:fetchedValueForValue:attribute:

- (id)`adaptor:`(EOAdaptor \*)_adaptor_`fetchedValueForValue:`(id)_value_`attribute:`(EOAttribute \*)_attribute_

Invoked from [`fetchedValueForValue:attribute:`](../Classes/EOAdaptor.md#apple-ha4ds) to allow the delegate to perform a database-specific transformation on _value_. The delegate should return the value that the adaptor's database server would ultimately store for _value_ if it was inserted or updated in the column described by _attribute._

Ordinarily, [`fetchedValueForValue:attribute:`](../Classes/EOAdaptor.md#apple-ha4ds) invokes one of the type-specific `fetchedValue...` methods depending on the type of _value_. If you implement this delegate method, [`fetchedValueForValue:attribute:`](../Classes/EOAdaptor.md#apple-ha4ds) does not invoke the other `fetchedValue...` methods. It simply invokes your delegate method and returns the value returned from it. Therefore, an implementation of [`adaptor:fetchedValueForValue:attribute:`](#apple-heydcoi) must handle values of all types.

---

[!](EOAdaptorContextDelegate.md)
[!](EOCustomClassArchiving.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
