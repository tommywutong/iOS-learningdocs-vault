---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSPathUtilities.html
archived_at: '2026-07-15T08:13:56.397143Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSPathUtilities

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

This class provides static methods that are useful when working with paths. Specifically, it includes methods that extract particular path components ( [lastPathComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxwyyltorigc5diinxw24dpnzsw45a) and [pathExtension](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxaylunbcxq5dfnzzws33o)), modify paths ( [stringByAppendingPathComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzifyhazlomruw4z2qmf2gqq3pnvyg63tfnz2a), [stringByAppendingPathExtension](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzifyhazlomruw4z2qmf2gqrlyorsw443jn5xa), [stringByDeletingLastPathComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzirswyzlunfxgotdbon2faylunbbw63lqn5xgk3tu), [stringByDeletingPathExtension](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzirswyzlunfxgoudboruek6dumvxhg2lpny), and [stringByStandardizingPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzkn2gc3temfzgi2l2nfxgoudborua)), and return special paths ( [homeDirectory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxwq33nmvcgs4tfmn2g64tz)).

The NSPathUtilities class cannot be instantiated.

## Method Types

---

> **Extracting path components**
>
> : [lastPathComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxwyyltorigc5diinxw24dpnzsw45a): [pathExtension](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxaylunbcxq5dfnzzws33o)
>
> **Manipulating paths**
>
> : [stringByAppendingPathComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzifyhazlomruw4z2qmf2gqq3pnvyg63tfnz2a): [stringByAppendingPathExtension](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzifyhazlomruw4z2qmf2gqrlyorsw443jn5xa): [stringByDeletingLastPathComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzirswyzlunfxgotdbon2faylunbbw63lqn5xgk3tu): [stringByDeletingPathExtension](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzirswyzlunfxgoudboruek6dumvxhg2lpny): [stringByNormalizingExistingPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzjzxxe3lbnruxu2lom5cxq2ltoruw4z2qmf2gq): [stringByStandardizingPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzkn2gc3temfzgi2l2nfxgoudborua)
>
> **Resolving special paths**
>
> : [homeDirectory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxwq33nmvcgs4tfmn2g64tz)
>
> **Deprecated methods**
>
> : [URLWithPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxvkusmk5uxi2cqmf2gq): [fileExistsAtPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxwm2lmmvcxq2ltorzuc5cqmf2gq): [pathIsAbsolute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxaylunbexgqlconxwy5lumu): [pathIsEqualToString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxaylunbexgrlrovqwyvdpkn2he2lom4)

## Static Methods

---

### fileExistsAtPath

`public static boolean fileExistsAtPath(String aString)`

Deprecated in the Java Foundation framework. Don't use this method. Use `(new File(aString)).exists()` instead.

---

### homeDirectory

`public static String homeDirectory()`

Returns a string containing the home directory path for the user who executes the application.

---

### lastPathComponent

`public static String lastPathComponent(String aString)`

Returns the last path component of _aString_. The following table illustrates the effect of __lastPathComponent__ on a variety of different paths:

|  |  |
| --- | --- |
| ___aString_'s Value__ | __String Returned__ |
| "`/tmp/scratch.tiff`" | "`scratch.tiff`" |
| "`/tmp/scratch`" | "`scratch`" |
| "`/tmp/`" | "`tmp`" |
| "`scratch`" | "`scratch`" |
| "`/`" | "" (an empty string) |

---

### pathExtension

`public static String pathExtension(String aString)`

Interprets _aString_ as a path, returning the _aString_'s extension, if any (not including the extension divider). The following table illustrates the effect of __pathExtension__ on a variety of different paths:

|  |  |
| --- | --- |
| ___aString_'s Value__ | __String Returned__ |
| "`/tmp/scratch.tiff`" | "`tiff`" |
| "`/tmp/scratch`" | "" (an empty string) |
| "`/tmp/`" | "" (an empty string) |
| "`/tmp/scratch..tiff`" | "`tiff`" |

---

### pathIsAbsolute

`public static boolean pathIsAbsolute(String aString)`

Deprecated in the Java Foundation framework. Don't use this method. Use `(new File(aString)).isAbsolute()` instead.

---

### pathIsEqualToString

`public static boolean pathIsEqualToString( String string1, String string2)`

Deprecated in the Java Foundation framework. Don't use this method. You should never have to invoke it.

---

### stringByAppendingPathComponent

`public static String stringByAppendingPathComponent( String string1, String string2)`

Returns a string made by appending _string1_ with _string2_, preceded by if necessary by a path separator. The following table illustrates the effect of this method on a variety of different paths, assuming that _string2_ is supplied as "`scratch.tiff`":

