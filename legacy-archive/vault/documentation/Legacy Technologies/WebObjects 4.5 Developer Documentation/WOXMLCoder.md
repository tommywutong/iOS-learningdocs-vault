---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/XML.framework/Java/Classes/WOXMLCoder.html
archived_at: '2026-07-15T08:11:47.940767Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
XML Reference

[![up](attachments/images/up.gif)](../XMLTOC.md)

# WOXMLCoder

> **__Inherits
> from:__**
> : Object

> **__Package:__**
> : com.apple.webobjects.xml

---

## Class Description

---

Use this class to encode objects as XML. Encoding can take
place either with or without a mapping model. The mapping model
provides greater control over the encoding process and is typically
used when you are encoding and decoding XML that is destined for,
or originates from, an external source. When the WOXMLCoder and [WOXMLDecoder](WOXMLDecoder.md#apple-k5hug33oorsxq5a) are used as an archiving
mechanism, the mapping model is usually not necessary. For more
information on the mapping model, see the ["The Format of the Mapping Model"](XML.md#apple-ijaucsshjfauq) in
the framework introduction.

When encoding without a mapping model, WOXMLCoder is
able to encode any object as long as the object and all of the objects
it encapsulates either implement the [WOXMLCoding](WOXMLCoding.md#apple-k5hug33oorsxq5a) interface
or are an instance of String, Number (or a subclass, providing that
the subclass doesn't add any new instance variables), NSArray,
NSDictionary, NSDate, NSData, or EOEnterpriseObject (or a subclass,
providing that all instance variables are either attributes or relationships).
During the encoding of an enterprise object, WOXMLCoder uses
attribute information stored in the EOModel when assigning an XML
type tag to an object. For objects that don't inherit from EOEnterpriseObject,
the tag supplied by WOXMLCoder's [encodeObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfj5rguzldordg64slmv4q) method
is used.

To encode an object, simply invoke the [encodeRootObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfkjxw65cpmjvgky3uizxxes3fpe) method. To
perform the reverse operation, generating an object from XML data,
see the [WOXMLDecoder](WOXMLDecoder.md#apple-k5hug33oorsxq5a) class.

## Method Types

---

> **Creating a WOXMLCoder**
> : [coder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6wcnjrbw6zdfoixwg33emvza)
> : [coderWithMapping](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6wcnjrbw6zdfoixwg33emvzfo2lunbgwc4dqnfxgo)
>
> **Encoding an object graph**
> : [encodeRootObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfkjxw65cpmjvgky3uizxxes3fpe)
>
> **Implementing the WOXMLCoding
> interface**
> : [encodeBooleanForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfijxw63dfmfxem33sjnsxs)
> : [encodeDoubleForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfirxxkytmmvdg64slmv4q)
> : [encodeFloatForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfizwg6yluizxxes3fpe)
> : [encodeIntForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfjfxhirtpojfwk6i)
> : [encodeObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfj5rguzldordg64slmv4q)

## Static Methods

---

### coder

`public static WOXMLCoder coder()`

Creates and returns a new [WOXMLCoder](#apple-k5hug33oorsxq5a) object.

---

### coderWithMapping

`public static WOXMLCoder coderWithMapping(String mappingURL)`

Creates and returns a new [WOXMLCoder](#apple-k5hug33oorsxq5a) object
initialized with the mapping model specified by _mappingURL_.
See ["The Format of the Mapping Model"](XML.md#apple-ijaucsshjfauq) for
a complete description of the mapping model.

|  |
| --- |
| Windows NT uses backslashes where other systems use forward slashes. When prepending the "file:" URL prefix to a path such as is returned by WOResourceManager's `pathForResourceNamed` method, on Windows NT the prefix must be "file:\\" while on all other platforms the prefix must be "file://". See the RelatedLinks example for one way to select the proper prefix based upon the underlying system. |

---

## Instance Methods

---

### encodeBooleanForKey

`public void encodeBooleanForKey(boolean flag, String key)`

Invoke from within in your implementation
of [WOXMLCoding](WOXMLCoding.md#apple-k5hug33oorsxq5a)'s [encodeWithWOXMLCoder](WOXMLCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6v2plbguyq3pmruw4zzpmvxgg33emvlws5dik5hvqtkminxwizls) method to append
an element with XML tag _key_ to the WOXMLCoder object's
internal string buffer. The element's XML content is the string
representation of _flag_-either True or False-and
the element has an attribute named type with
a value of boolean. For example, the following
call to [encodeBooleanForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfijxw63dfmfxem33sjnsxs):

> ```
> encodeBooleanForKey(true, "myTag");
> ```

causes
the following text to be appended to the WOXMLCoder's
internal string buffer:

> ```
> <myTag type="boolean">True</myTag>
> ```

---

### encodeDoubleForKey

`public void encodeDoubleForKey(double aDouble, String key)`

Invoke from within in your implementation
of [WOXMLCoding](WOXMLCoding.md#apple-k5hug33oorsxq5a)'s [encodeWithWOXMLCoder](WOXMLCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6v2plbguyq3pmruw4zzpmvxgg33emvlws5dik5hvqtkminxwizls) method to append
an element of type _key_ to the WOXMLCoder object's
internal string buffer. The element's content is the string value
of _aDouble_ and the element has an
attribute named type with a value of double.
For example, the following call to [encodeDoubleForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfirxxkytmmvdg64slmv4q):

> ```
> encodeDoubleForKey(1.23, "myTag");
> ```

causes
the following text to be appended to the WOXMLCoder's
internal string buffer:

> ```
> <myTag type="double">1.23</myTag>
> ```

---

### encodeFloatForKey

`public void encodeFloatForKey(float aFloat, String key)`

Invoke from within in your implementation
of [WOXMLCoding](WOXMLCoding.md#apple-k5hug33oorsxq5a)'s [encodeWithWOXMLCoder](WOXMLCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6v2plbguyq3pmruw4zzpmvxgg33emvlws5dik5hvqtkminxwizls) method to append
an element of type _key_ to the WOXMLCoder object's
internal string buffer. The element's content is the string value
of _aFloat_ and the element has an
attribute named type with a value of float. For
example, the following call to [encodeFloatForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfizwg6yluizxxes3fpe):

> ```
> encodeFloatForKey(1.23, "myTag");
> ```

causes
the following text to be appended to the WOXMLCoder's
internal string buffer:

> ```
> <myTag type="float">1.23</myTag>
> ```

---

### encodeIntForKey

`public void encodeIntForKey(int anInt, String key)`

Invoke from within in your implementation
of [WOXMLCoding](WOXMLCoding.md#apple-k5hug33oorsxq5a)'s [encodeWithWOXMLCoder](WOXMLCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6v2plbguyq3pmruw4zzpmvxgg33emvlws5dik5hvqtkminxwizls) method to append
an element of type _key_ to the WOXMLCoder object's
internal string buffer. The element's content is the string value
of _anInt_ and the element has an attribute
named type with a value of int.
For example, the following call to [encodeIntForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfjfxhirtpojfwk6i):

> ```
> encodeIntForKey(123, "myTag");
> ```

causes
the following text to be appended to the WOXMLCoder's
internal string buffer:

> ```
> <myTag type="int">123</myTag>
> ```

---

### encodeObjectForKey

`public void encodeObjectForKey(Object anObject, String key)`

Invoke from within in your implementation
of [WOXMLCoding](WOXMLCoding.md#apple-k5hug33oorsxq5a)'s [encodeWithWOXMLCoder](WOXMLCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6v2plbguyq3pmruw4zzpmvxgg33emvlws5dik5hvqtkminxwizls) method to append
an element of type _key_ to the WOXMLCoder object's
internal string buffer. The element's content depends on _anObject_'s
class. _anObject_ must meet the same
criteria outlined in [encodeRootObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfkjxw65cpmjvgky3uizxxes3fpe).

[encodeRootObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyq3pmrsxel3fnzrw6zdfkjxw65cpmjvgky3uizxxes3fpe) relies
upon this method to perform the actual encoding of objects.

---

### encodeRootObjectForKey

`public synchronized String encodeRootObjectForKey(Object anObject, String key)`

Encodes _anObject_ as
XML and returns the resulting XML string. The encoded root object
is tagged using _key_, and has a type attribute
that indicates _anObject_'s class. _anObject_ must
be one of the following:

- an instance of
  String
- an instance of NSArray
- an instance of NSDictionary
- an instance of NSDate
- an instance of Number (or a subclass, providing that the subclass
  doesn't add instance variables)
- an instance of NSData
- an object that implements the WOXMLCoding interface
- an instance of EOEnterpriseObject (or a subclass, providing
  that all instance variables are either attributes or relationships)

If _anObject_ is
not one of the above, __encodeRootObjectForKey__ throws
an exception.

---

[![up](attachments/images/up.gif)](../XMLTOC.md)
