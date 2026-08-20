---
title: AppleScript Overview
apple_id: 10000156i
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/work_with_as.html
archived_at: '2026-07-15T05:19:36.515274Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Overview](Introduction%20to%20AppleScript%20Overview.md)


[Next](Scriptable%20Applications.md)[Previous](Open%20Scripting%20Architecture.md)

# Scripting with AppleScript

The following is a brief introduction to AppleScript scripts, tools for working with them, and information on using AppleScript scripts together with other scripting systems. For related documents, see the learning paths in _Getting Started with AppleScript_.

An AppleScript script consists of one or more statements, written in a syntax described in [AppleScript Language Guide](https://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptLangGuide/index.html) (and in a number of third-party books). AppleScript defines some scripting terms, while scriptable applications and parts of the Mac OS specify additional terms for scriptable features they support. Scripting terminologies generally use common English words, resulting in scripts that are easier to read. For example, the following is a valid script statement:

```
display dialog "Welcome to AppleScript."
```

Users can compile and execute scripts with the [Script Editor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknryfuytcnjsgm3dk) application and can save them in various executable formats, including as stand-alone applications.

Listing 1 shows an AppleScript script that simply returns the number of files in the `Applications` folder on the current system disk (denoted by `startup disk`, a term understood by the Finder). If the folder cannot be found, the script returns a count of zero. This script counts just files in the specified folder, not folders or the files they might contain.

__Listing 1__  A script that counts the files in the Applications folder

```
tell application "Finder"
    if folder "Applications" of startup disk exists then
        return count files in folder "Applications" of startup disk
    else
        return 0
    end if
end tell
```

When a script is compiled and executed, some statements perform basic operations, such as assigning a variable or returning a value. A statement that targets a scriptable application results in an Apple event being sent to that application. The application can return information to the script in a reply Apple event.

The script in Listing 1 causes an Apple event to be sent to the Finder, which locates the Applications folder on the startup disk, counts the files in it, and returns that value. The `if...then...else` structure is one of several standard programming language features that AppleScript supports.

The Script Editor application is located in `/Applications/AppleScript`. It provides the ability to edit, compile, and execute scripts, display application scripting terminologies, and save scripts in a variety of formats, such as compiled scripts, applications, bundled applications, and plain text.

Script Editor can display the result of executing an AppleScript script and can display a log of the Apple events that are sent during execution of a script. In the Script Editor Preferences, you can also choose to keep a history of recent results or event logs.

Script Editor has text formatting preferences for various types of script text, such as language keywords, comments, and so on. You can also turn on or off the Script Assistant, a code completion tool that can suggest and fill in scripting terms as you type. In addition, Script Editor provides a contextual menu to insert many types of boilerplate script statements, such as conditionals, comments, and error handlers.

You can choose File > Open Dictionary in Script Editor to examine the scripting dictionary of a scriptable application or scripting addition on your computer. Or you can drag an application icon to the Script Editor icon to display its dictionary (if it has one). You can also open scripting dictionaries in Xcode.

To display a list that includes just the scriptable applications and scripting additions provided by the Mac OS, choose Window > Library. Double-click an item in the list to display its dictionary. Figure 1 shows the dictionary for the Finder application in OS X version 10.5. The dictionary is labeled as “Finder.sdef”. The sdef format, along with other terminology formats, is described in [Specifying Scripting Terminology](Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfuytcnjwge3dk).

__Figure 1__  The Finder dictionary in Script Editor (in OS X v10.5)

![The Finder dictionary in Script Editor (in OS X v10.5)](attachments/art/finder_dictionary_2x.png)

Script Editor supports only simple debugging strategies, such as logging event output and inserting `speak` or `display dialog` statements within scripts. However, there are a number of third-party products for working with AppleScript, some of them quite powerful. For example, there are script editors and tools for monitoring and debugging scripts, Apple events, and scriptable applications. Some of these third-party products are listed at the [AppleScript Resources](http://www.macosxautomation.com/applescript/resources.html) web page.

For information on debugging scriptable applications and Apple events, see the documents _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_ and _[Apple Events Programming Guide](../Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_.

AppleScript provides little direct support for interacting with the user in scripts. However, the Standard Additions scripting addition provides terminology for obtaining various choices from the user. For example, it includes commands for letting the user choose an application, a color, a file, a filename, and so on. It also provides the `display dialog` command, which allows you to display a dialog with various options for text labels, buttons, and text input. Scripting Additions are described in [Extending AppleScript with Coercions, Scripting Additions, and Faceless Background Applications](Open%20Scripting%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzrfuytcnruga3dq).

Many applications from Apple are scriptable and you can also script some parts of the Mac OS. For example, the Finder, iTunes, QuickTime Player, and Mail are highly scriptable. For a complete list, see the [Scriptable Applications](http://www.macosxautomation.com/applescript/resources.html) web page at the [AppleScript](http://www.macosxautomation.com/applescript/index.html) website. For more information on scriptability provided by Apple, see [AppleScript Utilities and Applications](AppleScript%20Utilities%20and%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzqfvbecqsfijdugrq).

Many third-party applications are scriptable—their advertising and packaging usually mention if they are scriptable. The documentation for a scriptable application typically lists the AppleScript terminology that the application understands. You can also determine if an application is scriptable by attempting to examine its dictionary with the Script Editor application, as described in [Displaying Scripting Dictionaries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknryfuytcnjtgaydm).

XML-RPC and SOAP are remote procedure call protocols that support exchanging commands and information over the Internet. Starting with OS X version 10.1, AppleScript and the Apple Event Manager provide XML-RPC and SOAP support such that:

- Scripters can make XML-RPC calls and SOAP requests from scripts.
- Developers can make XML-RPC calls and SOAP requests from applications or other code by sending Apple events.

For documentation on using AppleScript with web services, see _[XML-RPC and SOAP Programming Guide](../XML-RPC%20and%20SOAP%20Programming%20Guide/Introduction%20to%20XML-RPC%20and%20SOAP%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrw)_ (some examples may be out of date). For additional sources and examples, see [Web Services](http://www.macosxautomation.com/applescript/resources.html). For information on developing web content and applications for the web in OS X, see _[Getting Started with Internet and Web](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_WebInternet/_index.html#//apple_ref/doc/uid/TP30001123)_.

OS X supports a UNIX-like shell environment that is familiar to many developers. That support includes the Terminal application, located in `/Applications/Utilities`, which you can use to open shell windows and execute shell scripts. AppleScript provides two convenient mechanisms to interact with a shell environment: you can execute shell commands from within AppleScript scripts and you can execute AppleScript scripts as shell commands.

AppleScript provides the `do shell script` command to support executing a shell command as part of an AppleScript script. For example, the following script statement uses a `do shell script` command to change the directory to the current user’s home directory and obtain a list of the files found there. The list information is stored in the AppleScript variable `fileInfo`:

```
set fileInfo to do shell script "cd ~; ls"
```

The `do shell script` command is primarily of use to scripters. Although applications can execute AppleScript scripts that use the `do shell script` command, they have more efficient options for executing shell commands, as described in [Support for Carbon Applications](Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfuytcnjqhe2dc) and [Support for Cocoa Applications](Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfuytcnjrgu3do). For more information on the `do shell script` command, see Technical Note TN2065, [do shell script in AppleScript](https://developer.apple.com/technotes/tn2002/tn2065.html).

To execute AppleScript scripts as shell commands in a Terminal window or shell script file, you can use the `osacompile` command and the `osascript` command (located in `/usr/bin`). The former compiles an AppleScript script, while the latter executes a plain text or a compiled AppleScript script. Man pages provide documentation for these commands. For example, type `man osascript` in a Terminal window to get information on the `osascript` command.

Starting in OS X version 10.5, there is a command-line tool to display compiled scripts as text, `osadecompile`. Again, see the man page for details.

Also starting in Mac OX X v10.5, AppleScript allows use of the # symbol as a comment-to-end-of-line token (the traditional double hyphen (--) is also still supported). This means that you can make a plain AppleScript script into a Unix executable by beginning it with the following line and giving it execute permission.

```
#!/usr/bin/osascript
```


The Terminal application is itself scriptable. For example, you can use the `do script` command to execute text as a shell script or command. To see the operations Terminal supports, you can examine its scripting dictionary with Script Editor.

For those who have experience with various scripting languages and environments, the previous sections have probably already provided an urge to start experimenting. And you do have a lot of options for combining features from the scripting tools, languages, and environments that are most appropriate for specific kinds of tasks. For example, the following one-line shell script statement combines Perl, AppleScript, and various tools to find duplicate entries in the Address Book application.

```
osascript -e 'tell app "Address Book" to get the name of every person' | perl -pe 's/, /\n/g' | sort | uniq -d
```

This statement uses `osascript` to execute an inline AppleScript script (`'tell app "Address Book" to get the name of every person'`) that returns the names of every address entry from the Address Book application. It pipes the output of this script through the `perl` tool, and with a series of other commands and pipes, obtains and formats a (possibly empty) list of duplicate names.

For additional information about working with AppleScript from languages such as Ruby and Python, see [Scripting Bridge](Scripting%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinrxfvjvomi).

[Next](Scriptable%20Applications.md)[Previous](Open%20Scripting%20Architecture.md)

