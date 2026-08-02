---
title: Ruby and Python Programming Topics for Mac
apple_id: TP40004936
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: ScriptingBridge
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/RubyPythonCocoa/Articles/RubyPythonMacOSX.html
archived_at: '2026-07-15T07:18:40.287448Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ruby and Python Programming Topics for Mac](Introduction%20to%20Ruby%20and%20Python%20Programming%20Topics%20for%20OS%20X.md)


[Next](Building%20a%20RubyCocoa%20Application-%20A%20Tutorial.md)[Previous](Introduction%20to%20Ruby%20and%20Python%20Programming%20Topics%20for%20OS%20X.md)

# Ruby and Python on OS X

Ruby and Python, two immensely popular object-oriented scripting languages, have been installed as part of OS X for many years now. But their relevance to software development, and especially application development, assumes even greater importance in OS X v10.5. The following sections summarize the capabilities and components of Ruby and Python and describe the bridges being developed and enhanced for OS X to support Cocoa programming and AppleScript-command processing from those scripting languages.

Ruby and Python are interpreted object-oriented scripting languages. As interpreted languages, you can change and run code immediately, without having to wait for the code to compile. Python and Ruby also have all the features one would expect to find in dynamic object-oriented programming languages, such as inheritance, encapsulation, introspection, and subclassing. The syntax of both languages is simple, compact, and consistent, and supports both regular expressions and sophisticated string manipulations. Memory management is built into both languages; garbage collectors automatically free memory occupied by unneeded objects. With both Python and Ruby you can call operating system routines directly. They offer ways to extend their native capabilities, including C-language interfaces.

Although their similarities are striking, these scripting languages do have some differences. While Python code can contain both objects and built-in types, in Ruby everything is an object. There are no primitive or built-in types, such as integers. Thus anything in Ruby code can accept messages. And you don’t have to declare variables to be of specific object types. To distinguish variables as global, local, instance, and class, Ruby uses naming conventions. Ruby also has mix-in by modules and blocks, language features absent in Python.

Beyond the similarities of languages and interpreters, Python and Ruby share other things in common. Both have extensive standard libraries of classes and modules. Both scripting languages can be used in a wide variety of software projects, including system programming (command-line utilities and daemons), user-interface design, Internet and networking tasks, database programming, component integration, and, of course, rapid prototyping. And both are the products of open-source projects supported by large and enthusiastic developer communities.

Both languages come with a basic set of command-line utilities. In addition to the interactive interpreter, `irb`, Ruby includes `ri` and `rdoc` (for displaying and generating documentation, respectively), `erb` (for interpreting files with embedded Ruby code), and `testrb` (for running test suites on Ruby code). In addition to the language interpreter, `python`, Python includes `pydoc` for viewing documentation and `pythonw` for running Python scripts that display a graphical user interface. All of these utilities are located in `/usr/bin`.

On OS X Ruby includes more than the language interpreter and documentation and testing utilities. A standard installation offers the following Ruby-related services, frameworks, and protocols:

