---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOAdaptorChannel.html
archived_at: '2026-07-15T08:13:41.194880Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOAdaptorChannel

> __Inherits from:__ Object

> __Package:__ com.webobjects.eoaccess

---

## Class Description

---

EOAdaptorChannel is an abstract class that provides its concrete subclasses with a structure for performing database operations. It's associated with EOAdaptor and EOAdaptorContext, which, together with EOAdaptorChannel, form the __adaptor level__ of Enterprise Objects Framework's access layer. See the EOAdaptor class specification for more information about accessing, creating, and using adaptor level objects.

A concrete subclass of EOAdaptorChannel provides database-specific method implementations and represents an independent communication channel to the database server to which its EOAdaptor object is connected. You never interact with instances of the EOAdaptorChannel class, rather your Enterprise Objects Framework applications use instances of concrete subclasses that are written to interact with a specific database or other persistent storage system.

|  |
| --- |
| __Note:__ EOAdaptorChannel is abstract. Never create instances of the EOAdaptorChannel class. |

You use an adaptor channel to manipulate rows (records) by selecting, fetching, inserting, deleting, and updating them. An adaptor channel also gives you access to some of the metadata on the server, such as what stored procedures exist, what tables exist, and what their basic attributes and relationships are.

All of an adaptor channel's operations take place within the context of transactions controlled or tracked by its EOAdaptorContext. An adaptor context may manage several channels (though not all can), but a channel is associated with only one context.

## Notifying the Adaptor Channel's Delegate

You can assign a delegate to an adaptor channel. The EOAdaptorChannel sends certain messages directly to the delegate, and the delegate responds to these messages on the channel's behalf. Many of the adaptor channel methods notify the channel's delegate before and after an operation is performed. Some delegate methods, such as adaptorChannelShouldEvaluateExpression, let the delegate determine whether the channel should perform an operation. Others, such as adaptorChannelDidEvaluateExpression, are simply notifications that an operation has occurred. The delegate has an opportunity to respond by implementing the delegate methods. If the delegate wants to intervene, it implements adaptorChannelShouldEvaluateExpression. If it simply wants notification when a transaction has begun, it implements adaptorChannelDidEvaluateExpression.

The principal attributes of the EOAdaptorChannel class are:

- Adaptor context
- Delegate

To create an instance of a concrete EOAdaptorChannel subclass, you send a createAdaptorChannel message to an instance of the corresponding EOAdaptorContext subclass. You rarely create adaptor channels yourself. They are generally created automatically by other framework objects.

The following table lists EOAdaptorChannel's more commonly-used methods:

|  |  |
| --- | --- |
| __Method__ | __Description__ |
| [openChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpn5ygk3sdnbqw43tfnq) | Opens the channel so it can perform database operations. |
| [closeChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmnwg643finugc3tomvwa) | Close the channel. |
| [selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom) | Selects rows matching the specified qualifier. |
| [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo) | Fetches a row resulting from the last __selectAttributes__, __executeStoredProcedure__, or __evaluateExpression__. |
| [insertRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfxhgzlsorjg65y) | Inserts the specified row. |
| [updateValuesInRowsDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpovygiylumvlgc3dvmvzus3ssn53xgrdfonrxe2lcmvsee6krovqwy2lgnfsxe) | Updates the row described by the specified qualifier. |
| [deleteRowDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrswyzlumvjg652emvzwg4tjmjswiqtzkf2wc3djmzuwk4q) | Deletes the row described by the specified qualifier. |
| [executeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsq) | Performs the specified stored procedure. |
| [evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4) | Sends the specified expression to the database. |

