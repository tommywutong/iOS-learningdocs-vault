---
title: HeaderDoc User Guide
apple_id: TP40001215
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2016-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html
archived_at: '2026-07-15T07:24:28.287448Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HeaderDoc User Guide](Introduction.md)


[Next](Testing%20HeaderDoc.md)[Previous](Advanced%20HeaderDoc%20Configuration%20and%20Features.md)

# Using the MPGL Suite

In addition to the main `headerdoc2html` and `gatherheaderdoc` scripts, the HeaderDoc suite contains additional utilities for generating manual pages (using the mdoc macro set).

The Man Page Generation Language (MPGL) suite contains two utilities: `xml2man` and `hdxml2manxml`. The `xml2man` utility converts an mdoc-like XML dialect, the Man Page Generation Language (MPGL) into manual pages. The `hdxml2manxml` utility converts HeaderDoc XML output into a series of files that can then be processed using `xml2man`.

Both commands have a very simple syntax. Neither takes any arguments.

```
hdxml2manxml filename1 filename2 ... filenameN
xml2man inputfile.mxml [ outputfile.1 ]
```

In the case of `xml2man`, the output filename is generally left blank.

The remainder of this chapter describes the XML dialect used by these utilities.

This section describes the basic syntax of the Man Page Generation Language (MPGL). Portions of the syntax are abridged due to complexity. For information on these details, see the examples later in this chapter.

The MPGL syntax includes a subset of mdoc. All text is unjustified, and some redundancy was reduced. In particular, the `usage` section in an MPGL file provides the source information for both the SYNOPSIS and OPTIONS sections of a traditional man page. Beyond those changes, if you are familiar with the mdoc macro set, you should feel right at home.

At the top level (within the outer `<manpage>` tag), an MPGL page consists of some or all of the following large blocks:

__Table 5-1__  MPGL block tags

| Block tag | Description |
| `<docdate>` | The last modified date of the manual page. |
| `<description>` | A description of the technology as a whole. This is the first major section of the resulting manual page. |
| `<doctitle>` | The title of the manual page. |
| `<os>` | The operating system for which the manual page was written. |
| `<section>` | The man section in which the manual pages should appear. |
| `<names>` | Names and descriptions of functions or tools described in this manual page (see example for syntax). |
| `<usage>` | Command-line usage or function parameters (see example for syntax). |
| `<returnvalues>` | Function return value (text description). |
| `<environment>` | Interaction with environment variables. |
| `<files>` | Files used by a command-line tool. |
| `<examples>` | Usage examples. |
| `<diagnostics>` | Troubleshooting information. |
| `<errors>` | Function error values (generally restricted to those returned via the `errno` global variable). |
| `<seealso>` | Cross-references to other manual pages (see example). |
| `<conformingto>` | Standards to which a tool or function conforms. |
| `<history>` | Historical information. |
| `<bugs>` | Known bugs in a tool or function. |

Any field can contain either a block of raw text or the following subset of XHTML:

__Table 5-2__  XHTML tags supported by MPGL

| XHTML tag | Description |
| `<p>` | paragraph |
| `<blockquote>` | indented block |
| `<tt>` | indented literal text or code |
| `<ul>` | unordered (bullet) list |
| `<ol>` | ordered (numbered) list |
| `<li>` | list item (within a list) |
| `<code>` | literal text |
| `<dl>` | term and definition list |
| `<dt>` | term (within a term and definition list) |
| `<dd>` | definition (within a term and definition list) |

Any field can also contain any of the following MPGL-specific inline tags:

__Table 5-3__  Additional MPGL-specific inline tags

| Tag | Description |
| `<path>` | path name |
| `<function>` | function name |
| `<command>` | command name |
| `<manpage>` | man page cross-reference (see example) |

[Listing 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzvg4wugscejfeuoqke) is an example of how to write an MPGL manual page for a function.

__Listing 5-1__  A simple MPGL example for a function

```
<manpage>
<docdate>August 28, 2002</docdate>
<doctitle>Document title</doctitle>
<os>OS X</os>
<section>3</section>
<names>
        <name>foo<desc>This is foo's description</desc></name>
        <name>bar<desc>This is bar's description</desc></name>
</names>

<usage>
        <func><type>int</type><name>foo</name>
            <arg>int k<desc>This is a k.</desc></arg>
            <arg>char *b<desc>This is a b.</desc></arg>
        </func>
</usage>

<returnvalues>
        <p>Returns kIONotANumber if you can't count.</p>
        <p>Returns kIOMoron this if you REALLY can't count.</p>
</returnvalues>

<environment>
        TEXT
</environment>

<files>
        <file>/path/to/filename<desc>This is a waste of time</desc></file>
        <file>/path/to/another/filename<desc>This is also a waste of time</desc></file>
</files>

<examples>
        TEXT
</examples>

<diagnostics>
        TEXT
</diagnostics>

<errors>
        TEXT
</errors>

<seealso>
        <p>This is a text container, really, but generally contains
        lines like this:</p>
        <manpage>foo<section>1</section>, </manpage>
        <manpage>bar<section>3</section></manpage>
</seealso>

<conformingto>
        <p>Here's a list of conformance:</p>
        <ul>
            <li>Single UNIX Specification</li>
            <li>POSIX</li>
        </ul>
</conformingto>

<history>
        TEXT
</history>

<bugs>
        <p>Here are some bugs:</p>
        <p>
        <ol>
                <li>Bug one....</li>
                <li>Bug two....</li>
                <li>Bug three....</li>
        </ol>
        </p>
        <p>I think that pretty much covers it.</p>
</bugs>
</manpage>
```


