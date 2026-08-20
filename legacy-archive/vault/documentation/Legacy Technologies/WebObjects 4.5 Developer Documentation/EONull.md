---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EONull.html
archived_at: '2026-07-15T08:11:39.892829Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EONull

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : NSCoding
> : NSCopying
> : NSObject (NSObject)

> __Declared in:__ : EOControl/EONull.h

---

## Class Description

---

The EONull class defines a unique object used to represent
null values in collection objects (which don't allow nil values).
For example, NSDictionaries fetched by an EOAdaptorChannel contain
an EONull instance for such values. EONull is automatically translated
to nil in enterprise objects, however, so most applications should
rarely need to account for this class. See the NSObject Additions
class specification for details on where this translation is performed.

EONull has exactly one instance, returned by the [null](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu45lmnqxw45lmnq) class method. This object isn't
reference-counted, can't be copied (copyWithZone: returns self),
and is never deallocated. You can safely cache this instance and
use pointer comparison to test for the presence of a null value:

> ```
> static id NULL_VALUE;
>
> - (void)applicationDidFinishLaunching:(NSNotification *)aNotification
> {
>     /* ... */
>     NULL_VALUE = [EONull null];
>     return;
> }
>
> if (value == NULL_VALUE) {
>     /* ... */
> }
> ```

## Adopted Protocols

---

> NSCoding: __- encodeWithCoder:__
> : __- initWithCoder:__
>
> EOSortOrderingComparison: [- compareAscending](EOSortOrderingComparison-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2tn5zhit3smrsxe2lom5bw63lqmfzgs43pnyxwg33nobqxezkbonrwk3tenfxgo)
> : [- compareCaseInsensitiveAscending](EOSortOrderingComparison-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2tn5zhit3smrsxe2lom5bw63lqmfzgs43pnyxwg33nobqxezkdmfzwksloonsw443joruxmzkbonrwk3tenfxgo)
> : [- compareCaseInsensitiveDescending](EOSortOrderingComparison-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2tn5zhit3smrsxe2lom5bw63lqmfzgs43pnyxwg33nobqxezkdmfzwksloonsw443joruxmzkemvzwgzlomruw4zy)
> : [- compareDescending](EOSortOrderingComparison-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2tn5zhit3smrsxe2lom5bw63lqmfzgs43pnyxwg33nobqxezkemvzwgzlomruw4zy)
>
> NSCopying: __- copyWithZone:__

## Class Methods

---

### null

`+ (EONull *)null`

Returns the unique instance of EONull.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
