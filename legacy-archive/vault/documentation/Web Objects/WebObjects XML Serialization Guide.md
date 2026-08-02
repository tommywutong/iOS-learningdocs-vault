---
title: WebObjects XML Serialization Guide
apple_id: TP40000976
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/AboutThisBook/AboutThisBook.html
archived_at: '2026-07-18T02:22:15.792352Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Introduction/Introduction.html)

# Introduction to WebObjects XML Serialization Guide

This document explains how to you can use XML serialization in your applications. Binary serialization is a simple and efficient way of serializing data. To see this appealing format, invoke the `cat` command on an executable file. Binary is a wonderful format for computers to use, but it's not easy for people to understand. XML (Extensible Markup Language) is a specification that defines a format that can be used to represent data in a way that is more understandable to human beings than binary is.

The Java language has an excellent API for binary serialization. WebObjects extends that API to provide you with XML serialization.

Encoding objects and data into XML documents allows you to easily view and modify objects and data in their serialized form. It also lets you share information between applications, systems, and even organizations using a standard format. In addition, when receiving streams of serialized data over the Internet, you may want to make sure that the document is valid before deserializing it. XML serialization provides you with facilities to accomplish this.

This document assumes that you are familiar with XML, binary serialization in Java, and Sun's security manager. If you plan on using the XSLT processor included with WebObjects or one of your own, you should have enough knowledge of Extensible Stylesheet Language Transformations (XSLT) to develop XSLT stylesheets. [Additional Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcnzxfvjvomi) provides a list of resources that get you started in Java binary serialization and XSLT.

You should also have experience developing WebObjects applications. In particular, you need to know how to create applications using Project Builder (the project-management tool of WebObjects). See [Additional Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcnzxfvjvomi) for a list of documents that address this and other essential subjects.

The document contains the following chapters and appendixes:

- [XML Serialization Overview](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Introduction/Introduction.html#//apple_ref/doc/uid/TP30000178-SW10) provides you with an overview of XML, XML Schema files, document type definition (DTD) files, XML namespaces, and XSLT.
- [XML Serialization Essentials](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Serialization/Serialization.html#//apple_ref/doc/uid/TP30000179-SW16) explains XML serialization in WebObjects. In particular, you learn about the API used to serialize and deserialize objects and data, security, and versioning.
- [Serializing Objects and Data](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Serializing/Serializing.html#//apple_ref/doc/uid/TP30000180-SW36) walks you through the creation of a project that implements both binary and XML serialization.
- [XML Transformation](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Transformation/Transformation.html#//apple_ref/doc/uid/TP30000181-SW8) explains the process of transforming XML documents using an XSLT processor. It also contains details on how you can use your favorite XML parser and transformer in WebObjects applications and some performance issues to keep in mind when serializing and transforming data.
- [Transforming XML Documents](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Transforming/Transforming.html#//apple_ref/doc/uid/TP30000182-SW13) expands the project introduced in [Serializing Objects and Data](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Serializing/Serializing.html#//apple_ref/doc/uid/TP30000180-SW36) by adding transformation of serialized data.
- The woxml.dtd file contains listings of the XML Schema and DTD files that define the format of XML documents that represent serialized data.
- [Code Listings](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Listings/Listings.html#//apple_ref/doc/uid/TP30000184-SW7) contains listings of example classes and the XSLT script introduced in [Transforming XML Documents](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Transforming/Transforming.html#//apple_ref/doc/uid/TP30000182-SW13).

This document also contains a glossary of terms and an index.

[Serializing Objects and Data](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Serializing/Serializing.html#//apple_ref/doc/uid/TP30000180-SW36) and [Transforming XML Documents](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Transforming/Transforming.html#//apple_ref/doc/uid/TP30000182-SW13) walk you through developing applications that use binary and XML serialization. The projects created in those chapters are included in `/Developer/Documentation/WebObjects/XML_Serialization/Projects`. As a companion to the document, there is a compressed version of the projects at [http://developer.apple.com/documentation/WebObjects](https://developer.apple.com/documentation/WebObjects).

If you need to learn the basics about developing WebObjects applications, you can find that information in the following documents:

- _[WebObjects Overview](WebObjects%20Overview/Introduction%20to%20WebObjects%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamby)_ provides you with a survey of WebObjects technologies and capabilities.
- _[WebObjects Web Applications Programming Guide](WebObjects%20Web%20Applications%20Programming%20Guide/Introduction%20to%20WebObjects%20Web%20Applications%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjq)_ shows you how to develop HTML-based applications with WebObjects.
- _[WebObjects Java Client Programming Guide](WebObjects%20Java%20Client%20Programming%20Guide/Introduction%20to%20WebObjects%20Java%20Client%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjx)_ explains how to develop Swing-based applications with WebObjects.

For additional WebObjects documentation and links to other resources, visit [http://developer.apple.com/webobjects](https://developer.apple.com/webobjects).

### Additional Resources

In addition to WebObjects development experience, you also need to be acquainted with the Java binary serialization API and XML.

The following resources provide information on serialization and XML:

- "Advanced Object Serialization" ([http://developer.java.sun.com/developer/technicalArticles/ALT/index.html](http://developer.java.sun.com/developer/technicalArticles/ALT/index.html))
- _Java and XML_ (published by O'Reilly)
- _XSLT_ (published by O'Reilly)
- _XSLT Programmer's Reference_ (published by Wrox Press Ltd.)

Other related resources:

- _JAXP Tutorial_ ([https://jaxp.dev.java.net/](https://jaxp.dev.java.net/))
- [http://xml.apache.org](http://xml.apache.org/) contains information on the Apache Xerces XML parser and the Apache Xalan XSLT processor.
- _XSL Transformations (XSLT) Version 1.0_ ([http://www.w3.org/TR/xslt](http://www.w3.org/TR/xslt))
- _Working With XML_ ([http://java.sun.com/xml/tutorial_intro.html](http://java.sun.com/xml/tutorial_intro.html))
- _XML From the Inside Out_ ([http://xml.com](http://xml.com/)) is a great resource of XML-related information.
- _XML Schema_ ([http://www.w3.org/XML/Schema](http://www.w3.org/XML/Schema))
- Mulberry Technologies, Inc. ([http://www.mulberrytech.com](http://www.mulberrytech.com/))
- _Security in Java 2 SDK 1.2_ ([http://java.sun.com/docs/books/tutorial/index.html](http://java.sun.com/docs/books/tutorial/index.html))

[Next](https://developer.apple.com/library/archive/documentation/WebObjects/XML_Serialization/Introduction/Introduction.html)

