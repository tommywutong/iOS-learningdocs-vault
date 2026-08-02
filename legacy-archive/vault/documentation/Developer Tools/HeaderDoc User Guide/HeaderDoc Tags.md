---
title: HeaderDoc User Guide
apple_id: TP40001215
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2016-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/tags/tags.html
archived_at: '2026-07-15T07:24:28.319730Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HeaderDoc User Guide](Introduction.md)


[Next](Basic%20HeaderDoc%20Configuration.md)[Previous](Using%20HeaderDoc.md)

# HeaderDoc Tags

Tags, depending on type, generally require either one field of information or two:

- `@function` [FunctionName]
- `@param` [parameterName] [Some descriptive text...]

In the tables in this chapter, the “Fields” column indicates the number of textual fields each type of tag takes.

HeaderDoc comments in C and C-like languages (Java, JavaScript, IDL, PHP, and MIG) are of the form:

```

/*!
 This is a comment about FunctionName.
*/
char *FunctionName(int k);
```

In their simplest form (as above) they differ from standard C comments only by the addition of the `!` character next to the opening asterisk.

In AppleScript and Pascal, the syntax is almost identical except for the comment markers:

__Listing 2-1__  AppleScript comment example

```
(*! This is a comment about FunctionName. *)
on FunctionName(x,y)
    ...
end FunctionName
```


__Listing 2-2__  Pascal comment example

```
{! This is a comment about FunctionName. }
procedure FunctionName(a, b: String; j: Integer): Char;
begin
    ...
end;
```

In Perl, Tcl, and shell scripts, the syntax is slightly altered because of the lack of multi-line comments and the need to avoid conflicting with the shell magic (`#!`) syntax. Shell script and Perl script HeaderDoc comments look like this:

__Listing 2-3__  Perl comment example

```
# /*!
#     This is a comment about FunctionName.
#  */
sub FunctionName($$)
{
    ...
}
```


__Listing 2-4__  Shell comment example

```
# /*!
#     This is a comment about FunctionName.
#  */
FunctionName()
{
    ...
}
```

Similarly, Ruby and Python syntax do not lend themselves to a start-of-comment marker followed by a single exclamation point, so their comments look like this:

__Listing 2-5__  Ruby comment example

```
=begin
    !headerDoc!
    This is a comment about FunctionName.
=end
def FunctionName(arg)
    ...
end
```


__Listing 2-6__  Python comment example

```
"""
    !headerdoc!
    This is a comment about FunctionName.
"""
def FunctionName(x):
   ...
```

Historically, HeaderDoc tags were required to begin with an introductory tag that announces the type of API being commented (`@function`, below). You can find a complete list of these tags in [Groups of Declarations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzugywvgvzr). Beginning in HeaderDoc 8, these top-level tags became optional. However, providing these tags can, in some cases, be used to cause HeaderDoc to document something in a different way. One example of this is the use of the `@class` tag to modify the markup of a typedef, as described in [Overriding the Default Data Type: C Pseudoclass Tags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzugywugskiirbusr2d).

The following example shows the historical syntax:

```
/*!
 @function FunctionName
 This is a comment about FunctionName.
*/
char *FunctionName(int k);
```

Following the optional top-level `@function` tag, you typically provide introductory information about the purpose of the class. You can divide this material into a summary sentence and in-depth discussion (using the `@abstract` and `@discussion` tags), or you can provided the material as an untagged block of text, as the examples below illustrate. You can also add `@throws` tags to indicate that the class throws exceptions or add an `@namespace` tag to indicate the namespace in which the class resides.

__Listing 2-7__  Example of documentation with @abstract and @discussion tags

```
/*!
     @class IOCommandGate
     @abstract Single-threaded work-loop client request mechanism.
     @discussion An IOCommandGate instance is an extremely light weight mechanism that
         executes an action on the driver's work-loop...
     @throws foo_exception
     @throws bar_exception
     @namespace I/O Kit (this is just a string)
     @updated 2003-03-15
 */
class IOCommandGate: public IOEventSource
{
...
}
```


__Listing 2-8__  Example of documentation as a single block of text

```
/*!
     @class IOCommandGate
     A class that defines a single-threaded work-loop client request mechanism. An IOCommandGate
     instance is an extremely light weight mechanism that executes an action on the driver's work-loop...
     @abstract Single-threaded work-loop client request mechanism.
     @throws foo_exception
     @throws bar_exception
     @updated 2003-03-15
*/
class IOCommandGate: public IOEventSource
{
...
}
```

You can also use additional JavaDoc-like tags within the HeaderDoc comment to identify specific fields of information. These tags will make the comments more amenable to conversion to HTML. For example, a more complete comment might look like this:

```

/*!
     @function HMBalloonRect
     @abstract Reports size and location of help balloon.
     @discussion Use HMBalloonRect to get information about the size of a help balloon
         before the Help Manager displays it.
     @param inMessage
        The help message for the help balloon.
     @param outRect
        The coordinates of the rectangle that encloses the help message.
        The upper-left corner of the rectangle has the coordinates (0,0).
 */
```

Tags are indicated by the `@` character, which must generally appear as the first non-whitespace character on a line (with a few notable exceptions). If you need to include an at sign in the output (to put your email address in a class discussion, for example), you can do this by prefixing it with a backslash, that is, `\@`. (If you forget the backslash, to the extent that it is possible to do so, HeaderDoc ignores unknown tags and treats them as though you had quoted the `@` characters, but it does produce a warning. Because new tags are periodically added, you should not count on this behavior.)

