---
title: HeaderDoc User Guide
apple_id: TP40001215
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2016-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/usage/usage.html
archived_at: '2026-07-15T07:24:28.392125Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HeaderDoc User Guide](Introduction.md)


[Next](HeaderDoc%20Tags.md)[Previous](Introduction.md)

# Using HeaderDoc

HeaderDoc includes two scripts, `headerdoc2html` (`headerDoc2HTML.pl` in the source distribution), which generates documentation for each header it encounters, and `gatherheaderdoc` (`gatherHeaderDoc.pl` in the source distribution), which finds these islands of documentation and assembles a master table of contents linking them together.

The `gatherheaderdoc` tool is a postprocessing script for HeaderDoc. Its primary purpose is to take a directory containing output from HeaderDoc and create a table of contents with links.

The `gatherheaderdoc` tool is highly configurable. You can configure it to insert custom breadcrumb links, use a custom TOC template, and even automatically insert “framework” information into the TOC template, if desired.

This chapter is divided into three parts:

- [Running headerdoc2html](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmztg4wvgvzs)—information about running `headerdoc2html`.
- [Running gatherheaderdoc](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmztg4wvgvzr)—information about running `gatherheaderdoc`.

Once you have a header containing HeaderDoc comments, you can run the `headerdoc2html` script to generate HTML output like this:

```

 > headerdoc2html MyHeader.h
```

This will process `MyHeader.h` and create an output directory called `MyHeader` in the same directory as the input file. To view the results in your web browser, open the file `index.html` that you find inside the output directory.

Instead of specifying a single input file (as above), you can specify an input directory if you wish. HeaderDoc will process every `.h` file in the input directory (and all of its subdirectories), generating an output directory of HTML files for each header that contains HeaderDoc comments.

HeaderDoc processes C++ and Objective-C headers in much the same way that it does a C header. In fact, until HeaderDoc encounters a class declaration in a C++ header, the processing is identical.

When HeaderDoc generates the HTML documentation for a C++ or Objective-C header, it creates one frameset for the header as a whole, and separate framesets for each class, protocol, or category declared within the header.

Within Objective-C class declarations, you can use the `@method` tag to document each method. Since Objective-C is a superset of C, the header might also declare types, functions, or other API outside of any class declaration. You would use `@typedef`, `@function`, and other C tags to document these declarations.

HeaderDoc records the access control level (public, protected, or private) of API elements declared within a C++ class. This information is used to further group the API elements in the resulting documentation.

HeaderDoc has a number of useful command-line switches that alter its behavior.

