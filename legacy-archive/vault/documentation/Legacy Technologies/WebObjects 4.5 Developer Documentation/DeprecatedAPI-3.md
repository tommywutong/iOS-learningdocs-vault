---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Deprecated.html
archived_at: '2026-07-15T08:11:35.905686Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

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

`- (BOOL)canNestTransactions`

Deprecated in Enterprise Objects Framework 4.5.
Don't use this method. There is no new API or workaround; no adaptor
supports nested transactions.
Implemented by subclasses to return YES if the
database server and adaptor context could nest transactions, NO otherwise.

---

### transactionNestingLevel

`- (unsigned)transactionNestingLevel`

Deprecated in Enterprise Objects Framework 4.5.
Use [hasOpenTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfzu64dfnzkheyloonqwg5djn5xa) instead.
Returns the number of transactions in progress.
If the database server and the adaptor support nested transactions,
this number may be greater than 1

---

## EOLoginPanel

### runPanelForAdaptor:validate:

`- (NSDictionary *)runPanelForAdaptor:(EOAdaptor
*)adaptor
validate:(BOOL)flag`

Deprecated in Enterprise Objects Framework 3.0.
Use EOLoginPanel's [runPanelForAdaptor:validate:allowsCreation:](EOLoginPanel-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2mn5tws3sqmfxgk3bpoj2w4udbnzswyrtpojawiylqorxxeotwmfwgszdborstuylmnrxxo42dojswc5djn5xdu) instead.
To get the old behavior, don't allow creation.

---

## EOModelGroup

### delegate

`+ (id)delegate`

Deprecated in Enterprise Objects Framework 3.0.
Use the class method [classDelegate](EOModelGroup-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc6y3mmfzxgrdfnrswoylumu) instead.

---

### setDelegate:

`+ (void)setDelegate:(id)delegate`

Deprecated in Enterprise Objects Framework 3.0.
Use the class method [setClassDelegate:](EOModelGroup-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu233emvweo4tpovyc643forbwyyltoncgk3dfm5qxizj2) instead.

---

[![Table of Contents](attachments/images/up.gif)](EOAccessTOC.md)
