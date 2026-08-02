---
title: HeaderDoc User Guide
apple_id: TP40001215
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2016-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/anchors/anchors.html
archived_at: '2026-07-15T07:24:28.235414Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HeaderDoc User Guide](Introduction.md)


[Next](HeaderDoc%20Class%20Hierarchy.md)[Previous](HeaderDoc%20Release%20Notes.md)

# Symbol Markers for HTML-Based Documentation

As HeaderDoc generates documentation for a set of header files, it injects named anchors (`<a name=”marker”></a>`) into the HTML to mark the location of the documentation for each API symbol. This document describes the composition of these markers.

As you will see, each marker is self describing and can answer questions such as:

- What is the name of this symbol?
- What type of symbol is this (for example function, typedef, or method)?
- Which class does this method belong to?
- What is the language environment: C, C++, Java, Objective-C?

With this embedded information, the HTML documentation can be scanned to produce API lists for various purposes. For example, such a list could be used to verify that all declared API has corresponding documentation. Or, the documentation could be scanned to produce indexes of various sorts. The scanning script could as well create hyperlinks from the indexes to the source documentation. In short, these anchors retain at least some of the semantic information that is commonly lost when converting material to HTML format.

A _marker_ string is defined as:

`marker := prefix '/' lang-type '/' sym-type '/' sym-value`

A marker is a string composed of two or more values separated by a forward slash (`/`). The forward-slash character is used because it is not a legal character in the symbol names for any of the languages currently under consideration.

The prefix defines this marker as conforming to our conventions and helps identify these markers to scanners. The language type defines the language of the symbol. The symbol type defines some semantic information about the symbol, such as whether it is a class name or function name. The symbol value is a string representing the symbol.

Because the string must be encoded as part of a URL, it must obey a very strict set of rules. Specifically, any characters other than letters and numbers must be encoded as a URL entity. For example, the operator `+` in C++ would be encoded as `%2b`.

By default, the prefix is `//apple_ref`. However, the prefix string can be changed using HeaderDoc's configuration file.

The currently-defined language types are described in [Table B-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wugskiirdugqke).

__Table B-1__  HeaderDoc API reference language types

| `applescript` | AppleScript script |
| `c` | C header or source code |
| `cpp` | C++ header or source code |
| `doc` | Special namespace for documentation purposes. (Content should be considered unstructured except for the special forms noted in [Special API Reference Types in the doc Hierarchy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzv).) |
| `idl` | Interface Description Language file.  __Note:__ This value is the default value if no value for `IDLLanguage` is set in the configuration file. See [Basic HeaderDoc Configuration](Basic%20HeaderDoc%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawugrkhjjdeuskc) for more information. |
| `java` | Java header |
| `js` | JavaScript script  __Note:__ Some historical implementations used the string `javascript`. |
| `mig` | Mach Interface Generator interface description |
| `occ` | Objective-C header or source code |
| `pascal` | Pascal source code |
| `perl` | perl script |
| `php` | PHP script |
| `python` | Python script |
| `ruby` | Ruby script |
| `shell` | Bourne, Korn, Bourne Again, or C shell script |
| `tcl` | TCL script |

The language type defines the language binding of the symbol. Some logical symbols may be available in more than one language. The `c` language defines symbols which can be called from the C family of languages (C, Objective-C, and C++).

The symbol types common to all languages are described in [Table B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wugskijjcumr2k).

__Table B-2__  Symbol types for all languages

| tag | struct, union, or enum tag |
| `econst` | an enumerated constant—that is, a symbol defined inside an enum |
| `tdef` | typedef name (or Pascal `type`) |
| `macro` | macro name (without '()') |
| `data` | global, instance, or file-static data |
| `func` | function name (without '()') |

**`cat`**
: Category name (Objective-C only).

**`cl`**
: Class name.

__Note:__ In Perl, this is used for the names of packages, and thus the names may contain a double colon between parts of package names. For example:

```
//apple_ref/perl/cl/HeaderDoc::APIOwner
```

