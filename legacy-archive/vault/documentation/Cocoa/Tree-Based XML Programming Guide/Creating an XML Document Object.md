---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/Articles/CreatingXMLDoc.html
archived_at: '2026-07-15T07:16:59.395060Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tree-Based XML Programming Guide](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)


[Next](Writing%20XML%20From%20NSXML%20Objects.md)[Previous](The%20Data%20Model%20of%20NSXML.md)

# Creating an XML Document Object

You can create an object representing an XML document—that is, an instance of NSXMLDocument—in one of two general ways. Using NSXML, you can either parse an XML source and create a tree structure representative of the contents, or you can create an XML document programmatically.

The NSXMLDocument class lets you create a document instance from XML markup text in one of several forms: as a string object, as an NSData object, and as a URL-designated file (remote or local). The following initializers of NSXMLDocument (corresponding to these forms) also include parameters for input-handling options and for obtaining information about initialization errors:

- `initWithXMLString:options:error:`
- `initWithData:options:error:`
- `initWithContentsOfURL:options:error:`

Listing 1 shows how you might create an NSXMLDocument instance from an absolute path to a local XML file.

__Listing 1__  Creating a document from a file URL (local file)

```objc
- (void)createXMLDocumentFromFile:(NSString *)file {
    NSXMLDocument *xmlDoc;
    NSError *err=nil;
    NSURL *furl = [NSURL fileURLWithPath:file];
    if (!furl) {
        NSLog(@"Can't create an URL from file %@.", file);
        return;
    }
    xmlDoc = [[NSXMLDocument alloc] initWithContentsOfURL:furl
            options:(NSXMLNodePreserveWhitespace|NSXMLNodePreserveCDATA)
            error:&err];
    if (xmlDoc == nil) {
        xmlDoc = [[NSXMLDocument alloc] initWithContentsOfURL:furl
                    options:NSXMLDocumentTidyXML
                    error:&err];
    }
    if (xmlDoc == nil)  {
        if (err) {
            [self handleError:err];
        }
        return;
    }

    if (err) {
        [self handleError:err];
    }
}
```

If initialization fails, the NSXMLDocument `init` method directly returns `nil` and most likely returns by indirection an NSError reporting a parsing or connection error. If failure is due to a parsing error, you can try to recover (as in Listing 1) by initializing the document with the `NSXMLDocumentTidyXML` option; this option reformats the document prior to parsing to ensure that it is well-formed. However, it does have side effects, such as removing leading and trailing spaces; see the NSXMLDocument reference documentation for details.

If an NSXMLDocument `init` method indirectly returns an NSError object in its third parameter, you can display an alert dialog to inform the user about the error. However, NSError objects created for parsing errors or warnings might not contain much helpful information. Most NSError objects encapsulate errors or warnings emitted by the parser when documents are not well-formed; these can also be connection errors from attempts to access XML at a remote locations using `initWithContentsOfURL:options:error:`.

You set initialization options in the second parameter of the three NSXMLDocument initializers discussed above; if you want to specify multiple options, use a bitwise-OR expression. The initialization options cover three categories of input-handling:

- _Preservation_. The `enum` constants beginning with `NSXMLNodePreserve` support document fidelity. They allow you to ensure that aspects of the string XML input—for instance, quoting style of attribute values, CDATA sections, attribute and namespace order—remain the same when XML text is written out from the NSXMLDocument object. If you do not specify a preservation option for an aspect, NSXMLDocument handles it in a predetermined manner. For example, when NSXMLDocument reads in and parses an XML document, it normally strips white-space characters used in formatting (including tabs and carriage returns); however, if you specify `NSXMLNodePreserveWhitespace` these characters are kept hidden in the internal representation of the XML document. (“Hidden” means the white-space characters are retained for the output of the document, but are not visible within the tree representation.) Note that white space in text nodes is always preserved, and is not affected by the `NSXMLNodePreserveWhitespace` option.
- _Tidiness_. The `NSXMLDocumentTidyHTML` and `NSXMLDocumentTidyXML`  options correct any malformed parts of a source HTML or XML document, respectively, before creating the internal representation of the document. Tidying maintains document content, but not necessarily maintain white space or the order of constructs in the document. Entities and character references are always resolved to their text or unicode character.If the source is HTML and `NSXMLDocumentTidyHTML` is specified, NSXMLDocument attempts to convert it to XHTML; corrections take into account the HTML context. If the source is XML and `NSXMLDocumentTidyXML` is specified, NSXMLDocument attempts to fix any defects to make it well-formed.
- _Validation_. The `NSXMLDocumentValidate` option validates the source XML document against its associated schema. That schema can be defined through a DTD (internal or external) or XML Schema. The validator reports reasons for document invalidity indirectly through the NSError parameter. To validate against an XML Schema, you must identify the schema document through a combination of namespace, `xmlns:xsi`, and `xsi:schemaLocation` attribute declarations in the root element. The URI value of the namespace must match one of the values in the location-namespace tuples in the `xsi:schemaLocation` declaration. Here is an example:

