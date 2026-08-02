---
title: HeaderDoc User Guide
apple_id: TP40001215
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2016-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/classhierarchy/classhierarchy.html
archived_at: '2026-07-15T07:24:28.249644Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HeaderDoc User Guide](Introduction.md)


[Next](Troubleshooting.md)[Previous](Symbol%20Markers%20for%20HTML-Based%20Documentation.md)

# HeaderDoc Class Hierarchy

```

HeaderElement (Root Class--any header entity that's significant)
 | (to HeaderDoc is a HeaderElement)
 |
 |
 |-----------APIOwner (Object that owns declared API)
 | |
 | |-------Header (Owner for header-wide API)
 | |
 | |-------CPPClass (Container for all non-Objective-C classes and
 | |                    C pseudoclass/COM Interface APIs).
 | |
 | |-------ObjCContainer
 |   |
 |   |-------ObjCClass (Owner for Objective-C class API)
 |   |
 |   |-------ObjCCategory (Owner for Objective-C category API)
 |   |
 |   |-------ObjCProtocol (Owner for Objective-C protocol API)
 |
 |
 |-----------Method (an Objective-C method)
 |
 |-----------Constant
 |
 |-----------Enum
 |
 |-----------Function (any non-objective-C function or method)
 |
 |-----------MinorAPIElement (parameter, members of structs)
 |
 |-----------PDefine
 |
 |-----------Struct (for both structs and unions)
 | |
 | |-------Var (subclass of Struct so that it can contain fields)
 |
 |-----------Typedef


DocReference (Another root class. Used by gatherHeaderDoc to store
             information about documentation framesets within an
             input folder. The script uses this information to
             construct a top-level table of contents with links
             to each frameset.)

ParseTree (Token tree instantiated from BlockParse.pm.)

ParserState (Parser state instance instantiated from BlockParse.pm and stored
            in certain tokens within a ParseTree instance.)

IncludeHash (a simple data structure for storing information about a
            #include directive.)
```

In addition to the classes shown above, the `headerdoc2html`/`headerDoc2HTML.pl` script also uses the non–object-oriented modules `Utilities.pm`, `ClassArray.pm`, and `BlockParse.pm`. Most class instances are instantiated from `headerdoc2html`/`headerDoc2HTML.pl` based on the results of a call to `blockParse`.

The `ParseTree` class is instantiated in the block parser itself. It contains a token tree and a set of operations on that tree (print the tree, return a text or html representation of the tree, walk the parse tree for parameters, walk the parse tree for embedded HeaderDoc markup, and so on).

The `ParserState` class is also instantiated in the block parser. It contains only three methods (`new`, `_initialize`, and `print`), and is primarily just a giant hash with some pre-defined values.

The `IncludeHash` class is essentially just a simple data structure to handle basic information about #include directives. It has two methods (`new` and `_initialize`).

The `gatherHeaderDoc` tool uses an external program, `resolveLinks`, to convert special “link request” comments into links to other files in the directory being processed. This tool (written in C) resides in the `bin` directory within the HeaderDoc modules directory.

HeaderDoc uses `xmllint` (from libxml) to convert HTML into XHTML when generating XML output. HeaderDoc also uses `hdxml2manxml` and `xml2man` from the MPGL suite to generate man pages.

[Next](Troubleshooting.md)[Previous](Symbol%20Markers%20for%20HTML-Based%20Documentation.md)