**`clconst`**
: Constant values defined inside a class. For example:

```
//apple_ref/java/clconst/ClassName/kConstantName
```

**`clm`**
: Class (or static [in java or c++]) method.

__Note:__ The formats for method names are described in [Objective-C (occ) Method Name Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzx) and [C++/Java (cpp/java) Method Name Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzz).

**`data`**
: Instance data. For example:

```
//apple_ref/cpp/data/MyClass/MyVariable
```

**`intf`**
: Interface or protocol name.

**`intfcm`**
: Class method defined in a protocol

__Note:__ The formats for method names are described in [Objective-C (occ) Method Name Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzx) and [C++/Java (cpp/java) Method Name Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzz).

**`intfm`**
: Method defined in an interface (or protocol).

__Note:__ The formats for method names are described in [Objective-C (occ) Method Name Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzx) and [C++/Java (cpp/java) Method Name Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzz).

**`intfp`**
: Property defined in an interface (or protocol)

```
//apple_ref/occ/intfp/ClassName/PropertyName
```

**`instm`**
: Instance method.

__Note:__ The formats for method names are described in [Objective-C (occ) Method Name Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzx) and [C++/Java (cpp/java) Method Name Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzz).

**`instp`**
: Instance property. For example:

```
//apple_ref/occ/instp/ClassName/PropertyName
```


**`tmplt`**
: C++ class template.

**`ftmplt`**
: C++ function template.

__Note:__ The format for this type is described in [C++/Java (cpp/java) Method Name Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzz).

**`func`**
: C++ scoped function (in other words, not extern 'C'); includes return type and signature as described in [C++/Java (cpp/java) Method Name Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzz), but with no class name. For example:

```
//apple_ref/cpp/func/funcName/returnType/(argType,argType,argType)
```


The format for method names for Objective-C is:

```
class_name '/' method_name
e.g.: //apple_ref/occ/instm/NSString/stringWithCString:
```

For methods in Objective-C categories, the category name is _not_ included in the method name marker. The class named used is the class the category is defined on. For example, for the `windowDidMove:` delegate method on `NSWindow`, the marker would be:

```
e.g.: //apple_ref/occ/intfm/NSObject/windowDidMove:
```


The format for an Objective-C protocol is:

```
class_name '/' protocol_name
e.g. //apple_ref/occ/instp/MyClass/MyProp
```


The format for method names for Java and C++ is:

```
    class_name '/' method_name '/' return_type '/' '(' signature ')'
e.g.: //apple_ref/java/instm/NSString/stringWithCString/NSString/(char*)
```

For Java and C++, signatures are part of the method name; signatures are enclosed in parentheses. The algorithm for encoding a signature is:

1. Remove the parameter name; for example, `change (Foo *bar, int i)` to `(Foo *, int )`.
2. Remove spaces; for example, change `(Foo *, int )` to `(Foo*,int)`.

The format for Interface Builder bindings is:

```
'binding' '/' class_name '/' binding_name
e.g. //apple_ref/occ/binding/myclass/mybinding
```


In general, the `doc` hierarchy should be considered to be an opaque blob of content. You should not count on the structure of a `doc` API reference. However, there are a few special subtypes within the `doc` space that are significant and should be used only for the stated purpose.

- `uid`—A unique identifier for a document. You may use values generated by `uuidgen` here. All other values are reserved for use by Apple.
- `title:...`—A HeaderDoc-specific hierarchy for special identifiers generated from the name portion of a HeaderDoc comment. These are generated when:

  - A name is specified in the HeaderDoc comment that does not match any parsed name.
  - A declaration is parsed that has no name (such as an anonymous enumeration) and the specified name contains spaces or other illegal characters.

  The complete name for this reference part depends on the name of the original data type. For example, a typedef would be:

```
//apple_ref/doc/title:tdef/Whatever
```

  Most of the time, if you see these in HeaderDoc output, it means that the name specified in a HeaderDoc comment is wrong.