```
<MyRootElement xmlns="http://www.example.com/foo"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation=
        "http://www.example.com/foo http://www.example.com/foo.xsd
        http://www.w3.org/1999/xhtml http://www.w3.org/1999/xhtml.xsd">
```

  For information on how you specify the location of schema definitions on the web, see the W3C XML Schema recommendation ([http://www.w3.org/TR/xmlschema-1/](http://www.w3.org/TR/xmlschema-1/)). A schema should be physically installed on an OS X system at `/System/Library/Schemas/`_elementName_`.xsd`.
- _XInclude_. If the `NSXMLDocumentXInclude` option is specified, the parser replaces `xsi:include` elements that refer to other XML documents (or parts of documents) with the referenced content. By default this option is turned on so your application can query and edit the nodes that define inclusions.

These `enum` constants are defined in `NSXMLNodeOptions.h`. For specific information about the initialization options, check the reference documentation for NSXMLDocument.

Sometimes you might want to create an XML document that is entirely new, without there being any original source file or website page. You may want to manipulate all of the nodes in a tree structure—adding, removing, and relocating them—and let NSXML take care of the formatting details when the document is written to a file.

The `initWithRootElement:` initializer of NSXMLDocument allows you to do this. An NSXMLDocument object has two defining kinds of data: a set of document-global attributes and a root element. Once you have the root element you can construct the rest of the document’s tree representation by adding child nodes of various types to parent nodes at various levels.

Listing 2 shows an example of creating a brand-new XML document object.

__Listing 2__  Creating an NSXMLDocument instance representing a new document

```
NSXMLElement *root =
    (NSXMLElement *)[NSXMLNode elementWithName:@"addresses"];
NSXMLDocument *xmlDoc = [[NSXMLDocument alloc] initWithRootElement:root];
[xmlDoc setVersion:@"1.0"];
[xmlDoc setCharacterEncoding:@"UTF-8"];
[root addChild:[NSXMLNode commentWithStringValue:@"Hello world!"]];
```

This fragment of code uses methods of NSXMLDocument to set the `version` and `encoding` attributes of the XML declaration of the document. You could also set the standalone, URI, and MIME-type attributes using the corresponding NSXMLDocument “setter” methods. You may associate a Document Type Definition with the NSXMLDocument object through the `setDTD:` method. NSXMLDocument also allows you to specify the document’s output format (using `setDocumentContentKind:`) as HTML, XHTML, text, or (the default) XML. For example, the following lists the different handlings of the `<br>` element:

- XML: `<br></br>`
- XHTML: `<br />`
- HTML: `<br>`
- Plain text: nothing

Once you create an XML document object and set its attributes, you can start adding content to it—that is, the elements, attributes, and other nodes that make up an XML document—through the appropriate methods of NSXMLElement and NSXMLNode.

If the XML document has a schema associated with it—defined either with a DTD or XML Schema —you might want to validate the document periodically. To validate a document, send the `validateAndReturnError: ` message to the NSXMLDocument object. If the operation is not valid, the method returns `NO`; the reasons for invalidity are returned by indirection in the method’s NSError parameter.

[Next](Writing%20XML%20From%20NSXML%20Objects.md)[Previous](The%20Data%20Model%20of%20NSXML.md)

