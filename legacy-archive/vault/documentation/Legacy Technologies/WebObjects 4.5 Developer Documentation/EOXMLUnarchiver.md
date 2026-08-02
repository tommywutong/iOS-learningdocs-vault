---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Classes/EOXMLUnarchiver.html
archived_at: '2026-07-15T08:11:36.790802Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOXMLUnarchiver

> **__Inherits
> from:__**
> : Object

> **__Package:__**
> : com.apple.client.eoapplication

---

## Class Description

---

EOXMLUnarchiver objects
contain the parameters used to create controllers (objects of the EOController class
and its descendents) in the controller hierarchy. The parameters
are determined from an XML specification sent from server.

For more information on using this class, see the book _Getting
Started with Direct to Java Client_.

## Method Types

---

> **Decoding objects**
> : [decodeAlignmentForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfifwgsz3onvsw45cgn5zewzlz)
> : [decodeArrayForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfifzheylzizxxes3fpe)
> : [decodeBooleanForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfijxw63dfmfxem33sjnsxs)
> : [decodeClassForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfinwgc43tizxxes3fpe)
> : [decodeColorForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfinxwy33sizxxes3fpe)
> : [decodeDictionaryForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfiruwg5djn5xgc4tzizxxes3fpe)
> : [decodeEditabilityForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfivsgs5dbmjuwy2lupfdg64slmv4q)
> : [decodeFontForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfizxw45cgn5zewzlz)
> : [decodeIntForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfjfxhirtpojfwk6i)
> : [decodePositionForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfkbxxg2lunfxw4rtpojfwk6i)
> : [decodeStringForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfkn2he2lom5dg64slmv4q)
> : [decodeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfkzqwy5lfizxxes3fpe)
>
> **Other methods**
> : [EOXMLUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel2fj5me2tcvnzqxey3inf3gk4q)
> : [decodeRootObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6wcnjrkw4ylsmnugs5tfoixwizldn5sgkutpn52e6ytkmvrxi)
> : [decodeChildren](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkplbguyvlomfzgg2djozsxel3emvrw6zdfinugs3deojsw4)

## Constructors

---

### EOXMLUnarchiver

`public EOXMLUnarchiver(NSDictionary values)`

Creates an
XML archiver based on the _values_ NSDictionary.

---

## Static Methods

---

### decodeRootObject

`public static Object decodeRootObject(NSDictionary aNSDictionary)`

Decodes the
top controller in an XML description, which is represented by an NSDictionary.

---

## Instance Methods

---

### decodeAlignmentForKey

`public int decodeAlignmentForKey(
String key,
int defaultAlignment)`

Returns an
alignment specification (`JTextField.LEFT`, `JTextField.CENTER`,
or `JTextField.RIGHT`)
for the _key_ XML attribute. If no
value for _key_ is specified, returns _defaultAlignment_.

`public int decodeAlignmentForKey(String key)`

Returns an
alignment specification (`JTextField.LEFT`, `JTextField.CENTER`,
or `JTextField.RIGHT`)
for the _key_ XML attribute. If no
value for _key_ is specified, returns `JTextField.LEFT`.

---

### decodeArrayForKey

`public NSArray decodeArrayForKey(
String key,
NSArray defaultArray)`

Returns an NSArray for
the _key_ XML attribute. If no value
for _key_ is specified, returns _defaultArray_.

`public NSArray decodeArrayForKey(String key)`

Returns an NSArray for
the _key_ XML attribute. If no value
for _key_ is specified, returns `null`.

---

### decodeBooleanForKey

`public boolean decodeBooleanForKey(
String key,
boolean defaultBoolean)`

Returns a `boolean` for
the _key_ XML attribute. If no value
for _key_ is specified, returns _defaultBoolean_.

`public boolean decodeBooleanForKey(String key)`

Returns a `boolean` for _key_ XML
attribute. If no value for _key_ is
specified, returns `false`.

---

### decodeChildren

`public NSArray decodeChildren()`

Returns an
NSArray containing the receiver's decoded children. The children
are the objects created from XML tags contained in the receiver's
XML description.

---

### decodeClassForKey

