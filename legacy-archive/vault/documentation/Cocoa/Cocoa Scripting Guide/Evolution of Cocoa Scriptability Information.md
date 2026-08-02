---
title: Cocoa Scripting Guide
apple_id: TP40002164
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_evolution/SAppsEvolution.html
archived_at: '2026-07-15T07:18:50.795760Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Scripting Guide](Introduction%20to%20Cocoa%20Scripting%20Guide.md)


[Next](Script%20Suite%20and%20Script%20Terminology%20Files.md)[Previous](How%20Cocoa%20Applications%20Handle%20Apple%20Events.md)

# Evolution of Cocoa Scriptability Information

OS X and Cocoa provide various tools and formats for working with scriptability information. This appendix describes the history of those tools and shows how to convert between various scriptability formats and versions.

AppleScript is a mature technology that was first introduced in the early 1990’s. When scripting support was added to the Cocoa application framework, a significant part of its ease of use depended on its adoption of key-value coding (KVC), a mechanism for accessing an object’s properties indirectly.

When terms from KVC (some of which come from entity-relationship modeling) were used with Cocoa scripting, some terms overlapped or conflicted with terms already in use by AppleScript. For example, the term _property_ has more than one distinct meaning. For definitions of these terms, see the [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmrqfvjvomjs).

Additionally, there are some differences in how you use the original format for Cocoa scriptability information (provided in script suite and script terminology files) and the current format (based on the sdef file format). These differences are described throughout this chapter.

You provide scriptability information for your application in one of the two formats described in [Scriptability Information Formats](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzwfuytcnjvgqyts):

- The scripting definition (or sdef) format first became available in OS X version 10.2. Cocoa scripting can interpret sdef files natively starting in OS X version 10.4.

  For OS X version 10.3, an sdef file can be converted to a corresponding script suite and script terminology file pair.
- The script suite format, consisting of a script suite file and a corresponding script terminology file, has been in use since scriptability support first became available in Cocoa and works in any version. This is the only format Cocoa scripting can interpret natively prior to OS X version 10.4.

The traditional Carbon mechanism for supplying scriptability information is the `'aete'` resource file. Cocoa scripting doesn't use `'aete'` resources, but you can add one to your application to control how your scriptability information is displayed by Script Editor or other dictionary viewers. Starting in Mac OS version 10.4, however, the preferred mechanism for controlling how your scriptability information is displayed is to use an sdef file.

There are a number of advantages to using the native sdef format in OS X version 10.4, including:

- You can assemble information describing the terminology and implementation details for your application all in one file, so there is no need to synchronize separate files.
- You have more options for specifying scriptability information. For example, you can control the order in which information is displayed (without having to add an `'aete'` resource to your application). You can also use the `hidden` attribute to hide deprecated terms while still keeping them available for backward compatibility. Or you can hide terms that are not yet ready for release.
- With an sdef, only the parts of Cocoa’s default scriptability information that you specifically include are used by Cocoa scripting and are visible when your dictionary is displayed.

  By comparison, applications that use only script suite and script terminology files will include the terminology from all such files defined in any framework the application links to or bundles that it loads (including the files for the full Standard and Text suites defined in the Cocoa framework).
- Script Editor can display your application’s dictionary without launching the application. However, through OS X version 10.4, it does still need to open your application to compile a script that targets the application.

The main advantage of the script suite format is that it can be used in any scriptable version of Cocoa. If your scriptable application will run in versions of the Mac OS prior to version 10.4, it must include script suite and script terminology files. However, it can also contain an sdef file, so that it can gain the advantages that sdef files provide when running in OS X version 10.4.

Script suite and script terminology files do not allow detailed control of how your scriptability information is displayed in a dictionary viewer. But if you need finer control of the look of your dictionary, you can add an `'aete'` resource to your application bundle. You can generate the `'aete'` by creating an sdef file for your application, then using the `sdp` tool to create an `'aete'` resource. Or you can create an `'aete'` resource directly (some third party tools can aid in doing so).

Suite information is described in detail in [Script Suite and Script Terminology Files](Script%20Suite%20and%20Script%20Terminology%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dclkcijbueq2jjjcq).

There are several options available for converting between scriptability formats and updating scriptability information. Remember that after making any changes to your scriptability information, you should run your full suite of test scripts to make sure your scriptability support is working as expected.

You can use the `sdp` tool to convert an sdef file into a pair of script suite and script terminology files that Cocoa can work with in current or earlier versions of the operating system. However, the script suite files may require some modification, particularly if you use `sdp` in OS X version 10.4 to create script suite files you will use with earlier OS versions.

You can also use `sdp` to create an `'aete'` file from an sdef file. A Cocoa application that provides its scriptability information in the script suite format may want to also include an `'aete'` resource to provide more control over how its scriptability information is displayed. That comes in handy in the following situation:

