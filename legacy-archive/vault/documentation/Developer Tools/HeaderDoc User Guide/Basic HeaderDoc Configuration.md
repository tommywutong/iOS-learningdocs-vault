---
title: HeaderDoc User Guide
apple_id: TP40001215
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2016-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/config/config.html
archived_at: '2026-07-15T07:24:28.256978Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HeaderDoc User Guide](Introduction.md)


[Next](Advanced%20HeaderDoc%20Configuration%20and%20Features.md)[Previous](HeaderDoc%20Tags.md)

# Basic HeaderDoc Configuration

You can set values for some commonly altered variables that affect HeaderDoc’s behavior and output style. This chapter describes the configuration file format, location, and the available configuration file keys.

A variable can be assigned a value in any of these places, but only the last value read for a given variable will affect the output of a run of the script. If you are happy with the default values for these variables (as described above), you don't need to provide a configuration file. If you want to change just one or more values, provide a configuration file that declares just those values.

The format of the configuration file is this:

```

 key1 => value1
 key2 => value2
```

HeaderDoc looks for these variables in three places, in this order:

1. In the script itself (see the declaration of the `%config` hash near the top of `headerdoc2html` or `headerDoc2HTML.pl`).
2. For HeaderDoc 8.9 and later, in `/usr/share/headerdoc/conf` (open source builds) or `/path/to/Xcode.app/Contents/Developer/usr/share/headerdoc/conf` (when installed as part of the developer tools).
3. In the main Library folder, in `/Library/Preferences/com.apple.headerDoc2HTML.config` (in most versions)
4. In the home directory of the user, in `$HOME/Library/Preferences/com.apple.headerDoc2HTML.config`
5. In a file named `headerDoc2HTML.config` in the same folder as the script.

In iterating through these locations, HeaderDoc retains the last value that it sees. Thus, the most local copy of any variable overrides any more generic value.

Currently, the HeaderDoc configuration file lets you set the following things:

- General tool behavior—described in [Behavioral Settings Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawvgvzu).
- Output format—described in [General Output Style Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawvgvzv).
- CSS stylesheet fragments and references to external style sheets to insert into the output—described in [General CSS Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawvgvzs).
- CSS stylesheet fragments for specific parts of declarations—described in [Declaration CSS Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawvgvzt).

This section describes configuration keys that control HeaderDoc’s general behavior, not including any output formatting or styling.

**_apiUIDPrefix_**
: The prefix for named anchors (by default, `apple_ref`). In the output, HeaderDoc adds a self-describing named anchor near each API declaration—for example `<a name=”//apple_ref/c/func/CFArrayAppendValue”>`. These can be useful for index generation and other purposes. See [Symbol Markers for HTML-Based Documentation](Symbol%20Markers%20for%20HTML-Based%20Documentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wueqkcjjeumrse) for more information.

**_compositePageName_**
: The name of the file containing the printable HTML page (by default, `CompositePage.html`). Not used if `classAsComposite` is 1.

**_defaultFrameName_**
: The name of the file containing the frameset instructions (by default, `index.html`).

**__externalAPIUIDPrefixes__**
: A space-separated list of prefixes for API references. When `gatherheaderdoc` runs `resolveLinks`, it passes this list of prefixes to `resolveLinks`. This allows you to use (multiple) API reference prefixes other than apple_ref.

For more information, see [Symbol Markers for HTML-Based Documentation](Symbol%20Markers%20for%20HTML-Based%20Documentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wueqkcjjeumrse).

**__externalXRefFiles__**
: A space-separated list of paths to external files, each of which contains a list of cross references outside the current document. When `gatherheaderdoc` runs `resolveLinks` to link together cross-referenced content, it passes these external cross-reference files to `resolveLinks` so that you can look up API references (apple_ref-style markup) in other documents.

__Note:__ Generally, if you are using external cross-reference files, you should be running `resolveLinks` manually rather than using this setting.

For more information, see [Symbol Markers for HTML-Based Documentation](Symbol%20Markers%20for%20HTML-Based%20Documentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wueqkcjjeumrse).

**_ignorePrefixes_**
: A list of tokens to leave out of the final output if they occur at the start of a line (before any other non-whitespace characters). Although this feature still exists, it is usually better to use C preprocessor directives.

**_masterTOCName_**
: The name of the file containing the master table of contents for a series of headers (by default, `masterTOC.html`). (This variable is used by the `gatherheaderdoc` script, and can be overridden on the command line.)

