---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JDBCAdaptorRef/Java/Classes/JDBCAdaptor.html
archived_at: '2026-07-15T08:13:56.920307Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

# JDBCAdaptor

> **__Inherits from:__**
> : com.webobjects.eoaccess.EOAdaptor : Object

> **__Package:__**
> : com.webobjects.jdbcadaptor

---

## Class Description

---

Documentation for this class is forthcoming.

## Method Types

---

> **All methods**
> : [JDBCAdaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpjjceeq2bmrqxa5dpoi): [createAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5feiqsdifsgc4dun5zc6y3smvqxizkbor2he2lcov2gk): [getJDBCInfoWithConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5feiqsdifsgc4dun5zc6z3forfeiqsdjfxgm32xnf2gqq3pnzxgky3unfxw4rdjmn2gs33omfzhs): [typeInfoForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5feiqsdifsgc4dun5zc65dzobsus3tgn5dg64snn5sgk3a): [assertConnectionDictionaryIsValid](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpmfzxgzlsorbw63tomvrxi2lpnzcgsy3unfxw4ylspfexgvtbnruwi): [assignExternalInfoForEntireModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cjnztg6rtpojcw45djojsu233emvwa): [assignExternalTypeForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpmfzxg2lhnzcxq5dfojxgc3cupfygkrtpojaxi5dsnfrhk5df): [createAdaptorContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpmnzgkylumvawiylqorxxeq3pnz2gk6du): [defaultExpressionClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpmrswmylvnr2ek6dqojsxg43jn5xeg3dbonzq): [expressionFactory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpmv4ha4tfonzws33oizqwg5dpoj4q): [externalTypesWithModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpmv4hizlsnzqwyvdzobsxgv3jorue233emvwa): [fetchedValueForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpmzsxiy3imvsfmylmovsum33skzqwy5lf): [isDroppedConnectionException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpnfzui4tpobygkzcdn5xg4zldoruw63sfpbrwk4dunfxw4): [isValidQualifierType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpnfzvmylmnfsfc5lbnruwm2lfojkhs4df): [jdbcInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpnjsgey2jnztg6): [plugIn](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpobwhkz2jny): [setConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rponsxiq3pnzxgky3unfxw4rdjmn2gs33omfzhs): [synchronizationFactory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpon4w4y3iojxw42l2mf2gs33oizqwg5dpoj4q): [typeInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpor4xazkjnztg6): [varcharMaxLength](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6sseijbuczdbob2g64rpozqxey3imfze2ylyjrsw4z3una)

## Constructors

---

### JDBCAdaptor

`public JDBCAdaptor(String name)`

Description forthcoming.

---

## Static Methods

---

### createAttribute

`public static com.webobjects.eoaccess.EOAttribute createAttribute( String name, String columnName, short columnType, String externalType, int precision, int scale, int isNullable)`

Description forthcoming.

---

### getJDBCInfoWithConnectionDictionary

`protected static NSDictionary getJDBCInfoWithConnectionDictionary(NSDictionary connectionDictionary)`

Description forthcoming.

---

### typeInfoForModel

`protected static NSDictionary typeInfoForModel(com.webobjects.eoaccess.EOModel anEOModel)`

Description forthcoming.

---

## Instance Methods

---

### assertConnectionDictionaryIsValid

`public void assertConnectionDictionaryIsValid()`

Description forthcoming.

---

### assignExternalInfoForEntireModel

`public void assignExternalInfoForEntireModel(com.webobjects.eoaccess.EOModel anEOModel)`

Description forthcoming.

---

### assignExternalTypeForAttribute

`public void assignExternalTypeForAttribute( com.webobjects.eoaccess.EOAttribute anEOAttribute)`

Description forthcoming.

---

### createAdaptorContext

`public com.webobjects.eoaccess.EOAdaptorContext createAdaptorContext()`

Description forthcoming.

---

### defaultExpressionClass

`public Class defaultExpressionClass()`

Description forthcoming.

---

### expressionFactory

`public com.webobjects.eoaccess.EOSQLExpressionFactory expressionFactory()`

Description forthcoming.

---

### externalTypesWithModel

`public NSArray externalTypesWithModel(com.webobjects.eoaccess.EOModel anEOModel)`

Description forthcoming.

---

### fetchedValueForValue

`public Object fetchedValueForValue( Object value, com.webobjects.eoaccess.EOAttribute anEOAttribute)`

Description forthcoming.

---

### isDroppedConnectionException

`public boolean isDroppedConnectionException(Exception anException)`

Description forthcoming.

---

### isValidQualifierType

`public boolean isValidQualifierType( String typeName, com.webobjects.eoaccess.EOModel anEOModel)`

Description forthcoming.

---

### jdbcInfo

`protected NSDictionary jdbcInfo()`

Description forthcoming.

---

### plugIn

`public JDBCPlugIn plugIn()`

Description forthcoming.

---

### setConnectionDictionary

`public void setConnectionDictionary(NSDictionary aNSDictionary)`

Description forthcoming.

---

### synchronizationFactory

`public com.webobjects.eoaccess.EOSchemaGeneration synchronizationFactory()`

Description forthcoming.

---

### typeInfo

`protected NSDictionary typeInfo()`

Description forthcoming.

---

### varcharMaxLength

`protected int varcharMaxLength()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
