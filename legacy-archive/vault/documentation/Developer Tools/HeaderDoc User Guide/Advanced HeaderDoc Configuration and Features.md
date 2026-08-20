---
title: HeaderDoc User Guide
apple_id: TP40001215
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2016-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/gatherheaderdoc/gatherheaderdoc.html
archived_at: '2026-07-15T07:24:28.267011Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HeaderDoc User Guide](Introduction.md)


[Next](Using%20the%20MPGL%20Suite.md)[Previous](Basic%20HeaderDoc%20Configuration.md)

# Advanced HeaderDoc Configuration and Features

HeaderDoc contains a number of advanced features intended for users with more complex needs. This chapter describes some of these features.

TOC template files are basically ordinary HTML files. They can contain any HTML content. In addition to HTML content, they can also contain conditional HTML content—that is, content that is only included if certain conditions are met. Finally, they can include various lists.

The template support is particularly powerful when combined with support for frameworks (which, for HeaderDoc purposes, is essentially a loose grouping of related documentation stored in the same output directory).

Here are the special tags that indicate conditional or list content:

**`$$title@@`**
: Inserts “Foo Documentation” where Foo is the framework name.

**`$$tocname@@`**
: Inserts the name of the main TOC file. Useful when used with multiple landing page templates, as described in [Using Multiple Landing Page Templates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzvgawuerkkivdeir2g).

**`$$framework@@`**
: Inserts the full framework name, as specified by the `@framework` tag in the `.hdoc` file.

**`$$frameworkabstract@@`**
: Inserts the framework abstract, as specified by the `@abstract` tag in the `.hdoc` file.

**`$$frameworkdir@@`**
: Inserts the framework’s "short name”. This is determined by taking the filename of the “`.hdoc`” file and stripping off the `.hdoc` extension). This name is also prepended to the name of additional landing page template, as described in [Using Multiple Landing Page Templates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzvgawuerkkivdeir2g).

**`$$frameworkdiscussion@@`**
: Inserts the framework discussion, as specified by the `@discussion` tag (or implicitly as part of the `@framework` tag) in the `.hdoc` file.

**`$$frameworkuid@@`**
: Inserts a framework UID anchor.

**`$$headersection@@`**
: Start of conditional block for headers. If there are no headers listed, content between this tag and the closing conditional block tag will not appear.

**`$$/headersection@@`**
: End of conditional block for headers.

**`$$headerlist@@`**
: A list of all headers in the output directory.

**`$$classsection@@`**
: Start of conditional block for classes. If there are no classes listed, content between this tag and the closing conditional block tag will not appear.

**`$$/classsection@@`**
: End of conditional block for classes.

**`$$classlist@@`**
: A list of all classes in the output directory.

**`$$categorysection@@`**
: Start of conditional block for categories. If there are no categories listed, content between this tag and the closing conditional block tag will not appear.

**`$$/categorysection@@`**
: End of conditional block for categories.

**`$$categorylist@@`**
: A list of all categories in the output directory.

**`$$protocolsection@@`**
: Start of conditional block for protocols. If there are no protocols listed, content between this tag and the closing conditional block tag will not appear.

**`$$/protocolsection@@`**
: End of conditional block for protocols.

**`$$protocollist@@`**
: A list of all protocols in the output directory.

**`$$datasection@@`**
: Start of conditional block for data (globals and constants). If there are no data elements listed, content between this tag and the closing conditional block tag will not appear.

**`$$/datasection@@`**
: End of conditional block for data (globals and constants).

**`$$datalist@@`**
: A list of all data elements in the output directory.

**`$$typesection@@`**
: Start of conditional block for types. If there are no types listed, content between this tag and the closing conditional block tag will not appear.

**`$$/typesection@@`**
: End of conditional block for types.

**`$$typelist@@`**
: A list of all types in the output directory.

**`$$functionsection@@`**
: Start of conditional block for functions or methods. If there are no functions or methods listed, content between this tag and the closing conditional block tag will not appear.

