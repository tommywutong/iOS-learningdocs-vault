---
title: Documentation Set Guide
apple_id: TP40005266
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2009-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Documentation_Sets/820-Documentation-Set_Tokens_Schema_Reference/docset_tokens_schema_ref.html
archived_at: '2026-07-15T07:24:25.743829Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Documentation Set Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Documentation-Set%20Nodes%20Schema%20Reference.md)

# Documentation-Set Tokens Schema Reference

This chapter describes the element structure of the `Tokens.xml` (tokens) file used in documentation sets.

The schema for the nodes file, `TokensSchema.rng`, is located in the DocSetAccess framework in `<Xcode>/Library/PrivateFrameworks/DocSetAccess.framework`.

Listing D-1 lists the topology of the elements of a nodes file.

__Listing D-1__  `Tokens.xml` element topology

```
Tokens
   Token
      TokenIdentifier
         Name
         APILanguage
         Type
         Scope
      Path
      NodeRef
      Anchor
      Abstract
      Declaration
      Parameters
          Parameter
             Name
             Abstract
      ReturnValue
      DeclaredIn
         HeaderPath
         FrameworkName
      Availability
         IntroducedInVersion
         RemovedAfterVersion
         DeprecatedInVersion
         DeprecationSummary
      RelatedTokens
         TokenIdentifier
      RelatedDocuments
         NodeRef
         URL
      RelatedSampleCode
         NodeRef
         URL
   File
      Token
   RelatedTokens
      TokenIdentifier
```


The root element of a tokens file.

```
Tokens [version] ```  ``` 
   Token
   File
   RelatedTokens
```


| Name | Type | Description |
| --- | --- | --- |
| `version` | Decimal | The version number of the `NodesSchema.rng` file. The only supported version is 1.0. |

| Cardinality | Element | Para |
| --- | --- | --- |
| `1..*` | [Token](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomy) | Specifies a symbol. |
| `1..*` | [File](Documentation-Set%20Nodes%20Schema%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltcmq) | Identifies an HTML file and defines set of symbols that are documented in that file. See [Grouping Tokens by File](Supporting%20API%20Lookup%20in%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvooa) for details. |
| `1..*` | [RelatedTokens](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvooi) | Specifies a set of symbols in which each symbol is related to every other symbol in the set. See [Specifying Related Tokens](Supporting%20API%20Lookup%20in%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvomrt) for details. |

Describes a single symbol, or token.

```
Token [] ```  ``` 
   TokenIdentifier
   Path
   NodeRef
   Anchor
   Abstract
   Parameters
   ReturnValue
   Declaration
   DeclaredIn
   Availability
   RelatedTokens
   RelatedDocuments
   RelatedSampleCode
```

This element:

- Associates a symbol with its primary reference documentation.
- Supplies additional information—such as availability, declaration, and so forth—about the symbol.

For usage information, see [Defining a Symbol for Lookup](Supporting%20API%20Lookup%20in%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvomjv).

None.

| Cardinality | Element | Usage |
| --- | --- | --- |
| `1` | [TokenIdentifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomq) | Identifies the symbol. |
| `0..1` | [Path](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomrv) | Specifies the path to the HTML file containing the primary documentation. Must not be used when the token is located within a `File` element. |
| `0..1` | [NodeRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomru) | References the node representing the primary documentation for the symbol. Must not be used when the token is located within a `File` element. Can be used alone or in conjunction with a [Path](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomrv) element (see [Associating Symbols with API Reference Documentation](Supporting%20API%20Lookup%20in%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvomjw) for details). |
| `0..1` | [Anchor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvonq) | If you have a single HTML file that contains the primary reference documentation for more than one token, use this element to specify the location within that file of a particular token’s description. |
| `0..1` | [Abstract](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvony) | Provides a summary or brief description of the symbol. |
| `0..1` | [Declaration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvooa) | Specifies the symbol’s declaration statement. |
| `0..1` | [Parameters](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvonzv) | Specifies the list of parameters, if any, passed to the symbol. |
| `0..1` | [ReturnValue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvonzw) | Specifies the value returned by the symbol, if any. |
| `0..1` | [DeclaredIn](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomrt) | Specifies the header and framework in which the symbol is declared. |
| `0..1` | [Availability](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomzu) | Specifies the product versions and computer architectures in which the token appears. |
| `0..1` | [RelatedTokens](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvooi) | Specifies a set of symbols that are related to the token. The relationship is one way; there’s no inverse relationship from those symbols to this one. |
| `0..1` | [RelatedDocuments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomrx) | Specifies a list of documents that contain further information about the symbol. A token identifies its primary reference documentation through the [Path](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomrv), [NodeRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomru), or [File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomrw) elements; do not use this element to specify the primary reference documentation. |
| `0..1` | [RelatedSampleCode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomrz) | Specifies a list of documents containing sample code that showcase the symbol’s usage. |

