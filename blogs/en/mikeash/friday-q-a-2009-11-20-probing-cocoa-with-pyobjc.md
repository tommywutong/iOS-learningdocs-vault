---
title: 'Friday Q&A 2009-11-20: Probing Cocoa With PyObjC'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-11-20-probing-cocoa-with-pyobjc.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f45ab4f989079b7b'
translated: false
---

> 原文：[Friday Q&A 2009-11-20: Probing Cocoa With PyObjC](https://www.mikeash.com/pyblog/friday-qa-2009-11-20-probing-cocoa-with-pyobjc.html)　·　mikeash.com Friday Q&A

Posted at 2009-11-21 02:44 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-11-27: Using Accessors in Init and Dealloc](https://www.mikeash.com/pyblog/friday-qa-2009-11-27-using-accessors-in-init-and-dealloc.html)  
Previous article: [Deconstructing Apple's Copyright and Trademark Guidelines](https://www.mikeash.com/pyblog/deconstructing-apples-copyright-and-trademark-guidelines.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [pyobjc](https://www.mikeash.com/pyblog/?tag=pyobjc) [python](https://www.mikeash.com/pyblog/?tag=python)

Friday Q&A 2009-11-20: Probing Cocoa With PyObjC

by [Mike Ash](https://www.mikeash.com/)

I assume everybody reading this knows what Cocoa is, but may not know what the other two parts are:

- **Python:** A clean, fairly modern "scripting" language. Its object model is much like Smalltalk, in that pretty much everything is an object and there are no primitives, but the syntax is more C-like. Significantly, for the purposes of this article, Python provides a nice, friendly command-line interpreter that you can access by typing `python` into your nearest terminal window.
- **PyObjC:** A language bridge between Python and Objective-C. It will translate or proxy objects from one language into objects in the other language, bi-directionally. Allows you to write Cocoa apps partly or entirely in Python, and also lets you poke at Cocoa from Python's interpreter.

**Basics**  
 PyObjC gets implicitly loaded whenever you load one of the Python modules that need it. Most system frameworks have a corresponding Python module. To load such a module, you can enter `import FrameworkName` at the Python command line. However, since Python supports namespaces, this requires putting `FrameworkName.` before any symbol inside that framework that you want to use. This is usually a good thing for "real" code, but if we're just going to experiment with things from the command line, it's better to avoid that. You can tell Python to import everything in the framework into the top-level namespace instead with `from FrameworkName import *`. Then you can use symbols from the framework directly. Example:

```
    >>> from Foundation import *
    >>> NSFileManager
    <objective-c class NSFileManager at 0x7fff7101eb18>
```

And then you can send messages to these classes using Python's C++/Java-ish syntax:

```
    >>> NSFileManager.defaultManager()
    <NSFileManager: 0x100257900>
```

PyObjC automatically translates common object types across, such as strings, so you can just write normal string literals in Python and have it work. To pass a parameter, you have to deal with the syntax mismatch, because Python has a single method name, whereas Objective-C interleaves method name components with parameters. To translate to Python, glue all of the method's components together, then replace the colons with underscores. Examples:

```
    >>> NSFileManager.defaultManager().displayNameAtPath_('/')
    u'Fear'
    >>> NSFileManager.defaultManager().fileAttributesAtPath_traverseLink_('/', True) 
    {
        NSFileCreationDate = "2006-08-18 08:33:34 -0400";
        NSFileExtensionHidden = 0;
        NSFileGroupOwnerAccountID = 80;
        NSFileGroupOwnerAccountName = admin;
        NSFileModificationDate = "2009-11-16 23:58:45 -0500";
        NSFileOwnerAccountID = 0;
        NSFileOwnerAccountName = root;
        NSFilePosixPermissions = 1021;
        NSFileReferenceCount = 38;
        NSFileSize = 1360;
        NSFileSystemFileNumber = 2;
        NSFileSystemNumber = 234881026;
        NSFileType = NSFileTypeDirectory;
    }
```

Note that, while basic Python objects like strings and dictionaries will get converted to their Cocoa equivalents when passing through the bridge, they are not instances of their Cocoa equivalents if they stay in Python-land. In other words, if you have a Python string, you can't just go and use NSString methods with it:

```
    >>> 'abc'.length()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'str' object has no attribute 'length'
```

Instead, you can do a simple pass into Cocoa first to get it to work:

```
    >>> NSString.stringWithString_('abc').length()
    3
```

(Of course in this specific example, you could just use the built in Python way of getting the length, with `len('abc').)`

**Errors**  
 Cocoa methods that return `NSError` instances by reference get special treatment by PyObjC. Python cleanly supports returning multiple values from a method, but doesn't cleanly support return-by-reference, so PyObjC translates the `NSError` return by reference into a multiple return. You just assign two variables to the result of the method, and then pass `None` (Python's version of `nil` for the `NSError` argument. Example:

```
    >>> string, error = NSString.stringWithContentsOfFile_encoding_error_('/', NSUTF8StringEncoding, None)
    >>> string
    >>> error.description().encode('utf8')
    'Error Domain=NSCocoaErrorDomain Code=257 UserInfo=0x11994b610 "The file \xe2\x80\x9cFear\xe2\x80\x9d couldn\xe2\x80\x99t be opened because you don\xe2\x80\x99t have permission to view it." Underlying Error=(Error Domain=NSPOSIXErrorDomain Code=13 "The operation couldn\xe2\x80\x99t be completed. Permission denied")'
```

I have to engage in a bit of trickery to print the error object at the end because of the non-ASCII characters it contains. If I just try to print `error` directly, Python will complain that its description can't be converted to ASCII, so I have to manually get the description and convert it to UTF-8 for printing.

**Arrays and Dictionaries**  
 A Python array can be written like this:

```
    ['a', 'b', 'c']
```

And PyObjC will convert it to an NSArray as it crosses the bridge. This makes it trivial to pass arrays to Cocoa methods which take them:

```
    >>> data, error = NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(['hello', 'world'], NSPropertyListXMLFormat_v1_0, None)
    >>> NSString.alloc().initWithData_encoding_(data, NSUTF8StringEncoding)
    u'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<array>\n\t<string>hello</string>\n\t<string>world</string>\n</array>\n</plist>\n'
```

(Note that PyObjC is smart enough to understand Cocoa memory management conventions and so will automatically clean up the string that I allocated on the last line, rather than requiring me to explicitly release it.)

Dictionaries are written like this:

```
    { 'key' : 'value', 'key2' : 'value2' }
```

And likewise they get translated across the bridge:

```
    >>> data, error = NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_({ 'key' : 'value', 'key2' : 'value2' }, NSPropertyListXMLFormat_v1_0, None)
    >>> NSString.alloc().initWithData_encoding_(data, NSUTF8StringEncoding)         u'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>key</key>\n\t<string>value</string>\n\t<key>key2</key>\n\t<string>value2</string>\n</dict>\n</plist>\n'
```

**Custom Frameworks**  
 A fun thing with PyObjC is that it's not limited to system frameworks. You can load your own frameworks! It's trivial to do, because you can do it exactly as you would do it in a Cocoa program: just use NSBundle to load the framework and start getting and manipulating classes. Here's an example of doing this with a system framework, but it works just the same for your own:

```
    >>> bundle = NSBundle.bundleWithPath_('/System/Library/Frameworks/WebKit.framework')
    >>> bundle.principalClass()
    <objective-c class WebPlaceholderModalWindow at 0x7fff7095cc40>
    >>> bundle.classNamed_('WebView').alloc().init()
    <WebView: 0x100212490>
```

Once you have framework classes and objects, you can manipulate them just as you would Cocoa classes and objects.

Note that on 10.6 and 64-bit capable machines, Python loads as 64-bit by default, so if your framework is 32-bit only then this won't work. You can load Python in 32-bit mode by starting it with the following command (assuming you use the default bash shell):

```
    VERSIONER_PYTHON_PREFER_32_BIT=yes python
```

**AppKit**  
 So far we've just been working with Foundation-like objects, but PyObjC supports AppKit as well:

```
    >>> from AppKit import *
```

And it's trivial to get a little window up on the screen from there:

```
    >>> NSApplicationLoad()
    True
    >>> window = NSWindow.alloc().init()
    >>> window.makeKeyAndOrderFront_(None)
```

Where this really comes in handy is with things like NSImage. This lets you easily manipulate images using classes you already know. For example:

```
    >>> image = NSImage.alloc().initWithContentsOfFile_('brakes.jpg')
    >>> image
    <NSImage 0x1198b6f70 Size={483, 450} Reps=(
        "NSBitmapImageRep 0x1198bcfa0 Size={483, 450} ColorSpace=(not yet loaded) BPS=8 BPP=(not yet loaded) Pixels=483x450 Alpha=NO Planar=NO Format=(not yet loaded) CurrentBacking=nil (faulting) CGImageSource=0x1198bc220"
    )>
    >>> scaledImage = NSImage.alloc().initWithSize_((32, 32))
    >>> scaledImage.lockFocus()
    >>> image.drawInRect_fromRect_operation_fraction_(((0, 0), (32, 32)), NSZeroRect, NSCompositeCopy, 1.0)
    >>> scaledImage.unlockFocus()
    >>> scaledImage.TIFFRepresentation().writeToFile_atomically_('/tmp/brakes_thumb.tiff', True)
    True
```

**Conclusion**  
 This article barely scratches the surface of what's possible with PyObjC, but it should get you started. You can manipulate QuickTime movies, put up windows, test frameworks, and even write full-blown applications. For further reading, check out [the PyObjC documentation](http://pyobjc.sourceforge.net/documentation/) and [the Python documentation](http://www.python.org/doc/). This is a valuable tool to have in your kit, whether for testing, rapid prototyping, or just trying things out.

That's it for this week. Come back in seven days for another exciting edition. Until then, [send in your ideas for topics to cover](mailto:mike@mikeash.com). Friday Q&A is driven by your ideas, so send them in!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-11-20-probing-cocoa-with-pyobjc.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
