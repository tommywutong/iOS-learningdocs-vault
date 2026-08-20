---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Deprecated.html
archived_at: '2026-07-15T08:11:33.136679Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](EOAccessTOC.md) 

# DeprecatedAPI

This file enumerates those EOAccess Framework classes and
methods that have been deprecated and should no longer be used.
Wherever possible, notes have been included to indicate what API
should be used in place of the deprecated class or method.

## EOAdaptorContext

Nested transactions are no longer supported. Enterprise Objects
Framework never actually used nested transactions. Furthermore,
the concrete adaptors were not guaranteed to support them, especially
since the SQL/92 standard doesn't allow nested transactions. New
features in Enterprise Objects Framework 4.5 make nested transactions
impossible to support. Consequently, the methods supporting nested transactions
have been deprected.

### canNestTransactions

`public boolean canNestTransactions()`

Deprecated in Enterprise Objects Framework 4.5.
Don't use this method. There is no new API or workaround; no adaptor
supports nested transactions.
Implemented by subclasses to return true if
the database server and adaptor context could nest transactions, false otherwise.

---

### transactionNestingLevel

`public int transactionNestingLevel()`

Deprecated in Enterprise Objects Framework 4.5.
Use [hasOpenTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpnbqxgt3qmvxfi4tbnzzwcy3unfxw4) instead.
Returns the number of transactions in progress.
If the database server and the adaptor support nested transactions,
this number may be greater than 1

---

[![Table of Contents](attachments/images/up.gif)](EOAccessTOC.md)
