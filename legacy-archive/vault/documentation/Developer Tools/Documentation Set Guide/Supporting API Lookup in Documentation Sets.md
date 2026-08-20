---
title: Documentation Set Guide
apple_id: TP40005266
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2009-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Documentation_Sets/040-Supporting_API_Lookup_in_Documentation_Sets/docset_api_lookup.html
archived_at: '2026-07-15T07:24:25.102931Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Documentation Set Guide](Introduction.md)


[Next](Indexing%20Documentation%20Sets.md)[Previous](Configuring%20Documentation%20Sets.md)

# Supporting API Lookup in Documentation Sets

One of the key features of the Xcode Documentation window is fast API search, the ability to quickly filter large lists of API symbols to find a particular symbol and its associated documentation. If your documentation set contains reference documentation for API symbols or other tokens, you can support fast API lookup for that documentation set by including one or more `Tokens.xml` files. The tokens file associates symbols or tokens with their primary reference documentation.

Documentation sets can have more than one tokens file; however, if a documentation set lacks a tokens file, Xcode supports only title and full-text searches in the Documentation window for that documentation set—fast API search is disabled.

A tokens file consists of a series of token definitions. Each token definition represents information about a single symbol. This chapter shows how to create a token definition to describe a symbol for lookup, how to provide information about that symbol for use with Quick Help, and how to organize large numbers of token definitions.

You associate a symbol with its reference documentation using the `Token` element. Because this element represents a single token definition, you can think of it as the building block of the tokens file. A _token_ includes:

- A unique identifier representing the symbol described by the `Token` element
- The location of the symbol’s primary reference documentation
- Summary information about the symbol (for display in Quick Help)
- Information about documents and symbols related to the symbol

This section shows how to define a token using the `Token` element.

Every symbol that you describe in a tokens file must have a unique identifier, known as a _token identifier_. The information that uniquely identifies a symbol is the symbol’s name, type (function, method, and so forth), scope, and language (C, C++, Objective-C, and so forth). There are two ways to specify a token identifier:

