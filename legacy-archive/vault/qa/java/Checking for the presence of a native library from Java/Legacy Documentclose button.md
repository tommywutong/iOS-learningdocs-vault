---
title: Checking for the presence of a native library from Java
apple_id: DTS10001394
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-11-29'
source_url: https://developer.apple.com/library/archive/qa/java/java19.html
archived_at: '2026-07-18T02:29:41.927744Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA19Checking for the presence of a native library from Java |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: My Java application relies on a native library to be present in the MRJ Libraries folder, which is in the Extensions folder. How do I check to see if the user has correctly placed my library in the MRJ Libraries folder?  A: There are many ways to do this. Perhaps the simplest way is to do the following:    |  | | --- | | ``` if (!(new File(System.getProperty("java.home"), "myLibrary").exists()))     // report an error to the user ``` |     |  | | --- | | This is probably not the best approach. Native libraries really should reside either in the Extensions folder of the System, or in the local application directory. For example, if your application uses GL4Java, you will not be able to use the above approach because the native library is not in the MRJ Libraries folder. Furthermore, libraries used by a single app should not go in the Extensions folder but instead in the same folder as the app. This simplifies configuration, installation and de-installation, and reduces the chance of library name conflicts with some other vendor's code.  If you really do need to find a library in the extensions folder, you can do the following: |     |  | | --- | | ``` import com.apple.mrj.MRJFileUtils; import com.apple.mrj.MRJApplicationUtils; try {     if ( MRJApplicationUtils.isMRJToolkitAvailable() )     {         File theFile = MRJFileUtils.             findFolder(MRJFileUtils.kExtensionFolderType);         File libraryFile = new File( theFile, "myLibrary" );         if (( libraryFile.exists() )             System.out.println( "Found: "  + libraryFile.getPath() );         else             System.out.println( "Library " + libraryFile.getPath()                  + " not found" );      }      else         System.out.println("MRJ Toolkit is not available on this machine."); } catch ( FileNotFoundException fnf ) {     fnf.printStackTrace(); } ``` |     |  | | --- | | Keep in mind that you will need to add MRJToolkitStubs.zip to your project in order to link successfully. This library file contains the proper class declarations, but only stub implementations. The Java classes, such as `MRJFileUtils` which is used by this example, are stored in MRJClasses.zip, which is placed in the Extensions folder as part of the normal MRJ installation.  `MRJFileUtils` and `MRJApplicationUtils` are part of MRJToolkit which is part of the [MRJ SDK](https://developer.apple.com/java/text/download.html#sdk). The MRJToolkit provides several convenient functions for adding standard Macintosh functionality to your Java application. For more information on `findFolder( )` or other methods in the toolkit, please consult the document _About MRJToolkit_ in the [MRJ SDK](https://developer.apple.com/java/text/download.html#sdk).  This example is designed to work on a Macintosh using Macintosh Runtime for Java 2.1.4 or later. You may need to use a different approach on other platforms. Note that we check to see if the MRJ Toolkit is available before we call `findFolder( )`. Although this is not necesssary in this case (`findFolder( )` will return an empty file object if MRJ Toolkit is not available), it is good practice to take this approach when writing platform-specific code. |  [Nov 29 1999] |

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
