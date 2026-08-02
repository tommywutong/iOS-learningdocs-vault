---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOAdaptorDelegate.html
archived_at: '2026-07-15T08:11:33.202875Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOAdaptor.Delegate

> __(informal interface)__

> __Package:__
> com.apple.yellow.eoaccess

## Interface Description

---

The delegate for EOAdaptor can implement the method [adaptorFetchedValueForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifsgc4dun5zc4rdfnrswoylumuxwczdbob2g64sgmv2gg2dfmrlgc3dvmvdg64swmfwhkzi) to
perform a database-specific transformations on a value.

## Instance Methods

---

### adaptorFetchedValueForValue

`public abstract Object adaptorFetchedValueForValue(
EOAdaptor adaptor,
Object value,
EOAttribute attribute)`

Invoked from [fetchedValueForValue](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxevtbnr2wk) to
allow the delegate to perform a database-specific transformation
on _value_. The delegate should return
the value that the adaptor's database server would ultimately
store for _value_ if it was inserted
or updated in the column described by _attribute._

Ordinarily, [fetchedValueForValue](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxevtbnr2wk) invokes
one of the type-specific __fetchedValue...__ methods
depending on the type of _value_. If
you implement this delegate method, [fetchedValueForValue](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxevtbnr2wk) does
not invoke the other __fetchedValue...__ methods.
It simply invokes your delegate method and returns the value returned
from it. Therefore, an implementation of [adaptorFetchedValueForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifsgc4dun5zc4rdfnrswoylumuxwczdbob2g64sgmv2gg2dfmrlgc3dvmvdg64swmfwhkzi) must
handle values of all types.

---

### reconnectionDictionaryForAdaptor

`public abstract NSDictionary reconnectionDictionaryForAdaptor(EOAdaptor anEOAdaptor)`

Invoked from [handleDroppedConnection](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62dbnzsgyzkeojxxa4dfmrbw63tomvrxi2lpny) to provides
a new connection dictionary for reconnection attempts. If the adaptor's
database connection is dropped (and the adaptor supports database reconnection),
the adaptor attempts to recover by reconnecting. By default, the
adaptor attempts to connect using its original connection dictionary.
If you want it to connect to a different database, implement this
method to return a connection dictionary for the secondary database.
(Note that the secondary database should have the same data as the
original.) If the delegate method is not implemented, the adaptor
uses its existing connection dictionary to reconnect to the server.

__See Also:__
[isDroppedConnectionException](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62ltirzg64dqmvseg33onzswg5djn5xek6ddmvyhi2lpny)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
