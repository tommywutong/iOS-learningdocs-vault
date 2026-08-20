---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Protocols/EOAdaptorChannelDelegate.html
archived_at: '2026-07-15T08:11:35.943616Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOAdaptorChannel Delegate

> __(informal protocol)__

> __Declared in:__  EOAccess/EOAdaptorChannel.h

## Protocol Description

---

EOAdaptorChannel sends messages to its delegate for nearly
every operation that would affect data in the database server. The
delegate can use these methods to preempt these operations, modify
their results, or simply track activity.

## Instance Methods

---

### adaptorChannelDidChangeResultSet:

`- (void)adaptorChannelDidChangeResultSet:(id)channel`

Invoked from [fetchRowWithZone:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) when
a select operation resulted in multiple result sets. This method tells
the delegate that the next invocation of [fetchRowWithZone:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) will
fetch from the next result set. This method is invoked when [fetchRowWithZone:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) returns nil andthere
are still result sets left to fetch. The delegate can invoke [setAttributesToFetch:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2ec5duojuwe5lumvzvi32gmv2gg2b2) to
prepare for fetching the new rows.

---

### adaptorChannel:didEvaluateExpression:

`- (void)adaptorChannel:(id)channel
didEvaluateExpression:(EOSQLExpression
*)expression`

Invoked from [evaluateExpression:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) to
tell the delegate that a query language expression has been evaluated
by the database server.

---

### adaptorChannel:didExecuteStoredProcedure:withValues:

`- (void)adaptorChannel:(id)channel
didExecuteStoredProcedure:(EOStoredProcedure
*)procedure
withValues:(NSDictionary *)values`

Invoked from [executeStoredProcedure:withValues:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu) after _procedure_ is
executed successfully.

---

### adaptorChannel:didFetchRow:

`- (void)adaptorChannel:(id)channel
didFetchRow:(NSMutableDictionary
*)row`

Invoked from [fetchRowWithZone:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) after
a row is fetched successfully. This method is not invoked if an exception
occurs during the fetch or if the same returns nil because there
are no more rows in the current result set. The delegate may modify _row_,
which will be returned from [fetchRowWithZone:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi).

---

### adaptorChannelDidFinishFetching:

`- (void)adaptorChannelDidFinishFetching:(id)channel`

Invoked from [fetchRowWithZone:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) to
tell the delegate that fetching is finished for the current select operation.
This method is invoked when a fetch ends in [fetchRowWithZone:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) because
there are no more result sets.

---

### adaptorChannel:didPerformOperations:exception:

`- (NSException *)adaptorChannel:(id)channel
didPerformOperations:(NSArray
*)operations
exception:(NSException *)exception`

Invoked from [performAdaptorOperations:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xhgoq). _exception_ is nil if
no exception was raised while _operations_ were
performed. Otherwise, _exception_ is
the raised exception. The delegate can return the same or a different
exception, which is re-raised by [performAdaptorOperations:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xhgoq),
or it can return nil to prevent the adaptor channel from raising
an exception.

---

### adaptorChannel:didSelectAttributes:fetchSpecification:lock:entity:

`- (void)adaptorChannel:(id)channel
didSelectAttributes:(NSArray *)attributes
fetchSpecification:(EOFetchSpecification
*)fetchSpecification
lock:(BOOL)flag
entity:(EOEntity *)entity`

Invoked from [selectAttributes:fetchSpecification:lock:entity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a) to
tell the delegate that rows have been selected in the database server.

---

### adaptorChannelShouldConstructStoredProcedureReturnValues:

`- (NSDictionary *)adaptorChannelShouldConstructStoredProcedureReturnValues:(id)channel`

Invoked from [returnValuesForLastStoredProcedureInvocation](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3smv2hk4tokzqwy5lfondg64smmfzxiu3un5zgkzcqojxwgzleovzgksloozxwgylunfxw4) to
tell the delegate that _channel_ is constructing
return values for the last stored procedure evaluated. If the delegate
returns a value other than nil, that value will be returned immediately
from [returnValuesForLastStoredProcedureInvocation](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3smv2hk4tokzqwy5lfondg64smmfzxiu3un5zgkzcqojxwgzleovzgksloozxwgylunfxw4).