| Flag | Description |
| --- | --- |
| `-C`  `--class-as-composite` | Causes HeaderDoc to output class contents as a composite page instead of breaking it up into separate pages for functions, data types, and so on. |
| `-D` _<token>_  `-D` _<token>_`=`_<value>_  `--defined` _<token>_  `--defined` _<token>_`=`_<value>_ | Specifies that the token should be explicitly defined to the specified value (or 1 if no value is specified) for C preprocessing purposes. |
| `-E`  `--process-everything` | Process everything. With this flag, HeaderDoc attempts to process an entire file, including content that has no HeaderDoc markup.  __Note:__ Not all programming languages support this flag. |
| `-F`  `--old-style-frames` | Tells HeaderDoc to generate framesets instead of using iframe elements.  __Note:__ In HeaderDoc 8.7, you should generally specify this flag because of a problem with links opening in a new page in the iframe-based output. See [Late-Breaking Bugs](HeaderDoc%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmrqgewvgvzu) for more info and patches. |
| `-H`  `--insert-header` | Turns on inclusion of the `htmlHeader` line, as specified in the configuration file. |
| `-L`  `--suppress-local-variables` | Disables emission of documentation for function-local variables (documented with the `@var` tag inside a function’s documentation block). This allows you to have a traditional version of your documentation for public API purposes and a more complete version for internal purposes. |
| `-M`  `--man-section` | Specifies the section number to use when generating man page content with the `-m` flag. |
| `-N`  `--ignore-all-names` | Ignore all names specified in HeaderDoc tags (except for anonymous enums in which no name is provided by the code) and use the names specified by the code instead. |
| `-O`  `--outer-names-only` | Enables “outer name only” type handling, in which tag names for typedefs are not documented (for example, `foo` in `typedef struct foo {...} tdname;`). |
| `-P`  `--pipe-output` | Pipe mode. In this mode, HeaderDoc prints the resulting XML content (default) or function list to standard output. You can only process a single file at a time in this mode. |
| `-Q`  `--paranoid` | The opposite of quiet, this flag enables paranoid warnings about a number of common problems. |
| `-S`  `--merge-superclass-docs` | Causes HeaderDoc to include functions and data types from the superclass in the documentation of child classes (if they are processed at once). |
| `-T` _<mode>_  `--test` _<mode>_ | HeaderDoc test mode. Note that this test mode is only available when running from a source tarball, not from the installed system. For more information, see [Testing HeaderDoc](Testing%20HeaderDoc.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmjnknltc). |
| `-U` _<token>_  `--undefined` _<token>_ | Specifies that the token should be explicitly undefined for C preprocessing purposes. |
| `-X`  `--xml-output` | Causes HeaderDoc to output XML content instead of HTML. |
| `-a`  `--align-columns` | Tells HeaderDoc to attempt to align function parameters vertically after the opening parenthesis instead of indenting them by a single tab width. |
| `-b`  `--basic-processing-only` | Puts HeaderDoc into “basic” mode. In this mode, numbered lists are not automatically recognized, and embedded HeaderDoc comments are not removed from declarations. |
| `-c`  `--config-file` | Allows you to add an alternate configuration file. For example:   |  | | --- | | ``` headerdoc2html -c myCustomHeaderDocConfigFile.config MyHeader.h ``` | |
| `-d`  `--debugging` | Turns on extra debugging output. |
| `-e`  `--exclude-list-file` | Specifies an exclude list. The file passed as an argument to the `-e` flag contains a newline-separated list of Perl regular expressions. Any filename or file path that matches any of these regular expressions is excluded from processing. |
| `-f`  `--function-list-output` | Enables function list output mode. In this mode, HeaderDoc emits a simple list of function names encountered and the contents of those functions in an easily machine-parseable format. |
| `-g`  `--group-right-side` | Group content on the right side by group instead of alphabetically. |
| `-i`  `--truncate-function-like-macros` | Tells HeaderDoc to output the body of macro declarations. |
| `-j`  `--allow-javadoc-syntax` | Enables support for JavaDoc (`/**`) comment markers in other programming languages. |
| `-l`  `--no-link-requests` | Tells HeaderDoc not to generate link requests in declarations. |
| `-m`  `--man-page-output` | Tells HeaderDoc to generate a man page for each function found in lieu of generating XML or HTML output. |
| `-n`  `--ignore-apiowner-names` | Ignore the names of classes and headers specified in HeaderDoc tags and always use the names provided by the code itself. |
| `-o` _<directory>_  `--output-directory` _<directory>_ | Allows you to specify another directory for the output. For example:   |  | | --- | | ``` headerdoc2html -o /tmp MyHeader.h ``` | |
| `-p`  `--enable-cpp` | Enables the C preprocessor. With this switch, any `#define` with HeaderDoc markup affects any content that appears after it within the same header file, and also affects any content after the `#include` in any file that includes that header file. |
| `-q`  `--quiet` | Makes HeaderDoc operate silently (except for warnings and errors). |
| `-s`  `--strip` | Causes HeaderDoc to enter a comment stripping mode, in which it outputs a copy of your header file in the output directory from which all HeaderDoc comments have been removed. |
| `-t`  `--enforce-strict-tagging` | Enables strict tagging mode, in which any function parameters not described with an `@param` tag result in a warning. |
| `-u`  `--unsorted` | Disables sorting of functions, data types, and so on in the table of contents, thus preserving the original file order. Note that if you simply want to preserve groupings, you should use the `@group` or `@functiongroup` tags instead. |
| `-v`  `--version` | Tells HeaderDoc to print version information and exit. |
| `-x`  `--doxytags` | Causes HeaderDoc to emit a Doxygen-style tag file. (Note that this variant of the tag file format adds class inheritance information that is not typically included in a normal Doxygen tag file.) |
| `--tocformat` | Sets the format used for the table of contents (left side). Valid values are:   - `default`—use the most current TOC style (currently `div`). - `div`—use the div format (currently the default). - `frames`—use the legacy frames format. - `iframes`—use the legacy iframes format. |
| `--apple` | Enables various flags and additional policy checks specific to Apple internal use. |
| `--auto-availability` | Interpret `#if` and `#ifdef` blocks that contain availability information and automatically populate the availability information. (This is probably not useful for projects that are not part of OS X.) |
| `--document-internal` | Include documentation marked with `@internal`. By default, this documentation is omitted. |

Most of these switches can be used in combination with each other. The obvious exceptions are `-X` and `-m` (XML vs. man page output). If you need both XML and man page output, you should specify the `-X` flag (XML output), then run the scripts `hdxml2manxml` and `xml2man` to convert the XML output to a man page yourself.

The `gatherheaderdoc` script scans an input directory (recursively) for any documentation generated by `headerdoc2html`. It creates a master table of contents (named `masterTOC.html` by default—the name can be changed by setting a new name in the configuration file or by specifying a second argument). It also adds a “top” link to all the documentation sets it visits to make it easier to navigate back to the master table of contents.

Here's an example of how to create documentation for a number of headers (the sample ones provided with the scripts) and then generate a master table of contents:

```
 > headerdoc2html -o OutputDir ExampleHeaders
 > gatherheaderdoc OutputDir
```

You can now open the file `OutputDir/masterTOC.html` in your browser to see the interlinked sets of documentation.

You can also add a second argument to change the output file name. For example:

```
 > headerdoc2html -o OutputDir ExampleHeaders
 > gatherheaderdoc OutputDir MYTOCNAME.html
```

This time, `gatherheaderdoc` created the file `OutputDir/MYTOCNAME.html` instead of `OutputDir/masterTOC.html`.

For more information on configuring `gatherheaderdoc`, see [Basic HeaderDoc Configuration](Basic%20HeaderDoc%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzuhawugrkhjjdeuskc).

[Next](HeaderDoc%20Tags.md)[Previous](Introduction.md)