- By specifying each of the symbol’s properties individually
- Using an identifier that conforms to the standard described in “[Symbol Markers for HTML-Based Documentation](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/anchors/anchors.html#//apple_ref/doc/uid/TP40001215-CH347)” in _[HeaderDoc User Guide](../HeaderDoc%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjv)_

A token identifier is represented by the `TokenIdentifier` element. This element can contain either a combination of child elements—if you choose to identify the symbol by its individual properties—or a single string, if you choose to use the apple_ref convention to identify the symbol. These methods are described in greater detail in the following sections.

One way to specify a token identifier is to list the symbol’s identifying properties—name, type, language, and scope—as individual subelements within the `TokenIdentifier` element.

Use the following subelements of the `TokenIdentifier` element to specify each of the symbol’s identifying properties separately:

- __Name__. The name of the symbol. This is required information.
- __APILanguage__. This is the programming language to which the symbol applies. Use this element only if your tokens file represents an API symbol.

  Apple defines a small number of values, described in _[HeaderDoc User Guide](../HeaderDoc%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjv)_, for common languages. However, you can use any arbitrary string in this element. If you have symbols belonging to languages that are not covered by this specification, please [contact Apple](https://developer.apple.com/contact/), so that Apple can define a value for that language that everyone can use.
- __Type__. The type—such as function, method, class, and so forth—of the symbol. Acceptable values are described in “[Symbol Markers for HTML-Based Documentation](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/anchors/anchors.html#//apple_ref/doc/uid/TP40001215-CH347).” Arbitrary values are not allowed.
- __Scope__. The name of a namespace or container to which the symbol belongs. For example, the scope for most API symbols in object-oriented languages is the class or protocol in which the symbol is defined. API symbols that exist in a global namespace, such as data types or classes, do not have a scope.

For example, Listing 4-1 shows how you might construct the token identifier for the `NSArray` method `arrayWithContentsOfFile:` by listing each of its properties separately.

__Listing 4-1__  Specifying a token identifier with individual properties

```
<Token>
   <TokenIdentifier>
     <Name>arrayWithContentsOfFile:</Name>
     <APILanguage>occ</APILanguage>
     <Type>clm</Type>
     <Scope>NSArray</Scope>
   </TokenIdentifier>
</Token>
```

The contents of the token identifier for the `arrayWithContentsOfFile:` method are:

1. The `Name` element: Specifies the name of the method described by this token identifier, `arrayWithContentsOfFile:`.
2. The `APILanguage` element: Contains the string `occ`, which represents the Objective-C language, as defined in _[HeaderDoc User Guide](../HeaderDoc%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjv)_.
3. The `Type` element: Contains the string, `clm`, which identifies the `arrayWithContentsOfFile:` symbol as a class method. This and other values for the `Type` element are defined in _[HeaderDoc User Guide](../HeaderDoc%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjv)_.
4. The `Scope` element: Indicates that the scope of the `arrayWithContentsOfFile:` method is the `NSArray` class.

Another way to specify the token identifier for a symbol is to use a unique string that conforms to the specification in [Symbol Markers for HTML-Based Documentation](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/anchors/anchors.html#//apple_ref/doc/uid/TP40001215-CH347) in _[HeaderDoc User Guide](../HeaderDoc%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjv)_. These strings are known as _apple_ref_ strings, because they begin with the prefix `//apple_ref.`

As with the technique described in [Defining Tokens Using Individual Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvonq), an apple_ref string also uniquely identifies a symbol by listing the symbol’s name, programmatic type, and programming language context. Where appropriate, you can also specify the symbol’s containing scope, such as the name of the class in which a method is found.

Apple uses apple_ref strings in its own documentation sets to uniquely identify a symbol and mark the location of the symbol’s primary documentation. For example, the primary documentation for the `OpenMovieStorage` C function is marked by embedding the associated apple_ref string as a named anchor in the HTML files, as in the following example:

```
<a name="//apple_ref/c/func/OpenMovieStorage">OpenMovieStorage</a>
```

You can use the apple_ref format to specify token identifiers in the `Tokens.xml` file. Using the `arrayWithContentsOfFile:` method as an example again, you would specify an apple_ref identifier as shown in Listing 4-2.

__Listing 4-2__  Specifying a token identifier using an apple_ref string

```
<Token>
<TokenIdentifier>//apple_ref/occ/clm/NSArray/arrayWithContentsOfFile:</TokenIdentifier>
</Token>
```


The purpose of the tokens file is to associate symbols with a location within the documentation set. Therefore, after you have constructed a token identifier to uniquely identify a symbol, you need to specify the location of that symbol’s documentation.

To associate a token with a location, you:

1. Identify the node that represents the symbol’s documentation using the `NodeRef` element.

   This is useful when you’ve already defined a node that represents only the HTML files containing the symbol’s documentation.
2. Specify the path to the HTML file containing the symbol’s documentation, using the `Path` and `Anchor` elements, if the referenced node represents multiple symbols.

Listing 4-3 shows how you might use the `NodeRef` element to specify the location of a symbol’s documentation.

__Listing 4-3__  Referencing the documentation node for a token

```
<Token>
<TokenIdentifier>//apple_ref/occ/instm/NSArray/initWithArray:copyItems:</TokenIdentifier>
<NodeRef refid="22"> ```  ``` 
</Token>
```

The `refid` attribute of the `NodeRef` element identifies the documentation node that you are referencing. The value of this attribute should correspond to the value assigned to the target node’s `id` attribute in the `Nodes.xml` file. This attribute is described further in [Defining a Documentation Node](Configuring%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjrfvjvoni).

When referring to nodes that represent multiple symbols, you need to identify the HTML file that contains the symbol’s documentation using the `Path` and, if necessary, `Anchor` elements. The path specified is interpreted relative to the documentation set’s `Documents` directory. Listing 4-4 shows how you might specify the path to the documentation for the `NSArray` instance method `initWithArray:copyItems:`. In this example, the `Anchor` element specifies the location of an anchor marking the beginning of the symbol’s description.

__Listing 4-4__  Specifying the path to a symbol’s documentation

```
<Token>
<TokenIdentifier>//apple_ref/occ/instm/NSArray/initWithArray:copyItems:</TokenIdentifier>
<NodeRef refid="15"/>
<Path>documentation/Cocoa/Reference/NSArray.html</Path>
<Anchor>initWithArray:copyItems:</Anchor>
</Token>
```


One of the compelling features of Xcode’s documentation integration is the ability to provide context-sensitive information. Quick Help is one example of this ability. The user can select a symbol in the code editor and see additional information about that symbol in Quick Help.

If your documentation set includes a `Tokens.xml` file to support API lookup, you can also supply additional information about the tokens described therein, to allow you to take full advantage of features such as Quick Help.

The `Token` element allows a number of subelements that let you provide additional information—such as a declaration statement, version information and so forth—for a symbol. These are described in further detail in the following sections.

Documentation users commonly want access to the declaration statement for a symbol and a brief summary of what that symbol does when they are actively coding. You can provide this information for a token using the `Declaration` and `Abstract` elements, respectively. For symbols that represent methods or functions, you can also provide a summary of the parameters and the return value.

Listing 4-5 shows how you might use these elements to provide additional information about the `NSArray count` method.

__Listing 4-5__  Specifying a summary and declaration

```
<Token>
   <TokenIdentifier>//apple_ref/occ/instm/NSArray/indexOfObject:inRange:</TokenIdentifier>
   <Abstract>Returns the lowest index within a specified range whose corresponding array value is equal to a given object.</Abstract>
   <Declaration>- (NSUInteger)indexOfObject:(id)anObject inRange:(NSRange)range</Declaration>
   <Parameters>
     <Parameter>
        <Name>anObject</Name><Abstract type="html">An object.</Abstract>
     </Parameter>
     <Parameter>
        <Name>range</Name><Abstract type="html">The range of indexes in the receiver within which to search for anObject.</Abstract>
     </Parameter>
   </Parameters>
   <ReturnValue><Abstract>The lowest index within range whose corresponding array value is equal to anObject</Abstract></ReturnValue
</Token>
```


For tokens that represent an API symbol, you can provide information about the header in which the symbol is declared, using the `DeclaredIn` element. You specify header information using this element either by calling the components of the header location out explicitly or by specifying it as a path.

For symbols that are part of a framework, you can use the `HeaderPath` and `FrameworkName` subelements to explicitly call out the header file and framework name. Doing so allows Xcode to present the path to the symbol’s header file and the name of the framework that must be loaded to use the symbol as separate items.

Listing 4-6 shows how you would use this format to specify header file information for the `NSArray count` method.

__Listing 4-6__  Specifying header file information for a symbol

```
<Token>
<TokenIdentifier>//apple_ref/occ/instm/NSArray/count</TokenIdentifier>
<DeclaredIn>
<HeaderPath>/System/Library/Frameworks/Foundation.framework/Headers/NSArray.h</HeaderPath>
<FrameworkName>Foundation</FrameworkName>
</DeclaredIn>
</Token>
```

Alternatively, you can specify the path to the header file as a string directly within the `DeclaredIn` element. For example, if you don’t want to specify the framework name separately or the header file isn’t contained in a framework, you can restate the header file information for the `count` method as follows:

`<DeclaredIn>/System/Library/Frameworks/Foundation.framework/Headers/NSArray.h</DeclaredIn>`

You can provide availability information for a symbol—that is, information about the versions of a software product in which the symbol appears—using the `Availability` element. With it, you can specify when the symbol was introduced, when it became deprecated, and when it was removed from later versions.

You can specify version numbers using the following subelements of the `Availability` element:

- `IntroducedInVersion`. The first version of the product in which the symbol appears. This information is required.
- `DeprecatedInVersion`. For symbols whose use is no longer recommended, the first version of the product in which the use of the symbol is deprecated.
- `RemovedAfterVersion`. For symbols that have been removed from later versions of the product, the last version in which the symbol still appears.

For symbols that are deprecated or removed from the distribution, you can also provide a brief statement about that symbol’s status and other symbols that the user should use instead, using the `DeprecationSummary` element.

Listing 4-7 shows how you might provide version information for a token.

__Listing 4-7__  Specifying version information for a token

```
<Token>
  <TokenIdentifier>//apple_ref/occ/instm/NSArray/count</TokenIdentifier>
  <Availability distribution="OS X">
    <IntroducedInVersion>10.0</IntroducedInVersion>
    <DeprecatedInVersion>11.7</DeprecatedInVersion>
    <RemovedAfterVersion>11.9</RemovedAfterVersion>
    <DeprecationSummary>Replaced by newCount method.</DeprecationSummary>
  </Availability>
</Token>
```

Notice that version numbers are specified in the form `x.y.z`, where `x`, `y`, and `z` are integers: `x` specifies the major version number, `y` specifies the minor version number, and `z` specifies the maintenance version number. Only the major version number is required.

You must provide the name of the product to which the version information applies, using the `distribution` attribute. In the example shown in [Listing 4-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvomjz), the value of this attribute is “OS X.“ The `distribution` attribute is required.

If you have symbols whose version information is different for specific architectures, you can use the following attributes to contextualize the information in any of the version number elements—`IntroducedInVersion`, `DeprecatedInVersion`, and `RemovedAfterVersion`—for that architecture:

- `cputype`. This can be either `ppc` for the PowerPC architecture or `i386` for the Intel architecture.
- `bitsize`. This can be either `32` or `64`.

For example, imagine that the last version in which the `count` method appears differs for the PowerPC and Intel-based architectures. Listing 4-8 shows how you might specify the version information for this method.

__Listing 4-8__  Version information for multiple architectures

```
<Availability distribution="OS X">
     <IntroducedInVersion>10.0</IntroducedInVersion>
     <RemovedAfterVersion cputype="ppc">11.8</RemovedAfterVersion>
     <RemovedAfterVersion cputype="i386">11.9</RemovedAfterVersion>
</Availability>
```

Note that, in this case, you have multiple instances of the version element within a single `Availability` element. In the absence of architecture-specific version information, the availability information applies to all architectures. For example, Listing 4-8 specifies that the symbol was introduced in version 10.0 of the product for the `ppc32`, `ppc64`, `i386`, and `x86-64` architectures. After version 11.8 the symbol is not available for PowerPC architectures (both 32 bit and 64 bit). After version 11.9 the symbol is not available for any architecture.

Another type of information that users commonly want quick access to is a list of related resources, which they can consult to obtain further information about the symbol in question. You can provide this information for a symbol, using the following subelements of the `Token` element:

- `RelatedTokens`. Use this element to provide a list of other symbols that the reader may want to look at along with the current one.

  Each symbol in this list is identified using a `TokenIdentifier` element, as shown in Listing 4-9, and should correspond to a token definition in this or another tokens file in the documentation set.
- `RelatedDocuments`. Use this element to provide a list of documents, other than the symbol’s primary reference document, that give further information about or discussion of the current symbol.

  You specify an individual document in this list by referencing that document’s node, using the `NodeRef` element.
- `RelatedSampleCode`. Use this element to provide a list of documents containing examples and sample code that use the current symbol.

  You specify an individual piece of sample code in this list by referencing that document’s node, using the `NodeRef` element.

Listing 4-9 shows how you can use the elements described in this section to list related symbols and documents.

__Listing 4-9__  Specifying related symbols and documents

```
<Token>
  <TokenIdentifier>//apple_ref/occ/instm/NSArray/count</TokenIdentifier>
  <RelatedTokens>
    <TokenIdentifier>//apple_ref/occ/instm/NSArray/capacity</TokenIdentifier>
    <TokenIdentifier>
      <Name>objectAtIndex:</Name>
      <Scope>NSArray</Scope>
    </TokenIdentifier>
  </RelatedTokens>
  <RelatedDocuments>
    <NodeRef refid="17" />
  </RelatedDocuments>
  <RelatedSampleCode>
    <NodeRef refid="25" />
  </RelatedSampleCode>
</Token>
```

When using the `TokenIdentifier` element to reference an existing token, you need to specify only enough information to uniquely identify the token within your documentation set.

For large documentation sets, the number of token definitions in the tokens file can become unwieldy. There are several strategies you can use to reduce the amount of redundant information and make the large number of token definitions more manageable. You can:

- __Group token definitions according to the HTML file in which their associated documentation appears__. If your documentation set organizes the primary reference documentation for more than one symbol into a single HTML file, you can use this technique to avoid specifying the location of that file multiple times.
- __Define master lists of interrelated tokens__. If you have a group of symbols, each of which is related to all the other symbols in the group, you can simply specify a single list of interrelated tokens, rather than defining the list separately for each symbol.
- __Split symbol information into more than one tokens file__. A documentation set can have multiple tokens files; this allows you to split large sets of token definitions into more manageable chunks. You can separate symbol information based on the type of the information, programming language, or any other category that you choose.

The following sections describe these techniques in more detail.

For documentation sets that document a large number of symbols, it often makes sense to combine the documentation for multiple symbols into a single HTML file. For example, you might group documentation for API symbols in an object-oriented language according to the class to which those symbols belong.

When you do this, however, you may find that you have to specify the location of an HTML file multiple times, once for each symbol documented in that file, if you use the approach described in [Associating Symbols with API Reference Documentation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvomjw).

To eliminate this redundant information, you can group symbols according to the file in which they appear. To do so, you wrap the token definitions—the `Token` elements—for each symbol described in a given HTML file within a single `File` element.

When you specify a token definition inside of a `File` element, you do not need to specify the location of the HTML file separately for each token. Instead, you specify the path to the HTML file once, using the `path` attribute of the `File` element, as shown in Listing 4-10.

__Listing 4-10__  Grouping tokens by file

```
<File path="documentation/Cocoa/Reference/NSArray.html">
  <Token>
    <TokenIdentifier>//apple_ref/occ/cl/NSArray</TokenIdentifier>
  </Token>
  <Token>
    <TokenIdentifier>
      <Name>arrayWithContentsOfFile:</Name>
      <Type>clm</Type>
      <Scope>NSArray</Scope>
      <APILanguage>occ</APILanguage>
    </TokenIdentifier>
    <Anchor>arrayWithContentsOfFile:</Anchor>
  </Token>
  <Token>
    <TokenIdentifier>//apple_ref/occ/instm/NSArray/count</TokenIdentifier>
    <Anchor>count</Anchor>
  </Token>
</File>
```

To make sure that the Documentation window scrolls directly to the location of a symbol’s documentation when the user selects that symbol, you can specify an anchor location within the HTML file for that symbol’s token definition, using the `Anchor` element.

Although each symbol represented by a `Token` element can have its own list of related symbols, defining related symbols in this way only lets you specify a one-way relationship. The symbol described by the `Token` element is related to all of the symbols listed in the `RelatedTokens` subelement, but those symbols do not necessarily define the inverse relationship.

Often you will find that, for a given group of symbols dealing with a common area of functionality—hiding and showing a window, for example—the lists of related tokens for each symbol look very similar. If you list related tokens separately for each symbol in the group, you will end up repeating a lot of the same information more than once, bloating the tokens file and making the relationships hard to maintain.

You can instead take the simpler step of using the `RelatedTokens` element as a child of a `Tokens` element (the root of a tokens file) to create lists of interrelated symbols. Each symbol listed in this `RelatedTokens` element is related to all other symbols listed there. Listing 4-11 shows how you can use the `RelatedTokens` element as a subelement of the root element of the tokens file to specify a list of interrelated symbols.

__Listing 4-11__  Creating a list of related tokens

```
<Tokens>
<RelatedTokens title="Array Creation">
<TokenIdentifier>//apple_ref/occ/instm/NSArray/initWithArray:copyItems:</TokenIdentifier>
<TokenIdentifier>//apple_ref/occ/clm/NSArray/arrayWithContentsOfFile:</TokenIdentifier>
</RelatedTokens>
...
</Tokens>
```

Using this technique, rather than defining a list of related symbols for each individual token, you can eliminate a great deal of redundant information for large groups of interrelated symbols.

A documentation set is not limited to a single tokens file. The number of symbols documented in a single documentation set is potentially very large. In addition, there is a wide variety of information (which may come from a number of different sources) that can be associated with each token. Allowing multiple tokens files makes it possible to split this information into more manageable chunks.

The `docsetutil` tool looks for and processes all available XML files that are located in the documentation set’s `Resources` directory (or in the appropriate localized subfolder) and have names that start with the string “Tokens”. For example, you could create tokens files that divide the definitions of tokens into groups based on their programming language. In this case, your documentation set might have `Tokens-C.xml` and `Tokens-Java.xml` files.

Another possible way to divide tokens is to gather various types of information about the tokens in separate files. For example, you could have a file of abstracts, `Tokens-abstracts.xml`, and a file of documentation locations, `Tokens-files.xml`.

When the information for a single token is split across multiple `Token` elements, within the same file or across different files, `docsetutil` attempts to merge all the information for a single token together. If every token is uniquely identified by its `TokenIdentifier` element, the information for each token can be merged successfully. If there are tokens with duplicate identifiers in the documentation set, however, information in the duplicate records may be assigned to the wrong token.

If there is a file named `Tokens.xml`, `docsetutil` always processes that file first, followed by the remaining XML files in a case-sensitive alphabetical order.

The previous sections show how to construct individual token definitions, group token definitions according to file, and create lists of related tokens. Your tokens file can contain any number of these items—that is, of `Token`, `File`, and `RelatedTokens` elements—in any order. Listing 4-12 gives an example of a tokens file containing at least one of each of these items and shows how you might assemble them to create a complete tokens file. Note that the root element of the tokens file is the `Tokens` element.

__Listing 4-12__  An example tokens file

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Tokens version="1.0"> <!-- Root element -->
<!-- The File element groups symbols that are documented in a common HTML file--!>
<File path="documentation/Cocoa/Reference/NSArray.html">
  <Token>
    <TokenIdentifier>//apple_ref/occ/cl/NSArray</TokenIdentifier>
  </Token>
  <Token>
    <TokenIdentifier>
      <Name>arrayWithContentsOfFile:</Name>
      <Type>clm</Type>
      <Scope>NSArray</Scope>
      <APILanguage>occ</APILanguage>
    </TokenIdentifier>
  </Token>
  <Token>
    <TokenIdentifier>//apple_ref/occ/instm/NSArray/count</TokenIdentifier>
    <Abstract>Returns the number of objects in the array.</Abstract>
    <Declaration>- (unsigned)count;</Declaration>
    <DeclaredIn>
<HeaderPath>/System/Library/Frameworks/Foundation.framework/Headers/NSArray.h</HeaderPath>
      <FrameworkName>Foundation</FrameworkName>
    </DeclaredIn>
    <Availability distribution="OS X">
      <IntroducedInVersion>10.0</IntroducedInVersion>
      <DeprecatedInVersion>11.7</DeprecatedInVersion>
      <RemovedAfterVersion>11.9</RemovedAfterVersion>
      <DeprecationSummary>Replaced by newCount method.</DeprecationSummary>
    </Availability>
    <RelatedTokens>
      <TokenIdentifier>//apple_ref/occ/instm/NSArray/capacity</TokenIdentifier>
      <TokenIdentifier>
        <Name>objectAtIndex:</Name>
        <Scope>NSArray</Scope>
      </TokenIdentifier>
    </RelatedTokens>
    <RelatedDocuments>
      <NodeRef refid="17" />
    </RelatedDocuments>
    <RelatedSampleCode>
      <NodeRef refid="25" />
    </RelatedSampleCode>
  </Token>
</File>
<!-- You can also list token definitions individually, specifying a location for each --!>
<Token>
  <TokenIdentifier>//apple_ref/occ/instm/NSArray/initWithArray:copyItems:</TokenIdentifier>
  <Path>documentation/Cocoa/Reference/NSArray.html</Path>
  <Abstract>Initializes an instance from an array, optionally creating copies of the objects.</Abstract>
  <Availability distribution="OS X">
    <IntroducedInVersion>10.2</IntroducedInVersion>
  </Availability>
</Token>
<Token>
  <TokenIdentifier>//apple_ref/occ/instm/NSArray/initWithContentsOfFile:</TokenIdentifier>
  <NodeRef refid="22">
  <Availability distribution="OS X">
    <IntroducedInVersion>10.0</IntroducedInVersion/>
    <RemovedAfterVersion cputype="ppc">11.8</RemovedAfterVersion>
    <RemovedAfterVersion cputype="i386">11.9</RemovedAfterVersion>
  </Availability>
</Token>
<!-- If the same token identifier is used multiple times, the information in the token definition is merged together --!>
<Token>
  <TokenIdentifier>//apple_ref/occ/clm/NSArray/arrayWithContentsOfFile:</TokenIdentifier>
  <Availability distribution="OS X">
    <IntroducedInVersion>10.0</IntroducedInVersion>
  </Availability>
</Token>
<!-- Instead of defining related symbols for each individual token, use the RelatedTokens element at the root level to define a set of interrelated symbols --!>
<RelatedTokens title="Array Creation">
  <TokenIdentifier>//apple_ref/occ/instm/NSArray/initWithArray:copyItems:</TokenIdentifier>
  <TokenIdentifier>//apple_ref/occ/clm/NSArray/arrayWithContentsOfFile:</TokenIdentifier>
</RelatedTokens>
</Tokens>
```

[Next](Indexing%20Documentation%20Sets.md)[Previous](Configuring%20Documentation%20Sets.md)