---

### adaptorChannel:shouldEvaluateExpression:

`- (BOOL)adaptorChannel:(id)channel
shouldEvaluateExpression:(EOSQLExpression
*)expression`

Invoked from [evaluateExpression:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) to
tell the delegate that _channel_ is
sending an expression to the database server. The delegate returns YES to
permit the adaptor channel to send _expression_ to
the server. If the delegate returns NO, the adaptor channel does
not send the expression and returns immediately. When the delegate
returns NO, the adaptor channel expects that the implementor of
the delegate has done the work that [evaluateExpression:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) would
have done. The delegate can create a new EOSQLExpression and send
the expression itself before returning NO.

---

### adaptorChannel:shouldExecuteStoredProcedure:withValues:

`- (NSDictionary *)adaptorChannel:(id)channel
shouldExecuteStoredProcedure:(EOStoredProcedure
*)procedure
withValues:(NSDictionary *)values`

Invoked from [executeStoredProcedure:withValues:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu) to
tell the delegate that _channel_ is
executing a stored procedure. If the delegate returns a value other
than nil, that value is used as the arguments to the stored procedure
instead of _values_.

---

### adaptorChannel:shouldReturnValuesForStoredProcedure:

`- (NSDictionary *)adaptorChannel:(id)channel
shouldReturnValuesForStoredProcedure:(NSDictionary
*)returnValues`

Invoked from [returnValuesForLastStoredProcedureInvocation](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3smv2hk4tokzqwy5lfondg64smmfzxiu3un5zgkzcqojxwgzleovzgksloozxwgylunfxw4) to
tell the delegate that _channel_ is returning
values for a stored procedure. If the delegate returns a value other
than nil, that value is returned from [returnValuesForLastStoredProcedureInvocation](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3smv2hk4tokzqwy5lfondg64smmfzxiu3un5zgkzcqojxwgzleovzgksloozxwgylunfxw4) instead
of _returnValues_.

---

### adaptorChannel:shouldSelectAttributes:fetchSpecification:lock:entity:

`- (BOOL)adaptorChannel:(id)channel
shouldSelectAttributes:(NSArray
*)attributes
fetchSpecification:(EOFetchSpecification
*)fetchSpecification
lock:(BOOL)flag
entity:(EOEntity *)entity`

Invoked from [selectAttributes:fetchSpecification:lock:entity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a) to
ask the delegate whether a select operation should be performed.
The delegate should not modify fetchSpecification. Instead, if the delegate
wants to perform a different select it should invoke [selectAttributes:fetchSpecification:lock:entity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a) itself
with a new fetch specification, and return NO (indicating that the
adaptor channel should not perform the select itself).

---

### adaptorChannelWillFetchRow:

`- (void)adaptorChannelWillFetchRow:(id)channel`

Invoked from [fetchRowWithZone:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) to
tell the delegate that a single row will be fetched. The delegate
can determine the attributes used by the fetch by sending [attributesToFetch](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3bor2he2lcov2gk42un5dgk5ddna) to _channel_,
and can change the set of attributes to fetch by sending [setAttributesToFetch:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2ec5duojuwe5lumvzvi32gmv2gg2b2) to _channel_.
The adaptor channel performs the actual fetch.

---

### adaptorChannel:willPerformOperations:

`- (NSArray *)adaptorChannel:(id)channel
willPerformOperations:(NSArray
*)operations`

Invoked from [performAdaptorOperations:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xhgoq) to
tell the delegate that _channel_ is
performing the EOAdaptorOperations in _operations_.
The delegate may return _operations_ or
a different NSArray for the adaptor channel to perform. If the delegate
returns nil, the adaptor channel does not perform the operations
and returns from the method immediately.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
