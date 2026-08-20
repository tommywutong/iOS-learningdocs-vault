---
title: Ruby and Python Programming Topics for Mac
apple_id: TP40004936
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: ScriptingBridge
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/RubyPythonCocoa/Articles/GenerateFrameworkMetadata.html
archived_at: '2026-07-15T07:18:40.276354Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ruby and Python Programming Topics for Mac](Introduction%20to%20Ruby%20and%20Python%20Programming%20Topics%20for%20OS%20X.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Scripting%20Bridge%20in%20PyObjC%20and%20RubyCocoa%20Code.md)

# Generating Framework Metadata

The programmatic interfaces of virtually all frameworks on OS X, even Objective-C frameworks, have ANSI C elements such as functions, string constants, and `enum` constants. The scripting Objective-C bridges, RubyCocoa and PyObjC, can introspect most object-oriented symbols of Objective-C frameworks at runtime, but they cannot introspect ANSI C symbols. Fortunately, there is a utility, `gen_bridge_metadata`, that parses the non-introspectable symbols of framework and libraries and constructs a representation of them that the PyObjC and RubyCocoa bridges can read and internalize at runtime. These generated symbols are defined as XML elements in framework metadata files (also known as BridgeSupport files).

An obvious advantage of framework metadata is that gives the scripting bridges access to the programmatic interfaces of non-Objective-C frameworks, such as Core Foundation, Core Graphics, and Directory Services. Many of the ANSI C frameworks shipped by Apple in OS X v10.5 and later systems include metadata files, and thus their interfaces are accessible from RubyCocoa and PyObjC scripts.

The following sections describe the framework metadata generated to supported the RubyCocoa and PyObjC bridges and explains how to generate metadata files and create the exception files that support that metadata.

Framework metadata is XML markup stored in a file named after the framework and with an extension of `bridgesupport`. Thus, the metadata file for the Application Kit framework (`AppKit.framework`) is named `AppKit.bridgesupport`. Each metadata file describes exactly one framework or dynamically shared library. The RubyCocoa and PyObjC bridges look for metadata files in several places:

- Inside the `Resources` folder of the framework bundle (non-localized) inside a folder named `BridgeSupport`. This is the preferred approach if you own the framework.
- In `/System/Library/BridgeSupport` (this location is reserved for Apple)
- In `/Library/BridgeSupport`
- In `~/Library/BridgeSupport` (that is, in the user’s home directory)

The bridges search the locations in the above order and load the first metadata file they find for a given framework. Note that the bridges might also look in the RubyCocoa and PyObjC frameworks for metadata files.

A metadata file consists of several sections of different elements each defining an ANSI C symbol and, in some cases, an Objective-C symbol. The sections include metadata descriptions of string constants, enum constants, functions, structures, opaque objects, classes (with their methods), and informal protocols.

At the top of the metadata XML hierarchy is the root element, `signatures`. It has a version attribute.

```
<signatures version='1.0'>
```

Following this is a section dealing with string constants. Listing 1 shows a section of metadata markup that describes string constants by name and encoding type.

__Listing 1__  Part of the constants section, `AppKit.bridgesupport`

```
 <constant name='NSAlternateTitleBinding' type='@'/>
  <constant name='NSAlwaysPresentsApplicationModalAlertsBindingOption' type='@'/>
  <constant name='NSAnimateBinding' type='@'/>
  <constant name='NSAnimationDelayBinding' type='@'/>
  <constant name='NSAnimationProgressMark' type='@'/>
  <constant name='NSAnimationProgressMarkNotification' type='@'/>
  <constant name='NSAnimationTriggerOrderIn' type='@'/>
  <constant name='NSAnimationTriggerOrderOut' type='@'/>
  <constant name='NSAntialiasThresholdChangedNotification' type='@'/>
  <constant name='NSApp' type='@'/>
  <constant name='NSAppKitIgnoredException' type='@'/>
  <constant name='NSAppKitVersionNumber' type='d'/>
  <constant name='NSAppKitVirtualMemoryException' type='@'/>
```

Listing 2shows a section of metadata markup that describes `enum` constants by name and integer value.

__Listing 2__  Part of the enum section, `AppKit.bridgesupport`