- `enumconstant`, `functionparam`, `methodparam`, `defineparam`, `structfield`, `typedeffield`—Special reference types for fields within structures, parameters within functions, and so on. Appears at the relevant point in the documentation.

  These are rarely useful, but can be used in cases where, for example, a function has numerous parameters to link to a specific parameter in the list.

  The `enumconstant` field should only appear if a normal API reference marker (`econst`) does not, which means you are unlikely to actually see this marker type in practice.
- `anysymbol`—Valid in link requests _only_. A link request in this namespace causes the link resolver to look up the symbol by name instead of by API reference. For example, the link request:

```
//apple_ref/doc/anysymbol/MyProject
```

  would match any of the following API references:

```
//apple_ref/c/func/MyProject
//apple_ref/cpp/instm/MyClass/MyProject/bool/(char*,int)
//apple_ref/perl/data/MyProject
//apple_ref/java/cl/MyProject
```

  And so on. If more than one of these symbols exists, it matches the nearest symbol in the hierarchy (as determined by the number of leading absolute path parts).

When an API reference marker appears in a comment, it looks exactly like a normal API reference marker, with one exception: at any point where a slash appears, it is legal to precede that slash with a backslash. The reason for this can be demonstrated by the following symbol marker:

```
    //apple_ref/cpp/instm/MyClass/MyMethod/void*/(char*,int)
```

Notice that `*/` appears in the symbol marker, which would ordinarily end a comment in many programming languages. To fix this, you would tweak the symbol to look like this:

```
/* ...
    @link //apple_ref/cpp/instm/MyClass/MyMethod/void*\/(char*,int) ... @/link
 ...
 */
```

This prevents the compiler from choking on the API reference marker. HeaderDoc transparently removes the backslash when processing the marker.

HeaderDoc includes a tool called `resolveLinks` (in `/usr/bin` or `Xcode.app/Contents/Developer/usr/bin` beginning in 8.8, in `/System/Library/Perl/Extras/PERL_VERSION/HeaderDoc/bin` in previous versions) that is used for resolving cross-references for you Wherever a cross-reference appears, a link is generated if the destination exists.

The `resolveLinks` tool processes an entire tree of content in two passes. In the first pass, it locates destination anchors. These destination anchors look like this:

```
<a name="//apple_ref/..."></a>
```

Each of these `name` values is an identifier for an API symbol. The format for these identifiers is specified in [The Marker String](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzr).

In the second pass, `resolveLinks` searches for cross-references to these destinations. These cross-references can occur in one of two forms, depending on whether a destination is known to exist or not.

```
<a logicalPath=“//apple_ref/...“ href="path">foo</a>
<!-- a logicalPath=“//apple_ref/...“ -->
```

Each of these `logicalPath` values is then paired (if possible) with `name` values obtained during the first pass. If a destination exists for a cross-reference, `resolveLinks` inserts the relative path of the destination anchor in the cross-reference request’s `href` attribute. The result is that the cross-reference anchor is now a valid link to the requested destination anchor.

If the link exists and the cross-reference request is in the form of a comment, the `resolveLinks` tool changes the cross-reference request from a comment into an anchor (link) tag. Similarly, if the destination does not exist, it changes the cross-reference from an anchor tag to a comment tag. The result is that there should never be any broken links.

For the most part, this process is transparent to you as a user. There are two exceptions, however: cross-references between document sets and cross-references using multiple API reference prefixes (such as `apple_ref`).

In general, API references should not conflict. However, if two symbols with identical names and types occur in different namespaces, it is possible to have a conflict when you link together documentation that contains both namespaces.

When this occurs, HeaderDoc makes a best effort attempt at choosing the right match. For each potential link destination, HeaderDoc examines the path of the file containing that anchor and counts the number of leading path parts that match between that path and the path of the file that contains the link request. Then, HeaderDoc chooses the destination with the most matching path parts. (In the event of a tie, HeaderDoc typically chooses the first destination parsed, but you should not count on this ordering.)

