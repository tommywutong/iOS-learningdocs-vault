---
title: Runtime Configuration Guidelines
apple_id: 10000170i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPRuntimeConfig/Articles/ConfigFiles.html
archived_at: '2026-07-15T08:16:27.217372Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Runtime Configuration Guidelines](Introduction.md)


[Next](The%20Preferences%20System.md)[Previous](Introduction.md)

# Information Property List Files

An information [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) file is a structured text file that contains essential configuration information for a bundled executable. The file itself is typically encoded using the Unicode UTF-8 encoding and the contents are structured using XML. The root XML node is a dictionary, whose contents are a set of keys and values describing different aspects of the [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4). The system uses these keys and values to obtain information about your application and how it is configured. As a result, all bundled executables (plug-ins, frameworks, and applications) are expected to have an information property list file.

By convention, the name of an information property list file is `Info.plist`. This name of this file is case sensitive and must have an initial capital letter `I`. In iPhone applications, this file resides in the top-level of the bundle directory. In macOS bundles, this file resides in the bundle’s `Contents` directory. Xcode typically creates this file for you automatically when you create a project of an appropriate type.

The contents of a typical `Info.plist` file convey the following information to the system:

- The user-visible name to display for the bundle
- A unique identifier string (typically in the form `com.yourcompany.appname`) that can be used to locate the bundle at runtime
- The type of the bundle (application, framework, plug-in)
- Version information
- Information about how to launch the bundle or load its contents into memory
- The preferred execution environment for the bundle
- Information about the bundle’s supported document types (if any)
- For iPhone applications, information about how the application presents content initially

For information about how to create information property lists, along with keys and values that you can include in them, see _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

[Next](The%20Preferences%20System.md)[Previous](Introduction.md)

