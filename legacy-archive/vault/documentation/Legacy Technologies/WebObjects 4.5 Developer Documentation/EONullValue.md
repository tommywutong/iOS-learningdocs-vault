---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EONullValue.html
archived_at: '2026-07-15T08:11:37.793905Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EONullValue

> **__Inherits from:__**
> : (com.apple.client.eocontrol) Object
>
> (com.apple.yellow.eocontrol) NSObject

> **__Implements:__**
> : (com.apple.client.eocontrol only) NSCoding
> : (com.apple.client.eocontrol only) EOSortOrdering.Comparison
> : (com.apple.client.eocontrol only) Cloneable

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

The EONullValue class defines a unique object used to represent
null values in collection objects (which don't allow null values).
For example, NSDictionaries fetched by an EOAdaptorChannel contain
an EONullValue instance for such values. EONullValue is automatically
translated to null in enterprise objects, however, so most applications
should rarely need to account for this class.

EONullValue has exactly one instance, returned by the [nullValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ttvnrwfmylmovss63tvnrwfmylmovsq) static method. You can
safely cache this instance and use the == operator to test for the
presence of a null value:

> ```
> EONullValue myNull = EONullValue.nullValue();
> /* ... */
> if (value == myNull) {
>     /* ... */
> }
> ```

## Interfaces Implemented

---

> NSCoding (com.apple.client.eocontrol only): `classForCoder`
> : `encodeWithCoder`
>
> EOSortOrderingComparison: [compareAscending](EOSortOrderingComparison.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknxxe5cpojsgk4tjnztug33nobqxe2ltn5xc6y3pnvygc4tfifzwgzlomruw4zy)
> : [compareCaseInsensitiveAscending](EOSortOrderingComparison.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknxxe5cpojsgk4tjnztug33nobqxe2ltn5xc6y3pnvygc4tfinqxgzkjnzzwk3ttnf2gs5tfifzwgzlomruw4zy)
> : [compareCaseInsensitiveDescending](EOSortOrderingComparison.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknxxe5cpojsgk4tjnztug33nobqxe2ltn5xc6y3pnvygc4tfinqxgzkjnzzwk3ttnf2gs5tfirsxgy3fnzsgs3th)
> : [compareDescending](EOSortOrderingComparison.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknxxe5cpojsgk4tjnztug33nobqxe2ltn5xc6y3pnvygc4tfirsxgy3fnzsgs3th)
>
> Cloneable
> (com.apple.client.eocontrol only)

## Constructors

---

### EONullValue

`public EONullValue()`

Returns the unique instance of EONullValue.

---

## Static Methods

---

### nullValue

`public static EONullValue nullValue()`

Returns the unique instance of EONullValue.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
