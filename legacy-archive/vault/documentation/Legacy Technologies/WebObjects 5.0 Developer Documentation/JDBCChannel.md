---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JDBCAdaptorRef/Java/Classes/JDBCChannel.html
archived_at: '2026-07-15T08:13:57.181635Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

# JDBCChannel

> **__Inherits from:__**
> : com.webobjects.eoaccess.EOAdaptorChannel : Object

> **__Package:__**
> : com.webobjects.jdbcadaptor

---

## Class Description

---

Documentation for this class is forthcoming.

## Method Types

---

> **All methods**
> : [JDBCChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpjjceeq2dnbqw43tfnq): [addStoredProceduresNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmfsgiu3un5zgkzcqojxwgzleovzgk42omfwwkza): [attributesToFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmf2hi4tjmj2xizltkrxumzlumnua): [cancelFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmnqw4y3fnrdgk5ddna): [closeChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmnwg643finugc3tomvwa): [deleteRowsDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmrswyzlumvjg653tirsxgy3snfrgkzccpfixkylmnftgszls): [describeModelWithTableNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmrsxgy3snfrgktlpmrswyv3jorufiylcnrsu4ylnmvzq): [describeResults](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmrsxgy3snfrgkutfon2wy5dt): [describeStoredProcedureNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmrsxgy3snfrgku3un5zgkzcqojxwgzleovzgkttbnvsxg): [describeTableNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmrsxgy3snfrgkvdbmjwgkttbnvsxg): [evaluateExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4): [executeStoredProcedure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmv4gky3vorsvg5dpojswiudsn5rwkzdvojsq): [fetchRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpmzsxiy3ikjxxo): [insertRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpnfxhgzlsorjg65y): [isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpnfzumzlumnues3sqojxwo4tfonzq): [isOpen](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpnfzu64dfny): [openChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpn5ygk3sdnbqw43tfnq): [primaryKeyForNewRowWithEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpobzgs3lboj4uwzlzizxxettfo5jg652xnf2gqrlooruxi6i): [returnValuesForLastStoredProcedureInvocation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpojsxi5lsnzlgc3dvmvzum33sjrqxg5ctorxxezlekbzg6y3fmr2xezkjnz3g6y3boruw63q): [selectAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bponswyzldoraxi5dsnfrhk5dfom): [setAttributesToFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bponsxiqluorzgsytvorsxgvdpizsxiy3i): [updateValuesInRowsDescribedByQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbug2dbnzxgk3bpovygiylumvlgc3dvmvzus3ssn53xgrdfonrxe2lcmvsee6krovqwy2lgnfsxe)

## Constructors

---

### JDBCChannel

`public JDBCChannel(JDBCContext aJDBCContext)`

Description forthcoming.

---

## Instance Methods

---

### addStoredProceduresNamed

`public void addStoredProceduresNamed( NSArray storedProcedureNames, com.webobjects.eoaccess.EOModel anEOModel)`

Description forthcoming.

---

### attributesToFetch

`public NSArray attributesToFetch()`

Description forthcoming.

---

### cancelFetch

`public void cancelFetch()`

Description forthcoming.

---

### closeChannel

`public void closeChannel()`

Description forthcoming.

---

### deleteRowsDescribedByQualifier

`public int deleteRowsDescribedByQualifier( com.webobjects.eocontrol.EOQualifier anEOQualifier, com.webobjects.eoaccess.EOEntity anEOEntity)`

Description forthcoming.

---

### describeModelWithTableNames

`public com.webobjects.eoaccess.EOModel describeModelWithTableNames(NSArray tableNames)`

Description forthcoming.

---

### describeResults

`public NSArray describeResults()`

Description forthcoming.

---

### describeStoredProcedureNames

`public NSArray describeStoredProcedureNames()`

Description forthcoming.

---

### describeTableNames

`public NSArray describeTableNames()`

Description forthcoming.

---

### evaluateExpression

`public void evaluateExpression(com.webobjects.eoaccess.EOSQLExpression anEOSQLExpression)`

Description forthcoming.

---

### executeStoredProcedure

`public void executeStoredProcedure( com.webobjects.eoaccess.EOStoredProcedure anEOStoredProcedure, NSDictionary values)`

Description forthcoming.

---

### fetchRow

`public NSMutableDictionary fetchRow()`

Description forthcoming.

---

### insertRow

`public void insertRow( NSDictionary row, com.webobjects.eoaccess.EOEntity anEOEntity)`

Description forthcoming.

---

### isFetchInProgress

`public boolean isFetchInProgress()`

Description forthcoming.

---

### isOpen

`public boolean isOpen()`

Description forthcoming.

---

### openChannel

`public void openChannel()`

Description forthcoming.

---

### primaryKeyForNewRowWithEntity

`public NSDictionary primaryKeyForNewRowWithEntity(com.webobjects.eoaccess.EOEntity anEOEntity)`

Description forthcoming.

---

### returnValuesForLastStoredProcedureInvocation

`public NSDictionary returnValuesForLastStoredProcedureInvocation()`

Description forthcoming.

---

### selectAttributes

`public void selectAttributes( NSArray attributes, com.webobjects.eocontrol.EOFetchSpecification anEOFetchSpecification, boolean flag, com.webobjects.eoaccess.EOEntity anEOEntity)`

Description forthcoming.

---

### setAttributesToFetch

`public void setAttributesToFetch(NSArray attributes)`

Description forthcoming.

---

### updateValuesInRowsDescribedByQualifier

`public int updateValuesInRowsDescribedByQualifier( NSDictionary row, com.webobjects.eocontrol.EOQualifier anEOQualifier, com.webobjects.eoaccess.EOEntity anEOEntity)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