**`$$/functionsection@@`**
: End of conditional block for functions or methods.

**`$$functionlist@@`**
: A list of all functions/methods in the output directory.

List tags default to a raw list (single column) with no border. However, you can change the number of columns, the table width, and border quite easily. For example:

```
    $$functionlist cols=3 order=down atts=border=”0” cellpadding=”1” cellspacing=”0” width=”420”@@
```

specifies that the table will be three columns, listed down the first column, then down the next column, and so on. It also specifies that the additional attributes `border`, `cellpadding`, `cellspacing`, and `width` will be inserted into the table tag automatically. Note that the `atts` parameter must be the last parameter listed.

**`nogroups`**
: The `gatherheaderdoc` tool normally separates entries by TOC grouping. If you want this list to include everything in a single list, add this flag. For an example, see the alphabetical list of all OS X manual pages as part of _OS X Man Pages_.

**`cols`**
: Specifies the number of columns in the table. (Note that the number of rows cannot be specified, as it is calculated based on the number of columns and the number of entries in the table.) For example, you might specify `cols=3`.

**`order`**
: Specifies whether the table should read across or down. If you specify `order=across`, the first entry will be in the upper left cell, the second one will be to the right, and so on. If you specify `order=down`, the second entry will be below the first entry. The default is down.

**`trclass`**
: Specifies a CSS class to be applied to the `<tr>` (table row) tags within the table. For example, you might specify `trclass=toctrclass`.

**`tdclass`**
: Specifies a CSS class to be applied to the `<td>` (table data cell) tags within the table. For example, you might specify `tdclass=toctdclass`.

**`notable`**
: Disables generation of tables. If you specify this option, each entry will be separated by a `<br>` (line break) tag followed by a newline. This is primarily intended for generating a list that can be easily processed with custom tools, but it may be combined with CSS to create some interesting and useful layouts as well.

**`addempty`**
: This option tells `gatherheaderdoc` to include blank cells containing a non-breaking space to fill in unused slots in the last line of the table. The default, `addempty=0`, will simply close the final line of the table early. To add extra empty cells (as needed) to fill the last line in the table, specify `addempty=1`.

This usually matters very little unless you have table borders turned on (`atts=border=1`, for example).

**`atts`**
: Specifies a list of attributes to be added to the `<table>` tag. These are not CSS attributes, though you could specify CSS attributes by specifying `atts=style=“CSS props here”`. Everything up to the closing `@@` marker is included as part of the `atts` option.

For example:

```
    $$functionlist nogroups cols=3 order=down trclass=mytrclass tdclass=mytdclass notable addempty=1 atts=border=”0” cellpadding=”1” cellspacing=”0” width=”420”@@
```


HeaderDoc is not limited to a single landing page template. You can generate multiple landing pages with different content if desired. To do this, you might create two template files called `toctemplate.html` and `functions.tmpl`, then add a line in your configuration file like this:

```
TOCTemplateFile => toctemplate.html functions.tmpl
```

When you run `gatherheaderdoc`, you will now get two HTML landing pages, one for each template.

The first template file, `toctemplate.html`, is treated as the “main” template page. The `gatherheaderdoc` tool will generate a landing page based on that template with the filename specified by the `masterTOCName` variable in the configuration file (`masterTOC.html` by default).

After the first template file, each additional template file (`functions.tmpl`, in this case) is used to produce an HTML landing page whose name is derived from the framework’s “short name” (the name of the `.hdoc` file with the `.hdoc` extension stripped off the end), followed by a dash, followed by the template filename (without any “`.html`” or “`.tmpl`” extensions), followed by “`.html`”.

For example, if the `.hdoc` file is called `MyFramework.hdoc`, this second index file would be called `MyFramework-functions.html`.

Since these templates can be used for generating multiple documents, you should not specify this entire path in your template files, however. Instead, you should specify it relative to the framework name. To do this, in your `toctemplate.html` file, you should link to the functions index like this:

```
<A href="$$frameworkdir@@-functions.html">Functions Index</A><p>
```

