---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/Articles/CreateModifyDTDs.html
archived_at: '2026-07-15T07:16:58.884245Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tree-Based XML Programming Guide](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)


[Next](Binding%20NSXML%20Objects%20to%20a%20User%20Interface.md)[Previous](Handling%20Attributes%20and%20Namespaces.md)

# Creating and Modifying Document Type Definitions

With the DTD classes of NSXML you can create a Document Type Definition (DTD) or process an existing one, converting its string representation into a shallow tree structure. You can add nodes representing DTD declarations to the tree, remove nodes from it, or change the values of those declarations. Finally, you can write out the created or modified DTD “inline” with its XML string representation. The DTD classes are NSXMLDTD and NSXMLDTDNode.

Usually DTDs in NSXML are internal and are set as a property of an NSXMLDocument object. When it processes an XML document, NSXML creates a DTD tree structure and attaches it to a document but only if the DTD is internal. However, you can create a DTD programmatically and write it out to its own file (that is, an external DTD) using NSXML.

When NSXML processes an existing source of XML and the `NSXMLDocumentValidate` input option is specified, it validates the XML against an internal or external DTD (see [Creating a Document Object From Existing XML](Creating%20an%20XML%20Document%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjvfu4tmobugm)). However, validation is a separate process from the creation of the tree structure representing a DTD. (You can also dynamically validate an NSXMLDocument against its DTD by sending the `validateAndReturnError:` message to the document object.)

If you read and process an existing source of XML using the NSXML interfaces, and that XML includes an internal DTD, a shallow (two-level) tree is created to represent the DTD. At the root of this tree is an instance of the NSXMLDTD class; this object has children consisting of NSXMLDTDNodeDTD nodes objects, each representing the declaration for an element, entity, attribute-list, or notation in the DTD. (The children may also include NSXMLNode objects representing comments and processing instructions found in the source DTD.) As it parses declarations and creates DTD nodes, NSXML sets the kind (`NSXMLNodeKind`) and DTD subkind (`NSXMLDTDNodeKind`) of each created node.

You can also create a standalone NSXMLDTD object from an external DTD with the `initWithContentsOfURL:options:error:` or `initWithData:options:error: ` methods. Then you can associate this DTD object with an XML document object through the `setDTD:` method of the NSXMLDocument class.

The created DTD tree is associated with the XML document as a property. In programmatic terms, this means that you can access the NSXMLDTD object (and its NSXMLDTDNode children) by sending the NSXMLDocument object a `DTD` message. Once you have accessed the NSXMLDTD object you can add children, remove children, change declarations, and so on (see [Modifying a DTD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimbsfu4tmobzgy)).

You can also create an entirely new DTD tree programmatically. To do so, complete the following steps:

1. Create an instance of the NSXMLDTD class.
2. If the DTD is to be external, set its system ID (`setSystemID: `) and, if necessary, its public ID (`setPublicID:`).
3. Create instances of the NSXMLDTDNode class for each declaration you want in the DTD. To create these objects you can use the `initWithXMLString: ` method of the NSXMLDTDNode class, the NSXMLNode class method `DTDNodeWithXMLString: `, or the NSXMLNode `initWithKind:`method. The first two of these methods take a string equivalent to a DTD declaration, for example

```
<!ELEMENT name (#PCDATA)>
```

   (If you use the `initWithKind:` method, you must set the string or object value of the DTD node appropriately—see [Modifying a DTD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimbsfu4tmobzgy).) Each created DTD node is automatically assigned a node kind (if one is not explicitly assigned) and a DTD subkind, based on the declaration parsed. You may reassign the subkind with the `setDTDKind: ` method.
4. Add each created NSXMLDTDNode object to the NSXMLDTD object as a child (using `addChild:` or `insertChild:atIndex: `).

   For more on creating, adding, and otherwise manipulating children of an NSXMLDTD object, see [Modifying a DTD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimbsfu4tmobzgy).

Once you have created a DTD, you must decide whether it is to be an internal or external DTD. If an internal DTD, attach it to the NSXMLDocument object using the `setDTD:` method. When you write the XML document out, the DTD string representation appears inline in the XML. If the DTD is external, don’t attach it to an NSXMLDocument but write it out separately, as illustrated in Listing 1.

__Listing 1__  Creating an external DTD