The first tag in a comment announces the API type of the declaration (`function`, `struct`, `enum`, and so on). This tag is optional. If you leave it out, HeaderDoc will pick up this information from the declaration immediately following the comment.

The next two lines (tagged `@abstract` and `@discussion`) provide documentation about the API element as a whole. The abstract can be used in summary lists, and the discussion can be used in the detailed documentation about the API element.

The abstract and discussion tags are optional, but encouraged. Their use enables various improvements in the HTML output, such as summary pages. However, if there is untagged text following the API type tag and name (`@function HMBalloonRect`, above) it is assumed to be a discussion. With such untagged text, HeaderDoc assumes that the discussion extends from the end of the API type tag to the next HeaderDoc tag or to the end of the HeaderDoc comment, whichever occurs first.

HeaderDoc understands some variants in commenting style. In particular, you can have a one-line comment like this:

```

/*! @var settle_time Latency before next read. */
```

Be sure, however, to understand the difference between the above syntax and the following, which is treated as a multiword name (described in [Multiword Names](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzugywugskiirbeqrcd)):

```

/*! @enum my favorite enumeration
    This is the discussion here.
 */
```

You can also use leading asterisks on each line of a multiline comment (but you must use them consistently):

```

/*!
 * @function HMBalloonRect
 * @abstract Reports size and location of help ballon.
 * @discussion Use HMBalloonRect to get information about the size of a help balloon
 * before the Help Manager displays it.
 * @param inMessage The help message for the help balloon.
 * @param outRect The coordinates of the rectangle that encloses the help message.
 * The upper-left corner of the rectangle has the coordinates (0,0).
 */
```

If you want to specify a line break in the HTML version of a comment, use two newline characters between lines rather than one. For example, the text of the discussion in this comment:

```

/*!
 * @function HMBalloonRect
 * @discussion Use HMBalloonRect to get information about the size of a help balloon
 * before the Help Manager displays it.
 *
 * Always check the help balloon size before display.
 */
```

will be formatted as two paragraphs in the HTML output:

`OSErr HMBalloonRect (const HMMessageRecord *inMessage, Rect *outRect);`

Use HMBalloonRect to get information about the size of a help balloon before the Help Manager displays it.

Always check the help balloon size before display.

Top-level HeaderDoc tags, such as `@header` and `@function` can take multiword names. This is particularly useful for documenting anonymous types for enumerations, for example. However, HeaderDoc normally has no way to know whether a line containing multiple words is a multiword name or a name followed by a discussion.

There are two ways to get a multiword name. One way is to add an explicit discussion tag (which may be empty), like this:

__Listing 2-9__  Example of multiword names using @discussion

```
/*!
 * @enum example enum
 * @discussion This is a test, this is only a test.
 *
 * Because we included an \@discussion tag, the name of the enum is
 * “example enum”.
 */
```

The other way is to simply add a line break and additional discussion (which may _not_ be empty) after the name.

__Listing 2-10__  Example of multiword names using multiple lines

```
/*!
 * @enum example enum
 * Because the discussion continues on a second line,
 * the name of the enum is "example enum".
 */
```


Beginning in HeaderDoc 8, certain tags are often not needed. These include:

**Numbered lists**
: It is no longer necessary to mark up numbered lists with `<ol><li>`. HeaderDoc will automatically detect numbered lists.

