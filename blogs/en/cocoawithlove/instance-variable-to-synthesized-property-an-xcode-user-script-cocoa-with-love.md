---
title: 'Instance variable to synthesized property (an Xcode user script) | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/12/instance-variable-to-synthesized.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:3801a389bf6a431e'
translated: false
---

> 原文：[Instance variable to synthesized property (an Xcode user script) | Cocoa with Love](https://www.cocoawithlove.com/2008/12/instance-variable-to-synthesized.html)　·　Cocoa with Love (Matt Gallagher)

Xcode user scripts take the repetition out of many aspects of programming. To show you how this can work, here's a script I wrote to turn an instance variable into a property (complete with declaration and synthesis) just by selecting the variable and invoking the script.

> If you just want the solution, download the script here: [PropertyFromInstanceVariable.zip](https://www.cocoawithlove.com/assets/objc-era/PropertyFromInstanceVariable.zip).  
>   
> **Update 2008-09-29:** the script now contains additions from Yung-Luen Lan & [Mike Schrag](http://github.com/mschrag/xcode_property_from_ivar) (multiple line support) and [Pierre Bernard](http://www.bernard-web.com/pierre/blog/) (underbar storage name, behavior, dealloc).

## The repetition that I want to eliminate

For a class with a header file that looks like this:

```objc
@interface MyClass : NSObject
{
    NSString *someString;
}

@end
```

turning `someString` into an Objective-C 2.0 property involves two steps. First, add the property declaration to the header:

```objc
@interface MyClass : NSObject
{
    NSString *someString;
}

@property (nonatomic, retain) NSString *someString;

@end
```

and second, add the

```objc
@synthesize someString;
```

line to the implementation.

This isn't very much work but it's still menial and boring stuff. Also, even though it's simple, it is one of the most commonly performed tasks in Objective-C 2.0 programming, since every class will likely have multiple properties that will need to be created and configured in a similar fashion.

Instead of creating these two lines of code in the two different files, I would prefer to select the text "`NSString *someString;`" (by triple clicking on that line) and telling Xcode to instantly make it into a property with no further effort on my part.

## Xcode user scripts

[Xcode Text Macros](http://developer.apple.com/documentation/developertools/Conceptual/XcodeWorkspace/600-The_Text_Editor/chapter_7_section_8.html) are good for inserting boilerplate text at the insertion point but for this problem, we'll need something more programmable: Xcode User Scripts.

You can create and edit Xcode's user scripts by selecting the "Edit User Scripts..." item from the bottom of the Scripts menu.

The main method of operation for these scripts is that Xcode replaces various macros (identifiers) in the scripts before the script is invoked (macros like `%%%{PBXAllText}%%%` and `%%%{PBXSelectionStart}%%%`) and on completion, the "standard out" from the script can be applied to the document (to replace the current selection or document or insert text at the current insertion point).

I'm not going to talk too much about the basics of Xcode's user scripts here. You can read about them in Apple's documentation [Xcode Workspace Guide: User Scripts](http://developer.apple.com/documentation/developertools/Conceptual/XcodeWorkspace/950-User_Scrips/chapter_10_section_1.html) if you need to know more.

Instead I'm going to highlight what I consider to be their biggest limitation: they aren't really intended for making changes to multiple documents. The macros that Xcode user scripts can include allow easy access to the current document and current selection but for a script to access data from other documents is difficult.

However, this is exactly what I want to do: change both the header file and the implementation file for a class in order to add the two additions to make the variable into a property.

## An Applescript inside a Perl script

To get around the limitations of the Xcode user scripts setup, I'm going to use the current file name (available to user scripts as `%%%{PBXFilePath}%%%`) to look for the ".m" or ".mm" file with the same name in the same directory.

To complicate things, I can't just open the file on disk. Since Xcode is necessarily open when the script is invoked and the class is currently being edited, I have to assume that there may be unsaved changes to the file. For this reason, I use an Applescript to ask Xcode to select the file and give me its current text (which will include any unsaved changes).

In my Perl user script, getting the path to the implementation file and using Applescript to get the text of the implementation file looks like this:

```objc
my $implementationFilePath = "%%%{PBXFilePath}%%%";

# Replace the current file's extension with an "m"
$implementationFilePath =~ s/\.[hm]*$/.m/;
if (!(-e $implementationFilePath))
{
    # If no implementation file is found, try replacing with "mm"
    $implementationFilePath =~ s/.m$/.mm/;
}

# If still doesn't exist, don't continue
if (!(-e $implementationFilePath))
{
    exit 1;
}

# Applescript to read 1st argument as path, open in Xcode and get contents
my $getFileContentsScript = <<'GETFILESCRIPT';
on run argv
    set fileAlias to POSIX file (item 1 of argv)
    tell application "Xcode"
        set doc to open fileAlias
        set docText to text of doc
    end tell
    return docText
end run
GETFILESCRIPT

# Invoke the Applescript and get the results
open(SCRIPTFILE, '-|') || exec 'osascript', '-e', $getFileContentsScript, $implementationFilePath;
my $implementationFileContents = do {local $/; <SCRIPTFILE>};
close(SCRIPTFILE);
```

Yes, I know this is a _Cocoa_ blog and that's Perl and Applescript. I'm sorry. I felt dirty writing it.

## Parsing the variable declaration

The other important step for a user script to turn a variable declaration into a property is the step of parsing the declaration itself.

This will serve two purposes:

- Verify that the user has actually selected a variable declaration
- Detect a pointer (we will assume pointer variables are objects) and use the access specifiers `(nonatomic, retain)` instead of default access.

The regular expression I use to match is:

```objc
/([_A-Za-z][_A-Za-z0-9]*\s*)+([\s\*]+)([_A-Za-z][_A-Za-z0-9]*);/
```

This will match three different sections:

1. A series of C identifiers, separated by spaces (the variable type and qualifiers)
2. Asterisks and spaces in the middle
3. Another C identifier (the variable name)

The regular expression requires a semi-colon at the end of the selection but the semi-colon character is not extracted into any of the three match values.

These three matched values are used to build the property declaration and the synthesize statement. The property declaration will be `(nonatomic, retain)` if the second matched value contains exactly one asterisk.

### Limitations

This isn't a particularly thorough attempt to match a variable declaration. Lots of valid variable declarations will fail to be matched by this pattern. These include:

- Variables with "`const`" written to the right of the pointer asterisk (i.e. `SomePointerType * const myPointer;`)
- Most C-style function pointers
- Any variable declaration with a character that isn't an underscore, alphanumeric or asterisk
- Any declaration where the last non-whitespace character is not a semi-colon
- Any declaration containing a comment

For any of these cases, the match will fail and the script won't do anything.

Beyond this, many type qualifiers used for variables should not be included in the property declaration. This approach will always include them with the type name, so they may need to be manually removed afterwards.

## Putting it all together

The script performs the following tasks in order:

1. Get the full text of the current file (which is assumed to be the header file)
2. Grab the current selection from the full text and parse it using the regular expression (shown above)
3. Build a property declaration as appropriate for the matched variable declaration and insert it after the first closing brace found at the start of a line following the selection (this is assumed to be the end of the variables section of the class declaration)
4. Apply this modification to the header file
5. Get the contents of the implementation file, using the Perl/Applescript shown above
6. Insert a synthesize statement after the first `@implementation` statement found in the file (it is assumed that the first statement is the appropriate one
7. Commit the changes to the implementation file using Applescript again

To see how this is done, download the [PropertyFromInstanceVariable.zip](https://www.cocoawithlove.com/assets/objc-era/PropertyFromInstanceVariable.zip) and have a look. It should be adequately readable — I've commented most of it and Perl is relatively C-like.

## Installation

To install, open the "Edit User Scripts" item in the "Scripts Menu" of Xcode, create a new shell script, delete any content in the new script and paste in the contents of [PropertyFromInstanceVariable.pl](https://www.cocoawithlove.com/assets/objc-era/PropertyFromInstanceVariable.pl).

You will also need to set the "Input" popup menu to "Entire Document". You should also set the "Directory" popup menu to "Home Directory", the "Output" popup menu to "Discard Output" and the "Errors" popup menu to "Display in Alert".

You can set a keyboard shortcut for your script by double clicking in the "Command" column next to your script's name, otherwise you can select its entry from the "Script Menu" at the top of the screen.

## Conclusion

Writing an Xcode user script like this can involve a couple hours of setup and may still make many assumptions in order to work.

Despite this effort, taking a couple hours to turn your most repetitive tasks into completely automated actions can save you time in the long run — and can make you feel in control of your programming environment.
