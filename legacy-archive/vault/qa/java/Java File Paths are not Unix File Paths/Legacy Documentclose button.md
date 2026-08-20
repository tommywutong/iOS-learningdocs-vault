---
title: Java File Paths are not Unix File Paths
apple_id: DTS10001386
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-03-20'
source_url: https://developer.apple.com/library/archive/qa/java/java11.html
archived_at: '2026-07-18T02:29:41.311477Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA11Java File Paths are not Unix File Paths |

|  |  |  |
| --- | --- | --- |
| ---   Q: Why does my Java code dealing with files run perfectly on my Unix system, but it breaks when I move it to the Macintosh?  A: The file path specification in Java is different than Unix. Keep your Java code platform independent by avoiding the use of any of the following common Unix-isms:   - Do not assume a directory "`/tmp`" exists and is writable. As   an alternative, when using MRJ, you can use the MRJToolkit to locate the Temporary   Items Folder. See the sample class below:  |  | | --- | | ``` import java.io.File; import java.io.FileNotFoundException; import com.apple.mrj.MRJFileUtils; public class MRJTempFolder {     /**      * Returns the Temporary Items Folder on the Mac OS.      * @return a File object representing the Temporary Items Folder,      * or null, if it could not be found.      */     public static File getTempFolder()     {         File tempFolder = null;          try         {             tempFolder = MRJFileUtils.findFolder(MRJFileUtils.kTemporaryFolderType);         }         catch (FileNotFoundException exc) { }          return tempFolder;     } } ``` |     - Do not assume "`/dev/null`" exists as a way to write to the bit   bucket. Instead, subclass `java.io.OutputStream` and implement `write(int)`   as an empty method, then pass an instance of the subclass to `System.setOut`   via the `java.io.PrintStream` constructor. See the example class below:  |  | | --- | | ``` import java.io.*; /**  * A repository for unwanted bytes.  * Basically a replacement for <code>/dev/null</code>  */ public class BitBucketOutputStream extends OutputStream {     /**      * Sets System.out to use the BitBucketOutputStream as the output      * stream.  In effect, redirecting standard out to oblivion.      * @see restoreSystemOut      */     public static void nullSystemOut()     {         System.setOut(new PrintStream(new BitBucketOutputStream(), true));     }      /**      * Recreates a System.out similar to the default System.out, and restores      * the default behavior.      * @see #nullSystemOut      */     public static void restoreSystemOut()     {         FileOutputStream fdOut = new FileOutputStream(FileDescriptor.out);         System.setOut(new PrintStream(new BufferedOutputStream(fdOut, 128), true));     }     /**      * Sets System.err to use the BitBucketOutputStream as the output      * stream.  In effect redirecting standard error to oblivion.      * @see restoreSystemErr      */     public static void nullSystemErr()     {         System.setErr(new PrintStream(new BitBucketOutputStream(), true));     }      /**      * Recreates a System.err similar to the default System.err, and restores      * the default behavior.      * @see #nullSystemErr      */     public static void restoreSystemErr()     {         FileOutputStream fdErr = new FileOutputStream(FileDescriptor.err);         System.setErr(new PrintStream(new BufferedOutputStream(fdErr, 128), true));     }      /**      * Does nothing with the specified byte.      *      * @param      b the <code>byte</code> to ignore.      * @exception  IOException  if an I/O error occurs.      */     public void write(int b) throws IOException     { } } ``` | |

#### [Mar 20 2000]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