**Declaration types**
: Declaration type tags such as `@function`, `@class`, and `@typedef` are no longer required unless you are trying to override HeaderDoc’s normal behavior (such as using `@class` or `@interface` to change the display of a `typedef struct`.

**Availability macros**
: It is no longer necessary to ignore availability macros with `@ignore`. The file `Availability.list` in the HeaderDoc modules directory contains a mapping of availability macros to strings. When any macros described in this file appear in a declaration, the corresponding text will automatically be added to its documentation as an availability attribute.

You can add your own availability macros by adding them to the `Availability.list` file or by adding an `@availabilitymacro` block in your headers.

HeaderDoc tags can be grouped into two broad categories: top-level tags and second-level tags. Top-level tags describe the type of declaration that follows. For example, `@method` indicates that the following declaration is a method. All other tags are second-level tags.

Top-level HeaderDoc tags tell HeaderDoc what API type to expect after the declaration. These trace their roots back to HeaderDoc 7 and prior releases in which HeaderDoc could not interpret a declaration without these hints.

In HeaderDoc 8 and later, top-level tags are almost always optional (except for tags that are not tied to a declaration, such as `@header` or `@group`). Some top-level tags provide useful features, however—declaring new availability macros, treating one type of declaration as another type, and so on.

Most top-level HeaderDoc tags are treated as a term and definition list. This means that if you specify multiple words on a single line, the first word is treated as the name, and the remaining words are treated as the discussion. However, if the arguments span multiple lines, the entire first line is treated as a multi-word title. Similarly, if you specify an `@discussion` tag explicitly, the entire first line is treated as a multi-word title. For more information, see [Multiword Names](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzugywugskiirbeqrcd).

Group tags (`@functiongroup`, `@group`, and `@methodgroup`) always treat the remainder of the line as a multi-word name.

If you include a top-level tag, it _must_ appear at the beginning of the HeaderDoc comment. These tags represent declaration types. For example, the `@function` tag tells HeaderDoc that you are about to declare a function. These tags are optional, and are generally discouraged because they tend to cause frequent mistakes.

Second-level tags give HeaderDoc additional information about the declaration, such as specifying an abstract or a parameter description.

The set of second-level tags can be further divided up based on their behavior:

- __attribute__—A tag whose contents appear as an line in a table or list of attributes. Attribute tags continue until the next block or attribute tag; however, you should generally keep their contents short.
- __block__—A tag that can contain multiple paragraphs of text and is usually displayed as a normal block of text (often prefaced by a heading). Block tags continue until the next block or attribute tag.
- __flag__—A tag that modifies the behavior of a tagged declaration, including whether or not to emit it under certain circumstances (`@parseOnly`, for example). Flag tags take no arguments.
- __HTML tagging__—A tag that affects HTML tagging and is not directly emitted as part of the output.
- __inline__—A tag that can appear within a paragraph inside most tags (except for name or title fields). The contents of an inline tag do not break the text flow.
- __page footer__—A tag that modifies content that appears in the footer at the bottom of each content page (`@copyright`, for example).
- __parsing__—A tag that modifies the way the source code file is parsed.
- __term & definition__—A tag whose contents get split into two parts at the first space or newline, depending on whether the tag contains one or more lines of content. These tags are split according to the same rules as top-level tags. The splitting rules are described in [Multiword Names](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzugywugskiirbeqrcd)

In HeaderDoc 8.6 and later, second-level tags can appear anywhere in a HeaderDoc comment. (In HeaderDoc 8.5 and earlier, comments must begin with either a top-level tag or an untagged discussion.)

There are three exceptions, however: the `@const`, `@constant`, and `@var` tags. These tags cannot appear at the beginning of a HeaderDoc comment because they conflict with top-level tags.

The tags in the table below can be used in any comment for any data type, function, header, or class.

__Table 2-1__

| Tag | Example | Identifies | Usage |
| `@abstract` | `@abstract write the track to disk` | A short string that briefly describes a function, data type, and so on. This should not contain multiple lines (because it will look odd in the mini-TOCs). Save the detailed descriptions for the discussion tag. | block  (single short sentence recommended) |
| `@apiuid` | `@apiuid //my_ref/doc/magic` | Overrides the API UID (`apple_ref`) associated with this comment.  Note that very little checking is performed on this string. Thus, this tag has the potential to seriously break your output if used incorrectly. It is primarily provided for resolving symbol collisions that are otherwise unavoidable, and is generally discouraged. | attribute  Must contain no spaces, and must be a valid API reference. See [Symbol Markers for HTML-Based Documentation](Symbol%20Markers%20for%20HTML-Based%20Documentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wueqkcjjeumrse) for details. |
| `@attribute`  `@attributelist`  `@attributeblock` | See [Adding Arbitrary Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzugywvgvzs). | Adds arbitrary attributes. | attribute (short, term & definition list, or block) |
| `@availability` | `@availability 10.3 and later` | A string that describes the availability of a function, class, and so on. | attribute |
| `@brief` | `@brief write the track to disk` | Equivalent to @abstract. Provided for better Doxygen compatibility. | block  (single short sentence recommended) |
| `@discussion` | `@discussion This is what this function does. @some_other_tag` | A block of text that describes a function, class, header, or data type in detail. This may contain multiple paragraphs. `@discussion` may be omitted, as described above.  `@discussion` must be present if you have a multiword name for a data type, function, class, or header.  An `@discussion` block ends only when another block begins, such as an `@param` tag. | block |
| `@indexgroup` | `@indexgroup Name of Group` | Provides grouping information within the master TOC (landing page).  In the absence of an @indexgroup tag, the index group is inherited from the enclosing class or header. | block (short strings, please) |
| `@internal` | `@internal` | Marks the declaration as internal documentation. Such documentation is emitted only if the `--document-internal` flag is specified on the command line.  __Note:__ The declaration may still modify other declarations in the case of `#define` macros with C preprocessing enabled. | Flag (takes no arguments). |
| `@link` | `@link //apple_ref/c/func/function_name link text goes here @/link`  _or_  `@link function_name link text goes here @/link`  _or_  `@link function_name @/link` | Allows you to insert a link request for an API ref. See [Creating Links Between Symbols](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzugywvgvzwgy) for more information. | inline |
| `@namespace` | `@namespace BSD Kernel` | String describing the namespace in which the function, data type, etc. exists. | attribute |
| `@see` | `@see apple_ref Title for link` | Adds a “See:” entry to the attributes. Arguments are the same as `@link`. Note that this tag is ignored if the API reference marker already appears in the see or see also list. | attribute |
| `@seealso` | `@seealso apple_ref Title for link` | Adds a “See Also:” entry to the attributes. Arguments are the same as `@link`. Note that this tag is ignored if the API reference marker already appears in the see or see also list. | attribute |
| `@textblock` | `@textblock My text goes here @/textblock` | Treat everything until the trailing `@/textblock` as raw text, preserving initial spaces and line breaks, and converting “<” and “>” to “<” and “>”.  __Note:__ This tag does not automatically insert `<pre>` or `<tt>`. You may wrap it with whatever formatting you choose. | inline |
| `@updated` | `@updated 2003-03-14` | The date at which the header was last updated. | attribute |

In addition, HeaderDoc supports some common JavaDoc and Doxygen synonyms for other tags: `@since` (`@availability`), `@details` (`@discussion`), and `@description` (`@discussion`)

HeaderDoc handles comments differently based on the declaration that follows them. Although most tags are valid in any HeaderDoc comment, there are a few tags that only make sense in certain contexts. For example, a method can have parameters, but a class cannot.

This section describes each type of HeaderDoc comment, and provides a list of second-level tags that are specific to that comment type.

__Top-level tag:__ `@framework`

The `@framework` tag is used to describe a set of related headers. You should put this framework documentation into a file whose name ends with `.hdoc`. When you run `headerdoc2html` on such a file, it generates a documentation tree with special hidden markup that `gatherheaderdoc` then parses and uses while generating the landing page (master TOC).

Frameworks tags must contain an `@framework` tag that provides a human-readable (long) name for the framework that `gatherheaderdoc` inserts wherever the `$$framework@@` tag appears in the landing page template.

The following tags are specific to frameworks:

__Table 2-2__

| Tag | Example | Identifies | Type |
| `@frameworkcopyright` | `@frameworkcopyright 2010 Somebody Else.` | The copyright info for the header. | attribute |
| `@frameworkpath` | `@frameworkpath /System/Library/Frameworks/Kernel.framework` | The path to the framework. | attribute |
| `@frameworkuid` | `@frameworkuid myCustomUID` | Specifies a unique ID that `gatherHeaderDoc` inserts as part of a special anchor when building the main TOC. (This is not particularly useful externally, but is included for completeness.) | attribute |
| `@headerpath` | `@headerpath /blah/blah/blah.framework/Headers` | Provides the path to the `Headers` folder inside the framework. | attribute |

For example:

```
/*! @framework Kernel Framework Reference
    @abstract
    @discussion The Kernel Framework provides the APIs and support for
    kernel-resident device drivers and other kernel extensions.
    It defines the base class for I/O Kit device drivers (IOService),
    several helper classes, and the families supporting many types
    of devices.
    @frameworkpath /System/Library/Frameworks/Kernel.framework
    @frameworkuid TP30000816
    @seealso //apple_ref/doc/uid/TP0000011 I/O Kit Fundamentals
    @seealso //apple_ref/doc/uid/TP30000905-CH204 Kernel Programming
 */
```


__Top-level tags:__ `@header`, `@file`

Often, you'll want to add a comment for the header as a whole in addition to comments for individual API elements. For example, if the header declares API for a specific manager (in Mac OS terminology), you may want to provide introductory information about the manager or discuss issues that apply to many of the functions within the manager's API. Likewise, if the header declares a C++ class, you could discuss the class in relation to its superclass or subclasses.

In general, you should not specify a filename in the `@header` tag. However, if you do, the value you give for the `@header` tag serves as the title for the HTML pages generated by `headerdoc2html` (unless you pass the `-n` or `-N` flag, in which case it is ignored).

The discussion for the `@header` tag is used as the introduction.

Note that you must follow `@header` by a line break; otherwise, the first line of your documentation will be treated as if it were the name of the header.

The following tags are specific to header and source file comments:

| Tag | Example | Identifies | Type |
| --- | --- | --- | --- |
| `@author` | `@author Anon E. Mouse` | The author of the header. | attribute |
| `@charset` | `@charset utf-8` | Sets the character encoding for generated HTML files (same as `@encoding`). | HTML tagging |
| `@compilerflag` | `@compilerflag -lssl` | Compiler flag that should be set when using functions and types in this header. | attribute (term & definition) |
| `@copyright` | `@copyright Apple` | Copyright info to be added to each page. This overrides the config file value and may not span multiple lines. | page footer |
| `@CFBundleIdentifier` | `@CFBundleIdentifier org.mklinux.driver.test` | Which kernel subcomponent, loadable extension, or application bundle contains this header | attribute |
| `@encoding` | `@encoding utf-8` | Sets the character encoding for generated HTML files (same as `@charset`). | HTML Tagging |
| `@flag` | `@flag -lssl`  `The SSL Library` | Same as `@compilerflag`. | attribute (term & definition) |
| `@ignore` | `@ignore API_EXPORT` | Tells HeaderDoc to delete the specified token. | parsing |
| `@ignorefuncmacro` | `@ignorefuncmacro __P` | Tells HeaderDoc to unwrap occurrences of the specified function-like macro. | parsing |
| `@language` | `@language c++` | __Deprecated.__ Sets the current programming language. | parsing |
| `@meta` | `@meta robots index,nofollow`  _or_  `@meta http-equiv=”refresh” content=”0;http://www.apple.com”` | Meta tag info to be added to each page. This can be either in the form `@meta <name> <content>` or `@meta <complete tag contents>`, and may not span multiple lines. | HTML tagging |
| `@preprocinfo` | `@preprocinfo This header uses the DEBUG macro to enable additional debugging.` | Description of behavior when preprocessor macros are set (`-DDEBUG`, for example). | block |
| `@related` | `@related Sixth cousin of Kevin Bacon.` | Indicates another header that is related to this one. You may use multiple `@related` tags.  Similar to the `@seealso` tag. | attribute (term & definition) |
| `@unsorted` | `@unsorted` | Indicates that you do not want HeaderDoc to alphabetize the contents of this header. | flag |
| `@version` | `@version 2.3.1` | the version number to which this documentation applies. | attribute |
| `@whyinclude` | `@whyinclude Because it was there.` | Indicates why you should include the header. | attribute |

__Listing 2-11__  Example of `@header` tag

```

/*!
     @header Repast Manager
     The Repast Manager provides a functional interface to the repast driver.
     Use the functions declared here to generate, distribute, and consume meals.
     @copyright Dave's Burger Palace
     @updated 2003-03-14
     @meta http-equiv=”refresh” content=”0;http://www.apple.com”
 */
```


__Top-level tags:__ `@class`, `@interface`, `@protocol`, `@category`, `@template`

HeaderDoc supports a number of tags specific to classes, interfaces, protocols, and packages:

| Tag | Example | Identifies | Type |
| --- | --- | --- | --- |
| `@classdesign` | `@classdesign Multiple paragraphs go here.` | Description of any common design considerations that apply to this class, such as consistent ways of handling locking or threading. | block  in class declarations only |
| `@coclass` | `@coclass myCoClass Description of how class is used` | Class with which this class was designed to work. | attribute (term & definition)  in class declarations only |
| `@dependency` | `@dependency This depends on the FooFramework framework.` | External resource that this class depends on (such as a class or file). | attribute  in class declarations only |
| `@deprecated` | `@deprecated in version 10.4` | String telling when the function, data type, etc. was deprecated. | attribute  in class declarations only |
| `@helper` or `@helperclass` | `@helper myHelperClass`  `Description of how class is used.` | A helper class used by this class. | attribute (term & definition)  in class declarations only |
| `@helps` | `@helps This class provides additional stuff that does something.` | If this is a helper class, a short description of classes that this class was designed to help. | attribute  in class declarations only |
| `@instancesize` | `@instancesize Eight hundred megabytes and constantly swapping.` | The typical size of each instance of the class. | attribute  in class declarations only |
| `@ownership` | `@ownership MyClass objects are owned by the MyCreatorClass object that created them.` | Describes the ownership model to which this class conforms. | block  in class declarations only |
| `@performance` | `@performance This class is strongly discouraged in high-performance contexts.` | Describes special performance characteristics for this class. | block  in class declarations only |
| `@security` | `@security This class is feeling insecure today.` | Describes security considerations associated with the use of this class | block  in class and header declarations only |
| `@superclass` | `@superclass fasterThanASpeedingRuntime` | Overrides superclass name—see note below. | attribute  in class declarations only |
| `@templatefield` | `@templatefield base_type The base type to store in the linked list.` | Each of the function’s template fields (C++). | attribute (term & definition)  in C++ class declarations only |
| `@unsorted` | `@unsorted` | Indicates that you do not want HeaderDoc to alphabetize the contents of this class. | flag |
| `@var` | `@var myVar`  `Description goes here` | Used to document an instance variable in Perl.  __Note:__ Because this tag has the same name as a top-level tag, it cannot be the first tag in the HeaderDoc comment for a class. | Term & definition  Valid only for Perl packages. |

Here are some examples of classes in Objective-C:

__Listing 2-12__  Example of @class tag in Objective-C

```objc
/*!
     @class myInterface
     @discussion This is a discussion.
     It can span many lines or paragraphs.
*/
@interface myInterface : NSObject
@end
```


__Listing 2-13__  Example of @protocol tag in Objective-C

```objc
/*!
     @protocol myProtocol
     @discussion This is a discussion.
     It can span many lines or paragraphs.
*/
@protocol myProtocol
@end
```


__Listing 2-14__  Example of @category tag in Objective-C

```objc
/*!
 @category myMainClass(myCategory)
 @discussion This is a discussion.
 It can span many lines or paragraphs.
*/
@interface myMainClass(myCategory)
@end
```


__Listing 2-15__  Example of @class tag in C++

```
/*!
 @class myClass
 @discussion This is a discussion.
 It can span many lines or paragraphs.
*/
 class myClass : public mySuperClass;
```


__Listing 2-16__  Example of @templatefield tag

```
/*! @class mystackclass
    @templatefield Tthe data type stored in this stack */

 template <T> class mystackclass
```


__Top-level tags:__ `@functiongroup`, `@methodgroup`, `@group`

Grouping tags allow you to organize functions, methods, and variables into collections. In HTML output mode, the table of contents (left column) is organized into these groups. Also, the body content (right side) contains a documentation for each group. That documentation block contains the group’s name, discussion, and a list of any functions, data types, or variables contained within that group, along with their abstracts.

The `@group` tag provides grouping for all API elements except for methods and functions. In addition, until HeaderDoc encounters an `@functiongroup` or `@methodgroup` tag, functions and methods are also grouped by the `@group` tag. In effect, the `@functiongroup` or `@methodgroup` tag provides a way to override the `@group` tag in a way that only affects functions and methods.

Grouping tags remain in effect until the next grouping tag of the same type.

If you need to put functions or other API elements in different parts of the header into the same group, simply give them the same name (with the same capitalization, punctuation, spacing, etc.), and HeaderDoc merges the two function groups into one. (Omit the discussion after the first occurrence.)

Any functions or other API elements encountered before the first `@group` or `@functiongroup` are considered part of the “empty” group. These functions are listed before any grouped functions or API elements.

__Listing 2-17__  Example of group tags

```
/*!
 @functiongroup Core Functions
*/
/*!
 @methodgroup Core Methods
*/
/*!
 @group Core API
*/
```


__Top-level tags:__ `@function`, `@method`, `@callback`

Functions, methods, and callbacks have a number of special second-level tags:

| Tag | Example | Identifies | Type |
| --- | --- | --- | --- |
| `@param` | `@param myValue The value to process.` | The name and description of a parameter to a function or callback. | attribute (term & definition) |
| `@result` | `@result Returns 1 on success, 0 on failure..` | Describes the return values expected from this function.  Don't include if the return value is `void` or `OSERR`. | attribute (term & definition) |
| `@return` | `@return Returns 1 on success, 0 on failure..` | Same as `@result`. | attribute (term & definition) |
| `@templatefield` | `@templatefield base_type The base type to store in the linked list.` | Each of the function’s template fields (C++). | attribute (term & definition)  in C++ method declarations only |
| `@throws` | `@throws bananas` | Include one `@throws` tag for each exception thrown by this function (in languages that support exceptions). | attribute |
| `@var` | `@var myVar`  `Description goes here` | Documents a local variable in a function or method.  You can suppress local variables in the output by passing the `-L` flag to `headerdoc2html`.  __Note:__ Because this tag has the same name as a top-level tag, it cannot be the first tag in the HeaderDoc comment for a function or method. | Term & definition |

__Listing 2-18__  C function example

```
/*!
    This is a function.
    @param parmA
        Parameter A.
    @param parmB
        Parameter B.
    @result
        Returns something unexpected.
 */
SpanishInquisition *myFunction(char *parmA, int parmB);
```


__Listing 2-19__  Objective-C method example

```objc
/*!
    This is an objective-C method.
    @param parmA
        Parameter A.
    @param parmB
        Parameter B.
    @result
        Results in global warming.
 */
- (CO2 *)doSomething:(typeName)parmA withSomething:(typeName)parmB;
```


__Top-level tag:__ `@var`, `@const`, `@constant`

The `@var` tag should be used when marking up global variables, class variables, and instance variables (as opposed to declarations of new data types or macros).

Variables that are immutable (`const` in C, for example) should be marked with `@const` or `@constant`.

Variable and constant declarations have no special second-level tags associated with them.

__Listing 2-20__  Example of @const tag

```
 /*!
     @const kCFTypeArrayCallBacks
     @abstract Predefined CFArrayCallBacks structure containing a set of callbacks appropriate...
     @discussion Extended discussion goes here.
         Lorem ipsum....
 */
const CFArrayCallBacks kCFTypeArrayCallBacks;
```


__Listing 2-21__  Example of @var tag

```
/*!
     @var we_are_root
     @abstract Tells whether this device is the root power domain
     @discussion TRUE if this device is the root power domain.
         For more information on power domains....
 */

bool we_are_root;
```


__Top-level tag:__ `@property`

In Objective-C, a property is a special variable that also includes getter and setter methods. It supports any tag that is supported by `@method` or `@var`.

__Top-level tags:__ `@struct`, `@union`, `@typedef`

Structures, unions, and `typedef` declarations containing structures and unions can contain callbacks and fields. The corresponding second-level tags are described below.

| Tag | Example | Identifies | Type |
| --- | --- | --- | --- |
| `@callback` | `@callback testFunc The test function to call.` | Specifies the name and description of a callback field in a structure. | attribute (term & definition) |
| `@field` | `@field isOpen` `Specifies whether the file descriptor is open.` | A field in a structure declaration. | attribute (term & definition) |

__Listing 2-22__  Example of a structure

```
/*!
     @struct TableOrigin
     @abstract Locates lower-left corner of table in screen coordinates.
     @field x Point on horizontal axis.
     @field y Point on vertical axis
     @discussion Extended discussion goes here.
         Lorem ipsum....
*/
struct TableOrigin {
 int x;
 int y;
}
```


__Top-level tags:__ `@enum`, `@typedef`

The only tag specific to enumerations (and `typedef enum` declarations in C-based languages) is the `@const` or `@constant` tag.

| Tag | Example | Identifies | Type |
| --- | --- | --- | --- |
| `@constant`  `@const` | `@const kSilly A silly return value.` | A constant within an enumeration. | attribute (term & definition)  `enum` declarations only |

If an enumeration is named in the code, HeaderDoc automatically uses that name (unless you override it with an `@enum` tag). If it is not named, you must supply a name for the enumeration in the HeaderDoc comment. The listings below demonstrate both styles.

__Listing 2-23__  Example of a named enumeration

```
/*!
     @abstract Categorizes beverages into groups of similar types.
     @constant kSoda Sweet, carbonated, non-alcoholic beverages.
     @constant kBeer Light, grain-based, alcoholic beverages.
     @constant kMilk Dairy beverages.
     @constant kWater Unflavored, non-sweet, non-caloric, non-alcoholic beverages.
     @discussion Extended discussion goes here.
         Lorem ipsum....
*/
enum beverages {
 kSoda = (1 << 6),
 kBeer = (1 << 7),
 kMilk = (1 << 8),
 kWater = (1 << 9)
};
```


__Listing 2-24__  Example of an anonymous enumeration

```
/*!
     @enum Beverage Categories
     @abstract Categorizes beverages into groups of similar types.
     @constant kSoda Sweet, carbonated, non-alcoholic beverages.
     @constant kBeer Light, grain-based, alcoholic beverages.
     @constant kMilk Dairy beverages.
     @constant kWater Unflavored, non-sweet, non-caloric, non-alcoholic beverages.
     @discussion Extended discussion goes here.
         Lorem ipsum....
*/
enum {
 kSoda = (1 << 6),
 kBeer = (1 << 7),
 kMilk = (1 << 8),
 kWater = (1 << 9)
};
```


__Top-level tag:__ `@typedef`

The tags that can appear after an `@typedef` tag depend on the contents of the associated declaration. For example, a `typedef enum` declaration can contain anything that an `enum` declaration can contain.

An `@typedef` command can include any of the following:

- `@field` for `typedef struct` declarations
- `@constant` for `typedef enum` declarations
- `@param` for simple `typedef` declarations of individual function pointer types
- `@callback`, `@param`, and `@result` for `typedef struct` declarations containing function pointers as members

__Listing 2-25__  Typedef for a simple struct

```
/*!
     @typedef TypedefdSimpleStruct
     @abstract Abstract for this API.
     @field firstField Description of first field
     @field secondField Description of second field
     @discussion Discussion that applies to the entire typedef'd simple struct.
         Lorem ipsum....
 */

typedef struct _structTag {
 short firstField;
 unsigned long secondField
} TypedefdSimpleStruct;
```


__Listing 2-26__  Typedef for an enumeration

```
/*!
     @typedef TypedefdEnum
     @abstract Abstract for this API.
     @constant kCFCompareLessThan Description of first constant.
     @constant kCFCompareEqualTo Description of second constant.
     @constant kCFCompareGreaterThan Description of third constant.
     @discussion Discussion that applies to the entire typedef'd enum.
         Lorem ipsum....
*/
typedef enum {
 kCFCompareLessThan = -1,
 kCFCompareEqualTo = 0,
 kCFCompareGreaterThan = 1
} TypedefdEnum;
```


__Listing 2-27__  Typedef for a simple function pointer

```
/*!
     @typedef simpleCallback
     @abstract Abstract for this API.
     @param inFirstParameter Description of the callback's first parameter.
     @param outSecondParameter Description of the callback's second parameter.
     @result Returns what it can when it is possible to do so.
     @discussion Discussion that applies to the entire callback.
         Lorem ipsum...
*/
typedef long (*simpleCallback)(short inFirstParameter, unsigned long long *outSecondParameter);
```


__Listing 2-28__  Typedef for a struct containing function pointers

```
/*!
     @typedef TypedefdStructWithCallbacks
     @abstract Abstract for this API.
     @discussion Defines the basic interface for Command DescriptorBlock (CDB) commands.

     @field firstField Description of first field.

     @callback setPointers Specifies the location of the data buffer. The setPointers function has the following parameters:
     @param cmd A pointer to the CDB command interface.
     @param sgList A pointer to a scatter/gather list.
     @result An IOReturn structure which returns the return value in the structure returned.

     @field lastField Description of the struct's last field.
*/
typedef struct _someTag {
 short firstField;
 IOReturn (*setPointers)(void *cmd, IOVirtualRange *sgList);
 unsigned long lastField
} TypedefdStructWithCallbacks;
```


__Top-level tags:__ `@define`, `@defined`, `@defineblock`, `@definedblock`, `@/defineblock`, `@/definedblock`

C preprocessor (`#define`) macros have a few special tags:

| Tag | Example | Identifies | Type |
| --- | --- | --- | --- |
| `@define`  `@defined` | `@define MACRO_NAME` | Legacy top-level tag that provides the macro name. | Term & definition |
| `@noParse` | `@noParse` | Disables C preprocessor parsing of a macro. The macro will still be included as a `#define` entry in the resulting documentation. | parsing, flag |
| `@param` | `@param myValue The value to process.` | The name and description of a parameter to a function or callback. | attribute (term & definition)  in function-like macros only |
| `@parseOnly` | `@parseOnly` | Marks macro as “hidden”. The macro will be parsed and used by the C preprocessor, but will not be included as a separate `#define` entry in the resulting documentation. | parsing, flag |

__Listing 2-29__  Example of C preprocessor macro

```
 /*!
     @defined TRUE
     @abstract Defines the boolean true value.
     @parseOnly
     @discussion Extended discussion goes here.
         Lorem ipsum....
 */
 #define TRUE 1
```


__Listing 2-30__  Example of C preprocessor macro block

```
 /*!
     @definedblock Colors of the rainbow
     @abstract Defines some RGB colors.
     @discussion Extended discussion goes here.
         Lorem ipsum....
     @define kInfrared The color infrared.
     @define kRed The color red.
     @define kOrange The color orange.
     @define kYellow The color yellow.
     @define kGreen The color green.
     @define kCyan The color cyan.
     @define kBlue The color blue.
     @define kViolet The color violet.
     @define kUltraviolet The color ultraviolet.
 */

 #define kInfrared "#000000"
 #define kRed "#FF0000"
 #define kOrange "#FF8000"
 #define kYellow "#FFFF00"
 #define kGreen "#00FF00"
 #define kCyan "#00FFFF"
 #define kBlue "#0000FF"
 #define kViolet "#FF00FF"
 #define kUltraviolet "#000000"

/*! @/definedblock */
```


__Top-level tag:__ `@availabilitymacro`

The `@availabilitymacro` tag tells HeaderDoc that whenever the named token appears in a declaration, the token should be deleted and the “Availability:“ attribute for that declaration should be set to the string that follows.

__Listing 2-31__  Example of @availabilitymacro tag

```
/*!
 @availabilitymacro AVAILABLE_IN_MYAPP_1_0_AND_LATER This function is available in version 1.0 and later of MYAPP.
*/
```

This comment type is usually followed by a #define or similar, but that is not necessary. This HeaderDoc comment is a standalone comment—that is, it does not cause the code after it to be processed in any way. If you want to mark a `#define` as being an availability macro, you should follow this tag with a second HeaderDoc comment for the `#define` itself.

There are three tags provided for C pseudoclasses, such as COM interfaces. The `@class` tag is used for generic pseudoclasses. The `@interface` tag is used for COM interfaces. The `@superclass` tag can be added to an `@class` or `@interface` declaration to modify its behavior.

__Table 2-3__

| Tag | Identifies | Fields |
| `@superclass` | The name of the superclass. | 1 |

You should mark up any C pseudoclasses in the same way you would mark up a C++ class. Apart from the unusual form of function declarations (in the form of function pointers), the resulting output should be similar to that of a C++ class.

The `@superclass` tag can be used when you have a superclass-like relationship between two C pseudoclasses or COM interfaces. Using this tag will cause the documentation for the specified pseudo-superclass to be injected into the documentation for the current pseudoclass.

The primary purpose for this feature is to reduce the amount of bloat in headers, allowing you to document function pointers in the top-level pseudoclass and then only document the additional function pointers in pseudoclasses that expand upon them.

__Listing 2-32__  Example of @class tag

```
/*!
 @class IOFireWireDeviceInterface_t
 @superclass IOFireWireDevice
*/
 typedef struct IOFireWireDeviceInterface_t
{
    IUNKNOWN_C_GUTS;
.
.
.
}
```

The `@class` tag causes the `typedef struct`that follows the HeaderDoc comment to be treated as a class. This is a frequently-used technique in kernel programming. A slight variation of this tag, `@interface`, is provided for COM interfaces so that they can be identified as such in the TOC. An example of this tag follows:

__Listing 2-33__  Example of @interface tag

```objc
/*!
 @interface IOFireWireDeviceInterface_t
 @superclass IOFireWireDevice
*/
 typedef struct IOFireWireDeviceInterface_t
{
    IUNKNOWN_C_GUTS;
.
.
.
}
```


As mentioned in [Adding Arbitrary Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzugywvgvzs), there are three ways you can use the `@link` tag:

```
@link function_name @/link

or

@link function_name link text goes here @/link

or

@link //apple_ref/c/func/function_name link text goes here @/link
```

Beginning in HeaderDoc 8.7, you can link to any symbol by its name. (In previous versions of HeaderDoc, you can link to symbols by name if the link target is part of the same `.h` file or in any file processed before it in the same processing run.)

If there are multiple matches for a given name (or if you are using a pre-8.7 version of HeaderDoc and the symbol is parsed afterwards), you may need to explicitly specify which symbol to use. (See [Resolving Conflicting API References](Symbol%20Markers%20for%20HTML-Based%20Documentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzw) to learn about symbol matching precedence.) To avoid the conflict, you include an API reference marker for the symbol instead of its name. For some C++ methods, you may also need to tweak the reference marker so that it does not look like a C-style end-of-comment token. See [Using API References in the @link Tag](Symbol%20Markers%20for%20HTML-Based%20Documentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzrgu) for details.

Because the `headerdoc2html` script does not know the actual target for these links, it inserts special link request comments into the output. You must then run `gatherheaderdoc` or `resolveLinks` to actually turn those comments into working links.

See [Using resolveLinks to Resolve Cross References](Symbol%20Markers%20for%20HTML-Based%20Documentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wvgvzrge) to learn more about the resolving process and the various options available to you.

To avoid warnings and unexpected output, if you need to use an at sign (@) outside the scope of a HeaderDoc tag, you should quote it by preceding it with a backslash. For example:

```
/*! @header
        For more information, contact myemail\@myaddress.top.
 */
```

If you do not quote the at sign, it will be treated as the start of a tag name, and you may get unexpected behavior.

Beginning in HeaderDoc 8.6 and later, a warning is generated when an unknown tag is encountered, and the tag is converted into text.

Prior to version 8.6, unknown tags were partially removed. The initial at sign (`@`) was deleted, leaving only the content following it.

In addition to predefined attributes such as `@author`, `@coclass`, `@security`, and so on, HeaderDoc also supports the ability to add your own custom attributes by using the following tags:

- `@attribute`
- `@attributeblock`
- `@attributelist`

The first tag, `@attribute`, is straightforward:

```
@attribute My Attribute Name
    Value goes here.
```

This tag is intended for _short_ attributes. When this tag is used in HeaderDoc comments that describe API elements whose documentation provides a separate metadata table (classes and headers, for example), these attributes appear in that metadata table. In comments for other API elements, these attributes appear after the discussion.

The syntax for the second tag, `@attributeblock`, is the same as `@attribute`. The difference is that `@attributeblock` is intended for longer blocks of content (potentially containing multiple paragraphs instead of just a few words). Attributes tagged with `@attributeblock` always appear after the discussion.

The final tag, `@attributelist`, is intended for attributes containing very basic term-and-definition lists. For example:

```
@attributelist List name goes here
    Term Defintion goes here.
    Term2 Definition goes here.
```

These lists appear in the metadata table for the related API element, if applicable. Otherwise, they appear after the discussion. The use of `@attributelist` tags in HeaderDoc comments that describe API elements whose documentation provides a metadata table is discouraged for readability reasons.

[Next](Basic%20HeaderDoc%20Configuration.md)[Previous](Using%20HeaderDoc.md)

