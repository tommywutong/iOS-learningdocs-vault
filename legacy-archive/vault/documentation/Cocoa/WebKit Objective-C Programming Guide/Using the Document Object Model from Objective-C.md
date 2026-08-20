---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/DOMObjCBindings.html
archived_at: '2026-07-15T07:14:50.294250Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Using%20the%20Document%20Object%20Model%20Extensions.md)[Previous](Using%20Undo%20When%20Editing.md)

# Using the Document Object Model from Objective-C

The Document Object Model API implements the Level 2 Document Object Model (DOM) specification, developed by the World Wide Web Consortium. This specification provides a platform and language-neutral interface that allows programs and scripts to dynamically access and change the content, structure and style of a document —usually HTML or XML—by providing a structured set of objects that correspond to the document’s elements.

The intention of the DOM Objective-C API is to conform to—as close as technically possible—the W3C DOM specification. Therefore, standard Cocoa conventions such as method naming, argument titling, and exception handling may not be reflected in this API. Following a few conventions discussed in this article, you can derive the DOM Objective-C API from the specification. This article also discusses the differences between the DOM specification and DOM Objective-C API.

WebKit extensions to the DOM specification are covered in [Using the Document Object Model Extensions](Using%20the%20Document%20Object%20Model%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytembxfvbeeq2kjjeegsa). Refer to _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_ for more information on the DOM specification.

The DOM specification is written in Interface Definition Language (IDL) files available at the W3C web site. Links to them have been provided in the list that follows. The Objective-C DOM API is defined by header files in the WebKit framework, located at: `/System/Library/Frameworks/WebKit.framework`. Here is a list of the DOM specification’s IDL files and their associated Objective-C header files:

| W3C DOM IDL file | WebKit DOM header file |
| --- | --- |
| [dom.idl](http://www.w3.org/TR/DOM-Level-2-Core/idl/dom.idl) | `DOMCore.h` |
| [views.idl](http://www.w3.org/TR/DOM-Level-2-Views/idl/views.idl) | `DOMViews.h` |
| [events.idl](http://www.w3.org/TR/DOM-Level-2-Events/idl/events.idl) | `DOMEvents.h` |
| [html2.idl](http://www.w3.org/TR/DOM-Level-2-HTML/idl/html2.idl) | `DOMHTML.h` |
| [stylesheets.idl](http://www.w3.org/TR/DOM-Level-2-Style/idl/stylesheets.idl) | `DOMStylesheets.h` |
| [css.idl](http://www.w3.org/TR/DOM-Level-2-Style/idl/css.idl) | `DOMCSS.h` |
| [traversal.idl](http://www.w3.org/TR/DOM-Level-2-Traversal-Range/idl/traversal.idl) | `DOMTraversal.h` |
| [ranges.idl](http://www.w3.org/TR/DOM-Level-2-Traversal-Range/idl/ranges.idl) | `DOMRange.h` |

Two other header files are included in the Document Object Model API. `DOM.h` is a convenience header file that merely includes all of the other DOM header files. `DOMExtensions.h` defines additions that are not specified by the DOM specification. Use the extensions to help your DOM methods interact with the rest of WebKit, and to use some of WebKit’s higher abilities such as HTML editing. More information is available in the [Using the Document Object Model Extensions](Using%20the%20Document%20Object%20Model%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytembxfvbeeq2kjjeegsa) article.

The interfaces specified by the DOM IDL files are mapped to Objective-C classes. The names of interfaces are unchanged when the specification does not conflict with the namespaces of Objective-C, Java, or other common languages. For example, the `DOMImplementation` interface in the DOM Core IDL is reflected by the same name in the Objective-C `DOMCore` header file. Where namespaces conflict, the API prefixes the conflicting interface appropriately. For example, the DOM Core IDL’s `Node` interface appears as `DOMNode` in its Objective-C mapping.

This naming scheme also extends to constants. The API groups DOM constant lists into Objective-C `enum` types, and if a namespace conflict is present, the API prefixes them with an appropriate identifier. For example, the `ELEMENT_NODE` node type constant is reflected as `DOM_ELEMENT_NODE` in Objective-C.

Some names specified by the DOM specification may conflict with keywords or other reserved words in Objective-C. When this happens, they are given custom mappings and their Objective-C names must be inferred from the headers or from documentation. The API provides the custom mappings with appropriate names. For example, the two conflicting identifiers `id` and `name` (both Objective-C reserved words) are mapped to `idName` and `frameName`, respectively, and accurately reflect the intent of the specification.

Each Objective-C class derives, directly or indirectly, from the DOM root object `DOMObject`. This is an implementation detail that accommodates cross traffic between WebKit and the DOM. The hierarchy of interfaces as defined by the W3C specification is also maintained. For example, `DOMDocument` extends from `DOMNode` in the specification as well as in the API.

Method names are mapped into Objective-C directly from the specification with no namespace transition. However, methods with multiple arguments in the DOM specification do not specify labels for their arguments—this behavior carries on into the Objective-C methods. For example, the specification declares this method prototype:

```
Node insertBefore(in Node newChild, in Node refChild);
```

The Objective-C version is _not_, as you might expect, changed to something like:

```objc
- (DOMNode *)insertNewChild:(DOMNode *)newChild
                  BeforeOld:(DOMNode *)refChild
```

The actual Objective-C prototype is:

```objc
- (DOMNode *)insertBefore:(DOMNode *)newChild
                         :(DOMNode *)refChild
```

As you can see, this varies from typical Cocoa method-naming conventions. This is done for an important reason—to match the Document Object Model specification as closely as possible. But if you are a Cocoa developer new to the DOM, you may find the naming scheme confusing.

The API maps other objects to their appropriate equivalents. For example, it maps `DOMString` objects to `NSString`. All other types (such as `void`, `boolean,` `float`, and `unsigned long`) are mapped to their respective Objective-C types. Attributes which are both readable and writable are also given Cocoa-style get/set accessor methods. For example, the `DOMCore` IDL specifies this attribute:

```
attribute DOMString nodeValue;
```

Objective-C accesses this attribute using these methods:

```objc
- (NSString *)nodeValue;
- (void)setNodeValue:(NSString *)nodeValue;
```


The API also maps exceptions from the DOM specification to Objective-C. Methods that raise DOM exceptions also raise Objective-C exceptions (`NSException`), but because Objective-C exceptions are not part of a method interface as they are in the DOM specification, the exception class names are mapped to string constants. The main exception classes are raised as `DOMException`, `DOMEventException`, and `DOMRangeException`, and can alert you with any number of exception codes. See `DOMCore.h`, `DOMEvents.h`, and `DOMRange.h` for the codes.

[Next](Using%20the%20Document%20Object%20Model%20Extensions.md)[Previous](Using%20Undo%20When%20Editing.md)