**IDLLanguage**
: IDL files normally produce `apple_ref` markers with the language `"idl"`. However, an IDL file is inherently language-neutral. This flag allows you to tell HeaderDoc to use a different language in `apple_ref` markers resulting from processing an IDL file.

Legal values are, in practice, any arbitrary URL-encoded string, but ideally should be valid programming languages as defined in the `apple_ref` specification. See [Symbol Markers for HTML-Based Documentation](Symbol%20Markers%20for%20HTML-Based%20Documentation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzug4wueqkcjjeumrse) for the specification.

This section describes overall output style (not including CSS style sheets, which are described in [General CSS Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawvgvzs) and [Declaration CSS Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawvgvzt)).

**__appleTOC__**
: Specifies the Apple TOC format. This format requires extensive JavaScript and CSS support, and thus is not very useful outside of the developer.apple.com website. It is documented only for completeness.

**__classAsComposite__**
: By default, HeaderDoc splits the documentation on the right side into several files. This setting causes classes to be output in a single composite page instead.

**_copyrightOwner_**
: The copyright notice that appears at the bottom of the HTML pages. Unless you specify a value, no copyright will appear.

**_dateFormat_**
: A string specifying the date format to be used by HeaderDoc. This date format is specified using standard time formatting flags. For examples of valid date formats, see the man page for [strftime](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/strftime.3.html#//apple_ref/doc/man/3/strftime).

**__groupHierLimit__**
: The maximum number of entries allowed in a list of headers, functions, and so on before `gatherheaderdoc` inserts jump links to particular letters within the list. If this key is absent, no letter links are inserted. If you set this key, you _must_ also set the `groupHierSubgroupLimit` to a positive integer value.

**__groupHierSubgroupLimit__**
: The maximum number of entries that should ideally appear in a single letter grouping. When this limit is exceeded, a new group begins as soon as an entry is reached whose first two letters differ from those of the current entry. This key is mandatory if `groupHierLimit` is set, and must be a positive integer.

**_htmlFooter_**
: A string (generally a server-side include directive) that HeaderDoc will insert into the bottom of each right-side and composite HTML page if you specify the `-H` flag on the command line. For longer headers, use `htmlFooterFile`.

**_htmlFooterFile_**
: A file containing a longer HTML footer. The contents of this file will be added to the end of each content page if you specify the `-H` flag on the command line.

**_htmlHeader_**
: A string (generally a server-side include directive) that HeaderDoc will insert into the top of each right-side and composite HTML page if you specify the `-H` flag on the command line. For longer headers, use `htmlHeaderFile`.

**_htmlHeaderFile_**
: A file containing a longer HTML header. The contents of this file will be added at the top of each content page if you specify the `-H` flag on the command line.

**__stripDotH__**
: This option causes `gatherheaderdoc` to strip the trailing `.h` from the names of header filenames in header lists.

**__TOCFormat__**
: Chooses the TOC format style for individual documents. Legal values are `default` (new style with disclosure triangles), `frames` (old style), or `iframes` (8.7 style).

This option replaces the `-F` flag, though that flag is still supported for now.

**_TOCTemplateFile_**
: Specifies a TOC template file to use instead of the built-in TOC template. For more information, see [Creating a TOC Template File](Advanced%20HeaderDoc%20Configuration%20and%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzvgawueqkcjbaukqkd).

**__TOCTemplateEncoding__**
: The encoding used by your TOC template file. The `gatherHeaderDoc` tool uses this to ensure that any date stamps inserted into master TOCs are in the correct encoding.

**__useBreadcrumbs__**
: Setting this option to `1` tells HeaderDoc that you intend to use an external tool to create breadcrumb links in your documents. When you specify this option, it disables the insertion of the “[Top]“ link in the table of contents, since it is not necessary if you have such a tool. Because such breadcrumbs are site-specific, no such tools are provided as part of HeaderDoc.

**__externalStyleSheets__**
: A space-separated list of paths to external style sheet files on the server or destination volume. For example, if you set externalStyleSheets to /CSS/mysheet.css, HeaderDoc will insert the following:

```
<link rel="stylesheet" type="text/css" href="/CSS/mysheet.css">
```

These style sheets are inserted prior to any HeaderDoc-generated styles.

__Note:__ Using this option disables the built-in HeaderDoc styles. For your convenience, these built-in styles are listed in [Built-in HeaderDoc Styles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawvgvzr).

**__externalTOCStyleSheets__**
: Like externalStyleSheets, this is a space-separated list of paths to external style sheet files on the server or destination volume. If no TOC style sheets are specified, the style sheets specified in `externalStyleSheets` will be used.

__Note:__ Using this option disables the built-in HeaderDoc styles. For your convenience, these built-in styles are listed in [Built-in HeaderDoc Styles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawvgvzr).

**__styleImports__**
: A string of CSS to be inserted just prior to HeaderDoc-generated CSS, but after any external style sheets. This was originally intended to support the `@import` directive to import an external style sheet, but may be used for any arbitrary CSS content.

__Note:__ Using this option disables the built-in HeaderDoc styles. For your convenience, these built-in styles are listed in [Built-in HeaderDoc Styles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawvgvzr).

**__styleSheetExtrasFile__**
: A file containing local HeaderDoc-specific CSS. The contents of the file specified will be inserted at the end of the built-in HeaderDoc styles (after any styles specified by the HeaderDoc declaration styles, such as `varStyle`).

__Note:__ This option is the _only_ style sheet option that does _not_ disable the built-in HeaderDoc styles.

**__tocStyleImports__**
: Similar to `styleImports`, this is a string of CSS to be inserted just prior to HeaderDoc-generated CSS, but after any external style sheets. This was originally intended to support the `@import` directive to import an external style sheet, but may be used for any CSS content.

If no TOC style imports are specified, the value of `styleImports` will be used for the TOC.

__Note:__ Using this option disables the built-in HeaderDoc styles. For your convenience, these built-in styles are listed in [Built-in HeaderDoc Styles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawvgvzr).

These contain CSS formatting for various parts of declarations. For example:

```
funcNameStyle => background:#ffffff; color:#000000;
```

sets function names to be displayed in black text on a white background.

**_charStyle_**
: style for characters ('a')

**_commentStyle_**
: style for comments

**_funcNameStyle_**
: style for function names

**_keywordStyle_**
: style for keywords

**_numberStyle_**
: style for numbers

**_paramStyle_**
: style for function parameters

**_preprocessorStyle_**
: style for preprocessor directives

**_stringStyle_**
: style for strings

**__textStyle__**
: style for normal text if declarations (mainly parentheses, punctuation, and spaces)

**_typeStyle_**
: style for data types

**_varStyle_**
: style for variable names

[Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawueqkcjbdeoskj) is an example of a very basic HeaderDoc configuration file. Several additional examples are included as part of the HeaderDoc distribution.

__Listing 3-1__  Sample HeaderDoc configuration file

```

copyrightOwner => My Great Software Company
defaultFrameName => default.html
compositePageName => PrintablePage.html
masterTOCName => TOCCentral.html
apiUIDPrefix => greatSoftware
ignorePrefixes=> CF_EXTERN|CG_EXTERN
htmlHeader=>
dateFormat=> %m/%d/%Y
```


Many of the CSS options in HeaderDoc disable the built-in styles so that it is easier to override those styles in external style sheets. The built-in styles are listed below for your convenience.

__Listing 3-2__  Built-in HeaderDoc CSS Styles

```
a:link {text-decoration: none; font-family: lucida grande, geneva, helvetica, arial, sans-serif; font-size: small; color: #0000ff;}
a:visited {text-decoration: none; font-family: lucida grande, geneva, helvetica, arial, sans-serif; font-size: small; color: #0000ff;}
a:visited:hover {text-decoration: underline; font-family: lucida grande, geneva, helvetica, arial, sans-serif; font-size: small; color: #ff6600;}
a:active {text-decoration: none; font-family: lucida grande, geneva, helvetica, arial, sans-serif; font-size: small; color: #ff6600;}
a:hover {text-decoration: underline; font-family: lucida grande, geneva, helvetica, arial, sans-serif; font-size: small; color: #ff6600;}
h4 {text-decoration: none; font-family: lucida grande, geneva, helvetica, arial, sans-serif; font-size: tiny; font-weight: bold;}
body {text-decoration: none; font-family: lucida grande, geneva, helvetica, arial, sans-serif; font-size: 10pt;}
```

[Next](Advanced%20HeaderDoc%20Configuration%20and%20Features.md)[Previous](HeaderDoc%20Tags.md)

