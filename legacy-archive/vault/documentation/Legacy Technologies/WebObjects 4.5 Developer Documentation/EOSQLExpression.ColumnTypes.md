---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOColumnTypes.html
archived_at: '2026-07-15T08:11:33.216028Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOSQLExpression.ColumnTypes

> __Package:__
> com.apple.yellow.eoaccess

## Interface Description

---

This interface describes the API for interacting with objects
passed as arguments to the following [EOSQLExpression](EOSQLExpression.md#apple-infeoq2fi5cei) methods:

- [isColumnTypeEquivalentToColumnType](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxws42dn5whk3lokr4xazkfof2ws5tbnrsw45cun5bw63dvnvxfi6lqmu)
- [phraseCastingColumnNamed](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa2dsmfzwkq3bon2gs3thinxwy5lnnzhgc3lfmq)
- [statementsToConvertColumnType](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32dn5xhmzlsorbw63dvnvxfi6lqmu)

You only need to know about this interface if you are implementing
schema synchronization API for a custom adaptor. In that case, you
don't have to implement a class that implements this interface; EOSQLExpression's
implementation of the schema synchronization API uses a private
class that implements it. You only need to know about the interface because
your method implementations of the above methods needs to compare
two objects that implement the protocol.

## Instance Methods

---

### name

`public abstract String name()`

Returns the receiver's name.

---

### precision

`public abstract int precision()`

Returns the receiver's precision.

---

### scale

`public abstract int scale()`

Returns the receiver's scale.

---

### width

`public abstract int width()`

Returns the receiver's width.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
