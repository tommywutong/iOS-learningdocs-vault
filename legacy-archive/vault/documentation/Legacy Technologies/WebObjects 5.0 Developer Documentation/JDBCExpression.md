---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JDBCAdaptorRef/Java/Classes/JDBCExpression.html
archived_at: '2026-07-15T08:13:57.213922Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

# JDBCExpression

> **__Inherits from:__**
> : com.webobjects.eoaccess.EOSQLExpression : Object

> **__Package:__**
> : com.webobjects.jdbcadaptor

---

## Class Description

---

Documentation for this class is forthcoming.

## Method Types

---

> **All methods**
> : [JDBCExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6sseijbuk6dqojsxg43jn5xa): [stringForDate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5feiqsdiv4ha4tfonzws33of5zxi4tjnztum33sirqxizi): [addJoinClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6ylemrfg62loinwgc5ltmu): [addSelectListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6ylemrjwk3dfmn2ey2ltoraxi5dsnfrhk5df): [allowsNullClauseForConstraint](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6ylmnrxxo42oovwgyq3mmf2xgzkgn5zeg33oon2heyljnz2a): [appendItemToListString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6ylqobsw4zcjorsw2vdpjruxg5ctorzgs3th): [appendItemToOrderByString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6ylqobsw4zcjorsw2vdpj5zgizlsij4vg5dsnfxgo): [appendItemToValueListString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6ylqobsw4zcjorsw2vdpkzqwy5lfjruxg5ctorzgs3th): [bindVariableDictionaryForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tzizxxeqluorzgsytvorsq): [columnTypeStringForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6y3pnr2w23supfygku3uojuw4z2gn5zec5duojuwe5lumu): [externalNameQuoteCharacter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6zlyorsxe3tbnrhgc3lfkf2w65dfinugc4tbmn2gk4q): [formatValueForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc6ztpojwwc5cwmfwhkzkgn5zec5duojuwe5lumu): [jdbcInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc62temjrus3tgn4): [lockClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc63dpmnvug3dbovzwk): [mustUseBindVariableForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc63lvon2fk43fijuw4zcwmfzgsylcnrsum33sif2hi4tjmj2xizi): [prepareSelectExpressionWithAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc64dsmvygc4tfknswyzldorcxq4dsmvzxg2lpnzlws5diif2hi4tjmj2xizlt): [setJDBCInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc643forfeiqsdjfxgm3y): [shouldUseBindVariableForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc643in52wyzcvonsue2lomrlgc4tjmfrgyzkgn5zec5duojuwe5lumu): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc65dpkn2he2lom4): [useBindVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuk6dqojsxg43jn5xc65ltmvbgs3tekzqxe2lbmjwgk4y)

## Constructors

---

### JDBCExpression

`public JDBCExpression(com.webobjects.eoaccess.EOEntity anEOEntity)`

Description forthcoming.

---

## Static Methods

---

### stringForDate

`public static String stringForDate(NSTimestamp date)`

Description forthcoming.

---

## Instance Methods

---

### addJoinClause

`public void addJoinClause( String leftName, String rightName, int semantic)`

Description forthcoming.

---

### addSelectListAttribute

`public void addSelectListAttribute(com.webobjects.eoaccess.EOAttribute anEOAttribute)`

Description forthcoming.

---

### allowsNullClauseForConstraint

`public String allowsNullClauseForConstraint(boolean flag)`

Description forthcoming.

---

### appendItemToListString

`protected void appendItemToListString(String sqlString)`

Description forthcoming.

---

### appendItemToOrderByString

`protected void appendItemToOrderByString(String sqlString)`

Description forthcoming.

---

### appendItemToValueListString

`protected void appendItemToValueListString(String sqlString)`

Description forthcoming.

---

### bindVariableDictionaryForAttribute

`public NSMutableDictionary bindVariableDictionaryForAttribute( com.webobjects.eoaccess.EOAttribute anEOAttribute, Object value)`

Description forthcoming.

---

### columnTypeStringForAttribute

`public String columnTypeStringForAttribute( com.webobjects.eoaccess.EOAttribute anEOAttribute)`

Description forthcoming.

---

### externalNameQuoteCharacter

`public String externalNameQuoteCharacter()`

Description forthcoming.

---

### formatValueForAttribute

`public String formatValueForAttribute( Object value, com.webobjects.eoaccess.EOAttribute anEOAttribute)`

Description forthcoming.

---

### jdbcInfo

`protected NSDictionary jdbcInfo()`

Description forthcoming.

---

### lockClause

`public String lockClause()`

Description forthcoming.

---

### mustUseBindVariableForAttribute

`public boolean mustUseBindVariableForAttribute( com.webobjects.eoaccess.EOAttribute anEOAttribute)`

Description forthcoming.

---

### prepareSelectExpressionWithAttributes

`public void prepareSelectExpressionWithAttributes( NSArray attributes, boolean lock, com.webobjects.eocontrol.EOFetchSpecification anEOFetchSpecification)`

Description forthcoming.

---

### setJDBCInfo

`protected void setJDBCInfo(NSDictionary jdbcInfo)`

Description forthcoming.

---

### shouldUseBindVariableForAttribute

`public boolean shouldUseBindVariableForAttribute( com.webobjects.eoaccess.EOAttribute anEOAttribute)`

Description forthcoming.

---

### toString

`public String toString()`

Description forthcoming.

---

### useBindVariables

`public boolean useBindVariables()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
