---
title: HeaderDoc User Guide
apple_id: TP40001215
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2016-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/releasenotes/releasenotes.html
archived_at: '2026-07-15T07:24:28.304283Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HeaderDoc User Guide](Introduction.md)


[Next](Symbol%20Markers%20for%20HTML-Based%20Documentation.md)[Previous](Testing%20HeaderDoc.md)

# HeaderDoc Release Notes

The HeaderDoc Tools Suite consists of a series of Perl scripts and several small C helper applications that allows conversion of documentation embedded in header files in many languages into HTML and other output formats.

HeaderDoc 8 is the latest incarnation of the HeaderDoc tool and encompasses a series of versions:

**HeaderDoc 8.0**
: HeaderDoc 8 is nearly a rewrite of HeaderDoc from the ground up. It incorporates the functionality of previous versions but also provides a number of new features, such as declaration syntax coloring/highlighting and an easier-to-use comment syntax. These features are described in [Major Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmrqgewueq2jinceoq2f).

HeaderDoc 8 adds a number of additional languages with various levels of support. These are described in [Languages Supported](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmrqgewueq2jjbeueqkj).

HeaderDoc 8 also adds a number of new (optional) tags for convenience. These are described in [New Tags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmrqgewueq2jjfbukrck).

**HeaderDoc 8.5**
: HeaderDoc 8.5 adds a C preprocessor for more advanced header parsing. This is described in [Using the C Preprocessor](Advanced%20HeaderDoc%20Configuration%20and%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzvgawueqkci5euorsc).

**HeaderDoc 8.6**
: HeaderDoc 8.6 is a bug fix update to HeaderDoc 8.5, with a few minor features added.

**HeaderDoc 8.7**
: HeaderDoc 8.7 adds support for Doxygen tags (@ form only) and adds support for IDL files. In addition, it includes a test suite (source distribution only) and contains numerous bug fixes.

**HeaderDoc 8.8**
: HeaderDoc 8.8 adds support for AppleScript and Python, along with partial support for Tcl and Ruby. See [Troubleshooting](Troubleshooting.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzwgywvgvzr) for more information about limitations in Tcl and Ruby support.

HeaderDoc 8.8 also enhances the `resolveLinks` tool to support importing external cross-reference files.

Finally, HeaderDoc 8.8 bundles the regression test suite as part of the installation.

HeaderDoc 8 supports many more languages than HeaderDoc 7. This table shows the various languages and the level of support.

__Table A-1__  HeaderDoc 8 Language Support

| Language | HeaderDoc 7 support | HeaderDoc 8 support |
| AppleScript | no | yes (8.8) |
| C headers | yes | yes |
| C++ | yes | yes |
| Objective C | yes | yes |
| C source code | no | yes |
| IDL | no | yes (8.7) |
| K&R C sources | no | yes |
| Java | no | yes \* |
| JavaScript | no | yes \* |
| Pascal | no | yes |
| PHP | sort-of (hack) | yes |
| Perl | no | yes \*\* |
| Python | no | yes (8.8) |
| Ruby | no | yes (8.8) |
| Shell Scripts | no | yes \*\* |
| Mach IPC Interface Definitions | no | yes |

HeaderDoc 8 has a number of new features.

- Function/data type groupings
- Declaration syntax coloring
- New tagless syntax

  `/*! This is a comment about what comes next */`
- Support for HeaderDoc tags embedded in declarations
- Support for `//!` markup style for embedded HeaderDoc declarations
- Automatic linking of data types in declarations
- Improved C++ support (namespace/template/access)
- The `gatherheaderdoc` tool is now template based
- PHP support (and a bunch of other languages) now included without patching
- Support for linking to other methods and data types within the same file
- Comment stripper
- Support for exceptions
- Now warns if tagged parameters don’t match declaration
- Optional warning if parameters are not tagged
- Improved warnings for other invalid content
- Man page output path (via XML)
- DTD for output validation
- Translation of HTML to XHTML using `xmllint` when using XML output
- Nested class handling
- Customizable date format
- C pseudoclass support (`typedef struct`)
- Better nested class support
- C++ constructors/destructors now sorted first in the list of class methods.
- The @ignore tag—allows you to remove matching tokens from declarations
- “Unsorted” flag
- Summary function and method lists (a mini-TOC)
- Automated detection of numbered lists
- Automatic handling of availability macros
- Improved overall appearance
- Includes a regression test suite

This section attempts to list all of the new tags added in HeaderDoc 8 (some of which were actually available, but undocumented, in HeaderDoc 7).

**`@classdesign`**
: Text block describing the overall design of a class

**`@coclass`**
: String describing a class that this class was designed to work with

**`@dependency`**
: String describing a class upon which this class depends heavily

**`@exception`**
: String describing an exception thrown by a function/method/class

**`@functiongroup`**
: Tag for grouping functions and methods; this takes priority over the `@group` tag with respect to functions and methods.

**`@group`**
: Tag for grouping data, functions, and so on, thus changing the order in which they appear in the table of contents.

(Note: the `@functiongroup` tag takes priority over the `@group` tag for functions.)

**`@helper`**
: String telling what helper classes this class uses

**`@helps`**
: For helper classes, string telling what sort of classes this class was designed to help

**`@instancesize`**
: Text block containing the size of an instance of this class

**`@methodgroup`**
: See `@functiongroup`.

**`@ownership`**
: String describing what class instantiates the current class (for example, I/O Kit nubs)

**`@performance`**
: Text block to describe performance characteristics of a class (for example, “This class is not appropriate for use in high-performance environments”)

**`@security`**
: Text block to describe security considerations when using this class

**`@superclass`**
: Adds superclass info to a C pseudoclass; also can be used to cause members of the superclass to be merged into the subclass

**`@throws`**
: See `@exception`.

This section lists known issues in HeaderDoc 8. We hope to improve in these areas in future versions. If you find issues not listed here, please file bugs.

- HeaderDoc 8 is somewhat slower than previous versions. This is because the entire parser has been rewritten from the ground up and now does a token-based parse of the input file.

  While this approach should significantly improve the correctness of output (colorizer bugs notwithstanding), it is doing a lot more work than before, and thus takes longer.
- The default color scheme generated by HeaderDoc matches Xcode coloring. There are a number of files supplied as alternative color schemes, ranging from pleasant to utterly hideous and blinking (used mainly for testing). Swap out your `headerDoc2HTML.config` file as desired.
- Although a minimal `gatherheaderdoc` template is built into the tool itself, the default template used by `gatherheaderdoc` is an actual file that comes preinstalled as `Xcode.app/Contents/Developer/usr/share/headerdoc/conf/com.apple.headerdoc.exampletocteplate.html` inside the Xcode app bundle (or `/usr/share/headerdoc/conf/com.apple.headerdoc.exampletocteplate.html` if you built HeaderDoc yourself). The format for this template is described in [Advanced HeaderDoc Configuration and Features](Advanced%20HeaderDoc%20Configuration%20and%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzvgawueqkcircuqq2j). Also see [Example gatherheaderdoc Template](Advanced%20HeaderDoc%20Configuration%20and%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzvgawueqkcirdeur2d) for an example of the template format.

This section describes late-breaking bugs in HeaderDoc 8.9.

There are no known errata yet for HeaderDoc 8.9.

To keep up to date with the latest errata and bug fixes, join the [headerdoc-dev](http://lists.apple.com/mailman/listinfo/headerdoc-dev) mailing list.

[Next](Symbol%20Markers%20for%20HTML-Based%20Documentation.md)[Previous](Testing%20HeaderDoc.md)

