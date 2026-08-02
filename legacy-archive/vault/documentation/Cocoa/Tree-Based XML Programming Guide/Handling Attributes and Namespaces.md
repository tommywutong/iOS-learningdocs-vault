---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/Articles/AttributesNamespaces.html
archived_at: '2026-07-15T07:16:53.862519Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tree-Based XML Programming Guide](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)


[Next](Creating%20and%20Modifying%20Document%20Type%20Definitions.md)[Previous](Representing%20Object%20Values%20as%20Strings.md)

# Handling Attributes and Namespaces

XML namespaces and attributes are similar in some respects but different in others. Attributes are name-value pairs that are typically used to hold metadata related to the element. Namespaces are considerably more complex in purpose. They serve to distinguish elements and attributes from different sources that have identical names but different meanings. They are also used to group related attributes and elements so that a processing application can easily recognize them. Namespaces are declared in a manner similar to the way attributes are, but with an `xmlns:`_prefix_ name assigned a value that is a URI, for example:

```
<employee xmlns:emp=”http://www.acme.com/defs/empl.html”/>
```

This construction maps the prefix to a unique URI identifier; thereafter the prefix can be used to identify the namespace of an attribute or element (for example, “<emp:title></emp:title>”). Default, prefix-less namespaces can also be declared that affect all current and descendent elements and attributes past the point of declaration, unless they are overridden by another namespace.

Although the purposes of attributes and namespaces are different, they are conceptually similar. They cannot be children of an element node, but they are always closely associated with one. Indeed the associated element _is_ their parent. Even though they are NSXML nodes—NSXMLNode objects of kinds `NSXMLAttributeKind` and `NSXMLNamespaceKind`—they cannot have children and cannot be children of any node. (Namespaces, however, can qualify the attributes of an element as well as the element itself.) Namespace and attribute nodes are not encountered during document traversal.

The programmatic interface of NSXMLElement reflects this architectural affinity. It offers similar sets of methods for namespace nodes and attribute nodes. This articles explains how to use these methods and then discusses a unique feature of the namespace API: resolving namespaces.

The NSXMLElement class defines methods for manipulating and accessing an element’s attributes that are nearly identical in form to another set of methods for manipulating and accessing namespace nodes. Table 1 lists these complementary sets of methods.

__Table 1__  Attribute and namespace node manipulation methods

| Attribute methods | Namespace methods |
| `addAttribute:` | `addNamespace:` |
| `setAttributes:``setAttributesAsDictionary:` | `setNamespaces:` |
| `removeAttributeForName:` | `removeNamespaceForPrefix:` |
| `attributes` | `namespaces` |
| `attributeForName:``attributeForLocalName:URI:` | `namespaceForPrefix:` |

The names of these methods clearly indicate what you use them for, but some comments about each category of method are warranted:

- The `add...` and `set...` methods usually require you to create NSXMLNode objects of the appropriate kind (`NSXMLAttributeKind`or `NSXMXLNamespaceKind`) before adding or setting the object. To create these node objects, you can use the NSXMLNode class factory methods `namespaceWithName:stringValue:`, `attributeWithName:stringValue:`, and `attributeWithLocalName:URI:stringValue:`. The last of these methods creates an attribute that is bound to a namespace identified by the URI parameter.

  The `setAttributesAsDictionary:` method lets you set an element’s attributes without having to create NSXMLNode objects first. The keys in the dictionary are the names of the attributes and the values are the string values of the attributes.

  All of the methods that set attributes or namespaces of an element remove all existing attributes or namespaces.
- The methods that remove an attribute or namespace from an element, or that access a particular attribute or namespace, require you to know the name of the attribute or the prefix of the namespace. For an attribute node, you can simply ask the node for its name using the NSXMLNode `name` method. For a namespace node, however, the `name` method returns a qualified name (that is, the prefix plus the local name, separated by a colon). You can obtain the prefix by invoking the NSXMLNode class method `prefixForName:`, passing in the qualified name.
- The `attributeForLocalName:URI:` requires you to supply the local (non-qualified) name of an attribute as well as the namespace URI it’s bound to. If you can access the associated namespace node, you can obtain the URI by sending the node a `stringValue` message. You can get the local name from the qualified name by using the NSXMLNode class method `localNameForName:`.
- If you want to access or remove an existing namespace or attribute node, you can obtain a reference to its element by sending the namespace or attribute node a `parent` message.

Once you have accessed a specific namespace or attribute node, you can get or set its string or object value (see [Changing the Values of Nodes](Modifying%20an%20XML%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjzfu4tomzwgm) for details). Bear in mind that the value of a namespace node is the URI of the namespace; if you want to set the URI as an object value, make it an NSURL object.

If your application knows (or suspects) that it might be dealing with XML from different sources or authored in different XML vocabularies, such as XSLT and RDF, it has to deal with namespaces. At any point of processing it might have to know the namespace to which an element or attribute is bound in order to handle that element or attribute appropriately. A case in point is the `set` element, which is defined by both SVG and MathML for different purposes. Before you can determine the meaning of a `set` element in a document containing both SVG and MathGL markup, you have to find out which namespace it belongs to. To find out the namespace affiliation of an element you must resolve it.

For namespace resolution, NSXMLElement declares two methods beyond the ones discussed in [Methods for Manipulating Attributes and Namespaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrqfu4tmobvga).

- `resolveNamespaceForName:`
- `resolvePrefixForNamespaceURI:`

The first method takes the qualified or local name of an element and returns the namespace node representing the namespace to which the element belongs. Your application can get the URI from the node (its string value) and compare it to a list of known or expected URIs to determine namespace affiliation. If there is no associated namespace, the `resolveNamespaceForName:` method returns `nil`.

The second namespace-resolution method, `resolvePrefixForNamespaceURI:`, works in the opposite direction. You pass in a URI and get back the prefix bound to that URI. You can use this method, for example, when you are adding elements to a document and need to know the prefixes of their qualified names.

[Next](Creating%20and%20Modifying%20Document%20Type%20Definitions.md)[Previous](Representing%20Object%20Values%20as%20Strings.md)