```objc
- (void)createExternalDTD {
    NSXMLDTD *theDTD = [[[NSXMLDTD alloc] init] autorelease];
    [theDTD setSystemID:@"http://www.boggle.com/DTDs/index.html"];
    NSXMLDTDNode *attrNode = [[[NSXMLDTDNode alloc] initWithXMLString:
        @"<!ATTLIST phone location (home | office | mobile) 'home'>"]
        autorelease];
    NSXMLDTDNode *elemNode = [[[NSXMLDTDNode alloc] initWithXMLString:
        @"<!ELEMENT address (street1, street2, city, state, zip)>"]
        autorelease];
    NSXMLDTDNode *entNode = [[[NSXMLDTDNode alloc] initWithXMLString:
        @"<!ENTITY % children 'first, middle, last'>" ]
         autorelease];
    NSString *thePath = [self savePath]; // custom method
    [theDTD addChild:attrNode];
    [theDTD addChild:elemNode];
    [theDTD addChild:entNode];
    [[theDTD XMLString] writeToFile:thePath atomically:YES];
}
```


As with modifying an XML document, you can modify a DTD in two general ways. You can alter the structure of the tree representing the DTD by adding, removing, and replacing nodes. And you can change the value of DTD nodes, essentially modifying the declaration.

When you change the value of NSXMLDTDNode objects using `setStringValue:` or `setObjectValue:` what changes depends on the type of declaration:

- If the type is mixed or an element declaration, the validation string is changed. For example, in the declarations

```
<!ELEMENT title (#PCDATA)*>
<!ELEMENT item (head, (p | list | note))>
```

  `(#PCDATA)*` and `(head, (p | list | note))` are validation strings.
- If the type is an entity, the entity value changes. In the declaration

```
<!ENTITY foo “bar”>
```

  `“bar”` is the entity value.
- If the type is an attribute-list declaration, the default value changes. In the declaration

```
<!ATTLIST bar foo (moo | boo) “moo”>
```

  `“moo”` is the default value.
- Notations have no changeable value.

The NSXMLDTD methods for manipulating the structure of a DTD are the following:

- `- (void)addChild:(NSXMLNode *)child`
- `- (void)setChildren:(NSArray *)children`
- `- (void)insertChild:(NSXMLNode *)child atIndex:(unsigned)index`
- `- (void)insertChildren:(NSArray *)children atIndex:(unsigned)index`
- `- (void)removeChildAtIndex:(unsigned)index`
- `- (void)replaceChildAtIndex:(unsigned)index withNode:(NSXMLNode *)node`

These methods, which are identical in signature and purpose to methods of NSXMLDocument and NSXMLElement, have unambiguous usages. All of them except `removeChildAtIndex:` require you to create an NSXMLDTDNode object first (or detach an existing NSXMLDTDNode object first). As briefly discussed in [Creating a DTD](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimbsfu4tonrwha), you typically create an NSXMLDTDNode object with the `initWithXMLString:` method or the `DTDNodeWithXMLString:` or `initWithKind:` methods of the NSXMLNode class. The argument of the first two methods is an NSString object representing a DTD declaration, as shown in this example:

```
    NSXMLDTDNode *attrNode = [[[NSXMLDTDNode alloc] initWithXMLString:
        @"<!ATTLIST phone location (home | office | mobile) 'home'>"]
        autorelease];
```

Note that you can also create and add children to an NSXMLDTD object that are NSXMLNode objects representing comments and processing instructions.

If you are implementing your own scheme for dynamic validation of XML, you need to know which DTD declaration governs the placement, form, and allowable values of a particular XML construct. The following convenience methods of NSXMLDTD provide you with that information:

- `- (NSXMLDTDNode *)entityDeclarationForName:(NSString *)name`
- `- (NSXMLDTDNode *)elementDeclarationForName:(NSString *)name`
- `- (NSXMLDTDNode *)attributeDeclarationForName:(NSString *)name elementName:(NSString *)elementName`
- `- (NSXMLDTDNode *)notationDeclarationForName:(NSString *)name`

You provide these methods with the name of an entity, element, notation, and attribute (plus, for attributes, the element name), and they return the NSXMLDTDNode that governs the XML construct. 

Alternatively, you could get the children of an NSXMLDTD object and analyze them.

[Next](Binding%20NSXML%20Objects%20to%20a%20User%20Interface.md)[Previous](Handling%20Attributes%20and%20Namespaces.md)

