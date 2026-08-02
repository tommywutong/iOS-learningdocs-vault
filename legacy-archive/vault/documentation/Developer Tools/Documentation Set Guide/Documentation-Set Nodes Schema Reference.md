---
title: Documentation Set Guide
apple_id: TP40005266
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2009-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Documentation_Sets/810-Documentation-Set_Nodes_Schema_Reference/docset_nodes_schema_ref.html
archived_at: '2026-07-15T07:24:25.731752Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Documentation Set Guide](Introduction.md)


[Next](Documentation-Set%20Tokens%20Schema%20Reference.md)[Previous](Documentation-Set%20Property%20List%20Key%20Reference.md)

# Documentation-Set Nodes Schema Reference

This chapter describes the element structure of the `Nodes.xml` (nodes) file used in documentation sets.

The schema for the nodes file, `NodesSchema.rng`, is located in the DocSetAccess framework in `<Xcode>/Library/PrivateFrameworks/DocSetAccess.framework`.

Listing C-1 lists the topology of the elements of a nodes file.

__Listing C-1__  Nodes.xml element topology

```
DocSetNodes
   TOC
      Node
         Name
         URL
         Path
         File
         Anchor
         Subnodes
            Node
            NodeRef
      NodeRef
         Subnodes
   Library
      Node
```


Root element of the nodes file.

```
DocSetNodes [version] ```  ``` 
   TOC
   Library
```


| Name | Type | Description |
| --- | --- | --- |
| `version` | Decimal | The version number of the `NodesSchema.rng` file. The only supported version is 1.0. |

| Cardinality | Element |
| --- | --- |
| `1` | [TOC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknlte) |
| `0..1` | [Library](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltema) |

Defines the document hierarchy.

```
TOC [] ```  ``` 
   Node|NodeRef
```


None.

| Cardinality | Element | Usage |
| --- | --- | --- |
| `1` | [Node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltc) or [NodeRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknlto) | Although this element must contain a `Name` element, the Documentation window actually displays the localized documentation set name (specified by the `CFBundleName` property) for this root node.  The documentation set name is displayed in the Home pop-up menu in the Documentation window. |

Represents a single node in the document hierarchy.

```
Node [ id,type,isPrimaryTOCNode,noindex] ```  ``` 
   Name
   URL
   Path
   File
   Anchor
   Subnodes
```

A node represents a file or a group of files within the documentation set. A node is associated with a location in the HTML files, specified by a combination of its `URL`, `Path`, `File` and `Anchor` subelements.

See [Specifying Subnodes](Configuring%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjrfvjvomjt) for usage details.

| Name | Type | Description |
| --- | --- | --- |
| `id` | Integer | _Optional_. This unique—within the documentation set—identifier allows the node to be referenced elsewhere in the `Nodes.xml` or `Tokens.xml` files. |
| `type` | String | _Optional_. Specifies the node type. Values: `file` (default), `folder`, `bundle`. |
| `isPrimaryTOCNode` | Boolean | _Optional_. Indicates whether the node represents the primary TOC location of the document the node represents. This is relevant only if this node appears in the node hierarchy multiple times. Default: `false`. |
| `noindex` | Boolean | _Optional_. Species whether the node is excluded from the documentation set’s indexes and from any searches. Default: `false`. |

| Cardinality | Element | Usage |
| --- | --- | --- |
| `1` | [Name](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltg) | Specifies the node’s name, which appears in the Documentation window. |
| `0..1` | [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknlts) | Specifies the location of the files the node represents. |
| `0..1` | [Path](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltcma) | Specifies the location of the files the node represents. |
| `0..1` | [File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltcmq) | Specifies the name of the file the node represents. |
| `0..1` | [Anchor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltcmi) | Specifies a scroll-to location within the node’s landing page. |
| `0..1` | [Subnodes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltq) | Defines a group of subnodes. |

Specifies a name.

```
Name [] {string} ```  ``` 
```


None.

String.

Defines a list of nodes.

```
Subnodes [] ```  ``` 
   Node,NodeRef
```


None.

| Cardinality | Element |
| --- | --- |
| `1..*` | [Node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltc) |
| `1..*` | [NodeRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknlto) |

Refers to a node defined elsewhere in the nodes file.

```
NodeRef [refid, isPrimaryTOCNode] ```  ``` 
   Subnodes
```

You can also use this element in tokens files to associate a symbol with a documentation node. This is useful when a `Node` element describing the symbol’s reference documentation already exists.

When it appears within a `Subnodes` or `TOC` element, a `NodeRef` is treated as if the `Node` element it references was itself listed there. This allows a document to be listed multiple times in the document hierarchy of the documentation set.

| Name | Type | Description |
| --- | --- | --- |
| `refid` | Integer | Specifies the `id` of the referenced node. |
| `isPrimaryTOCNode` | Boolean | _Optional_. Indicates whether the node represents the primary TOC location of the document the node represents. Default: `false`. |

| Cardinality | Element | Usage |
| --- | --- | --- |
| `0..1` | [Subnodes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltq) | Defines a group of subnodes. These subnodes are used only when the node identified by the `refid` attribute does not contain subnodes. |

Specifies the base location of the node’s documentation as a URL.

```
URL [] {URL} ```  ``` 
```

When used alone, the `URL` element is interpreted as the full path to the file to load when the user selects the node. See [Specifying the Location of a Documentation Node](Configuring%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjrfvjvomy) for details about using this element with other `Node` subelements.

None.

URL.

Specifies the path to the file or directory associated with a node.

```
Path [] {filepath} ```  ``` 
```

The Path element can specify:

- The relative path to the node’s landing page.
- A subpath to the directory containing the node’s landing page.

See [Specifying the Location of a Documentation Node](Configuring%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjrfvjvomy) for details about using this element with other `Node` subelements.

None.

Filepath.

Specifies a filename.

```
File [] {normalizedString} ```  ``` 
```

See [Specifying the Location of a Documentation Node](Configuring%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjrfvjvomy) for details about using this element with other `Node` subelements.

None.

Normalized string.

Identifies a scroll-to-here location within a node's landing page.

```
Anchor [] {normalizedString} ```  ``` 
```

See [Specifying the Location of a Documentation Node](Configuring%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjrfvjvomy) for details about using this element with other `Node` subelements.

None.

Normalized string.

Defines a library of nodes.

```
Library [] ```  ``` 
   Node
```

See [Creating a Library of Node Definitions](Configuring%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjrfvjvomjy) for usage details.

None.

| Cardinality | Element |
| --- | --- |
| `1..*` | [Node](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltc) |

[Next](Documentation-Set%20Tokens%20Schema%20Reference.md)[Previous](Documentation-Set%20Property%20List%20Key%20Reference.md)