1. A user tries to display your application's scripting dictionary with Script Editor (or another dictionary viewer). Script Editor sends your application an Apple event asking for its scriptability information.
2. If your application has an `'aete'` resource, Cocoa returns that. Only the information you choose to put in the `'aete'` resource is displayed.
3. If your application does not have an `'aete'` resource, Cocoa scripting creates one from the information in any script suites available to the application. The information that gets displayed may include terminology that you do not wish to expose.

However, you do not need an `'aete'` for this purpose in OS X version 10.4 if your application uses an sdef file, because the sdef format gives you full control over what gets displayed.

You can execute a statement like the following in the Terminal application to create both script suite files and an `'aete'` resource from an sdef file:

```
sdp -fast -o ~myHome MyApplication.sdef
```

By specifying `"ast"` with the `-f` parameter, this command tells `sdp` to create `'aete'`, script suite, and script terminology files. It actually creates a pair of script suite files for each `suite` element defined in the sdef, placing them in the directory specified by the `-o` argument.

You can invoke `sdp` in a shell script build phase in Xcode if you want to make it part of your build process. If you do so, your command invocation should include the build style as part of the target directory. Here is an example of such a command:

```
/usr/bin/sdp -fast -o "$BUILD_DIR/$BUILD_STYLE/$FULL_PRODUCT_NAME/Contents/Resources" "$SOURCE_ROOT/MyApplication.sdef"
```

For more information, see the `sdp` man page and the Xcode documentation.

In OS X version 10.4, if you have existing script suite and script terminology files or a resource file containing an `'aete'` resource, you can use the `desdp` tool to convert them to the sdef format. The resulting sdef will contain all the information in the original dictionary, but is likely to require some changes, because the sdef format is more expressive than the older formats. For example, in the older format you cannot specify the ordering of terms. For more information on the `desdp` tool, see its man page.

The scripting definition format experienced a number of changes for OS X version 10.4. (For a complete listing, see the History section of the `sdef` man page.) If you have an existing sdef file created for an earlier version of the Mac OS, you can use the `xsltproc` tool to upgrade it for OS X version 10.4. You use this command line tool to apply XSLT stylesheets (such as the OS X file `/usr/share/sdef/upgrade.xsl` referred to in the example that follows) to XML documents (in this case, the sdef file to be upgraded).

You can use a line like the following in the Terminal application to upgrade an sdef file named `MyApplication.sdef`:

```
xsltproc --novalid -o MyNewApplication.sdef /usr/share/sdef/upgrade.xsl MyApplication.sdef
```

In this invocation:

- The `--novalid` argument causes the tool to skip loading the document's DTD file.
- The `-o` argument specifies the name of the new file to create.
- The `/usr/share/sdef/upgrade.xsl` argument specifies the file from which to obtain the upgrade information.
- The final argument, `MyApplication.sdef`, specifies the existing sdef file to upgrade.

For more information, see the `xsltproc` man page.

In OS X version 10.4, both Xcode and Script Editor understand the sdef format. Double-clicking an sdef file in the Finder will launch Script Editor and display the scripting terminology in a dictionary viewer, while double-clicking an sdef file in an Xcode project will open it in a dictionary viewer in Xcode. [Figure 1-4](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzwfvjvomjq) shows an sdef displayed in a dictionary viewer.

To edit an sdef file in Xcode, select the sdef file and choose File > Open As > Plain Text File. You can also view and edit the XML for an sdef file by opening it with any plain text editor or XML editor.

You can use File > Open Dictionary in Script Editor or Xcode to choose any scriptable application and display its dictionary.

In OS X version 10.3 and earlier, Cocoa scripting cannot directly parse sdef files, and neither Xcode nor Script Editor can display native sdef files in a dictionary viewer.

For all scriptable versions of Cocoa, you can supply scriptability information in script suite files and script terminology files. Dragging a scriptable Cocoa application that contains these files onto Script Editor will display its dictionary. However, neither Script Editor nor Xcode can interpret script suite and script terminology files natively to display a dictionary.

Double-clicking a script suite or script terminology file will typically open it in Property List Editor (if you have not changed the Finder default). After opening a file in Property List Editor, you can save it in XML format, or in a plain ASCII format that may be somewhat easier to read and work with. You can edit suite files in any of these formats, though editing property lists with Property List Editor has some limitations.

For information on creating a new sdef file, see [Create a Scripting Definition File](Preparing%20a%20Scripting%20Definition%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzzfvjvomq). For information on creating a new script suite, see [Creating Your Own Script Suite Files](Script%20Suite%20and%20Script%20Terminology%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dclktk4za). If you already have existing scriptability information, see [Converting and Updating Scriptability Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjzfvjvomq).

[Next](Script%20Suite%20and%20Script%20Terminology%20Files.md)[Previous](How%20Cocoa%20Applications%20Handle%20Apple%20Events.md)

