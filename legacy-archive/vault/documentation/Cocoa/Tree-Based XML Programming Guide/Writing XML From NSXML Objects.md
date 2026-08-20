---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/Articles/WritingXML.html
archived_at: '2026-07-15T07:17:08.716005Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tree-Based XML Programming Guide](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)


[Next](Traversing%20an%20XML%20Tree.md)[Previous](Creating%20an%20XML%20Document%20Object.md)

# Writing XML From NSXML Objects

All NSXML objects can emit a textual representation of themselves as XML markup. In addition, NSXMLDocument objects can write themselves out as complete XML or XHTML documents. NSXML provides different sets of methods and options (as `enum` constants) for both writing out the contents of NSXMLNode and NSXMLDocument objects. It also offers methods for performing XSLT transformations on XML documents.

Perhaps the most common pattern of an application that processes XML is something like the following:

1. Read an XML document from a file or website, converting it to an internal tree structure.
2. Modify, add, and delete nodes in the tree.
3. From the objects in the tree, write a new or updated XML document to a file or website.

Two methods of the NSXMLDocument class help you with the final step, `XMLData` and `XMLDataWithOptions:`. As the method names imply, both methods return an NSData object. The character data of the output is encoded based on the encoding specified as an attribute in the document’s XML declaration. (If that doesn’t exist, NSXML uses UTF-8 as a default encoding.)

`XMLData` simply invokes `XMLDataWithOptions:` with an argument of `NSXMLNodeOptionsNone`, requesting no output options. The latter method allows you to specify the following `enum`-constant options:

- `NSXMLNodePrettyPrint`—Makes the XML output more human-readable by, for example, inserting carriage returns and indenting nested elements.
- `NSXMLDocumentIncludeContentTypeDeclaration`—Includes a content type declaration for HTML or XHTML output.

If you want to specify multiple constants, use a bitwise-OR expression.

Listing 2 shows how you might invoke the `XMLDataWithOptions:` method in the `writeToFile:ofType:` method of an NSDocument subclass.

__Listing 1__  Writing an XML document to a file (NSDocument subclass)

```objc
- (BOOL)writeToFile:(NSString *)fileName ofType:(NSString *)type {

    NSData *xmlData = [xmlDoc XMLDataWithOptions:NSXMLNodePrettyPrint];
    if (![xmlData writeToFile:fileName atomically:YES]) {
        NSBeep();
        NSLog(@"Could not write document out...");
        return NO;
    }
    return YES;
}
```


Occasionally you might want to have specific nodes or branches of an XML tree express themselves as XML markup rather than the entire document. For example, an application could walk through a large XML document looking for nodes matching specific criteria, and then construct a smaller XML document from the output of these nodes.

The primary NSXMLNode methods that you use for this purpose are `XMLString` and `XMLStringWithOptions:`. The former method simply invokes the latter specifying no output options (`NSXMLNodeOptionsNone`). Aside from being invokable on any NSXMLNode object (including NSXMLDocument objects), what distinguishes these methods from their NSXMLDocument counterparts is that they return a string object (NSString) rather than a data object (NSData).

When you send one of these messages to an NSXMLNode object that can (and does) have children—specifically, document, element, or document-type declaration nodes—the effect is recursive. All descendants of the node object print themselves out in document order.

`XMLStringWithOptions:` permits only one of the output options available to the NSXMLDocument method `XMLDataWithOptions:` — `NSXMLNodePrettyPrint`— for inserting whitespace to improve XML readability.

The method in Listing 2 gets the string representation of an XML document and uses that for the content of a text view and a web view. (WebView and WebFrame, which are referenced in the following two code listings, are classes of the Web Kit framework.)

__Listing 2__  Creating a second XML document using XMLStringWithOptions:

```objc
- (IBAction)reloadPreview:(id)sender {
    if (xmlDocument) {
        NSString *displayString = [xmlDocument
            XMLStringWithOptions:NSXMLNodePrettyPrint];
        [previewTextView setString:displayString];
        [[previewWebView mainFrame] loadHTMLString:displayString
            baseURL:[self baseDocURL]];
    }
}
```

You can obtain XML markup text that is in canonical form by sending any NSXMLNode object the message `canonicalXMLStringPreservingComments:`. By converting an XML document or node to canonical form you can determine if it is logically equivalent to another XML document (or node) in canonical form—which is perhaps the same document after minor changes are made to it. Putting XML in canonical form involves various conversions and “normalizations,” such as resolving character and entity references, converting empty element tags to start-end pairs, and inserting default attribute values. See the reference documentation for the NSXMLNode class for a fuller description of `canonicalXMLStringPreservingComments:`.

NSXML includes support for XSLT. With XSLT you can apply a set of template rules and patterns to a source XML document and thereby transform that document into another XML document or into an HTML, RTF, or plain-text document. Three NSXMLDocument methods are the interface to XSLT processing:

- `- (id)objectByApplyingXSLT:(NSData *)xslt arguments:(NSDictionary *)arguments error:(NSError **)error`
- `- (id)objectByApplyingXSLTString:(NSString *)xslt arguments:(NSDictionary *)arguments error:(NSError **)error`
- `- (id)objectByApplyingXSLTAtURL:(NSURL *)xsltURL arguments:(NSDictionary *)arguments error:(NSError **)error`

These methods return transformed XML or HTML documents in the form of an NSXMLDocument object; they return RTF or plain-text documents as NSData objects.

The first of these methods takes the XSLT code as a data object, the second as a string object, and the third takes a URL identifying a source of XSLT code. Listing 3 illustrates the usage of the third method. In this case, the file containing the XSLT code is stored as a nonlocalized resource of the application. The method gets the path to the XSLT file, converts the path to a URL, and then sends the `objectByApplyingXSLTAtURL:arguments:error:` method to an NSXMLDocument object. It gets the HTML contents of the resulting document object using `XMLString`; it then loads that string into a WebView object from which it is printed.

__Listing 3__  Transforming an XML document to HTML using XSLT

```objc
- (IBAction)printDocument:(id)sender {
    NSError *err=nil;
    // webView is an off-screen WebView (ivar)
    WebFrame *frame = [webView mainFrame];

    // find XSLT code
    NSString *xsltPath = [[NSBundle mainBundle]
        pathForResource:@"addresses_transform" ofType:@"xml"];
    if (!xsltPath)
        return;

    // transform through XSLT
    NSXMLDocument  *printDoc = (NSXMLDocument *)[xmlDoc
        objectByApplyingXSLTAtURL:[NSURL fileURLWithPath:xsltPath]
        arguments:nil  // no extra XSLT parameters needed
        error:&err];
    if (err) {
        [self handleError:err];
        if (!printDoc) return;
    }
    // put in WebFrame and print
    [frame loadHTMLString:[printDoc XMLString] baseURL:nil];
    [webView print:self];
}
```

Many online tutorials on XSLT are available, including one from W3Schools ([http://www.w3schools.com/xsl/](http://www.w3schools.com/xsl/)). You can search the web to find other sources of information on XSLT.

[Next](Traversing%20an%20XML%20Tree.md)[Previous](Creating%20an%20XML%20Document%20Object.md)