If you use multiple API reference prefixes in a single tree of output content and want to link it together using `resolveLinks`, you must tell `resolveLinks` to look for all of the prefixes you care about. There are two ways to do this:

- Run `resolveLinks` manually, specifying the `-r` flag for each prefix. For example:

```
resolveLinks -r david_ref -r joe_ref /path/to/dir
```
- Specify a list of valid prefixes in your `headerDoc2HTML.config` file using the `externalAPIUIDPrefixes` option.

  __Note:__ This configuration file is read by `gatherHeaderDoc`, not by `resolveLinks`. Thus, this configuration file setting affects the behavior of `resolveLinks` _only_ when `resolveLinks` is run by `gatherHeaderDoc`, not when you run `resolveLinks` manually.

Whenever `resolveLinks` processes a tree, it generates a cross-reference file for that content. By default, it saves this file as `/tmp/xref_out`, but you can change this with the `-x` flag for later use.

If you want to process a tree in read-only mode (without writing back changes to the tree itself), you can specify the `-n` (no write) flag. In this mode, it will generate a cross-reference output file, but will not modify the HTML input files.

Beginning in HeaderDoc 8.8, `resolveLinks` supports additional flags to take advantage of these cross-reference files. Typically, you would use some combination of the `-s`, `-S`, `-b`, and `-i` flags.

These three flags are interrelated in subtle ways. The purpose of the complexity is so that you can construct links between two folders in such a way that the links will be valid after the folders are put into their final location. To that end, the flags provide prefix stripping and prepending.

It is easiest to explain these flags by providing an example of a common use case. You have two directories, A and B.

| Current location | Final location |
| --- | --- |
| `/Users/myusername/A` | `/Library/WebServer/Documents/Tools/A` |
| `/Users/myusername/B` | `/Library/WebServer/Documents/Utilities/B` |

To create these links, you would first generate cross-reference files for each folder like this:

```
resolveLinks -n -x /tmp/A.xrefs -b "$PWD/" "A"
resolveLinks -n -x /tmp/B.xrefs -b "$PWD/" "B"
```

The paths in the resulting cross-reference file are in the form `A/...` or `B/...`.

Next, you must actually resolve the links. This is where the other flags come into play.

```
resolveLinks -b "$PWD/" -s /tmp/B.xrefs -S "/Library/WebServer/Documents/Utilities/" -i "/Library/WebServer/Documents/Tools/" "A"
resolveLinks -b "$PWD/" -s /tmp/A.xrefs -S "/Library/WebServer/Documents/Tools/" -i "/Library/WebServer/Documents/Utilities/" "B"
```

You can pass in multiple pairs of `-s` and `-S` flags (up to a maximum of 1024) for additional flexibility. For each seed file, you must first use the `-s` flag to specify the location of the seed file itself, then use the `-S` flag to specify the location where the content described by that seed file will eventually be installed.

In addition to seed file paths, you should also use the `-i` flag to tell `resolveLinks` where the folder you are processing will eventually be installed. Note that as before, the `-b` flag determines what portion to strip from each path in the folder you are processing, and that the trailing slash in the `-b` flag is significant here as well.

In effect, you can think of the flags like this:

- `-b`—Strips off leading path parts from the folder you are _currently_ processing. The last path part is stripped _only_ if followed by a trailing slash.
- `-i`—Adds leading path parts to the folder you are _currently_ processing (representing the proposed final install location).
- `-S`—Adds leading path parts to folders processed _previously_ and imported from a seed file (representing their proposed final install locations).

Finally, if desired, you can pass the `-a` flag to tell `resolveLinks` to use absolute paths instead of relative paths when linking to the content described by a particular seed file or by all seed files. Like the `-S` flag, if passed before the first `-s` flag, the `-a` flag modifies the linking behavior globally. Otherwise, it modifies only the linking behavior for the preceding `-s` flag.

For more information, see the manual page for `resolveLinks`.

[Next](HeaderDoc%20Class%20Hierarchy.md)[Previous](HeaderDoc%20Release%20Notes.md)

