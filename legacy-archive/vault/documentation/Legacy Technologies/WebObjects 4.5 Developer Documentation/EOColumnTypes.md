---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Protocols/EOColumnTypes.html
archived_at: '2026-07-15T08:11:35.989461Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOColumnTypes

> __Declared in:__  EOAccess/EOSchemaSynchronization.h

## Protocol Description

---

This protocol describes the API for interacting with objects
passed as arguments to the following [EOSQLExpression](EOSQLExpression-3.md#apple-infeoq2fi5cei) methods:

- [+ isColumnType:equivalentToColumnType:options:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5uxgq3pnr2w23supfygkotfof2ws5tbnrsw45cun5bw63dvnvxfi6lqmu5g64dunfxw44z2)
- [+ phraseCastingColumnNamed:fromType:toType:options:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5ygq4tbonsugyltoruw4z2dn5whk3lojzqw2zlehjthe33nkr4xazj2orxvi6lqmu5g64dunfxw44z2)
- [+ statementsToConvertColumnNamed:inTableNamed:fromType:toType:options:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6q3pnz3gk4tuinxwy5lnnzhgc3lfmq5gs3sumfrgyzkomfwwkzb2mzzg63kupfygkotun5khs4dfhjxxa5djn5xhgoq)

You only need to know about this protocol if you are implementing
schema synchronization API for a custom adaptor. In that case, you
don't have to implement a class that adopts this protocol; EOSQLExpression's
implementation of the schema synchronization API uses a private
class that implements it. You only need to know about the protocol because
your method implementations of the above methods needs to compare
two objects that adopt the protocol.

## Instance Methods

---

### name

`- (NSString *)name`

Returns the receiver's name.

---

### precision

`- (unsigned)precision`

Returns the receiver's precision.

---

### scale

`- (int)scale`

Returns the receiver's scale.

---

### width

`- (unsigned)width`

Returns the receiver's width.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
