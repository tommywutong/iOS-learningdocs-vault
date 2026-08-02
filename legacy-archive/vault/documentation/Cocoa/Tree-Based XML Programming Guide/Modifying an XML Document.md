---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/Articles/ModifyingXML.html
archived_at: '2026-07-15T07:16:59.891878Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tree-Based XML Programming Guide](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)


[Next](Representing%20Object%20Values%20as%20Strings.md)[Previous](Querying%20an%20XML%20Document.md)

# Modifying an XML Document

You can modify an XML document with NSXML methods in two general ways:

- By changing the values of node objects
- By adding, removing, or replacing nodes, or by changing their locations within the tree

This article discusses both aspects of XML modification.

Most kinds of NSXMLNode objects have values associated with them. The NSXMLNode class lets you set a node’s value either to a string object or to some other type of object. The two major value-setting NSXMLNode methods reflect this choice:

- `- (void)setStringValue:(NSString *)string;`
- `- (void)setObjectValue:(id)value;`

When NSXML processes an input file or other source of XML, it automatically sets the values of nodes as string objects. (It has no other indication of the types of values other than the form it finds them in: strings.) Keeping the value of nodes as strings is acceptable for most applications. Changing the string value is simply a matter of finding a particular node and sending `setStringValue:` or `setStringValue:resolvingEntities:` to it. The value itself often comes from the user interface, as shown in Listing 1.

__Listing 1__  Setting the string value of a node

```
int index = [form indexOfSelectedItem];
NSXMLNode *node;
switch (index) {
    case 0: // idField
        [[person attributeForName:@"idnum"] setStringValue:
            [idField stringValue]];
        break;
    case 1: // lastName
        node = [[person elementsForName:@"lastName"] objectAtIndex:0];
        if (!node) {
            node = [NSXMLElement elementWithName:@"lastName"];
            [person addChild:node];
        }
        [node setStringValue:[lastName stringValue]];
        break;
// ...
```

Setting the value of a node to an object other than an NSString object can give you certain advantages. As an example, suppose your application has element nodes for such financial values as item price, quantity, tax, and total. By converting the values of these nodes from strings (`“45.99”`) to numbers (`45.99`), your application can perform calculations directly with the object values of the nodes.

You can set any arbitrary object as the object value of the node. When an NSXMLNode object is asked to emit its object value as an XML string, it produces a string representation of the value. For the standard atomic types, this value is in a canonical form for the type (as defined by the W3C XML Schema Data Types specification). To take advantage of this default behavior, the object you set should be an instance of a Foundation class that corresponds to one of the atomic types in the XQuery data model. Table 1 lists these classes and their corresponding types.

__Table 1__  Equivalent classes and atomic types

| Foundation class | Atomic type |
| NSString | string (use `setObjectValue:`) |
| NSNumber | integer, decimal, float, double, Boolean |
| NSCalendarDate | date |
| NSData | base64 and hexadecimal binary |
| NSURL | URI |
| NSArray | `NMTOKENS`, `IDREFS`, `ENTITIES` |

You can also create value transformers that render string values representative of custom objects. For more on this subject, and for further information on the standard string representations, see [Representing Object Values as Strings](Representing%20Object%20Values%20as%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytiojxfvbecsseizceiqy).

You must set the object value of each node in a document yourself—NSXML does not do it for you automatically. Typically you would first set object values globally after NSXML processes a source of XML and produces a tree representation of the document. You can walk the tree or otherwise search for the nodes of the document whose values you want to set to objects. If thereafter you create new nodes, you can set their object values at that point.

The code fragment in Listing 2 uses the NSTableView data-source method `tableView:objectValueForTableColumn:row:` as the point in which to set the object values of attribute nodes representing dates. The string values of these attributes must conform to a pattern of “mm/dd/yy” where “mm” is the month number, “dd” is the day of the month, and “yy” is the last two digits of the year. (You can attach an NSDateFormatter object to an input field to ensure that newly entered dates conform to this pattern too.) The code fragment uses the NSCalendarDate method `dateWithString:calendarFormat:` to effect the conversion from string value to object value.

__Listing 2__  Setting an object value based on a string pattern

```
// in tableView:objectValueForTableColumn:row:...
 if ([columnID isEqualToString:@"Hire Date"]) {
        NSXMLNode *attrNode = [[employeeArray objectAtIndex:rowIndex]
            attributeForName:@"hireDate"];
        if (attrNode) {
            if (![[attrNode objectValue] isKindOfClass:
                [NSCalendarDate class]]) {
                NSCalendarDate *date = [NSCalendarDate dateWithString:
                    [attrNode stringValue] calendarFormat:@"%m/%d/%y"];
                [attrNode setObjectValue:date];
            }
            return [attrNode objectValue];
        }
    }
// ...
```

Once the object values of the `hireDate` attributes have been set, the application can go about comparing dates, computing periods between dates, and anything else that can be done with the methods of the NSCalendarDate and NSDate classes. Listing 3 is a method that uses the NSCalendarDate object values to identify the employee that has worked the longest for a hypothetical company.

__Listing 3__  Using the object value of an attribute

