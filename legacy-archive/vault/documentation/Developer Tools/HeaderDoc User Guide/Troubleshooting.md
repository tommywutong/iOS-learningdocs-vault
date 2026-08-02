---
title: HeaderDoc User Guide
apple_id: TP40001215
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2016-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/troubleshooting/troubleshooting.html
archived_at: '2026-07-15T07:24:28.381862Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HeaderDoc User Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](HeaderDoc%20Class%20Hierarchy.md)

# Troubleshooting

This chapter explains how to troubleshoot HeaderDoc issues, including explanations of error messages, in the form of a Q&A list.

This troubleshooting guide assumes that you are running the latest version of HeaderDoc (currently 8.8). If not, you should first upgrade to the latest version and see if your problem goes away.

You can get the latest version of HeaderDoc on the Apple Open Source website: [http://www.opensource.apple.com/](http://www.opensource.apple.com/). Choose the most recent version of OS X or Xcode, then search for `headerdoc` on the page, and click the download link in the rightmost column. Except as described below, HeaderDoc should work correctly on earlier versions of OS X. If it does not, please file a bug.

- __Q:__ When running gatherheaderdoc, I get the error message “Using the -d flag requires the HTML::FormatText module. To install it, type: sudo cpan HTML::FormatText”.
- __A:__ Doc set generation requires two Perl modules that are not present in OS X prior to 10.7. To install those modules, log in as an admin user, then type:

```
sudo cpan HTML::FormatText
sudo cpan HTML::TreeBuilder
```

  Enter your admin password when prompted. For more information, see the `cpan` man page and [http://www.cpan.org/](http://www.cpan.org/).
- __Q:__ When running gatherheaderdoc, I get an error from something called resolveLinks that says “I/O error: encoder error”. What’s going on?
- __A:__ You have a header file that was not written in UTF-8. Change the encoding for that file by adding an `@encoding` or `@charset` entry within the `@header` tag.

  Beginning in HeaderDoc 8.8, HeaderDoc attempts to detect this automatically. If you see this error in HeaderDoc 8.8 or later, please file a bug and enclose a copy of the header.

- __Q:__ HeaderDoc keeps warning me that my LibXML2 version is too old. How do I fix this problem?
- __A:__ Obtain a more recent version of LibXML2 from [http://www.xmlsoft.org](http://www.xmlsoft.org/).

- __Q:__ I’m trying to do an @link to a method, but HeaderDoc insists that myMethodname%58 could not be found.
- __A:__ Beginning in HeaderDoc 8.5, you should use colons in the names of methods in @link tags, rather than replacing them with %58.

- __Q:__ HeaderDoc is choking on classes with multiple inheritance.
- __A:__ Update to HeaderDoc 8.5.

- __Q:__ Why isn’t HeaderDoc doing C preprocessing? I thought you said this version did.
- __A:__ It does, but you have to specify an additional flag, `-p`, to invoke this behavior.

- __Q:__ The C preprocess keeps including the wrong files.
- __A:__ HeaderDoc has no way of knowing the final installed location of header files. To work correctly, it depends on all header files having a unique name. Rename your header files so that no two files have exactly the same name.

- __Q:__ I keep getting the error “Name being changed (oldname -> newname).”
- __A:__ This is usually caused by one of the following:

  - 1.Multiple @discussion blocks. Remove one of them.
  - 2.An extra preprocessor macro token after the close parenthesis in a function declaration. HeaderDoc thinks you are writing a K&R C declaration. Either use @ignore to ignore the token or explicitly mark up the preprocessor macro and enable C preprocessing.

- __Q:__ HeaderDoc says “Can’t open <filename> for availability macros.”
- __A:__ Your installation is likely missing the `Availability.list` file. In Xcode 4.3 and later, it lives in `/usr/share/headerdoc/`. In OS X v10.6 and v10.7 with Xcode 4.2.1 and earlier, it lived in `/System/Library/Perl/Extras/version/HeaderDoc`. In OS X v10.5 and earlier, it lived in `/System/Library/Perl/version/HeaderDoc`.

- __Q:__ I’m getting the error “Conflicting declarations for function/method ($name1) outside a class. This is probably not what you want.”
- __A:__ As it says, you have two functions that are not class members, but have the same name (or you forgot to put HeaderDoc markup on the enclosing class). This is legal in C++ but is discouraged because the apple_ref syntax does not provide a uniqueness guarantee in these instances. HeaderDoc tries to fudge this by appending a signature when it sees this situation, but as a general rule, you should not rely on this behavior if you care about apple_ref markup.

- __Q:__ HeaderDoc is spewing warnings about “Parsed parameter <blah> not found in declaration of function/method/typedef <blah>.”
- __A:__ Chances are, you made a typographical error when adding `@param` or `@field` markers in the HeaderDoc comment. Check your spelling carefully and remember that capitalization matters.

- __Q:__ HeaderDoc keeps saying “Tagged parameter <blah> not found in declaration of function/method/typedef <blah>.”
- __A:__ You turned on the strict parameter/field checking with the `-t` flag. Turn it off if you don’t want those warnings.

- __Q:__ HeaderDoc says “Braces/class braces/parentheses/square braces do not match. We may have a problem.”
- __A:__ This usually means exactly what it says. If you are depending on a C preprocessor macro to make braces match, you should try to avoid doing so. If you cannot avoid this, make sure you enable C preprocessing and add HeaderDoc markup to the macro definition.

- __Q:__ HeaderDoc says “End of parse tree reached while searching for matching definition”.
- __A:__ This is generally caused by either placing a HeaderDoc comment immediately prior to a close curly brace or by placing the wrong HeaderDoc type tag in the comment (such as preceding a `typedef` with an `@function` comment).

- __Q:__ HeaderDoc says “No matching declaration found. Last name was <blah>.”
- __A:__ This is generally caused by either placing a HeaderDoc comment immediately prior to a close curly brace or by placing the wrong HeaderDoc type tag in the comment (such as preceding a `typedef` with an `@function` comment).

- __Q:__ I’m getting the error “Unable to process #define macro “<name>.”
- __A:__ Please file a bug.

- __Q:__ HeaderDoc says “WARNING: multiple matches found for symbol “<blah>.” Only the first matching symbol will be linked.”
- __A:__ You have multiple symbols with the same name (possibly in different files, or possibly different types—for example a function and a `#define`). HeaderDoc has no way to know which of those two or more “myname” symbols you’re talking about when you say `@link myname`. To fix this problem, look in the HeaderDoc-generated HTML for the desired destination. Find the name anchor that looks like `<a name=”//apple_ref/...”>` and instead of just giving the name, give the entire contents of that anchor.

- __Q:__ HeaderDoc says ‘WARNING: no symbol matching “<blah>” found. If this symbol is not in this file or class, you need to specify it with an api ref tag (e.g. apple_ref).’
- __A:__ You may not be processing all of the needed files at once, or HeaderDoc may be feeling cranky. In any case, to fix this problem, look in the HeaderDoc-generated HTML for the desired destination. Find the name anchor that looks like `<a name=”//apple_ref/...”>` and instead of just giving the name, give the entire contents of that anchor.

- __Q:__ HeaderDoc issues the warning “WARNING: resolveLinks not installed. Please check your installation.”
- __A:__ Be sure you are installing correctly. First, type “`make`”, then “`make realinstall`”.

- __Q:__ HeaderDoc says “WARNING: Unexpected headerdoc markup found in <blah> declaration.”
- __A:__ Chances are, you followed one HeaderDoc comment with another HeaderDoc comment without anything in-between.

- __Q:__ HeaderDoc warns “Unterminated @link tag (starting field was: @link...).”
- __A:__ If you are using JavaDoc-style @link tagging (`{@link symbol Link Text}`), don’t forget the close curly brace. If you are doing HeaderDoc-style @link tagging (`@link symbol Link Text @/link`), don’t forget the `@/link`.

- __Q:__ HeaderDoc said “Parser bug: empty outer type.”
- __A:__ This is probably a bug unless you’re doing something really weird with preprocessor directives that violate the normal C syntax rules (in which case you should either @ignore the extraneous tokens or enable C preprocessing). In general, though, you should probably file a bug.

- __Q:__ HeaderDoc keeps saying “Objective-C method found outside a class or interface (or in a class or interface that lacks HeaderDoc markup).”
- __A:__ Make sure you properly tagged the enclosing class or interface declaration.

- __Q:__ HeaderDoc keeps saying “Unable to find parse tree. Please file a bug.”
- __A:__ This should not happen; please file a bug.

- __Q:__ HeaderDoc keeps saying “Couldn’t find parser state. Using slow method.”
- __A:__ If you have a class that starts with a preprocessor token (such as `DeclareStructors(MyClass)` or similar), this will break things badly. There are two solutions. The easiest solution is to add `@ignorefuncmacro DeclareStructors` (or whatever the macro name happens to be) in your `@header` declaration.
- An alternative fix is to make sure that you are processing the header file that contains the macro at the same time as you process the class. Enable C preprocessing with the `-p` flag. Finally, add a HeaderDoc comment before the macro definition.
- If this problem is not caused by use of a macro, please file a bug. This fallback case should not affect output, however.

- __Q:__ HeaderDoc keeps saying ‘Could not determine include file name for “#include FW(Carbon,CarbonEvents.h)”’ or similar.
- __A:__ Ideally, you should use a standard include file syntax. If that is not possible, you should enable the C preprocessor with the `-p` flag, include the file containing the FW macro on the command line, and add HeaderDoc markup to that macro.

- __Q:__ HeaderDoc says “Unknown regexp delimiter “...”. Please file a bug.
- __A:__ This should not happen; please file a bug.

- __Q:__ HeaderDoc keeps saying “Unknown keyword <blah> in block-parsed declaration”.
- __A:__ Make sure that the header compiles correctly with `gcc`. If it does, please file a bug.

Other error messages generally fall into one of two categories: self-explanatory errors (such as “Unknown tag @whatever in function comment”) or utterly unintelligible (such as “Parser bug: empty outer type”). In the case of the former, please fix the appropriate declaration. In the case of the latter, pleas file a bug. Which brings us to the last question....

- __Q:__ How do I file a bug?
- __A:__ Before filing a bug, you should subscribe to the HeaderDoc-dev mailing list on lists.apple.com. Ask if anyone else has seen the problem. If not, you should file a bug. To subscribe, visit [http://lists.apple.com/mailman/listinfo/headerdoc-dev](http://lists.apple.com/mailman/listinfo/headerdoc-dev).
- If you are an ADC member with access to bugreport.apple.com, please file a bug through that mechanism. The correct component is “HeaderDoc”, with version “Darwin”.

- __Q:__ Some of my Ruby, JavaScript, or Tcl scripts are missing content.
- __A:__ HeaderDoc 8.8 did not parse regular expressions in any language other than Perl.

  In most languages, this makes no difference because regular expressions are stored in strings and obey normal string parsing rules. In Python, this makes no difference because its parser is based solely on indentation depth. This leaves three languages in which regular expressions can cause problems: Ruby, JavaScript, and Tcl.

  Although most regular expressions do not cause problems, expressions that match literal braces, quotation marks, parentheses, and other symbols may confuse HeaderDoc because it is unaware that they are appearing in the context of a regular expression.

  The recommended solution is to upgrade to HeaderDoc 8.9, which should fix the problem. If upgrading is not possible, you can work around this issue by adding a throwaway regular expression in a previous or subsequent line that contains the necessary matching open or close brace, parenthesis, or quotation mark to work around the problem. (This extra regular expression must _not_ be in a comment.)

- __Q:__ I’m seeing multiple copies of my functions/typedefs/defines/\*. Why?
- __A:__ You probably specified a name in the `@function` tag (or `@typedef` or...) that was different from the actual name. Delete the incorrect name or pass the -N flag to HeaderDoc, which tells it to globally ignore any names specified in the HeaderDoc markup (HeaderDoc 8.8 and later).

- __Q:__ I’m still seeing multiple copies of a typedef, but with different names.
- __A:__ HeaderDoc, by default, also generates an entry for “tag names” and for every type name. You can remove the tag names by specifying the -O (outer names only) flag. In the following example, the tag name is `mystruct`, and the type name (a.k.a. the “outer name”) is `mystruct_t`:

```
        typedef struct mystruct {int a;} mystruct_t;
```

- __Q:__ Why does my function/method/type/variable/class/\* have a name that appears to include an entire paragraph of the discussion?
- __A:__ One of two things is wrong. Either you included multiple words after the `@function/@typedef/@whatever` and also included an `@discussion` tag or you began a multi-line declaration at the end of the `@function/@typedef/@whatever` line. Don’t do this. See [Multiword Names](HeaderDoc%20Tags.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytemjvfvbuqmzugywugskiirbeqrcd) for more information.

- __Q:__ A bunch of my `functions/typedefs/*` are being linked together with “See Also” attributes. What’s up?
- __A:__ You probably marked a `typedef` with an `@function` comment (or some other incorrect pairing). HeaderDoc will assume that you knew what you were doing and will keep looking through the code until it finds whatever was requested (a function in this case). Everything in-between will get linked together. The purpose for this is primarily to allow you to mark `@typedef` for a `struct` followed by a `typedef`, but it is useful in other situations as well. Fix the incorrectly matched comment, and the problem should go away.

- __Q:__ Why am I not getting links when I add `@link` tags?
- __A:__ There are several possible reasons:

  - 1.If you used `apple_ref` markup, you may have made a typo.
  - 2.If you used a symbol name that did not exist, you would get a warning when running `headerdoc2html` and no link will be generated.
  - 3.The `@link` tag only inserts a link request into the HTML. To turn this into an actual link, you must run `gatherheaderdoc` (which in turn runs `resolveLinks` to create the links). Until you run gatherHeaderDoc, all you will see in the HTML are a bunch of specially-formatted comments.

- __Q:__ Every time I run `gatherheaderdoc`, all of the spaces in my declarations go away. What’s going on?
- __A:__ This is a bug in `libxml2` that is fixed in more recent versions. Please visit [http://www.xmlsoft.org](http://www.xmlsoft.org/) to obtain a more recent version (or upgrade to OS X v10.4 or later).

- __Q:__ I’m confused. Where can I get help?
- __A:__ The best place to get help is the HeaderDoc-dev mailing list. To subscribe, go to [http://lists.apple.com/mailman/listinfo/headerdoc-dev](http://lists.apple.com/mailman/listinfo/headerdoc-dev).

[Next](Document%20Revision%20History.md)[Previous](HeaderDoc%20Class%20Hierarchy.md)