The framework’s “short name” will automatically be substituted in place of the `$$frameworkdir@@` keyword. Similarly, in the functions template, you can link to the main TOC like this:

```
<A href="$$tocname@@">Headers Index</A><p>
```

This will ensure that your template will generate valid links even if you change the name of the MasterTOC in your configuration file.

The following is an example template for `gatherheaderdoc`:

```
<html>
 <head>
 <title>API Reference: Device Drivers (Kernel/IOKit)</title>
 <style type="text/css"><!--#pagehead {
    FONT-WEIGHT: bold; FONT-SIZE: 32px; COLOR: #000000;
    FONT-FAMILY: lucida grande, geneva, helvetica, arial, sans-serif; }
    td { font-size: 10px; } a:link {text-decoration: none;
    font-family: lucida grande, geneva, helvetica, arial, sans-serif;
    color: #0000ff;} a:visited {text-decoration: none;
    font-family: lucida grande, geneva, helvetica, arial, sans-serif;
    color: #0000ff;} a:visited:hover {text-decoration: underline;
    font-family: lucida grande, geneva, helvetica, arial, sans-serif;
    color: #ff6600;} a:active {text-decoration: none;
    font-family: lucida grande, geneva, helvetica, arial, sans-serif;
    color: #ff6600;} a:hover {text-decoration: underline;
    font-family: lucida grande, geneva, helvetica, arial, sans-serif;
    color: #ff6600;} h4 {text-decoration: none;
    font-family: lucida grande, geneva, helvetica, arial, sans-serif;
    font-size: tiny; font-weight: bold;} body {text-decoration: none;
    font-family: lucida grande, geneva, helvetica, arial, sans-serif;
    font-size: 10pt;} -->
 </style>
 </head>
 <Meta name="ROBOTS" content="NOINDEX">

<body bgcolor="#ffffff">
<center>

<!-- start of header -->
<!--#include virtual="/path/to/header.html"-->
<!-- end of header -->

<table border="0" cellpadding="0" cellspacing="0" width="600">

    <tr height="5">
        <td width="600" height="5"><br>
        </td>
    </tr>
    <tr>
        <td width="600">
            <div id="pagehead">$$framework@@</div>
        </td>
    </tr>
    <tr height="10">
        <td width="600" height="10"><br>
        </td>
    </tr>
    <tr>
        <td valign="top" width="600"><font face="Geneva,Helvetica,Arial"
        size="2"><span id="bodytext"> $$frameworkdiscussion@@ </span></font>
        </td>
    </tr>
    <tr height="10">
        <td height="10" width="600"></td>
    </tr>
    <tr height="5">
        <td height="5" width="600">
            <hr alt="">
            <br>
        </td>
    </tr>
    <tr>
        <td width="600" align="center" valign="top">
            <H2>Headers</H2>

                $$headerlist cols=3 order=down atts=border="0"
                cellpadding="1" cellspacing="0" width="420"@@
        <H2>Functions</H2>
                $$functionlist cols=3 order=down atts=border="0"
                cellpadding="1" cellspacing="0" width="420"@@
        </td>
    </tr>
</table>
</center>
</body>
</html>
```


Beginning in HeaderDoc 8.5, HeaderDoc contains a basic C preprocessor implementation (enabled with the `-p` flag). Because HeaderDoc does not have access to the full compile-time environment of the headers, its behavior may differ from normal C preprocessors in certain cases. This section describes some of those differences.

Most `#define` macros are not parsed by default, even if the preprocessor is enabled. This permits you as the user to choose which macros to process.

Macros are processed if any of the following are true:

- They are preceded by a HeaderDoc comment block.
- They appear between the beginning and end of a class that is preceded by a HeaderDoc comment block.

The reason for this second case is a side-effect of the way that HeaderDoc parses classes to ensure that lines are processed in the order in which they appear in the file (which is necessary for a preprocessor to even be possible). For maximum control, preprocessor directives should be at the start of the file, outside of class braces.