[Listing 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzvg4wugscejbbeiq2g) is an example of how to write an MPGL manual page for a single command or a series of commands with the same syntax.

__Listing 5-2__  A simple MPGL example for a command

```
<manpage>
<docdate>August 28, 2002</docdate>
<doctitle>Document title</doctitle>
<os>Darwin</os>
<section>1</section>
<names>
        <name>foo<desc>this is a description</desc></name>
        <name>bar<desc>this is also a description</desc></name>
</names>

<usage>
        <flag optional="1">a<arg>attributes</arg><desc>This is the atts flag</desc></flag>
        <flag>d<arg>date</arg><desc>This is the date flag</desc></flag>
        <flag>x<desc>This is the -x flag</desc></flag>
        <arg>filename<desc>This is the filename</desc></arg>
</usage>

<returnvalues>
        <p>Returns kIONotANumber if you can't count.</p>
        <p>Returns kIOMoron if you REALLY can't count.</p>
</returnvalues>

<environment>
        TEXT
</environment>

<files>
        <file>/path/to/filename<desc>This is a waste of time</desc></file>
        <file>/path/to/another/filename<desc>This is also a waste of time</desc></file>
</files>

<examples>
        TEXT
</examples>

<diagnostics>
        TEXT
</diagnostics>

<errors>
        TEXT
</errors>

<seealso>
        <p>This is a text container, really, but generally contains
        lines like this:</p>
        <manpage>foo<section>1</section>, </manpage>
        <manpage>bar<section>3</section></manpage>
</seealso>

<conformingto>
        <p>Here's a list of conformance:</p>
        <ul>
            <li>Single UNIX Specification</li>
            <li>POSIX</li>
        </ul>

        <p>Here's a definition list:</p>
        <dl>
            <dd>foo_aaa</dd>
                <dt>This is foo</dt>
            <dd>bar</dd>
                <dt>This is bar</dt>
        </dl>

</conformingto>

<history>
        This program should be history....
</history>

<bugs>
        <p>Here are some bugs:</p>
        <p>
        <ol>
                <li>Bug one....</li>
                <li>Bug two....</li>
                <li>Bug three....</li>
        </ol>
        </p>
        <p>I think that pretty much covers it.</p>
</bugs>
</manpage>
```


[Listing 5-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzvg4wugsceineucqkd) is an example of how to write an MPGL manual page for multiple commands in a single page.

__Listing 5-3__  An MPGL example for multiple commands

```
<manpage>
<docdate>August 28, 2002</docdate>
<doctitle>Document title</doctitle>
<os>Darwin</os>
<section>1</section>
<names>
        <name>hdxml2manxml<desc>HeaderDoc XML to MPGL translator</desc></name>
        <name>xml2man<desc>MPGL to mdoc (man page) translator</desc></name>
        <name>examplemc<desc>MPGL to mdoc (man page) translator</desc></name>
</names>

<usage>
        <command name="hdxml2manxml">
                <arg>filename [ filename ... ]<desc>the filename(s) to be processed</desc></arg>
        </command>
        <command name="xml2man">
                <arg>filename<desc>This is the filename</desc></arg>
                <arg optional="1">output_filename<desc>This is the filename</desc></arg>
        </command>
        <command name="example">
                <arg>filename<desc>This is the filename</desc></arg>
                <arg optional="1">output_filename<desc>This is the filename</desc></arg>
        </command>
        <command name="example">
                <arg>filename [ filename ... ]<desc>the filename(s) to be processed</desc></arg>
                <flag optional="1">c<arg>time_to</arg><arg optional="1">crash</arg><desc>Seems like a useful flag</desc></flag>
        </command>
</usage>

<environment>
        <p>The <name>xml2man</name> program was designed to convert Man Page
        Generation Language (MPGL) XML files into mdoc-based manual pages.
        The MPGL is a fairly direct translation of mdoc to XML.</p>

        <p>The <name>hdxml2manxml</name> tool was designed to translate
        from headerdoc's XML output to an mxml file for use with xml2man.</p>
</environment>

<seealso>
        <p>For more information on xml2man, see</p>
        <manpage>xml2man<section>1</section>, </manpage>
        <manpage>hdxml2manxml<section>1</section>, </manpage>
</seealso>

</manpage>
```

[Next](Testing%20HeaderDoc.md)[Previous](Advanced%20HeaderDoc%20Configuration%20and%20Features.md)

