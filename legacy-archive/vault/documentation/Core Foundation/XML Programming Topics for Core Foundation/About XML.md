---
title: XML Programming Topics for Core Foundation
apple_id: 10000138i
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreFoundation
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFXML/Concepts/About.html
archived_at: '2026-07-15T07:22:59.944776Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [XML Programming Topics for Core Foundation](Introduction%20to%20XML%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Core%20Foundation%20XML%20Parser.md)[Previous](Introduction%20to%20XML%20Programming%20Topics%20for%20Core%20Foundation.md)

# About XML

Extensible Markup Language, or XML, is a scripting language for representing structured data in a text file. The structured data you want to represent using XML can be virtually anything—address books, configuration parameters, spreadsheets, Web pages, financial transactions, technical drawings, and so on. XML defines a set of rules for designing text formats for such data. By storing data in a structured text format, XML allows you to look at data without the program that produced it. XML files are easy for computers to generate and read, they are unambiguous, and they avoid common pitfalls of text data formats, such as lack of extensibility, lack of support for internationalization and localization, and platform dependency.

XML is a complex subject whose thorough treatment is beyond the scope of this topic. Developers new to XML concepts can find the XML 1.0 specification and supporting material at the website maintained by the World Wide Web Consortium at `http://www.w3c.org/XML`. The Organization for the Advancement of Structured Information Standards hosts two excellent sites on XML at `http://www.xml.org/` and `http://www.oasis-open.org/cover/`. There is also a great deal of information about XML and its various uses at the following corporate sites: `http://www.ibm.com/developer/xml/`, `http://msdn.microsoft.com/xml/default.asp`, and `http://java.sun.com/xml/`.

Like HTML, XML is based on the Standard Generalized Markup Language, or SGML. This common heritage renders XML familiar in look and feel to those accustomed to HTML. Unlike HTML, though, XML syntax requires the use of matching start and end tags, such as `<string>` and `</string>`, to demarcate logical sections of a document or data sets. A unit of information enclosed by tags is called an _element_. As a shortcut, if an element has no content between its start and end tags, the tags can be merged into a single tag that ends with `“/>”`, such as `<true/>`. This simple syntax is easy to process by a computer, with the added benefit of remaining understandable to humans.

The best way to illustrate the basic features of XML is with a simple example. The document shown in Listing 1 contains the XML representation of a customer object that might have been exported from a customer database.

__Listing 1__  A simple XML document

```xml
<?xml version="1.0" encoding="UTF-8"?>
<customer>
    <name>Jane Doe</name>
    <address region="USA">
        <street>6236 Nicolet Rd</street>
        <city>Richmond</city>
        <state>VA</state>
        <postal>23225</postal>
    </address>
    <birthday>
        <month>10</month>
        <day>11</day>
        <year>1949</year>
    </birthday>
</customer>
```

This example document contains the basic XML structural features. First there is the required prolog—also called the XML declaration—containing XML version and character encoding information. (In the absence of an encoding attribute, Core Foundation assumes UTF-8.) The remainder of the document is simply the listing of elements that constitute the customer information.

In computing terms, a parser is a program that takes input in the form of sequential instructions, tags, or some other defined sequence of tokens, and breaks them up into easily manageable parts. An XML parser is designed to read and, in a sense, interpret XML documents. As it executes, the parser recognizes and responds to each XML structure it encounters by taking some specified action based on the structure type. Many XML parsers, called tree-based parsers, convert an XML document into a tree structure that reflects the structural hierarchy of the XML data. This tree is then made available to your application, which is free to interpret and modify the data as appropriate. Other parsers are event-driven, and report to their client each XML construct they encounter.

In addition to being event-driven or tree-based, XML parsers can be validating or nonvalidating. Validating parsers check a document’s contents against a set of specific rules stating what elements are allowed in a document and in what order they must appear. These rules appear in an XML document either as an optional XML structure called a document type definition, or DTD, or as an XML Schema. Nonvalidating parsers are smaller and faster, but they don’t check documents against the DTD; they only check if the document is structurally well-formed.

[Next](Core%20Foundation%20XML%20Parser.md)[Previous](Introduction%20to%20XML%20Programming%20Topics%20for%20Core%20Foundation.md)