HeaderDoc does not attempt to handle `#if`, `#ifdef`, or `#ifndef` directives. This may, in certain circumstances, result in multiple definitions of a `#define` directive if the preprocessor is enabled. As with most preprocessors, all such definitions are ignored except for the one that appears first in the file.

This is made slightly more complicated by the parsing rules described in [Parsing Rules](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzvgawugskijbauosci).

With most data types, HeaderDoc comments appearing inside the data type are associated with the data type itself. This is normally true for `#define` macros as well. However, that behavior would create a problem when the C preprocessor is enabled, as it is reasonable to allow macros to define contents to be blown into a class, and those contents could potentially include HeaderDoc markup.

For this reason, when the C preprocessor is enabled, embedded HeaderDoc processing is disabled for `#define` macros. Any HeaderDoc markup within the body of such a macro will be blown in wherever the macro is used, and will only be processed in the resulting context.

While HeaderDoc does allow a macro to insert multiple declarations and HeaderDoc comment blocks within a class, it does not allow this outside of a class. When a macro inserts contents outside of a class scope, parsing will end at the end of the first declaration and any other contents inserted by the macro will be skipped.

HeaderDoc’s implementation of `#include` behaves differently than you might expect. The differences include the following:

- No notion of paths.

  Because the include paths are not specified as they are with a compiler, HeaderDoc cannot reasonably determine that `<dir1/file.h>` and `<dir2/file.h>` are distinct. For this reason, processing files with the same name in different directories is discouraged.
- Mandatory recursion protection.

  Because HeaderDoc does not process `#if`, `#ifdef`, and `#ifndef` conditionals, HeaderDoc enforces recursion protection by not allowing a file to get processed twice. Once a file is processed, a precompiled copy of its macros is stored for future use, and is automatically inserted whenever another `#include` requests it.

  This causes two side-effects. First, a `#include` cannot be altered in a context-dependent way—that is, if a header includes `<a.h>` and then `<b.h>`, the macros defined in `<a.h>` will not affect the parse of `<b.h>` unless `<b.h>` includes `<a.h>` on its own.

  Second, `#include` behaves much like `#import`. The result is that if `<a.h>` includes `<b.h>` which includes `<c.h>` which includes `<a.h>`, the definitions leading up to the re-inclusion of `<a.h>` will not affect the way `<a.h>` is parsed.
- Macro contents will be shown in the documentation output.

  Rather than try to carry around some notion of the original tokens read from the file, HeaderDoc inserts macros into the parse tree as if the modified version had been read from the file. This means that it is not possible, for example, for HeaderDoc to show you the unaltered definition of a macro that includes another macro.

These differences generally do not affect headers written in a typical fashion, but may cause problems if you are using preprocessor directives in a nonstandard way.

A few common function-like preprocessor macros are predefined within HeaderDoc itself to avoid parse problems with I/O Kit headers. These will probably not affect you, but you should be aware of them.

Because HeaderDoc does not strip comments prior to processing macros (since doing so would remove HeaderDoc markup), the preprocessor may behave in subtly different ways. In particular, newlines are preserved, and any closing single-line (`//`) comments will automatically be converted into a multi-line (`/* */`) comment to avoid causing the rest of the line to disappear when that macro actually gets used.

Finally, HeaderDoc does do basic string and character handling, even within macros. As a result, mismatched single and double quotes within a `#define` macro may cause serious problems.

Most of the time, having `#define` macros defined in the documentation is helpful. In some cases, though, the macros get so big and ugly that you just want to get rid of them. For this reason, HeaderDoc has the `@parseOnly` tag.

For example:

```
/*! This is an ugly internal macro. @parseOnly */
#define CreateStructors \
    /*! Constructor */ \
    blah(); \
    /*! Destructor */ \
    ~blah();
```

By adding this tag at the end of the HeaderDoc comment block for the macro, the macro will be parsed and used by the preprocessor, but will not appear in the documentation.

[Next](Using%20the%20MPGL%20Suite.md)[Previous](Basic%20HeaderDoc%20Configuration.md)