`public Class decodeClassForKey(
String key,
Class defaultClass)`

Returns a Class for
the _key_ XML attribute. If no value
for _key_ is specified, returns _defaultClass_.

`public Class decodeClassForKey(String key)`

Returns a Class for the _key_ XML
attribute. If no value for _key_ is
specified, returns `null`.

---

### decodeColorForKey

`public java.awt.Color decodeColorForKey(
String key,
java.awt.Color defaultColor)`

Returns a
color (a java.awt.Color object) for the _key_ XML
attribute. If no value for _key_ is
specified, returns _defaultColor_.

`public java.awt.Color decodeColorForKey(String key)`

Returns a
color (a java.awt.Color object) for the _key_ XML
attribute. If no value for _key_ is
specified, returns `null`.

---

### decodeDictionaryForKey

`public NSDictionary decodeDictionaryForKey(
String key,
NSDictionary defaultDictionary)`

Returns a NSDictionary for
the _key_ XML attribute. If no value
for _key_ is specified, returns _defaultDictionary_.

`public NSDictionary decodeDictionaryForKey(String key)`

Returns a NSDictionary for
the _key_ XML attribute. If no value
for _key_ is specified, returns `null`.

---

### decodeEditabilityForKey

`public int decodeEditabilityForKey(
String key,
int defaultEditability)`

Returns an
editability specification (`EOEditable.IfSupercontrollerEditable`, `EOEditable.AlwaysEditable`,
or `EOEditable.NeverEditable`)
for the _key_ XML attribute. If no
value for _key_ is specified, returns _defaultEditibility_.

`public int decodeEditabilityForKey(String key)`

Returns an
editability specification (`EOEditable.IfSupercontrollerEditable`, `EOEditable.AlwaysEditable`,
or `EOEditable.NeverEditable`)
for the _key_ XML attribute. If no
value for _key_ is specified, returns `EOEditable.IfSupercontollerEditable`.

---

### decodeFontForKey

`public java.awt.Font decodeFontForKey(
String key,
java.awt.Font defaultFont)`

Returns a
font specification (a java.awt.Font object)
for the _key_ XML attribute. If no
value for _key_ is specified, returns _defaultFont_.

`public java.awt.Font decodeFontForKey(String key)`

Returns a
font specification (a java.awt.Font object)
for the _key_ XML attribute. If no
value for _key_ is specified, returns `null`.

---

### decodeIntForKey

`public int decodeIntForKey(
String key,
int defaultInt)`

Returns an `int` for
the _key_ XML attribute. If no value
for _key_ is specified, returns _defaultInt_.

`public int decodeIntForKey(String key)`

Returns an `int` for
the _key_ XML attribute. If no value
for _key_ is specified, returns 0.

---

### decodePositionForKey

`public int decodePositionForKey(
String key,
int defaultPosition)`

Returns a
position specification (`EOComponentController.Top`, `EOComponentController.Bottom`, `EOComponentController.Left`, `EOComponentController.Right`, `EOComponentController.TopLeft`, `EOComponentController.TopRight`, `EOComponentController.BottomLeft`,
or `EOComponentController.BottomRight`)
for the _key_ XML attribute. If no
value for _key_ is specified, returns _defaultPosition_.

`public int decodePositionForKey(String key)`

Returns a
position specification (`EOComponentController.Top`, `EOComponentController.Bottom`, `EOComponentController.Left`, `EOComponentController.Right`, `EOComponentController.TopLeft`, `EOComponentController.TopRight`, `EOComponentController.BottomLeft`,
or `EOComponentController.BottomRight`)
for the _key_ XML attribute. If no
value for _key_ is specified, returns `EOComponentController.Center`.

---

### decodeStringForKey

`public String decodeStringForKey(
String key,
String defaultString)`

Returns a String for
the _key_ XML attribute. If no value
for _key_ is specified, returns _defaultString_.

`public String decodeStringForKey(String key)`

Returns a String for
the _key_ XML attribute. If no value
for _key_ is specified, returns `null`.

---

### decodeValueForKey

`public Object decodeValueForKey(String key)`

Returns an
Object for the _key_ XML attribute.
If no value for _key_ is specified,
returns `null`.

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