```
  <enum name='NSServiceMalformedServiceDictionaryError' value='66564'/>
  <enum name='NSServiceMiscellaneousError' value='66800'/>
  <enum name='NSServiceRequestTimedOutError' value='66562'/>
  <enum name='NSShadowlessSquareBezelStyle' value='6'/>
  <enum name='NSShiftKeyMask' value='131072'/>
  <enum name='NSShowControlGlyphs' value='1'/>
  <enum name='NSShowInvisibleGlyphs' value='2'/>
  <enum name='NSSingleDateMode' value='0'/>
  <enum name='NSSingleUnderlineStyle' value='1'/>
  <enum name='NSSizeDownFontAction' value='4'/>
  <enum name='NSSizeUpFontAction' value='3'/>
  <enum name='NSSmallCapsFontMask' value='128'/>
  <enum name='NSSmallControlSize' value='1'/>
```

The metadata for functions is more complicated, as it has to describe argument and return types. Listing 3 shows the metadata definition of several functions.

__Listing 3__  Part of the function section, `AppKit.bridgesupport`

```
 <function name='NSDrawBitmap'>
    <arg type='{_NSRect={_NSPoint=ff}{_NSSize=ff}}'/>
    <arg type='i'/>
    <arg type='i'/>
    <arg type='i'/>
    <arg type='i'/>
    <arg type='i'/>
    <arg type='i'/>
    <arg type='B'/>
    <arg type='B'/>
    <arg type='@'/>
    <arg type='^*'/>
  </function>
  <function name='NSDrawButton'>
    <arg type='{_NSRect={_NSPoint=ff}{_NSSize=ff}}'/>
    <arg type='{_NSRect={_NSPoint=ff}{_NSSize=ff}}'/>
  </function>
  <function name='NSDrawColorTiledRects'>
    <arg type='{_NSRect={_NSPoint=ff}{_NSSize=ff}}'/>
    <arg type='{_NSRect={_NSPoint=ff}{_NSSize=ff}}'/>
    <arg c_array_length_in_arg='4' type='^i' type_modifier='n'/>
    <arg c_array_length_in_arg='4' type='^@' type_modifier='n'/>
    <arg type='i'/>
    <retval type='{_NSRect={_NSPoint=ff}{_NSSize=ff}}'/>
```

