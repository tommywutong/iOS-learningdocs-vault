---
title: 'Using libxml2 for XML parsing and XPath queries in Cocoa | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/10/using-libxml2-for-parsing-and-xpath.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:13c137edad549ffc'
translated: false
---

> 原文：[Using libxml2 for XML parsing and XPath queries in Cocoa | Cocoa with Love](https://www.cocoawithlove.com/2008/10/using-libxml2-for-parsing-and-xpath.html)　·　Cocoa with Love (Matt Gallagher)

NSXMLDocument is the normal tree-based XML parser in Cocoa. But if you're writing for the iPhone, this class isn't available. Even on the Mac, sometimes you want tree-based parsing without the full overhead of NSXMLDocument. Here's how to use libxml2 to perform tree-based parsing in a Cocoa-friendly way.

## Introduction

`NSXMLDocument` is an excellent XML parser and XML document generator. Sadly, Apple have chosen not to include it in the current iPhone SDK. Apple instead recommend `NSXMLParser` on the iPhone.

Personally, I don't like the "event-driven" parsing of `NSXMLParser`. For the types of project I find myself writing, it is time-consuming and fiddly. I also like throwing HTML at my XML parsers and `NSXMLParser` (which is a strict, non-correcting parser) requires that HTML be cleaned-up first (using libtidy or similar), which eliminates much of the performance gain from this type of parsing anyway.

Fortunately, libxml2 exists on the iPhone and we can use it to perform much of the same parsing that `NSXMLDocument` performs for us on the Mac.

[Other programmers](http://blogs.newsgator.com/newsgator_widget_blog/2008/10/netnewswire-iph.html) have noted that libxml2 can be faster and more memory efficient than `NSXMLDocument` on the Mac, so there may be reasons to use libxml2 directly, even when `NSXMLDocument` is available.

## Downside to libxml2

libxml2 itself is a fairly simple, clean library but the [official documentation](http://xmlsoft.org/) is famously confusing. The documentation is really just a slightly commented version of the header files — not a great way to learn. Being pure C, the structure and style of the declarations and the datatypes used are also a long way from what is normally expected in Cocoa.

If you want to use libxml2 in Cocoa, you'll want a wrapper around it.

## Proposed solution

Reflecting the manner in which I use XML, my solution will have two functions declared as follows:

```objc
NSArray *PerformXMLXPathQuery(NSData *document, NSString *query);
NSArray *PerformHTMLXPathQuery(NSData *document, NSString *query);
```

For an entire XML document, contained in the `NSData` object "`document`", this function executes the XPath query in the `NSString` "`query`" and returns an `NSArray` of `NSDictionary` node objects for nodes that match the query.

The only difference between the two listed functions is that the the first expects proper XML data and the second expects HTML data.

Each result in the array of nodes returned will be an `NSDictionary` with the following structure:

- **nodeName** — an `NSString` containing the name of the node
- **nodeContent** — an `NSString` containing the textual content of the node
- **nodeAttributeArray** — an `NSArray` of `NSDictionary` where each dictionary has two keys: _attributeName_ (`NSString`) and _nodeContent_ (`NSString`)
- **nodeChildArray** — an `NSArray` of child nodes (same structure as this node)

Any of these fields may absent if not found in the libxml2 result.

If you don't know how or why to use an XPath query on an XML document, please look at my previous post titled [A Cocoa application driven by HTTP data](https://www.cocoawithlove.com/2008/09/cocoa-application-driven-by-http-data.html) which shows how XPath queries can be used to extract specific sections of data from an HTML document.

## The implementation

Download the full solution here: [XPathQuery.m and XPathQuery.h as a 2kb zip file](https://www.cocoawithlove.com/assets/objc-era/XPathQuery.zip).

The implementation is very straightforward. The entry point looks like this:

```objc
NSArray *PerformXMLXPathQuery(NSData *document, NSString *query)
{
    xmlDocPtr doc;
    
    /* Load XML document */
    doc = xmlReadMemory(
        [document bytes], [document length], "", NULL, XML_PARSE_RECOVER);
    
    if (doc == NULL)
    {
        NSLog(@"Unable to parse.");
        return nil;
    }
    
    NSArray *result = PerformXPathQuery(doc, query);
    xmlFreeDoc(doc); 
    
    return result;
}
```

The only real difference in the `PerformHTMLXPathQuery` version is that it calls `htmlReadMemory` instead of `xmlReadMemory`.

The query itself is then performed in an internal function common to both entry functions:

```objc
NSArray *PerformXPathQuery(xmlDocPtr doc, NSString *query)
{
    xmlXPathContextPtr xpathCtx; 
    xmlxpathObjectPtr xpathObj; 

    /* Create XPath evaluation context */
    xpathCtx = xmlXPathNewContext(doc);
    if(xpathCtx == NULL)
    {
        NSLog(@"Unable to create XPath context.");
        return nil;
    }
    
    /* Evaluate XPath expression */
    xmlChar *queryString =
        (xmlChar *)[query cStringUsingEncoding:NSUTF8StringEncoding];
    xpathObj = xmlXPathEvalExpression(queryString, xpathCtx);
    if(xpathObj == NULL) {
        NSLog(@"Unable to evaluate XPath.");
        return nil;
    }
    
    xmlNodeSetPtr nodes = xpathObj->nodesetval;
    if (!nodes)
    {
        NSLog(@"Nodes was nil.");
        return nil;
    }
    
    NSMutableArray *resultNodes = [NSMutableArray array];
    for (NSInteger i = 0; i &lt; nodes-&gt;nodeNr; i++)
    {
        NSDictionary *nodeDictionary = DictionaryForNode(nodes->nodeTab[i], nil);
        if (nodeDictionary)
        {
            [resultNodes addObject:nodeDictionary];
        }
    }

    /* Cleanup */
    xmlXPathFreeObject(xpathObj);
    xmlXPathFreeContext(xpathCtx); 
    
    return resultNodes;
}
```

The work done is here simple: create the working space for the XPath query on the document, evalute the XPath query, get all the nodes from the result and use the `DictionaryForNode` function to parse them into our `NSDictionary` objects, and clean up when done.

The implementation of the `DictionaryForNode` function is the only one I haven't shown. If you [download the full solution](https://www.cocoawithlove.com/assets/objc-era/XPathQuery.zip), you can see how it's done. It's a bit bigger than I want to dump into my blog's text but it really just traverses the libxml2 `xmlNodePtr` structures, getting the fields it needs and converting them to `NSString`, `NSArray` and `NSDictionary` as appropriate.

## Setting up your project file

You need to add libxml2.dylib to your project (don't put it in the Frameworks section). On the Mac, you'll find it at `/usr/lib/libxml2.dylib` and for the iPhone, you'll want the `/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.0.sdk/usr/lib/libxml2.dylib` version.

Since libxml2 is a .dylib (not a nice friendly .framework) we still have one more thing to do. Go to the Project build settings (Project-\>Edit Project Settings-\>Build) and find the "Search Paths". In "Header Search Paths" add the following path:

```objc
$(SDKROOT)/usr/include/libxml2
```

## Conclusion

This solution will let you get the results of an XPath query on the iPhone in nice Cocoa friendly objects.

I've only tested this on textual data — I don't know how it will behave on XML CDATA.

If you don't want an XPath query (for example: if you need the whole document) you can either run the query "/" to get the root node or drop the `PerformXPathQuery` function and instead run `DictionaryForNode` on the `children` of the `xmlDocPtr` or even cast the `xmlDocPtr` to an `xmlNodePtr` and run it directly on that (in either case, pass `NULL` in as the `parentResult` to `DictionaryForNode`).
