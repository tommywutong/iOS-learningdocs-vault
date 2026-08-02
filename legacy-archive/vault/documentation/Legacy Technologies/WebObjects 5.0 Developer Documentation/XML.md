---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/XML/Introduction.html
archived_at: '2026-07-15T08:14:47.366357Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/XML/Art/up.gif)](XMLTOC.md)

# XML

> __Package:__ com.webobjects.appserver.xml

---

## Introduction

The XML framework consists of two main classes-WOXMLCoder and WOXMLDecoder-which can encode and decode objects as XML. These classes can be used to archive and unarchive object data, or to parse and/or generate XML obtained from or destined for an external source (such as the World Wide Web). When working with such "foreign" XML, you describe the XML elements and properties and their mapping to objects in an XML-format "mapping model" that you can create with either a text editor or an XML editor.

The mapping model provides greater control over the decoding process and is typically used when you are encoding and decoding XML that is destined for, or originates from, an external source. When the WOXMLCoder and WOXMLDecoder are used as an archiving mechanism, the mapping model is usually not necessary. See ["The Format of the Mapping Model" (page 4)](#apple-ijaucsshjfauq) for more information on the contents and structure of the mapping model.

When archiving and unarchiving custom objects using the WOXMLCoder and WOXMLDecoder without a mapping model, your custom classes need to:

- implement the single method declared in the WOXMLCoding interface (your implementation of this method is where you encode the custom class's instance variables)
- implement the single-argument constructor described in the WOXMLDecoder class introduction

You don't need to do the above if the object you are archiving and unarchiving-as well as any encapsulated objects-are an instance of String, Number (or a subclass, providing that the subclass doesn't add any new instance variables), NSArray, NSDictionary, NSDate, NSData, or EOEnterpriseObject (or a subclass, providing that all instance variables are either attributes or relationships). You also don't need to implement the above if you are working with a mapping model.

Exceptions raised by the underlying SAX parser are, for simplicity's sake, wrapped in a WOXMLException object, greatly reducing the number of exceptions your code needs to catch.

## The Format of the Mapping Model

The mapping model is a text file-created manually with a text editor or an XML editor-that consists of one or more entity elements, each of which can enclose zero or more property elements, all enclosed within a single model element.

The following is a simple mapping model:

```
<model>
    <entity name="Command" xmlTag="command">
        <property name="qty" xmlTag="quantity" attribute="YES"/>
        <property name="movie" xmlTag="movie"/>
        <property name="customer" xmlTag="customer"/>
    </entity>
    <entity name="MyMovie" xmlTag="movie">
        <property name="title" xmlTag="name" attribute="YES"/>
        <property name="dateReleased" xmlTag="date">
        <property name="roles" xmlTag="role">
        <property name="category" xmlTag="cat"/>
    </entity>
    <entity name="com.webobjects.eocontrol.EOGenericRecord" xmlTag="role">
        <property name="roleName" xmlTag="name" attribute="YES"/>
    </entity>
</model>
```

When creating a mapping model, be aware that mappings must be unique for a given property when decoding (that is, you cannot have two mappings for the same property). The same applies for XML tags when encoding: you cannot have two mappings for the same XML tag.

### The "model" Tag

The model tag has no attributes.

### The "entity" Tag

The entity tag has two required attributes and a number of optional ones:

name=_property_ (required) The name of the property on the key-value coding side (the name of the object, attribute, or dictionary key to which the XML data is to be mapped). xmlTag=_tag_ (required) The XML tag. unmappedTagsKey=_key_ (optional) The name of the property on the key-value coding side to be used when, while parsing the XML for the entity, a tag is encountered for which there is no specified mapping in the mapping model. ignoreUnmappedTags=`"YES" | "NO"` (optional) "YES" causes a WOXMLException to be thrown if `unmappedTagsKey` isn't specified and, while parsing the XML for the entity, a tag is encountered for which there is no specified mapping in the mapping model. Note that an exception isn't thrown if the object being decoded is an NSDictionary. contentsKey=_key_

(optional) The property name to be used for text enclosed by the XML element being parsed. For example, if the mapping model contained the following:

```
...
<entity name="com.webobjects.foundation.NSMutableDictionary" xmlTag="text" contentsKey="contents"/ >
...
```

And if the following was encountered while parsing XML:

```
<text>Hello, <b>World!</b></text>
```

An NSMutableDictionary object would be created with a single key-value pair: the key "contents" would have as its value an array containing two elements: the string "Hello, " and a dictionary with a single key-value pair: the key "b" would have as its value the string "World".

### The "property" Tag

Within an entity element, you can have zero or more property elements. The property tag also has two required attributes and a number that are optional:

name=_property_ (required) The name of the property on the key-value coding side (the name of the object, attribute, or dictionary key to which the XML data is to be mapped). xmlTag=_tag_ (required) The XML tag. attribute=`"YES" | "NO"`

(optional) Used during encoding, "YES" causes a given property "a" to be encoded like:

```
<foo a="someValue"> .. </foo>
```

instead of:

```
<foo> <a>someValue</a> .. </foo>
```

forceList=`"YES" | "NO"`

(optional) Used for decoding only. "YES" causes a single enclosed element to be decoded as an NSMutableArray with a single object of the appropriate type.

Decoding an XML structure like the following:

```
<foo>
    <a>value1</a>
    <a>value2</a>
</foo>
```

results in a key-value coding call with key `"foo"` and value an NSMutableArray containing the two "<a>" elements. When there is only a single enclosed element, as in this example:

```
<foo>
    <a>some Value</a>
</foo>
```

decoding will result in a key-value coding call with key `"foo"` and value an object of type "a". `forceList` alters this default behavior, causing the value in this instance to be an NSMutableArray containing a single object of type "a".

codeBasedOn=`"TAG"` (optional) The WOXMLCoder normally uses the value of the property's name attribute as the key during key-value coding. This is the desired behavior in most situations since the name attribute typically indicates the name of an instance variable in a custom class. When working with NSDictionary objects, however, you may instead want to use the value of the xmlTag attribute as the key. To do this, specify codeBasedOn=`"TAG"` in the property's list of attributes. reportEmptyValues=`"YES" | "NO"` (optional) When an empty element is encountered while decoding XML (for instance, `<myElement></myElement>`), the WOXMLDecoder normally creates an empty NSDictionary object. Setting reportEmptyValues to "NO" prevents this empty object from being created. outputTags=`"class"` | `"property"` | `"both"` | `"neither"`

(optional) Used when encoding, this attribute specifies which XML tag specified in the mapping model should be output for the given property. "property", the default, specifies that the property's XML tag should be output. "class" specifies that the XML tag associated with the property's enclosing class should be output instead. "both" indicates that both the property and the class tags should be output, and "neither" indicates that neither XML tag should be placed in the XML.

To illustrate the use of the outputTags attribute, the following mapping model could be used to produce HTML tags from an NSMutableDictionary object:

```
<model>
    <entity name="com.webobjects.foundation.NSMutableDictionary"  xmlTag="text">
        <property name="p" xmlTag="ignore" outputTags="neither"/>
    </entity>
    <entity name="Paragraph"  xmlTag="p">
        <property name="text.contents" xmlTag="text"  outputTags="class"/>
    </entity>
    <entity name="ItemList"  xmlTag="ul">
        <property name="contents" xmlTag="li" outputTags="both"/>
    </entity>
    <entity name="Item"  xmlTag="item">
        <property name="contents" xmlTag="ignore" outputTags="class"/>
    </entity>
    <entity name="LineBreak"  xmlTag="br"/>
    <entity name="ExternalLink"  xmlTag="a">
        <property name="url" xmlTag="href" attribute="YES"/>
        <property name="anchorText" xmlTag="ignore" outputTags="neither"/>
    </entity>
</model>
```

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/Reference/XML/Art/up.gif)](XMLTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