The `gen_bridge_metadata` tool also processes some aspects of Objective-C that the bridges cannot introspect at runtime, such as type modifiers, C-array arguments, and values returned by reference. It also reconciles some aspects that are different in the scripting languages and Objective-C, such as Boolean values. These details mostly derive from exceptions files (see [Creating the Exceptions File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrwfvjvooa)). Listing 4 shows a section of metadata specifying methods of the [NSTypesetter](https://developer.apple.com/documentation/appkit/nstypesetter) class.

__Listing 4__  Part of the class and methods section, `AppKit.bridgesupport`

```
  <class name='NSTypesetter'>
    <method selector='usesFontLeading'>
      <retval type='B'/>
    </method>
    <method selector='bidiProcessingEnabled'>
      <retval type='B'/>
    </method>
    <method selector='shouldBreakLineByWordBeforeCharacterAtIndex:'>
      <retval type='B'/>
    </method>
    <method selector='shouldBreakLineByHyphenatingBeforeCharacterAtIndex:'>
      <retval type='B'/>
    </method>
    <method class_method='true' selector='printingAdjustmentInLayoutManager:forNominallySpacedGlyphRange:packedGlyphs:count:'>
      <arg c_array_length_in_arg='3' index='2' type_modifier='n'/>
    </method>
    <method ignore='true' selector='getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:'/>
    <method ignore='true' selector='substituteGlyphsInRange:withGlyphs:'/>
    <method ignore='true' selector='setLocation:withAdvancements:forStartOfGlyphRange:'/>
```

The last part of a framework metadata file describes any informal protocols in the framework, as illustrated by Listing 5. Again, this information is manually specified in an exceptions file.

__Listing 5__  Part of the informal protocol section, `AppKit.bridgesupport`

```
 <informal_protocol name='NSDraggingSource'>
    <method type='v20@0:4@8{_NSPoint=ff}12' selector='draggedImage:beganAt:'/>
    <method type='v24@0:4@8{_NSPoint=ff}12c20' selector='draggedImage:endedAt:deposited:'/>
    <method type='v24@0:4@8{_NSPoint=ff}12I20' selector='draggedImage:endedAt:operation:'/>
    <method type='v20@0:4@8{_NSPoint=ff}12' selector='draggedImage:movedTo:'/>
    <method type='I12@0:4c8' selector='draggingSourceOperationMaskForLocal:'/>
    <method type='c8@0:4' selector='ignoreModifierKeysWhileDragging'/>
    <method type='@12@0:4@8' selector='namesOfPromisedFilesDroppedAtDestination:'/>
  </informal_protocol>
  <informal_protocol name='NSDrawerDelegate'>
    <method type='c12@0:4@8' selector='drawerShouldClose:'/>
    <method type='c12@0:4@8' selector='drawerShouldOpen:'/>
    <method type='{_NSSize=ff}20@0:4@8{_NSSize=ff}12' selector='drawerWillResizeContents:toSize:'/>
  </informal_protocol>
```


The `gen_bridge_metadata` tool parses framework header files and runs the `gcc` compiler on a framework binary to extract the public symbols. With this data, it composes an XML metadata file for the specified framework. The simplest form of the command requires only the name of the framework (minus the `framework` extension) and the name of the output file:

```
$> gen_bridge_metadata -f MyFramework -o MyFramework.bridgesupport
```

For this shorthand reference to a framework to work, the framework must be installed in one of the standard file-system locations: `/System/Library/Frameworks`, `/Library/Frameworks`, `/Network/Library/Frameworks`, or `~/Library/Frameworks.` If the framework is located elsewhere, you can specify an absolute path to the framework instead.

Most frameworks require a manually prepared exceptions file to complete the framework metadata. You specify this file on the command line with the `-e` option:

```
$> gen_bridge_metadata -f MyFramework -e MyFrameworkExceptions.xml -o MyFramework.bridgesupport
```

For more about the exceptions file, see [Creating the Exceptions File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrwfvjvooa).

Framework metadata files cannot describe inline functions in a form that the bridges can use. If your framework has inline functions, you therefore also need to generate a dynamically shared library, which the bridges can use. The file extension for the created file should be `dylib`. The following is an example command:

```
$> gen_bridge_metadata -f MyFramework -F dylib -o MyFramework.dylib
```

The `-F` option is for specifying a format, one of “final”, “exceptions-format”, or “dylib”. The default format is “final”.

For more information on `gen_bridge_metadata` consult the `gen_bridge_metadata(1)` man page. You can also run the tool with an argument of `-h` (or `--help`) to get a list of options.

You might have to supplement the metadata for your framework with an exceptions file. An exceptions file records aspects of a framework’s programmatic interface that the bridges cannot introspect at runtime or that conflict with something in a scripting language. These items include type modifiers, C-array arguments, informal protocols, values returned by reference, and Boolean values.

First, you need to create an exception template, which will provide the structure of the XML file. Run the following at the command line to create the exceptions template:

```
gen_bridge_metadata -f MyFramework -F exceptions-template -o MyFrameworkExceptions.xml
```

Next open the template file in a text editor and insert your framework-specific information in the appropriate places.

When your exception file is complete, you can generate the final bridge support file for your framework, as described in [Using the gen_bridge_metadata Tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrwfvjvooi). Make sure that you supply the `-e` parameter and the path to the exceptions file. The `gen_bridge_metadata` tool will fail if your exception file contains any errors.

Beginning in OS X version 10.5, you can easily create your own bridge between Objective-C and any language. You can use the generated bridge support files and the libffi library to have your bridge call C functions and create C closures in a dynamic, architecture-agnostic way. Libffi provides a bridge from interpreted code to compiled code that can tell the interpreter at runtime the number and types of function arguments and return values.

You can learn more about libffi by reading the manual pages for `ffi`, `ffi_prep_cif`, `ffi_prep_closure`, and `ffi_call`.

[Next](Document%20Revision%20History.md)[Previous](Using%20Scripting%20Bridge%20in%20PyObjC%20and%20RubyCocoa%20Code.md)