- RubyGems—A package manager for Ruby
- rake—A `make`-like utility for Ruby scripts
- Rails (or Ruby on Rails)—A framework for creating database-backed web applications with designs conforming to the Model-View-Controller pattern

  For more information on Ruby on Rails, go to [http://developer.apple.com/tools/rubyonrails.html](https://developer.apple.com/tools/rubyonrails.html).
- Mongrel—A fast HTTP library and server used for hosting Ruby web applications
- Capistrano—A framework and utility for executing commands in parallel on multiple remote machines, via SSH, primarily to expedite the deployment of web applications
- Ferret—A search engine
- OpenID—A service that provides OpenID identification to Ruby programs
- sqlite3-ruby—A module that enables Ruby scripts to interact with a SQLite3 database
- libxml-ruby—A module for reading and writing XML documents using Ruby
- dnssd—Ruby interface for DNS Service Discovery (that is, Bonjour)
- net-ssh and net-sftp—Pure Ruby implementations of the SSH and SFTP client protocols

The Python modules included in the standard package for OS X are the following:

- altgraph — Python graph (network) package
- bdist_mpkg — Builds OS X installer packages from distutils
- macholib — Mach-O header analysis and editing
- modulegraph — Python module dependency analysis tool
- numpy (or NumPy) — Array processing for numbers, strings, records, and objects
- py2app — Creates standalone Mac apps with Python
- setuptools — Downloads, builds, installs, upgrades, and uninstalls Python packages
- xattr — A Python wrapper for Darwin’s extended filesystem attributes

Except for `numpy` and `xattr`, all of these modules are used by PyObjC.

You can find out more about Python from the following websites:

- Main Python website: [http://www.python.org/](http://docs.python.org/)
- Documentation: [http://docs.python.org/](http://docs.python.org/)
- Other developer resources: [http://www.python.org/dev/](http://www.python.org/dev/)

On-line resources for Ruby include the following websites:

- Documentation, downloads, and other resources: [http://www.ruby-lang.org/](http://www.ruby-lang.org/)
- Libraries: [http://rubyforge.org/](http://rubyforge.org/)
- _why’s (poignant) guide to Ruby_ ([http://poignantguide.net/ruby/](http://poignantguide.net/ruby/)), a whimsical, cartoon-illustrated introduction to Ruby

Both Ruby and Python include bridges to the Objective-C runtime. Although these bridges are open-source projects, some changes have been made to the implementation and tool support on OS X v10.5 and later systems.

Because Ruby and Objective C share a common ancestor in Smalltalk, creating a bridge between them was relatively straightforward. RubyCocoa is a bridge that makes it possible for Ruby scripts to access Objective-C objects defined in frameworks and local project code. Consequently, one can do Cocoa programming in a Ruby script. RubyCocoa works by creating—automatically and upon demand—Ruby proxy objects that are bridged to Objective-C classes. It also forwards Ruby messages to the instances of these Objective-C classes. You can have a Cocoa application project that mixes Ruby and Objective-C source files. RubyCocoa supports all important features of Cocoa, such as key-value coding, key-value observing, Core Data, the document architecture, notifications, and undo management.

The following line of code creates a Ruby proxy class that wraps the Cocoa class NSButton:

```
OSX::NSButton
```

A message sent to an instance of this class is forwarded to the Objective-C instance within the proxy object. (If the object doesn’t respond to the message, then RubyCocoa raises a runtime error.) As illustration, consider the following lines of Objective-C code:

```
// the NSRect structure (rect) is specified earlier
NSButton *button = [[NSButton alloc] initWithFrame:rect];
[button setTarget:self];
[button setAction:@selector(doGoodThings:)];
[button setEnabled:YES];
[view addSubview:button];
[button release];
```

In RubyCocoa, the equivalent to these lines would be the following:

```
button = NSButton.alloc.initWithFrame_(rect)
button.setTarget_(self)
button.setAction_(:doGoodThings)
button.setEnabled_(true)
view.addSubview_(button)
```

As you can see, RubyCocoa uses keypath-style dot notation is used to indicate (potentially nested) message invocations, starting with the object or class initiating the invocations. Note that the `release` is omitted in the RubyCocoa code snippet because the garbage collector takes care of object disposal.

The snippet of RubyCocoa code above uses the default messaging syntax, where underscores replace the colons of the Objective-C keywords . But RubyCocoa supports a variant of the default syntax that omits the final underscore. Thus, the two message syntaxes are:

```
# Default calling syntax
NSURL.alloc.initWithScheme_host_path_('http', 'localhost', 'sample')
# Same, but no underscore for final keyword
NSURL.alloc.initWithScheme_host_path('http', 'localhost', 'sample')
```

In a standard OS X installation, the second syntax is disabled. However, you can enable it by setting the `OSX.relaxed_syntax` flag to `true`.

RubyCocoa takes care of object type conversions for you. When you pass parameters to a Ruby proxy object, RubyCocoa automatically converts the more basic Ruby types to proxies representing their Objective-C counterparts (for example, Ruby strings and `NSString` objects). It also converts objects returned from the Objective-C side to Ruby objects that act as proxies to those Objective-C objects. On the Ruby side, these proxy objects have more or less the same interfaces as their Ruby equivalents.

RubyCocoa adds several Xcode templates for building RubyCocoa applications of various types. The templates make it unnecessary for developers to create applications by writing RubyCocoa code using a shell editor (for example, Emacs or `vi`) and then manually constructing the various pieces of the application bundle. The Xcode templates make sure the application project is properly set up for RubyCocoa and that the application executable and its bundle are properly built. And they let you access the conveniences of a first-class integrated development environment. You can also design your user interfaces using the Interface Builder application. Currently there are four RubyCocoa application templates:

- Cocoa-Ruby applications (single window)
- Cocoa-Ruby document-based applications
- Cocoa-Ruby Core Data applications
- Cocoa-Ruby Core Data document-based applications

In addition to the project templates, RubyCocoa adds support for test units. In Xcode you can create a test-unit file by choosing New File from the File menu and then selecting “Ruby test case class” under the Ruby category in the New File Assistant. You can also set up a test-unit target by choosing “New Target” from the Project menu and then selecting “Unit Test Target” option in the New Target Assistant.

Apple’s implementation of RubyCocoa adds some features and makes some performance improvements, including the following:

- Apple has added support for generating metadata about the C-language parts of a framework’s Objective-C API.

  RubyCocoa can extract most of the information it needs about object-oriented symbols (such as classes and methods) from frameworks at runtime. Unfortunately, there is no purely dynamic way to introspect framework data that is C-based, such as constants, enumerations, and functions. To resolve this problem (in a way that avoids generating static code at build time), RubyCocoa reads a per-framework metadata file, which it loads at runtime. A command-line tool generates most of this metadata XML automatically but the framework developer may have to specify certain items manually, such as pass-by-reference parameters.. See [Generating Framework Metadata](Generating%20Framework%20Metadata.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrwfvjvomi) for more information on framework metadata and instructions on how to create the metadata description.
- Apple has made many performance improvements, involving the following:

  - RubyCocoa uses the `libffi` library for function calling and message dispatch.

    Instead of a message-dispatch implementation based on `objc_msgSend` or `NSInvocation`, RubyCocoa uses the `libffi` library from the GCC project. `libffi` makes it possible to call an arbitrary C function in a processor-agnostic way. It provides more scalability and better performance than the other alternatives. RubyCocoa also uses `libffi` when overriding or registering an Objective-C method implemented in Ruby, and when converting Ruby closures to C function pointers.
  - RubyCocoa efficiently copies objects as they cross the bridge either way.
  - RubyCocoa efficiently looks up selectors and classes.
- Apple’s RubyCocoa accurately translates the Objective-C class hierarchy when it creates Ruby proxy objects, taking into account those classes that can be toll-free bridged to the Core Foundation counterparts

PyObjC is a bridge that lets you write sophisticated Cocoa applications using the Python scripting language. It enables Python objects to send messages to Objective-C objects and vice versa. With PyObjC you’re not limited to the core Cocoa frameworks, Foundation and Application Kit. You can use any Objective-C framework from Python, and your projects can be a mix of Objective-C, C, and C++ code. PyObjC also supports full introspection of Objective-C classes and direct invocation of Objective-C APIs from the interactive interpreter. Like RubyCocoa, PyObjC incorporates supports the full range of Cocoa features such as key-value coding, key-value observing, Core Data, document-based applications, notifications, and undo management..

PyObjC is useful for more than just Cocoa application (GUI) development. You can also use PyObjC for rapid prototyping of projects, and for writing Foundation-based command-line tools, screen savers, preference panes, and other forms of software.

PyObjC leaves little that is unbridged between Objective-C and Python. Objective-C classes can inherit from Python classes, and Python classes can inherit from Objective-C classes. You can declare categories on Objective-C classes, with the method definition given in Python. Python classes can implement and define Objective-C protocols, and it's possible to establish a binding between a Python object and an Objective-C object in Interface Builder.

In PyObjC, Cocoa classes are treated as normal Python classes, but (for Python programmers) with a somewhat different naming scheme for methods . The PyObjC equivalent of the RubyCocoa button code above is:

```
button = NSButton.alloc().initWithFrame_(rect)
button.setTarget_(self)
button.setAction_('doGoodThings:')
button.setEnabled_(True)
view.addSubView_(button)
```

PyObjC performs a simple translation from Objective-C selector names to Python method names (and vice versa when new methods are defined), replacing all colons by underscores. This is the only messaging syntax supported.

PyObjC automatically converts Python objects passed to the Objective-C runtime to the correct Objective-C type, and also converts Objective-C objects passed back into Python. For example, Python strings are proxied using an NSString subclass when they are passed to Objective-C code; likewise, an NSString object is proxied using a Python unicode-subclass when the object passes into Python. Unlike RubyCocoa, predicates work without further work on your part; in other words, `if button.isEnabled: doSomething()`) works as one would expect.

PyObjC's support for pass-by-reference arguments is similar to that for RubyCocoa, and predates it by many years. You can learn more about the exact semantics in the introductory documentation for PyObjC ([http://pyobjc.sourceforge.net/documentation/pyobjc-core/intro.html](http://pyobjc.sourceforge.net/documentation/pyobjc-core/intro.html)).

A change in the Leopard version of PyObjC is that it uses the same XML metadata description as does RubyCocoa (see [RubyCocoa](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrtfvjvomq) for an overview). Another change is that PyObjC now supports all Core Foundation–based types as well, not only those that can be toll-free bridged to Cocoa classes.

The open-source version of PyObjC includes a number of Xcode templates that make it easy to create and configure Cocoa-Python application projects. By using the templates, you can have the development environment for your project set up for you; it eliminates the need to code using a shell editor or text processor and then manually construct the various parts of the application bundle. You can compose your user interfaces using Interface Builder and then save them to a nib file. And you have access to a sophisticated integrated development environment with features such as multiple build targets and symbol and documentation look-up. Four PyObjC application templates are offered:

- Cocoa-Python applications (single window)
- Cocoa-Python document-based applications
- Cocoa-Python Core Data applications
- Cocoa-Python Core Data document-based applications

The Apple version of PyObjC for OS X version 10.5 includes two additional improvements:

- PyObjC uses the same the same XML metadata scheme as RubyCocoa to define the non-object-oriented parts of a framework..
- PyObjC supports all Core Foundation opaque types and not only those that can be toll-free bridged to Cocoa classes..

The RubyCocoa and Python bridges bring several advantages to Cocoa development, both for experienced Ruby and Python “scripters” and for Objective-C developers. By letting you mix and match Objective-C, Ruby, and Python, the bridges give you the option of choosing the best language tool for whatever programming goal you have. At the same time, they give your code access to Cocoa technologies such as bindings and Core Data. Moreover, your RubyCocoa and PyObjC projects can use the capable project management of Xcode and the rapid interface development offered by Interface Builder.

By bridging the Ruby and Python languages to the Objective-C runtime, PyObjC and RubyCocoa open the door to Cocoa application development for thousands of Python and Ruby scripters. But they also offer benefits to experienced Objective-C developers. If you are such a developer, you can take advantage of both scripting languages’ sophisticated regular-expression features for textual processing. You also have access to the extensive libraries for both Python and Ruby. The interpretive nature of RubyCocoa and PyObjC means you can use them for rapid application prototyping to help you locate design problems early in the development cycle. Using the interpreter, you can inject code into your application on the fly and instantly inspect and manipulate objects in your application.

The bridges’ conjunction of two object-oriented languages—Ruby and Python on one side and Objective-C on the other—enables even more dynamism than any of the languages provides on its own. For example, with PyObjC you can create Cocoa-compatible classes at runtime and even create new methods while your application continues to execute.

A final advantage of RubyCocoa and PyObjC is that they are extensions of languages that run on a variety of systems, including Linux and Windows. In other words, they are cross-platform. You could thus maintain a cross-platform code base in Ruby or Python—your model objects, as it were—and use the bridged version of the language to control the user interface and manage the application.

You have several options for writing Ruby or Python scripts that can communicate with scriptable applications, enabling them to control those applications and exchange data with them. These technologies are bridges to the Open Scripting Architecture (OSA) infrastructure, which uses Apple events for interprocess communication. The native solution is Scripting Bridge, which is a bridge to the Objective-C runtime and thus can be used in RubyCocoa or PyObjC scripts. You also use open-source Ruby and Python bridges to OSA, and thereby merge the power of Ruby or Python with that of AppleScript and Apple event processing.

Many applications installed on OS X are scriptable. Through the Scripting Bridge technology, RubyCocoa and PyObjC scripts and programs can communicate with these applications, controlling them and exchanging data with them. For example, using Scripting Bridge a RubyCocoa script could select and play music tracks in iTunes; or it could search a mailbox (maintained by the Mail application) for messages with a certain phrase and put those messages into a new TextEdit document.

Scriptable applications define a interface through which they can respond to Apple events, which are a part of the Open Scripting Architecture (OSA). Apple events frequently originate in AppleScript scripts and make use of the Apple Event Manager of OSA as the mechanism of delivery. Scripting Bridge is a framework that implements an Objective-C bridge to OSA-compliant applications—that is to say, applications having a scripting interface that follows the guidelines described in [Technical Note T2106](https://developer.apple.com/technotes/tn2002/tn2106.html) and _[Cocoa Scripting Guide](../Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_. It enables programs written in Objective-C to use the OSA infrastructure to control and communicate with OSA-compliant applications. With Scripting Bridge you can perform the same tasks in Objective-C that you can in AppleScript scripts.

Scripting Bridge is dynamic. At runtime it retrieves the scripting definition of a given application and generates Objective-C class implementations of the classes it finds in the scripting interface, including objects and methods representing properties, elements, commands, and so on. These objects become part of the Objective-C namespace that PyObjC and RubyCocoa scripts are bridged to, and through them these scripting languages are bridged to OSA-compliant applications. As a result, you can control and obtain data from those applications from RubyCocoa and PyObjC code. And you also have at your disposal all the rich features and capabilities of the native languages, such as regular expressions, string manipulations, and easy access to the native libraries and modules.

To find out how to use Scripting Bridge in RubyCocoa and PyObjC scripts, see [Using Scripting Bridge in PyObjC and RubyCocoa Code](Using%20Scripting%20Bridge%20in%20PyObjC%20and%20RubyCocoa%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrufvjvomi).

RubyOSA is a open-source bridge that connects Ruby to the Apple Event Manager infrastructure, thereby enabling you to do in Ruby what you can do in AppleScript. It works by retrieving the scriptable definition of a given application (in its `sdef` file) and using that to populate a new namespace with classes, methods, constants, enumerations, and all other symbols described by the definition.

Most Mac apps are scriptable, and they define their scriptable interface in the `sdef` XML format. RubyOSA parses this file and creates Ruby proxy objects with it on the fly. RubyOSA does its work transparently for you to build, send, and receive Apple events.

To give you an example of how simple and even elegant RubyOSA can be, consider the following code snippet, which gets the name of the current iTunes track:

```
require 'rbosa'
puts OSA.app('iTunes').current_track_name
```

RubyOSA is an improved alternative to RubyAEOSA. The latter bridge is implemented as a set of Ruby bindings to the Apple event C API, while RubyOSA is a higher level framework that completely hides the Apple event infrastructure. It is simpler and more efficient than RubyAEOSA.

You can download RubyOSA from [http://rubyosa.rubyforge.org/](http://rubyosa.rubyforge.org/) or, if you already have RubyGems installed, download and install it from the command line. To learn how, and for a practical look at RubyOSA, see [Using Scripting Bridge in PyObjC and RubyCocoa Code](Using%20Scripting%20Bridge%20in%20PyObjC%20and%20RubyCocoa%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrufvjvomi).

py-appscript is an Python-OSA bridge that lets you control scriptable applications from Python scripts. It uses a high-level RPC mechanism for sending commands to applications via Apple events and converts data between common Python and Apple event types. py-appscript features an object-oriented style syntax and a simple embedded query language for identifying objects in an applicaitons object model.

You can download py-appscript from [http://sourceforge.net/projects/appscript](http://sourceforge.net/projects/appscript). The package includes installation instructions, examples, and documentation.

Because Ruby in its latest stable version (the 1.8 branch) is not thread-safe, you cannot call the Ruby runtime in a thread other than the main one. When Ruby is bridged to Objective-C this creates problems because Objective-C isn’t able to call back to Ruby in a secondary thread. (If it did, an application would crash.) The version of RubyCocoa on Leopard consequently routes calls from Objective-C to Ruby so that all are on the main thread.

Ruby 1.8 also implements its threading model using the `setjmp` and `longjmp` primitives; this can sometimes cause unexpected behavior when a Ruby thread calls a Cocoa object, especially autorelease pools. Consequently, both the Ruby interpreter and the RubyCocoa bridge have been modified to properly handle these situations by saving and restoring the appropriate context variables during Ruby thread switching.

Fortunately, the next stable release of Ruby (the 2.0 branch) will be thread-safe and will use native threads. Unfortunately, this is not the version installed on Leopard.

[Next](Building%20a%20RubyCocoa%20Application-%20A%20Tutorial.md)[Previous](Introduction%20to%20Ruby%20and%20Python%20Programming%20Topics%20for%20OS%20X.md)

