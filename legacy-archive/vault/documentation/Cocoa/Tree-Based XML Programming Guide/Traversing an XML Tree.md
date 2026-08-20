---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/Articles/TraversingTree.html
archived_at: '2026-07-15T07:17:04.904739Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tree-Based XML Programming Guide](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)


[Next](Querying%20an%20XML%20Document.md)[Previous](Writing%20XML%20From%20NSXML%20Objects.md)

# Traversing an XML Tree

NSXML gives you several ways to explore the tree structure representing an XML document and find nodes that are of interest. Each approach is based on a different conceptual model:

- Traversing nodes in document order
- Traversing the children of a node
- Accessing element nodes by name

Traversing a tree in document order is perhaps the simplest approach. You start at some node in the tree—specifically the root element if you want to go through the entire document—and iteratively invoke `nextNode` to get the next node in document order until you reach the end of the document. Along the way you can query nodes for attributes of interest, such as name, value, kind, or level. Listing 1 illustrates the use of `nextNode`, in this case extracting comments that are used as translation notes for the string value of the subsequent node.

__Listing 1__  Walking an XML tree with nextNode messages

```
NSXMLNode *aNode = [xmlDoc rootElement];
NSMutableString *translator_notes=nil;
while (aNode = [aNode nextNode]) {
    if ( [aNode kind] == NSXMLCommentKind ) {
        if (!translator_notes) {
            translator_notes = [[NSMutableString alloc] init];
        }
        [translator_notes appendString:[aNode stringValue]];
        [translator_notes appendString:@" ========> "];
        aNode = [aNode nextNode]; // element to be translated
        [translator_notes appendString:[aNode stringValue]];
        [translator_notes appendString:@"\n"];
    }
}
if (translator_notes) {
    [translator_notes writeToFile:[NSString stringWithFormat:@"%@/translator_notes.txt", NSHomeDirectory()] atomically:YES];
    [translator_notes release];
}
```

Of course you can also go backward in document order by repeatedly sending `previousNode` to each returned node object.

While `nextNode` and `previousNode` take you sequentially through a represented XML document, many other NSXMLNode methods help you navigate hierarchically within an XML tree structure, between parent and children nodes and among the sibling nodes of a common parent. These methods include `children `, `childCount `, `childAtIndex: `, `nextSibling `, and `previousSibling `. The following code-fragment examples show how these methods might be used in combination to traverse sibling nodes and accomplish some task. In Listing 2, the `children` and `childCount` methods are used, along with the NSArray `objectAtIndex:` method.

__Listing 2__  Using the children and childCount methods to traverse sibling nodes

```
NSArray *children = [[xmlDoc rootElement] children];
int i, count = [children count];
for (i=0; i < count; i++) {
    NSXMLNode *child = [children objectAtIndex:i];
    [self doSomethingWithNode:child];
}
```

If you can, use the NSXMLNode `childCount` method to obtain the number of child nodes instead of sending `count` to the result of `children`. The former method offers better performance. The code example in Listing 3 is slightly simpler and bypasses the `children` method altogether.

__Listing 3__  Using the childAtIndex: and childCount methods to traverse sibling nodes

```
int i, count = [[xmlDoc rootElement] childCount];
for (i=0; i < count; i++) {
    NSXMLNode *child = [[xmlDoc rootElement] childAtIndex:i];
    [self doSomethingWithNode:child];
}
```

An even simpler approach to the same task is illustrated in Listing 4, which uses the NSXMLNode `childAtIndex:` and `nextSibling ` methods.

__Listing 4__  Using the childAtIndex: and nextSibling methods to traverse sibling nodes

```
NSXMLNode *child = [[xmlDoc rootElement] childAtIndex:0];
do {
    [self doSomethingWithNode:child];
} while ( child = [child nextSibling] );
```

For going upward in the tree hierarchy, from child node to parent, you have the `parent` method. This is the only method needed for this direction because, except for the root element and standalone nodes, there is almost always a one-to-one relationship from a child to its parent in an XML tree. (Namespace and attribute nodes are also an exception to this relationship rule because they have an element as a parent but are not children of that element.)

If you want a more directed search, you can use the `elementsForName: ` method. If you know the name of a child element, send `elementsForName:` to the parent element. This method returns the child NSXMLElement nodes with matching names in an array (an NSArray object is used in case more than one child has the specified name). If you have to deal with namespace-qualified elements, use the `elementsForLocalName:URI: ` method instead.

[Next](Querying%20an%20XML%20Document.md)[Previous](Writing%20XML%20From%20NSXML%20Objects.md)

