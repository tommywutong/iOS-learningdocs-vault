---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html
archived_at: '2026-07-15T07:17:09.021826Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](NSXML%20and%20XML%20Processing.md)

# Introduction to Tree-Based XML Programming Guide for Cocoa

XML is a ubiquitous and flexible markup standard for processing and exchanging data. You can find XML in property lists, as the file format of various applications, and as the format of various sources of information on the Internet, including web-based services. The NSXML classes of Foundation give you a way to process this information efficiently. NSXML logically represents an XML document as a hierarchical tree structure and allows you to query this structure and manipulate its nodes. It supports several XML-related technologies and standards, such as XQuery, XPath, XInclude, XSLT, DTD, and XHTML.

This document explains how you can use NSXML effectively. You might find this information valuable if you need to create, modify, and repeatedly query XML documents. If you simply need to parse XML and extract information from an existing source of XML, the NSXMLParser class is more suited to your needs. For information on using the NSXMLParser class, which is the Cocoa interface to a streaming XML parser, see _[Event-Driven XML Programming Guide](../Event-Driven%20XML%20Programming%20Guide/Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dm2i)_.

This document includes the following articles:

- [NSXML and XML Processing](NSXML%20and%20XML%20Processing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjtfvbeeq2cjjeeera) describes the features and capabilities of NSXML and suggests how you can use it in your applications.
- [The Data Model of NSXML](The%20Data%20Model%20of%20NSXML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjufvbuuqsjivdumri) describes the XQuery-derived data model on which NSXML is based.
- [Creating an XML Document Object](Creating%20an%20XML%20Document%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjvfvbegskhjbbeisi) explains how to process input sources of XML, how to create an XML document programmatically, and how to transform an existing XML tree structure using XSLT.
- [Writing XML From NSXML Objects](Writing%20XML%20From%20NSXML%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjwfvbegskhirbuera) describes how to request an XML document, or a branch of a document, to emit its represented content as XML markup text.
- [Traversing an XML Tree](Traversing%20an%20XML%20Tree.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjxfvbecsski5eecsi) explains how to use NSXML programmatic interfaces to move around within an XML tree structure.
- [Querying an XML Document](Querying%20an%20XML%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjyfvbuuqsgindukry) explains how to use the methods that allow you to perform XQuery and XPath queries to locate particular nodes and objects in an XML tree structure.
- [Modifying an XML Document](Modifying%20an%20XML%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjzfvbuuqseijcekra) describes how to add, remove, and replace nodes in an XML tree and now to change the values of nodes.
- [Representing Object Values as Strings](Representing%20Object%20Values%20as%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytiojxfvbecsseizceiqy) describes the string representations for the standard atomic types and explains how you can obtain string representations of custom objects used as node values.
- [Handling Attributes and Namespaces](Handling%20Attributes%20and%20Namespaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrqfvbecssgjfdumqy) discusses how to use the methods that are specific to attribute nodes and namespace nodes.
- [Binding NSXML Objects to a User Interface](Binding%20NSXML%20Objects%20to%20a%20User%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrrfvbeeq2kjfeumsi) examines a sample NSXML application to illustrate how you can establish bindings between NSXML objects and a user interface.
- [Using Tree Controllers With NSXML Objects](Using%20Tree%20Controllers%20With%20NSXML%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknrvfvjvomi) shows how you can establish bindings between an NSXML document, an `NSTreeController` object, and an `NSOutlineView` object.

A [XML Glossary](XML%20Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tclktk4yq) of XML terms is also included.

Many sources of information on XML and related standards and technologies are available on the Internet, including the following documents from the World Wide Web Consortium (W3C) website:

- “XQuery 1.0 and XPath 2.0 Data Model”—[http://www.w3.org/TR/xpath-datamodel/](http://www.w3.org/TR/xpath-datamodel/)
- “XMLSchema Part 1: Structures”—[http://www.w3.org/TR/xmlschema-1/](http://www.w3.org/TR/xmlschema-1/)
- “XML Schema Part 2: Datatypes —[http://www.w3.org/TR/xmlschema-2/](http://www.w3.org/TR/xmlschema-2/)
- “XML Query Use Cases”—[http://www.w3.org/TR/xquery-use-cases/](http://www.w3.org/TR/xquery-use-cases/)
- “XML Path Language (XPath) 2.0”—[http://www.w3.org/TR/xpath20/](http://www.w3.org/TR/xpath20/)
- “DOM Object Model Core”—[http://www.w3.org/TR/2003/CR-DOM-Level-3-Core-20031107/core.html](http://www.w3.org/TR/2003/CR-DOM-Level-3-Core-20031107/core.html)

The following are useful websites on XML:

- The Annotated XML Specification—[http://www.xml.com/axml/testaxml.htm](http://www.xml.com/axml/testaxml.htm)
- O’Reilly XML.com—[http://www.xml.com/](http://www.xml.com/)

Several XQuery tutorials are listed at the end of [Querying an XML Document](Querying%20an%20XML%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjyfvjvomi) under[Resources For Learning XQuery](Querying%20an%20XML%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjyfuytkmbxha4a).

[Next](NSXML%20and%20XML%20Processing.md)