Uniquely identifies a symbol or token.

```
TokenIdentifier [] {tokenizedString} ```  ``` 
   Name
   APILanguage
   Type
   Scope
```

There are two ways to specify a token identifier (use only one):

1. Using the `Name`, `Type`, `APILanguage`, and `Scope` subelements to individually specify the token's properties ([Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomjs)).
2. Using an identifier that conforms to the apple_ref convention ([Content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomjt)), described in “[Symbol Markers for HTML-Based Documentation](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/anchors/anchors.html#//apple_ref/doc/uid/TP40001215-CH347)” in _[HeaderDoc User Guide](../HeaderDoc%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjv)_.

For more information, see [Identifying Symbols](Supporting%20API%20Lookup%20in%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvomy).

None.

Each subelement specifies a specific component of a symbol identifier. See [Defining Tokens Using Individual Properties](Supporting%20API%20Lookup%20in%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvonq) for details.

| Cardinality | Element | Usage |
| --- | --- | --- |
| `1` | [Name](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvona) | Specifies the name of the symbol. For example: `arrayWithContentsOfFile:`. |
| `0..1` | [APILanguage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomjx) | Specifies the programming language in which the symbol is defined. For example: `occ`. |
| `1` | [Type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomjy) | Specifies the symbol’s type. For example: `clm`. |
| `0..1` | [Scope](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomjz) | Specifies the scope within which the symbol is defined. For example: `NSArray`. |

Tokenized string. This string identifies a symbol. For example: `//apple_ref/occ/clm/NSArray/arrayWithContentsOfFile:`. See [Defining Tokens Using apple_ref Identifiers](Supporting%20API%20Lookup%20in%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvona) for details.

Specifies a name.

```
Name [] {string} ```  ``` 
```


None.

String.

Species a programming language.

```
APILanguage [] {string} ```  ``` 
```


None.

String.

Specifies a symbol type.

```
Type [] {string} ```  ``` 
```


None.

String. Valid values are described in “[Symbol Markers for HTML-Based Documentation](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/anchors/anchors.html#//apple_ref/doc/uid/TP40001215-CH347)” in _[HeaderDoc User Guide](../HeaderDoc%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjv)_.

Specifies a programming scope (namespace or container).

```
Scope [] {string} ```  ``` 
```


None.

String.

Specifies a summary or brief description.

```
Abstract [type] {HTMLCode|string} ```  ``` 
```

This element lets you provide a summary description, usually one sentence.

When using HTML content, it must be valid; this includes double-escaping of entities. You can include links or basic HTML formatting. Hyperlinks with relative paths are resolved relative to the `Documents` directory.

| Name | Type | Description |
| --- | --- | --- |
| `type` | String | _Optional_. The type of the content. Values: `"text"` (default), `"html"`. |

HTML code or string.

Specifies the name of an anchor in an HTML file.

```
Anchor [] {normalizedString} ```  ``` 
```


None.

Normalized string.

References a node defined in the nodes file.

```
NodeRef [refid] ```  ``` 
```


| Name | Type | Description |
| --- | --- | --- |
| `refid` | Integer | Specifies the `id` of the referenced node. |

Specifies a symbol’s declaration statement.

```
Declaration [type] {HTMLCode|string} ```  ``` 
```

When using HTML content, it must be valid; this includes double-escaping of entities. You can include links or basic HTML formatting. Hyperlinks with relative paths are resolved relative to the `Documents` directory.

Use an HTML `PRE` element to ensure the line breaks and indentations are preserved when the content is displayed.

| Name | Type | Description |
| --- | --- | --- |
| `type` | String | _Optional_. The type of the content. Values: `"text"` (default), `"html"`. |

HTML code or string.

Specifies the list of parameters that can be passed to the symbol, if any.

```
Parameters ```  ``` 
    Parameter
```

`Parameters` encloses one or more `Parameter` elements. Each parameter element encloses the parameter name followed by an abstract.

| Cardinality | Element | Usage |
| --- | --- | --- |
| 1..\* | [Parameter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvonzx) | Specifies a parameter that can be passed to the symbol. |

Specifies a parameter that can be passed to the symbol, if any.

```
Parameter ```  ``` 
    Name
    Abstract
```


| Cardinality | Element | Usage |
| --- | --- | --- |
| 1 | [Name](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvona) | Specifies the parameter name. |
| 1 | [Abstract](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvony) | Specifies a short description of the parameter. |

Specifies the value returned by the symbol, if any.

```
ReturnValue ```  ``` 
    Abstract
```


| Cardinality | Element | Usage |
| --- | --- | --- |
| 1 | [Abstract](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvony) | Provides a short description of the value returned by the symbol. |

Specifies the header and framework in which the symbol is declared, for tokens that describe an API symbol.

```
// Usage 1:
DeclaredIn [] ```  ``` 
   HeaderPath
   FrameworkName
// Usage 2:
DeclaredIn [] {filepath} ```  ``` 
```

This element supports two usage patterns:

1. You can specify the file path to the header in which the symbol is declared and the name of the framework that must be loaded to use that symbol separately, using the `HeaderPath` and `FrameworkName` elements, respectively. See [Subelements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomju) for details.
2. If the API is not part of a framework, you can specify the path to the header as a string, directly within the `DeclaredIn` element. See [Content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomjv) for details.

| Cardinality | Element | Usage |
| --- | --- | --- |
| `1` | [HeaderPath](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomrr) | Specifies the pathname of the symbol’s header file. |
| `0..1` | [FrameworkName](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomrs) | Specifies the name of the symbol’s framework. Needed only when the symbol is part of a framework. |

Pathname. The pathname of the symbol’s header file.

Specifies availability information related to a product and computer architecture.

```
Availability [distribution] ```  ``` 
   IntroducedInVersion
   RemovedAfterVersion
   DeprecatedInVersion
   DeprecationSummary
```

See [Version Information](Supporting%20API%20Lookup%20in%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvomrs) for usage details.

| Name | Type | Description |
| --- | --- | --- |
| `distribution` | String | Specifies the name of a product, such as `OS X`. |

| Cardinality | Element | Usage |
| --- | --- | --- |
| `1..*` | [IntroducedInVersion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomzq) | Specifies a product version and computer architecture in which a symbol was introduced. |
| `0..*` | [RemovedAfterVersion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomzs) | Specifies a product version and computer architecture in which a symbol was last available. |
| `0..*` | [DeprecatedInVersion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomzr) | Specifies a product version and computer architecture in which a symbol was deprecated. |
| `0..1` | [DeprecationSummary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomzt) | Provides information about a symbol whose usage is not recommended. |

Specifies a filepath.

```
Path [] {filepath} ```  ``` 
```


None.

Filepath.

Species the pathname of a header file.

```
HeaderPath [] {pathname} ```  ``` 
```


None.

Pathname.

Specifies the name of a framework.

```
FrameworkName [] {string} ```  ``` 
```


None.

String.

Specifies an introduced-in version number.

```
IntroducedInVersion [cputype,bitsize] {threeTupleNumber} ```  ``` 
```


| Name | Type | Description |
| --- | --- | --- |
| `cputype` | String | Specifies the CPU type to which this version information applies. Values: `ppc` (PowerPC), `i386` (Intel). When unspecified, the version applies to both CPU types. |
| `bitsize` | Integer | Specifies the CPU bitsize to which this version information applies. Values: `32` (32 bit), `64` (64 bit). When unspecified, the version number applies to both CPU bitsizes. |

Period-separated, three-tuple number in the form `x.y.z`, where `x`, `y`, and `z` are integers. Only the major version number—`x`—is required.

Specifies a deprecated-in version number.

```
DeprecatedInVersion [cputype,bitsize] {threeTupleNumber} ```  ``` 
```


| Name | Type | Description |
| --- | --- | --- |
| `cputype` | String | Specifies the CPU type to which this version information applies. Values: `ppc` (PowerPC), `i386` (Intel). When unspecified, the version applies to both CPU types. |
| `bitsize` | Integer | Specifies the CPU bitsize to which this version information applies. Values: `32` (32 bit), `64` (64 bit). When unspecified, the version number applies to both CPU bitsizes. |

Period-separated, three-tuple number in the form `x.y.z`, where `x`, `y`, and `z` are integers. Only the major version number—`x`—is required.

Specifies a removed-after version number.

```
RemovedAfterVersion [cputype,bitsize] {threeTupleNumber} ```  ``` 
```


| Name | Type | Description |
| --- | --- | --- |
| `cputype` | String | Specifies the CPU type to which this version information applies. Values: `ppc` (PowerPC), `i386` (Intel). When unspecified, the version applies to both CPU types. |
| `bitsize` | Integer | Specifies the CPU bitsize to which this version information applies. Values: `32` (32 bit), `64` (64 bit). When unspecified, the version number applies to both CPU bitsizes. |

Period-separated, three-tuple number in the form `x.y.z`, where `x`, `y`, and `z` are integers. Only the major version number—`x`—is required.

Specifies summary information about a symbol whose usage is not recommended.

Use this element to provide additional information about other symbols or technologies that the user should use instead.

```
DeprecationSummary [type] {HTMLCode|String} ```  ``` 
```

When using HTML content, it must be valid; this includes double-escaping of entities. You can include links or basic HTML formatting. Hyperlinks with relative paths are resolved relative to the `Documents` directory.

| Name | Type | Description |
| --- | --- | --- |
| `type` | String | _Optional_. The type of the content. Values: `"text"` (default), `"html"`. |

HTML code or string.

Defines a list of tokens.

```
RelatedTokens [title] ```  ``` 
   TokenIdentifier
```


| Name | Type | Description |
| --- | --- | --- |
| `title` | String | Specifies a label for the token list. (Optional) |

| Cardinality | Element | Usage |
| --- | --- | --- |
| `1..*` | [TokenIdentifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomq) | Identifies a token defined in the documentation set. |

Defines a list of documents.

```
RelatedDocuments [] ```  ``` 
   NodeRef, URL
```


None.

| Cardinality | Element | Usage |
| --- | --- | --- |
| `1..*` | [NodeRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomru) | References a node defined in the nodes file. |
|  | URL | Absolute URL to a document outside the documentation set. |

Defines a list of documents containing sample code.

```
RelatedSampleCode [] ```  ``` 
   NodeRef, URL
```


None.

| Cardinality | Element | Usage |
| --- | --- | --- |
| `1..*` | [NodeRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomru) | References a node defined in the nodes file. |
|  | URL | Absolute URL to a document outside the documentation set. |

Identifies an HTML file and a set of tokens that are documented in that file.

```
File [path,noderef] ```  ``` 
   Token
```

When you use the `File` element to group token definitions, the individual `Token` elements inside of the `File` element cannot contain `Path` or `NodeRef` elements.

| Name | Type | Description |
| --- | --- | --- |
| `path` | Filepath | Specifies the path to the HTML file that documents the tokens. See [Grouping Tokens by File](Supporting%20API%20Lookup%20in%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvooa) for details. |
| `noderef` | Integer | Specifies the `id` of the node to associate with the tokens this element specifies. See [Node](Documentation-Set%20Nodes%20Schema%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltc) for more information. |

| Cardinality | Element | Usage |
| --- | --- | --- |
| `1..*` | [Token](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomy) | Specifies a token that is documented in the HTML file. |

Identifies the location of a document that is outside of the documentation set.

```
URL [] {URL} ```  ``` 
```


None.

URL.

[Next](Document%20Revision%20History.md)[Previous](Documentation-Set%20Nodes%20Schema%20Reference.md)