|  |  |
| --- | --- |
| ___string1_'s Value__ | __Resulting String__ |
| "`/tmp`" | "`/tmp/scratch.tiff`" |
| "`/tmp/`" | "`/tmp/scratch.tiff`" |
| "`/`" | "`/scratch.tiff`" |
| "" (an empty string) | "`scratch.tiff`" |

__See Also:__ [stringByAppendingPathExtension](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzifyhazlomruw4z2qmf2gqrlyorsw443jn5xa), [stringByDeletingLastPathComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzirswyzlunfxgotdbon2faylunbbw63lqn5xgk3tu)

---

### stringByAppendingPathExtension

`public static String stringByAppendingPathExtension( String string1, String string2)`

Returns a string made by appending to _string1_ an extension separator followed by _string2_. Note that if _string1_ ends with one or more slashes ("/"), these slashes are deleted. The following table illustrates the effect of this method on a variety of different paths, assuming that _string2_ is supplied as `"tiff"`:

|  |  |
| --- | --- |
| ___string1_'s Value__ | __Resulting String__ |
| "`/tmp/scratch.old`" | "`/tmp/scratch.old.tiff`" |
| "`/tmp/scratch.`" | "`/tmp/scratch..tiff`" |
| "`/tmp/`" | "`/tmp.tiff`" |
| "`scratch`" | "`scratch.tiff`" |

---

### stringByDeletingLastPathComponent

`public static String stringByDeletingLastPathComponent(String aString)`

Returns a string made by deleting the last path component from _aString_, along with any final path separator. If _aString_ represents the root path, however, it's returned unaltered. The following table illustrates the effect of this method on a variety of different paths:

|  |  |
| --- | --- |
| ___aString_'s Value__ | __Resulting String__ |
| "`/tmp/scratch.tiff`" | "`/tmp`" |
| "`/tmp/lock/`" | "`/tmp`" |
| "`/tmp/`" | "`/`" |
| "`/tmp`" | "`/`" |
| "`/`" | "`/`" |
| "`scratch.tiff`" | "" (an empty string) |

__See Also:__ [stringByDeletingPathExtension](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzirswyzlunfxgoudboruek6dumvxhg2lpny), [stringByAppendingPathComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzifyhazlomruw4z2qmf2gqq3pnvyg63tfnz2a)

---

### stringByDeletingPathExtension

`public static String stringByDeletingPathExtension(String aString)`

Returns a string made by deleting the extension (if any, and only the last) from _aString_. Strips any trailing path separator before checking for an extension. If _aString_ represents the root path, however, it's returned unaltered. The following table illustrates the effect of this method on a variety of different paths:

|  |  |
| --- | --- |
| ___aString_'s Value__ | __Resulting String__ |
| "`/tmp/scratch.tiff`" | "`/tmp/scratch`" |
| "`/tmp/`" | "`/tmp`" |
| "`scratch.bundle/`" | "`scratch`" |
| "`scratch..tiff`" | "`scratch.`" |
| ".`tiff`" | "" (an empty string) |
| "`/`" | "`/`" |

__See Also:__ [pathExtension](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxaylunbcxq5dfnzzws33o), [stringByDeletingLastPathComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzirswyzlunfxgotdbon2faylunbbw63lqn5xgk3tu)

---

### stringByNormalizingExistingPath

`public static String stringByNormalizingExistingPath(String aString)`

Returns a string containing the "normalized" path for an existing file with path _aString_. If the file does not exist, this method returns `null`. The normalized path is always absolute and corresponds to the canonical path returned by the __java.io.File.getCanonicalPath__ method. See Sun's documentation for this method for more information.

__See Also:__ [stringByStandardizingPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgudborufk5djnruxi2lfomxxg5dsnfxgoqtzkn2gc3temfzgi2l2nfxgoudborua)

---

### stringByStandardizingPath

`public static String stringByStandardizingPath(String aString)`

Returns a string made by resolving various elements of _aString_. If the path contains tilde (~), inserts the home directory path in its place. If the path contains the parent directory marker (..) removes the previous path component from the path. If the parent directory marker is at the beginning of _aString_, throws an IllegalArgumentException. The following table illustrates the effect of this method on a variety of different paths assuming that the home directory is "/Local/Users/guest":

|  |  |
| --- | --- |
| ___aString_'s Value__ | __Resulting String__ |
| "`~/scratch.tiff`" | "`/Local/Users/guest/scratch.tiff`" |
| "`~`" | "`/Local/Users/guest`" |
| "`~/..`" | "`/Local/Users/`" |
| "`guest/../john/scratch.tiff`" | "`john/scratch.tiff`" |
| "`../scratch.tiff`" | throws IllegalArgumentException |

---

### __URLWithPath__

`public static java.net.URL URLWithPath(String aString)`

Deprecated in the Java Foundation framework. Don't use this method. Use `new URL("file://" + aString)` instead.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
