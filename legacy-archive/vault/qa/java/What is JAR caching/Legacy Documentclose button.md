---
title: What is JAR caching?
apple_id: DTS10001402
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-10-06'
source_url: https://developer.apple.com/library/archive/qa/java/java27.html
archived_at: '2026-07-18T02:29:43.489141Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA27What is JAR caching? |

|  |  |  |
| --- | --- | --- |
| ---   Q: What is JAR caching?  A: Java code is frequently stored on servers in a special type of file called a JAR (for Java Archive). If a Java applet uses many JARs, or if the JARs are very large, it can take considerable time for the browser to load these files. MRJ 2.2.3 greatly improves JAR caching.  Previous versions of MRJ had caching, but it was up to the browser, and the cache was shared with HTML files. MRJ JAR caching saves copies of these files on your local hard drive. When you use a JAR again, MRJ checks to see if there is a newer version on the server by sending a HTTP `GET` for the JAR file with an if-modified-since modifier, using the last modified date it previously got from the server. If the response from the server is `HTTP_NOT_MODIFIED`, the cached JAR is used and the applet runs immediately. If the response from the server is a variation of `HTTP_OK`, MRJ looks at the last modified field, and if it is not the cached value, the JAR is re-fetched.  MRJ cached JAR files are saved by default in a folder named "MRJ Cache" located in the System Preferences folder. Over time, this folder may grow in size, but by default, storage space will not exceed 100MB. If you want to reclaim some of this space, you can quit all running applications that use Java and then drag the "MRJ Cache" folder to the trash. The next time MRJ needs to cache a JAR file, it will create a new "MRJ Cache" folder.    Q: How do I change the default settings for JAR caching?  A: It is possible to change the default settings by modifying properties in the "mrj.properties" file. These properties can be set by adding a file called "mrj.properties" to the "lib" folder within the "MRJLibraries" folder (in the System Folder:Extensions folder). This file does not exist by default - it can be created and edited with any text editor.  Setting the property `com.apple.mrj.cache.size` to 50M represents a JAR cache size of 50MB. You may set this value larger or smaller as needed. To disable JAR caching, set the property `com.apple.mrj.useJarCaching` to `false`. If a cache directory is specified with the `property com.apple.mrj.cache.directory`, the directory must exist or JAR caching will be disabled. The JAR cache options are sensitive to trailing spaces and MRJ provides no error checking on property values.  The default values are in __bold__:  com.apple.mrj.cache.size __100M__  com.apple.mrj.useJarCaching __true__/false Enable/disable caching.   com.apple.mrj.cache.verbose true/__false__ Log caching information to the Java console. com.apple.mrj.cache.verbose.miss true/__false__ Log cache misses to the Java console   com.apple.mrj.cache.verbose.hit true/__false__ Log cache hits to the Java console  com.apple.mrj.cache.logfile <path to log file> Log information to file instead of console.  com.apple.mrj.cache.directory <path to existing folder> Specify the location of the JAR cache folder.      |  |  | | --- | --- | | __Listing 1__. An example mrj.properties file that sets the JAR caching to 200MB, the cache folder on the desk top of a volume named "HD" in a folder called "JCache", and logs cache information to a file name "JLogFile" at the root of a volume named "HD".   |  | | --- | | ``` com.apple.mrj.cache.size=200M com.apple.mrj.cache.directory=/HD/Desktop Folder/JCache com.apple.mrj.cache.verbose=true com.apple.mrj.cache.logfile=/HD/JLogFile ``` | |  [Oct 06 2000] |

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