|  |  |
| --- | --- |
| __Method__ | __Description__ |
| [openChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpn5ygk3sdnbqw43tfnq) | Opens the channel so it can perform database operations. |
| [closeChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmnwg643finugc3tomvwa) | Close the channel. |
| [selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom) | Selects rows matching the specified qualifier. |
| [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo) | Fetches a row resulting from the last __selectAttributes__, __executeStoredProcedure__, or __evaluateExpression__. |
| [insertRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfxhgzlsorjg65y) | Inserts the specified row. |
| [updateValuesInRowDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpovygiylumvlgc3dvmvzus3ssn53uizltmnzgsytfmrbhsulvmfwgsztjmvza) | Updates the row described by the specified qualifier. |
| [deleteRowDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrswyzlumvjg652emvzwg4tjmjswiqtzkf2wc3djmzuwk4q) | Deletes the row described by the specified qualifier. |
| [executeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsq) | Performs the specified stored procedure. |
| [evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4) | Sends the specified expression to the database. |
| [performAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobsxeztpojwuczdbob2g64spobsxeylunfxw4) | Performs an adaptor operation by invoking the EOAdaptorChannel method appropriate for performing the specified operation. |

For more information on subclassing EOAdaptorChannel, see ["Creating an EOAdaptorChannel Subclass" (page 55)](EOAdaptorChannel.Concepts.md#apple-ijaucq2hivdeo).

## Constants

---

EOAdaptorChannel defines several String constants for use as keys and values in an exception's userInfo dictionary (see [performAdaptorOperations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobsxeztpojwuczdbob2g64spobsxeylunfxw44y)).

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| AdaptorOperationsKey | A userInfo dictionary key. |
| FailedAdaptorOperationKey | A userInfo dictionary key. |
| AdaptorFailureKey | A userInfo dictionary key. |
| AdaptorOptimisticLockingFailure | A userInfo dictionary value. |

## Method Types

---

> Accessing the adaptor context[adaptorContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmfsgc4dun5zeg33oorsxq5a)Opening and closing a channel[openChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpn5ygk3sdnbqw43tfnq)[closeChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmnwg643finugc3tomvwa)[isOpen](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfzu64dfny)Modifying rows[insertRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfxhgzlsorjg65y)[updateValuesInRowDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpovygiylumvlgc3dvmvzus3ssn53uizltmnzgsytfmrbhsulvmfwgsztjmvza)[updateValuesInRowsDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpovygiylumvlgc3dvmvzus3ssn53xgrdfonrxe2lcmvsee6krovqwy2lgnfsxe)[deleteRowDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrswyzlumvjg652emvzwg4tjmjswiqtzkf2wc3djmzuwk4q)[deleteRowsDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrswyzlumvjg653tirsxgy3snfrgkzccpfixkylmnftgszls)[lockRowComparingAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnrxwg22sn53ug33nobqxe2lom5axi5dsnfrhk5dfom)Fetching rows[selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom)[describeResults](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrsxgy3snfrgkutfon2wy5dt)[setAttributesToFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponsxiqluorzgsytvorsxgvdpizsxiy3i)[attributesToFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmf2hi4tjmj2xizltkrxumzlumnua)[fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo)[dictionaryWithObjectsForAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmruwg5djn5xgc4tzk5uxi2cpmjvgky3uondg64sbor2he2lcov2gk4y)[cancelFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmnqw4y3fnrdgk5ddna)[isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfzumzlumnues3sqojxwo4tfonzq)Invoking stored procedures[executeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsq)[returnValuesForLastStoredProcedureInvocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpojsxi5lsnzlgc3dvmvzum33sjrqxg5ctorxxezlekbzg6y3fmr2xezkjnz3g6y3boruw63q)Assigning primary keys[primaryKeyForNewRowWithEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobzgs3lboj4uwzlzizxxettfo5jg652xnf2gqrlooruxi6i)Sending SQL to the server[evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4)Batch processing operations[performAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobsxeztpojwuczdbob2g64spobsxeylunfxw4)[performAdaptorOperations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobsxeztpojwuczdbob2g64spobsxeylunfxw44y)Accessing schema information[describeTableNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrsxgy3snfrgkvdbmjwgkttbnvsxg)[describeStoredProcedureNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrsxgy3snfrgku3un5zgkzcqojxwgzleovzgkttbnvsxg)[addStoredProceduresNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmfsgiu3un5zgkzcqojxwgzleovzgk42omfwwkza)[describeModelWithTableNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrsxgy3snfrgktlpmrswyv3jorufiylcnrsu4ylnmvzq)Accessing the delegate[delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrswyzlhmf2gk)[setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponsxirdfnrswoylumu)

## Constructors

---

### EOAdaptorChannel

`public EOAdaptorChannel(EOAdaptorContext adaptorContext)`

Creates and returns an EOAdaptorChannel, with _adaptorContext_. When you create an adaptor channel subclass, override this method.

Don't invoke this method directly unless you are implementing a concrete adaptor context. It is invoked automatically from createAdaptorChannel-the EOAdaptorContext method you use to create a new adaptor channel.

__See Also:__ [adaptorContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmfsgc4dun5zeg33oorsxq5a)

---

## Instance Methods

---

### adaptorContext

`public EOAdaptorContext adaptorContext()`

Returns the receiver's EOAdaptorContext. A subclass of EOAdaptorChannel doesn't need to override this method.

__See Also:__ [EOAdaptorChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpivhuczdbob2g64sdnbqw43tfnq) constructor

---

### addStoredProceduresNamed

`public void addStoredProceduresNamed( NSArray storedProcedureNames, EOModel model)`

Overridden by subclasses to create EOStoredProcedure objects for the stored procedures named in _storedProcedureNames_ and then to add them to _model_. This method is used in conjunction with [describeStoredProcedureNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrsxgy3snfrgku3un5zgkzcqojxwgzleovzgkttbnvsxg) to build a default model in EOModeler. Throws an exception if an error occurs.

---

### attributesToFetch

`public abstract NSArray attributesToFetch()`

Implemented by subclasses to return the set of attributes to retrieve when [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo) is next invoked. An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

---

### cancelFetch

`public abstract void cancelFetch()`

Implemented by subclasses to clear all result sets established by the last [selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom), [executeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsq), or [evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4) message and terminate the current fetch, so that __isFetchInProgress__ returns `false`.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

---

### closeChannel

`public abstract void closeChannel()`

Implemented by subclasses to close the EOAdaptorChannel so that it can't perform operations with the server. Any fetch in progress is canceled. If the receiver is the last open channel in an adaptor context and if the channel's adaptor context has outstanding transactions, closing the channel has server-dependent results: some database servers roll back all outstanding transactions but others do nothing. Regardless of whether outstanding transactions are rolled back, this method has the side effect of closing the receiver's adaptor context's connection with the database if the receiver is its adaptor context's last open channel.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See Also:__ [cancelFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmnqw4y3fnrdgk5ddna), hasOpenTransaction (EOAdaptorContext)

---

### delegate

`public Object delegate()`

Returns the receiver's delegate, or `null` if the receiver doesn't have a delegate. A subclass of EOAdaptorChannel doesn't need to override this method.

---

### deleteRowDescribedByQualifier

`public void deleteRowDescribedByQualifier( com.webobjects.eocontrol.EOQualifier qualifier, EOEntity entity)`

Deletes the row described by _qualifier_ from the database table corresponding to _entity_. Invokes [deleteRowsDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrswyzlumvjg653tirsxgy3snfrgkzccpfixkylmnftgszls) and throws an exception unless exactly one row is deleted. A subclass of EOAdaptorChannel doesn't need to override this method.

---

### deleteRowsDescribedByQualifier

`public abstract int deleteRowsDescribedByQualifier( EOQualifier qualifier, EOEntity entity)`

Implemented by subclasses to delete the rows described by _qualifier_ from the database table corresponding to _entity_. Returns the number of rows deleted. Throws an exception on failure. Some possible reasons for failure are:

- The adaptor channel isn't open.
- The adaptor channel is in an invalid state (for example, it's fetching).
- An error occurs in the database server.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See Also:__ [deleteRowDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrswyzlumvjg652emvzwg4tjmjswiqtzkf2wc3djmzuwk4q), [isOpen](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfzu64dfny), [isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfzumzlumnues3sqojxwo4tfonzq), hasOpenTransaction (EOAdaptorContext)

---

### describeModelWithTableNames

`public EOModel describeModelWithTableNames(NSArray tableNames)`

Overridden by subclasses to create and return a default model containing entities for the tables specified in tableNames. Assigns the adaptor name and connection dictionary to the new model. This method is typically used in conjunction with [describeTableNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrsxgy3snfrgkvdbmjwgkttbnvsxg) and [describeStoredProcedureNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrsxgy3snfrgku3un5zgkzcqojxwgzleovzgkttbnvsxg).

EOAdaptorChannel's implementation does nothing. An adaptor channel subclass should override this method to create a default model from the database's metadata.

---

### describeResults

`public abstract NSArray describeResults()`

Implemented by subclasses to return an array of EOAttributes describing the properties available in the current result set, as determined by [selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom), [executeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsq), or a statement evaluated by [evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4). Only invoke this method if a fetch is in progress as determined by [isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfzumzlumnues3sqojxwo4tfonzq).

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

---

### describeStoredProcedureNames

`public NSArray describeStoredProcedureNames()`

Overridden by subclasses to read and return an array of stored procedure names from the database. This method is used in conjunction with [addStoredProceduresNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmfsgiu3un5zgkzcqojxwgzleovzgk42omfwwkza) to build a default model in EOModeler. Throws an exception if an error occurs.

---

### describeTableNames

`public NSArray describeTableNames()`

Overridden by subclasses to read and return an array of table names from the database. This method in conjunction with [describeModelWithTableNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmrsxgy3snfrgktlpmrswyv3jorufiylcnrsu4ylnmvzq) is used to build a default model.

EOAdaptorChannel's implementation simply returns `null`. An adaptor channel subclass should override this method to construct an array of table names from database metadata.

---

### dictionaryWithObjectsForAttributes

`public NSMutableDictionary dictionaryWithObjectsForAttributes( Object[] objects, NSArray attributes)`

Used by EOAdaptorChannel subclasses to create dictionaries that can be returned from [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo). You don't ordinarily invoke this method unless you are writing your own concrete adaptor. If you are writing a concrete adaptor, use of this method is optional but strongly recommended because it enables performance optimizations. The objects in _objects_ are the values for the row that correspond to the EOAttribute objects in _attributes_.

A subclass of EOAdaptorChannel shouldn't override this method.

---

### evaluateExpression

`public abstract void evaluateExpression(EOSQLExpression expression)`

Implemented by subclasses to send _expression_ to the database server for evaluation, beginning a transaction first and committing it after evaluation if a transaction isn't already in progress. Throws an exception if an error occurs. An EOAdaptorChannel uses this method to send SQL expressions to the database.

If expression results in a select operation being performed, you can fetch the results as you would if you had sent a [selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom). You must use the method [setAttributesToFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponsxiqluorzgsytvorsxgvdpizsxiy3i) before you begin fetching. Also, if _expression_ evaluates to multiple result sets, you must invoke __setAttributesToFetch__ before you begin fetching each subsequent set.

[evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4) invokes the delegate methods adaptorChannelShouldEvaluateExpression and adaptorChannelDidEvaluateExpression.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation. Note, however, that the upper layers of the Framework never invoke [evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4) directly. Thus, adaptors for data stores that don't naturally support an expression language (for example, flat file adaptors) don't need to implement this method to work with the Framework.

__See Also:__ [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo)

---

### executeStoredProcedure

`public abstract void executeStoredProcedure( EOStoredProcedure storedProcedure, NSDictionary values)`

Implemented by subclasses to execute storedProcedure. Any arguments to the stored procedure are in _values_, a dictionary whose keys are the argument names. Use [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo) to get result rows and [returnValuesForLastStoredProcedureInvocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpojsxi5lsnzlgc3dvmvzum33sjrqxg5ctorxxezlekbzg6y3fmr2xezkjnz3g6y3boruw63q) to get return arguments and result status, if any. Throws an exception if an error occurs.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation. Note, however, that the upper layers of the Framework never invoke [executeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsq) directly. Thus, adaptors for data stores that don't support stored procedures (for example, flat file adaptors) don't need to implement this method to work with the Framework

---

### fetchRow

`public abstract NSMutableDictionary fetchRow()`

Implemented by subclasses to fetch the next row from the result set of the last [selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom), [executeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsq), or [evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4) message sent to the receiver. Returns values for the receiver's [attributesToFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmf2hi4tjmj2xizltkrxumzlumnua) in a dictionary whose keys are the attribute names. When there are no more rows in the current result set, this method returns `null`, and invokes the delegate method adaptorChannelDidChangeResultSet if there are more results sets. When there are no more rows or result sets, this method returns `null`, ends the fetch, and invokes adaptorChannelDidFinishFetching. [isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfzumzlumnues3sqojxwo4tfonzq) returns `true` until the fetch is canceled or until this method exhausts all result sets and returns `null`. This method also invoke the delegate methods adaptorChannelWillFetchRow and adaptorChannelDidFetchRow. Throws an exception if an error occurs.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See Also:__ [setAttributesToFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponsxiqluorzgsytvorsxgvdpizsxiy3i)

---

### insertRow

`public abstract void insertRow( NSDictionary row, EOEntity entity)`

Implemented by subclasses to insert the values of _row_ into the table in the database that corresponds to _entity_. _row_ is a dictionary whose keys are attribute names and whose values are the values to insert. Throws an exception on failure. Some possible reasons for failure are:

- The user logged in to the database doesn't have permission to insert a new row.
- The adaptor channel is in an invalid state (for example, fetching).
- The row fails to satisfy a constraint defined in the database server.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

---

### isFetchInProgress

`public abstract boolean isFetchInProgress()`

Implemented by subclasses to return `true` if the receiver is fetching, `false` otherwise. An adaptor channel is fetching if:

- It's been sent a successful [selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom) message.
- A stored procedure that returns rows has been successfully executed using [executeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsq).
- An expression sent through __evaluateExpression__ resulted in a select operation being performed.

An adaptor channel stops fetching when there are no more records to fetch or when it's sent a __cancelFetch__ message.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See Also:__ [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo)

---

### isOpen

`public abstract boolean isOpen()`

Implemented by subclasses to return `true` if the channel has been opened with __openChannel__, `false` if not. An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See Also:__ [closeChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmnwg643finugc3tomvwa)

---

### lockRowComparingAttributes

`public void lockRowComparingAttributes( NSArray attributes, EOEntity entity, com.webobjects.eocontrol.EOQualifier qualifier, NSDictionary snapshot)`

Attempts to lock a row in the database by selecting it with locking on. The lock operation succeeds if a select statement generated with _qualifier_ retrieves exactly one row and the values in the row match the values in _snapshot_, a dictionary whose keys are attribute names and whose values are the values that were last fetched from the database.

__lockRowComparingAttributes__ invokes [selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom) with _attributes_ as the attributes to select, a fetch specification built from _qualifier_, locking on, and _entity_ as the entity. If the select returns no rows or more than one row, the method throws an exception. It also throws an exception if the values in the returned row don't match the corresponding values in _snapshot_.

The Framework uses this method whenever it needs to lock a row. When the Framework invokes it, _qualifier_ specifies the primary key of the row to be locked and attributes used for locking to be compared in the database server. If any of the values specified in _qualifier_ are different from the values in the database row, the select operation will not retrieve or lock the row. When this happens, the row to be locked has been updated in the database since it was last retrieved, and it isn't safe to update it.

Some attributes (such as BLOB types) can't be compared in the database. _attributes_ should specify any such attributes. (If the row doesn't contain any such attributes, _attributes_ can be `null`.) If _qualifier_ generates a select statement that returns and locks a single row, this method performs an in-memory comparison between the value in the retrieved row and the value in _snapshot_ for each attribute in _attributes_. Therefore, _snapshot_ must contain an entry for each attribute in _attributes_. In addition, it must contain an entry for the row's primary key.

A subclass of EOAdaptorChannel doesn't need to override this method.

---

### openChannel

`public abstract void openChannel()`

Implemented by subclasses to put the channel and both its context and adaptor into a state where they are ready to perform database operations. Throws an exception if an error occurs. An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See Also:__ [isOpen](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfzu64dfny), [closeChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmnwg643finugc3tomvwa)

---

### performAdaptorOperation

`public void performAdaptorOperation(EOAdaptorOperation adaptorOperation)`

Performs _adaptorOperation_ by invoking the adaptor channel method appropriate for performing the specified operation. For example, if the adaptor operator for _adaptorOperation_ is EOAdaptorInsertOperator, this method invokes [insertRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpnfxhgzlsorjg65y) using information in _adaptorOperation_ to supply the arguments. Throws an exception if an error occurs.

A subclass of EOAdaptorChannel doesn't need to override this method.

__See Also:__ [performAdaptorOperations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobsxeztpojwuczdbob2g64spobsxeylunfxw44y)

---

### performAdaptorOperations

`public void performAdaptorOperations(NSArray adaptorOperations)`

Performs adaptor operations by invoking [performAdaptorOperation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobsxeztpojwuczdbob2g64spobsxeylunfxw4) with each EOAdaptorOperation object in the array _adaptorOperations_. An adaptor channel subclass may be able to override this method to take advantage of database-specific batch processing capabilities. Invokes the delegate methods adaptorChannelWillPerformOperations and adaptorChannelDidPerformOperations.

This method throws an exception if an error occurs. The exception's userInfo dictionary contains these keys:

|  |  |
| --- | --- |
| __Constant__ | __The corresponding value in the exception's userInfo dictionary__ |
| `AdaptorOperationsKey` | An array of the EOAdaptorOperations being executed. |
| [FailedAdaptorOperationKey](#apple-ijaucrcgivdes) | The particular EOAdaptorOperation that failed. |
| `AdaptorFailureKey` | If present, offers additional information on the type of error that occurred. Currently, the only possible value for this key is `AdaptorOptimisticLockingFailure`, which indicates that an update or lock operation failed because the row found in the database did not match the snapshot taken when the row was last fetched into the application. |

A subclass of EOAdaptorChannel doesn't need to override the __performAdaptorOperations__ method.

---

### primaryKeyForNewRowWithEntity

`public NSDictionary primaryKeyForNewRowWithEntity(EOEntity entity)`

Overridden by subclasses to return a primary key for a new row in the database table that corresponds to _entity_. The primary key returned from this method is a dictionary whose keys are the primary key attribute names. For example, suppose you've got a table MOVIE with primary key MOVIE_ID, and the corresponding Movie entity's primary key attribute is __movieID__. In this scenario, the dictionary returned from [primaryKeyForNewRowWithEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobzgs3lboj4uwzlzizxxettfo5jg652xnf2gqrlooruxi6i) has one entry whose key is __movieID__ and whose value is the unique value to assign. If the primary key is compound (made up of more than one attribute), the dictionary should contain an entry for each primary key attribute. Note, however, that the Enterprise Objects Frameworks adaptors don't handle compound primary keys; they return `null` from [primaryKeyForNewRowWithEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobzgs3lboj4uwzlzizxxettfo5jg652xnf2gqrlooruxi6i) if the primary key is compound.

If information in _entity_ specifies an adaptor-specific means to assign a new primary key (for example, a sequence name or stored procedure), then this method returns a new primary key. Otherwise, if the key is a simple integer, the method tries to fetch a new primary key from the database using an adaptor-specific scheme. Otherwise, the method returns `null`.

EOAdaptorChannel's implementation simply returns `null`. See your adaptor channel's documentation for information on how it generates primary keys.

A subclass of EOAdaptorChannel must override this method. For example, to return a value generated by a sequence, you'd create the proper SQL statement (using EOSQLExpression's expressionForString method) and evaluate it (using the [evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4) method).

---

### __primaryKeysForNewRowsWithEntity__

`public NSArray primaryKeysForNewRowsWithEntity( int numRows, EOEntity anEntity)`

Description forthcoming.

---

### returnValuesForLastStoredProcedureInvocation

`public abstract NSDictionary returnValuesForLastStoredProcedureInvocation()`

Implemented by subclasses to return stored procedure parameter and return values. Used in conjunction with [executeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsq). The dictionary returned by this method has entries whose keys are stored procedure parameter names and whose values are the parameter values. The dictionary also contains a special entry for the stored procedures return value with the key "returnValue". Returns an empty dictionary for stored procedures that have void return types. Returns `null` if the stored procedure has results to fetch. In this case, you must use [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo) until there are no more results to fetch before the return value will be available.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

---

### selectAttributes

`public abstract void selectAttributes( NSArray attributes, EOFetchSpecification fetchSpecification, boolean flag, EOEntity entity)`

Implemented by subclasses to select attributes in rows matching the qualifier in _fetchSpecification_ and set the receiver's attributes to fetch. The selected rows compose one or more result sets, each row of which will be returned by subsequent [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo) messages according to fetchSpecification's sort orderings. If flag is `true`, the rows are locked if possible so that no other user can modify them (the lock specification in _fetchSpecification_ is ignored). Throws an exception if an error occurs. Some possible reasons for failure are:

- The adaptor channel is in an invalid state (for example, fetching).
- The database failed to lock the specified rows.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See Also:__ [setAttributesToFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponsxiqluorzgsytvorsxgvdpizsxiy3i)

---

### setAttributesToFetch

`public abstract void setAttributesToFetch(NSArray attributes)`

Implemented by subclasses to specify the set of attributes used to describe fetch data from a corresponding select. _attributes_ is an array of the attributes to fetch. This method is invoked after [evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4) but before the first call to [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmzsxiy3ikjxxo). This method throws an exception if invoked when there is no fetch in progress.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See Also:__ [selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom)

---

### setDelegate

`public void setDelegate(Object delegate)`

Sets the receiver's delegate to _delegate_, or removes its delegate if _delegate_ is `null`. A subclass of EOAdaptorChannel doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to __super__.

---

### updateValuesInRowDescribedByQualifier

`public void updateValuesInRowDescribedByQualifier( NSDictionary values, com.webobjects.eocontrol.EOQualifier qualifier, EOEntity entity)`

Updates the row described by _qualifier_. Invokes [updateValuesInRowsDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpovygiylumvlgc3dvmvzus3ssn53xgrdfonrxe2lcmvsee6krovqwy2lgnfsxe) and raises an exception unless exactly one row is updated.

A subclass of EOAdaptorChannel doesn't need to override this method.

---

### updateValuesInRowsDescribedByQualifier

`public abstract int updateValuesInRowsDescribedByQualifier( NSDictionary values, EOQualifier qualifier, EOEntity entity)`

Implemented by subclasses to update the rows described by qualifier with the values in _values_. _values_ is a dictionary whose keys are attribute names and whose values are the new values for those attributes (the dictionary need only contain entries for the attributes being changed). Returns the number of updated rows. Throws an exception if an error occurs. Some possible reasons for failure are:

- The user logged in to the database doesn't have permission to update.
- The adaptor channel is in an invalid state (for example, fetching).
- The new values fail to satisfy a constraint defined in the database server.

An adaptor channel subclass should override this method without invoking EOAdaptorChannel's implementation.

__See Also:__ [updateValuesInRowDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpovygiylumvlgc3dvmvzus3ssn53uizltmnzgsytfmrbhsulvmfwgsztjmvza)

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