```objc
- (NSXMLElement *)earliestHire {

    NSXMLElement *earliest;
    int i;
    NSError *err;
    NSArray *nodes = [xmlDoc nodesForXPath:@".//employee" error:&err];
    if (!nodes || [nodes count] == 0)
        return nil;
    earliest = [nodes objectAtIndex:0];
    for (i = 1; i < [nodes count]; i++) {
        NSXMLElement *current = [nodes objectAtIndex:i];
        id date1 = [[earliest attributeForName:@"hireDate"] objectValue];
        id date2 = [[current attributeForName:@"hireDate"] objectValue];
        if ([date1 isKindOfClass:[NSDate class]] &&
            [date2 isKindOfClass:[NSDate class]] ) {
            if ([(NSDate *)date2 compare:(NSDate *)date1]
                        == NSOrderedAscending) {
                earliest = current;
            }
        }
    }
    return earliest;
}
```


In addition to modifying an XML document’s content, you can modify a document’s structure using NSXML methods. Structure modification entails adding, deleting, and replacing nodes, as well as moving existing nodes to new locations in the XML tree. Table 2 lists the methods that enable you to perform these operations.

__Table 2__  NSXML methods for manipulating nodes

| Method | Declared in classes |
| `detach` | NSXMLNode |
| `addChild:` | NSXMLElement, NSXMLDocument, and NSXMLDTD |
| `setChildren:` | NSXMLElement, NSXMLDocument, and NSXMLDTD |
| `insertChild:atIndex:` | NSXMLElement, NSXMLDocument, and NSXMLDTD |
| `insertChildren:atIndex:` | NSXMLElement, NSXMLDocument, and NSXMLDTD |
| `removeChildAtIndex:` | NSXMLElement, NSXMLDocument, and NSXMLDTD |
| `replaceChildAtIndex:withNode:` | NSXMLElement, NSXMLDocument, and NSXMLDTD |

The `detach` method is different from the others in this list in that you invoke it on the child node itself and not the parent of the node. You can send `detach` to any NSXMLNode object (not just the ones allowed to have children) to break the connection between that node and its parent. Once a node is detached from its parent, you are free to reattach it to another parent elsewhere in the tree using one of the methods for inserting, adding, or replacing child nodes.

All the other methods in Table 2 are sent to the parent of the node being added, removed, or replaced. The parent must be an object that is an instance of the NSXMLElement, NSXMLDocument, or NSXMLDTD class. Some of these classes place restrictions on what kinds of children can be added, depending on the class of the parent:

- NSXMLDocument objects can take only comment nodes, processing-instruction nodes, and a single element node (the root element) as children.
- NSXMLDTD objects can take only children that are comment nodes, processing-instruction nodes, and NSXMLDTDNode objects with kinds as specified by `NSXMLDTDNodeKind`  constants.

The node-manipulation methods of these classes are identical. And they are straightforward, with their intended uses made unambiguous by their names. They may require you to do one or more things before invoking them:

- Find the parent node, the receiver of the message.

  If you already have a reference to an existing child node, you can get its parent by sending the child a `parent` message.
- Find the index of the child to replace, remove, or insert the new child before.

  You can get the index by sending the node object an `index` message.
- Create the node object to be added to the parent.

  The methods that add or replace children usually (but not always) require you to create the child node first. Create the required node object using the `initWithKind:` method of the NSXMLNode class, one of the class factory methods of the same class, one of the initializers of the NSXMLElement class, or the `initWithXMLString:` method of the NSXMLDTDNode class.

The most common receiver of node-manipulation messages is an instance of the NSXMLElement class. The following code examples illustrate how the NSXMLElement node-manipulation methods might be used in your application. Listing 4 includes code that creates nested elements (the inner one containing an attribute) with the following XML string form:

```
<Figure><Graphic href="../Art/cc_finalui.gif"></Graphic>
```


__Listing 4__  Adding nested elements

```
// Note: relativePathToFilename is a custom method
NSString *relativePathToArt = [[self fileName]
    relativePathToFilename:selectedFile];

NSXMLElement *newFigureElement = [NSXMLElement elementWithName:@"Figure"];
NSXMLElement *newGraphicElement = [NSXMLElement elementWithName:@"Graphic"];
NSXMLNode *pathToHrefAttribute = [NSXMLNode attributeWithName:@"href"
    stringValue:relativePathToArt];

[newGraphicElement addAttribute:pathToHrefAttribute];
[newFigureElement addChild:newGraphicElement];

NSXMLElement *selectedParent = [treeView selectedItem];
[selectedParent addChild:newFigureElement];
// ...
```

Listing 5 is a method that replaces a child node with a text node containing the child’s string value.

__Listing 5__  Replacing an element

```objc
- (void)unwrapElement:(NSXMLElement *)childToUnwrap {

    id parent = [childToUnwrap parent];
    int indexOfChildToUnwrap = [childToUnwrap index];
    NSXMLNode *textNode = [NSXMLNode textWithStringValue:[childToUnwrap stringValue]];

    // Unwrapping is defined as replacing the selected element
    // with a text representation of itself.
    [parent replaceChildAtIndex:indexOfChildToUnwrap withNode:textNode];
}
```

As you add and relocate nodes, you may occasionally want to validate the document to verify that the changes conform to the governing schema. To validate a document, send the `validateAndReturnError: ` message to the NSXMLDocument object. If the operation is not valid, the method returns `NO`; the reasons for invalidity are returned by indirection in the method’s NSError parameter.

[Next](Representing%20Object%20Values%20as%20Strings.md)[Previous](Querying%20an%20XML%20Document.md)

