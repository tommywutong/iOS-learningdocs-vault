---
title: UTType
framework: Uniform Type Identifiers
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct.json'
content_hash: 'sha256:b42ae1c99ba98348'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTType

<sub>Structure</sub>

A structure that represents a type of data to load, send, or receive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UTType
```

## Overview

The [UTType](uttype-swift.struct.md) instance may represent files on disk, abstract data types with no on-disk representation, or entirely unrelated hierarchical classification systems, such as hardware. Each instance has a unique [identifier](uttype-swift.struct/identifier.md), and helpful properties, such as [preferredFilenameExtension](uttype-swift.struct/preferredfilenameextension.md) and [preferredMIMEType](uttype-swift.struct/preferredmimetype.md).

> [!note] Note
> The system includes static declarations for many common types, which you can look up by identifier, filename extension, or MIME type.

A [UTType](uttype-swift.struct.md) instance may provide additional information related to the type. For example, it may include a localized user-facing description, a reference URL to technical documentation about the type, or its version number. You can look up types by their conformance to get either a type or a list of types that are relevant to your use case.

To define your own types in your app’s `Info.plist`, see [Defining file and data types for your app](defining-file-and-data-types-for-your-app.md).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ReferenceConvertible](../foundation/referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Looking up a type

- [types(tag:tagClass:conformingTo:)](<uttype-swift.struct/types(tag_tagclass_conformingto_).md>) — Returns an array of types from the provided tag and tag class.

### Creating a type

- [init(_:)](<uttype-swift.struct/init(__).md>) — Creates a type based on an identifier.
- [init(mimeType:conformingTo:)](<uttype-swift.struct/init(mimetype_conformingto_).md>) — Creates a type based on a MIME type and a supertype that it conforms to.
- [init(filenameExtension:conformingTo:)](<uttype-swift.struct/init(filenameextension_conformingto_).md>) — Creates a type based on a filename extension and an existing supertype that it conforms to.
- [init(tag:tagClass:conformingTo:)](<uttype-swift.struct/init(tag_tagclass_conformingto_).md>) — Creates a type based on a tag, a tag class, and a supertype that it conforms to.
- [init(exportedAs:conformingTo:)](<uttype-swift.struct/init(exportedas_conformingto_).md>) — Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs:conformingTo:)](<uttype-swift.struct/init(importedas_conformingto_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.

### Identifying a type

- [ReferenceType](uttype-swift.struct/referencetype.md) — An alias for the associated reference type.
- [identifier](uttype-swift.struct/identifier.md) — The string that represents the type.

### Obtaining tags

- [preferredFilenameExtension](uttype-swift.struct/preferredfilenameextension.md) — The preferred filename extension for the type.
- [preferredMIMEType](uttype-swift.struct/preferredmimetype.md) — The preferred MIME type for the type.
- [tags](uttype-swift.struct/tags.md) — The tag specification dictionary of the type.

### Obtaining additional type information

- [isDeclared](uttype-swift.struct/isdeclared.md) — A Boolean value that indicates whether the system declares the type.
- [isDynamic](uttype-swift.struct/isdynamic.md) — A Boolean value that indicates whether the system generates the type.
- [isPublic](uttype-swift.struct/ispublic.md) — A Boolean value that indicates whether the type is in the public domain.
- [referenceURL](uttype-swift.struct/referenceurl.md) — The reference URL for the type.
- [version](uttype-swift.struct/version.md) — The type’s version, if available.

### Checking a type’s relationship to another type

- [supertypes](uttype-swift.struct/supertypes.md) — The set of types the type directly or indirectly conforms to.
- [conforms(to:)](<uttype-swift.struct/conforms(to_).md>) — Returns a Boolean value that indicates whether a type conforms to the type.
- [isSubtype(of:)](<uttype-swift.struct/issubtype(of_).md>) — Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [isSupertype(of:)](<uttype-swift.struct/issupertype(of_).md>) — Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.
- [Navigating Hierarchical Data Using Outline and Split Views](../appkit/navigating-hierarchical-data-using-outline-and-split-views.md) — Build a structured user interface that simplifies navigation in your app.

### Describing a type

- [localizedDescription](uttype-swift.struct/localizeddescription.md) — A localized description of the type.

### 3D content

- [threeDContent](uttype-swift.struct/threedcontent.md) — A base type that represents 3D content.
- [usd](uttype-swift.struct/usd.md) — A type that represents Universal Scene Description content.
- [usdz](uttype-swift.struct/usdz.md) — A type that represents Universal Scene Description Package content.

### Apple 3D content

- [realityFile](uttype-swift.struct/realityfile.md) — A type that represents a Reality Composer file.
- [sceneKitScene](uttype-swift.struct/scenekitscene.md) — A type that represents a SceneKit serialized scene.
- [arReferenceObject](uttype-swift.struct/arreferenceobject.md) — A type that represents an augmented reality reference object.

### Apple file system objects

- [directory](uttype-swift.struct/directory.md) — A type that represents a file system directory, including packages and folders.
- [symbolicLink](uttype-swift.struct/symboliclink.md) — A type that represents a symbolic link.
- [mountPoint](uttype-swift.struct/mountpoint.md) — A type that represents a volume mount point.
- [aliasFile](uttype-swift.struct/aliasfile.md) — A type that represents an alias file.
- [folder](uttype-swift.struct/folder.md) — A type that represents a user-browsable directory.
- [volume](uttype-swift.struct/volume.md) — A type that represents the root folder of a volume or mount point.
- [diskImage](uttype-swift.struct/diskimage.md) — A type that represents a data item that’s mountable as a volume.

### Apple image formats

- [heic](uttype-swift.struct/heic.md) — A type that represents High Efficiency Image Coding images.
- [heif](uttype-swift.struct/heif.md) — A type that represents High Efficiency Image File Format images.
- [livePhoto](uttype-swift.struct/livephoto.md) — A type that represents Live Photos.

### Apple system types

- [framework](uttype-swift.struct/framework.md) — A type that represents an Apple framework bundle.
- [applicationBundle](uttype-swift.struct/applicationbundle.md) — A type that represents a bundled app.
- [applicationExtension](uttype-swift.struct/applicationextension.md) — A type that represents an app extension.
- [spotlightImporter](uttype-swift.struct/spotlightimporter.md) — A type that represents a Spotlight metadata importer bundle.
- [quickLookGenerator](uttype-swift.struct/quicklookgenerator.md) — A type that represents a QuickLook preview generator bundle.
- [xpcService](uttype-swift.struct/xpcservice.md) — A type that represents an XPC service bundle.
- [systemPreferencesPane](uttype-swift.struct/systempreferencespane.md) — A type that represents a System Preferences pane.

### Application files

- [pdf](uttype-swift.struct/pdf.md) — A type that represents Adobe Portable Document Format (PDF) documents.
- [rtfd](uttype-swift.struct/rtfd.md) — A type that represents Rich Text Format Directory documents.
- [flatRTFD](uttype-swift.struct/flatrtfd.md) — A type that represents flattened Rich Text Format Directory documents.
- [epub](uttype-swift.struct/epub.md) — A type that represents data in the electronic publication (EPUB) format.

### Audio

- [mp3](uttype-swift.struct/mp3.md) — A type that represents MP3 audio.
- [aiff](uttype-swift.struct/aiff.md) — A type that represents data in AIFF audio format.
- [wav](uttype-swift.struct/wav.md) — A type that represents data in Microsoft Waveform Audio File Format.
- [midi](uttype-swift.struct/midi.md) — A type that represents data in MIDI audio format.
- [playlist](uttype-swift.struct/playlist.md) — A base type that represents a playlist.
- [m3uPlaylist](uttype-swift.struct/m3uplaylist.md) — A type that represents an M3U or M3U8 playlist.

### Audio and video

- [quickTimeMovie](uttype-swift.struct/quicktimemovie.md) — A type that represents a QuickTime movie.
- [mpeg](uttype-swift.struct/mpeg.md) — A type that represents an MPEG-1 or MPEG-2 movie.
- [mpeg2Video](uttype-swift.struct/mpeg2video.md) — A type that represents an MPEG-2 video.
- [mpeg2TransportStream](uttype-swift.struct/mpeg2transportstream.md) — A type that represents data in MPEG-2 transport stream movie format.
- [mpeg4Movie](uttype-swift.struct/mpeg4movie.md) — A type that represents an MPEG-4 movie.
- [mpeg4Audio](uttype-swift.struct/mpeg4audio.md) — A type that represents an MPEG-4 audio layer file.
- [appleProtectedMPEG4Video](uttype-swift.struct/appleprotectedmpeg4video.md) — A type that represents data in Apple-protected MPEG-4 format.
- [appleProtectedMPEG4Audio](uttype-swift.struct/appleprotectedmpeg4audio.md) — A type that represents data in Apple-protected MPEG-4 format.
- [avi](uttype-swift.struct/avi.md) — A type that represents data in AVI movie format.

### Compiled programming language sources

- [assemblyLanguageSource](uttype-swift.struct/assemblylanguagesource.md) — A type that represents assembly language source code.
- [cHeader](uttype-swift.struct/cheader.md) — A type that represents a C header file.
- [cSource](uttype-swift.struct/csource.md) — A type that represents a C source code file.
- [cPlusPlusHeader](uttype-swift.struct/cplusplusheader.md) — A type that represents a C++ header file.
- [cPlusPlusSource](uttype-swift.struct/cplusplussource.md) — A type that represents a C++ source code file.
- [objectiveCPlusPlusSource](uttype-swift.struct/objectivecplusplussource.md) — A type that represents an Objective-C++ source code file.
- [objectiveCSource](uttype-swift.struct/objectivecsource.md) — A type that represents an Objective-C source code file.
- [swiftSource](uttype-swift.struct/swiftsource.md) — A type that represents a Swift source code file.

### Compressed archives

- [archive](uttype-swift.struct/archive.md) — A base type that represents an archive of files and directories.
- [zip](uttype-swift.struct/zip.md) — A type that represents a zip archive.
- [gzip](uttype-swift.struct/gzip.md) — A type that represents a GNU zip archive.
- [bz2](uttype-swift.struct/bz2.md) — A type that represents a bzip2 archive.
- [appleArchive](uttype-swift.struct/applearchive.md) — A type that represents an Apple archive of files and directories.

### Cryptographic files

- [pkcs12](uttype-swift.struct/pkcs12.md) — A type that represents Public Key Cryptography Standard (PKCS) 12 data.
- [x509Certificate](uttype-swift.struct/x509certificate.md) — A type that represents an X.509 certificate.

### Data interchange formats

- [delimitedText](uttype-swift.struct/delimitedtext.md) — A base type that represents text containing delimited values.
- [commaSeparatedText](uttype-swift.struct/commaseparatedtext.md) — A type that represents text containing comma-separated values.
- [tabSeparatedText](uttype-swift.struct/tabseparatedtext.md) — A type that represents text containing tab-separated values.
- [utf8TabSeparatedText](uttype-swift.struct/utf8tabseparatedtext.md) — A type that represents UTF-8–encoded text containing tab-separated values.
- [rtf](uttype-swift.struct/rtf.md) — A type that represents Rich Text Format data.
- [xml](uttype-swift.struct/xml.md) — A type that represents generic XML data.
- [yaml](uttype-swift.struct/yaml.md) — A type that represents Yet Another Markup Language data.
- [json](uttype-swift.struct/json.md) — A type that represents JavaScript Object Notation (JSON) data.
- [vCard](uttype-swift.struct/vcard.md) — A type that represents a vCard file.

### Executables

- [executable](uttype-swift.struct/executable.md) — A type that represents an executable.
- [unixExecutable](uttype-swift.struct/unixexecutable.md) — A type that represents a UNIX executable.
- [exe](uttype-swift.struct/exe.md) — A type that represents a Windows executable.

### Icon images

- [ico](uttype-swift.struct/ico.md) — A type that represents Windows icon data.
- [icns](uttype-swift.struct/icns.md) — A type that represents Apple icon data.

### Images

- [png](uttype-swift.struct/png.md) — A type that represents a PNG image.
- [gif](uttype-swift.struct/gif.md) — A type that represents a GIF image.
- [jpeg](uttype-swift.struct/jpeg.md) — A type that represents a JPEG image.
- [webP](uttype-swift.struct/webp.md) — A type that represents a WebP image.
- [tiff](uttype-swift.struct/tiff.md) — A type that represents a TIFF image.
- [bmp](uttype-swift.struct/bmp.md) — A type that represents a Windows bitmap image.
- [svg](uttype-swift.struct/svg.md) — A type that represents a scalable vector graphics (SVG) image.
- [rawImage](uttype-swift.struct/rawimage.md) — A base type that represents a raw image format that you use in digital photography.

### Internet-specific

- [html](uttype-swift.struct/html.md) — A type that represents any version of HTML.
- [webArchive](uttype-swift.struct/webarchive.md) — A type that represents WebKit web archive data.
- [internetLocation](uttype-swift.struct/internetlocation.md) — A base type that represents an Apple internet location file.
- [internetShortcut](uttype-swift.struct/internetshortcut.md) — A type that represents a Microsoft internet shortcut file.

### Property lists

- [propertyList](uttype-swift.struct/propertylist.md) — A base type that represents a property list.
- [xmlPropertyList](uttype-swift.struct/xmlpropertylist.md) — A type that represents an XML property list.
- [binaryPropertyList](uttype-swift.struct/binarypropertylist.md) — A type that represents a binary property list.

### Shazam

- [shazamSignature](uttype-swift.struct/shazamsignature.md) — A type that represents a signature.
- [shazamCustomCatalog](uttype-swift.struct/shazamcustomcatalog.md) — A type that represents a custom catalog.

### Scripted programming language sources

- [script](uttype-swift.struct/script.md) — A base type that represents any scripting language source.
- [appleScript](uttype-swift.struct/applescript.md) — A type that represents an AppleScript text-based script.
- [javaScript](uttype-swift.struct/javascript.md) — A type that represents JavaScript source code.
- [osaScript](uttype-swift.struct/osascript.md) — A type that represents an Open Scripting Architecture binary script.
- [osaScriptBundle](uttype-swift.struct/osascriptbundle.md) — A type that represents an Open Scripting Architecture script bundle.
- [makefile](uttype-swift.struct/makefile.md) — A type that represents a Makefile.
- [shellScript](uttype-swift.struct/shellscript.md) — A base type that represents a shell script.
- [pythonScript](uttype-swift.struct/pythonscript.md) — A type that represents a Python script.
- [rubyScript](uttype-swift.struct/rubyscript.md) — A type that represents a Ruby script.
- [perlScript](uttype-swift.struct/perlscript.md) — A type that represents a Perl script.
- [phpScript](uttype-swift.struct/phpscript.md) — A type that represents a PHP script.

### Text files

- [text](uttype-swift.struct/text.md) — A base type that represents all text-encoded data, including text with markup.
- [plainText](uttype-swift.struct/plaintext.md) — A type that represents text with no markup and an unspecified encoding.
- [utf8PlainText](uttype-swift.struct/utf8plaintext.md) — A type that represents plain text encoded as UTF-8.
- [utf16PlainText](uttype-swift.struct/utf16plaintext.md) — A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [utf16ExternalPlainText](uttype-swift.struct/utf16externalplaintext.md) — A type that represents plain text encoded as UTF-16 with an optional bill of materials.
- [markdown](uttype-swift.struct/markdown.md) — A type that represents Markdown data. _(beta)_

### URLs

- [url](uttype-swift.struct/url.md) — A type that represents a URL.
- [fileURL](uttype-swift.struct/fileurl.md) — A type that represents a URL to a file in the file system.
- [urlBookmarkData](uttype-swift.struct/urlbookmarkdata.md) — A type that represents a URL bookmark.

### Apple system base types

- [item](uttype-swift.struct/item.md) — A generic base type for most objects, such as files or directories.
- [content](uttype-swift.struct/content.md) — A base type that represents anything containing user-viewable content.
- [compositeContent](uttype-swift.struct/compositecontent.md) — A base type that represents a content format supporting mixed embedded content.
- [data](uttype-swift.struct/data.md) — A base type that represents any sort of byte stream, including files and in-memory data.
- [resolvable](uttype-swift.struct/resolvable.md) — A base type that represents a resolvable reference, including symbolic links and aliases.
- [package](uttype-swift.struct/package.md) — A base type that represents a packaged directory.
- [bundle](uttype-swift.struct/bundle.md) — A base type that represents a directory that conforms to one of the bundle layouts.
- [pluginBundle](uttype-swift.struct/pluginbundle.md) — A base type that represents a bundle-based plug-in.
- [application](uttype-swift.struct/application.md) — A base type that represents a macOS, iOS, iPadOS, watchOS, and tvOS app.
- [sourceCode](uttype-swift.struct/sourcecode.md) — A base type that represents source code of any programming language.
- [bookmark](uttype-swift.struct/bookmark.md) — A base type that represents bookmark data.
- [log](uttype-swift.struct/log.md) — A base type that represents console log data.

### Application base types

- [spreadsheet](uttype-swift.struct/spreadsheet.md) — A base type that represents a spreadsheet document.
- [presentation](uttype-swift.struct/presentation.md) — A base type that represents a presentation document.
- [database](uttype-swift.struct/database.md) — A base type that represents a database store.
- [message](uttype-swift.struct/message.md) — A base type that represents a message.
- [contact](uttype-swift.struct/contact.md) — A base type that represents contact information.
- [calendarEvent](uttype-swift.struct/calendarevent.md) — A base type that represents a calendar event.
- [toDoItem](uttype-swift.struct/todoitem.md) — A type that represents a to-do item.
- [emailMessage](uttype-swift.struct/emailmessage.md) — A type that represents an email message.
- [font](uttype-swift.struct/font.md) — A base type that represents a font.

### Image, audio, and video base types

- [image](uttype-swift.struct/image.md) — A base type that represents image data.
- [audio](uttype-swift.struct/audio.md) — A type that represents audio that doesn’t contain video.
- [audiovisualContent](uttype-swift.struct/audiovisualcontent.md) — A base type that represents data that contains video content that may or may not also include audio.
- [movie](uttype-swift.struct/movie.md) — A base type representing media formats that may contain both video and audio.
- [video](uttype-swift.struct/video.md) — A type that represents video that doesn’t contain audio.

### Initializers

- [init(identifier:allowUndeclared:)](<uttype-swift.struct/init(identifier_allowundeclared_).md>) — Create a type given a type identifier, optionally allowing identifiers that do not have an active declaration on the current system. _(beta)_

### Type Properties

- [ahap](uttype-swift.struct/ahap.md)
- [css](uttype-swift.struct/css.md) — Cascading Style Sheets (CSS)
- [dng](uttype-swift.struct/dng.md) — An Adobe DNG (digital negative) image.
- [exr](uttype-swift.struct/exr.md) — An EXR image.
- [geoJSON](uttype-swift.struct/geojson.md) — A GeoJSON file.
- [heics](uttype-swift.struct/heics.md) — A High Efficiency Image Coding Image Sequence.
- [jpegxl](uttype-swift.struct/jpegxl.md) — A JPEG-XL encoded image.
- [linkPresentationMetadata](uttype-swift.struct/linkpresentationmetadata.md) — Serialized LinkPresentation metadata.
- [paperkit](uttype-swift.struct/paperkit.md) — The UTType for storing paper data.
- [tarArchive](uttype-swift.struct/tararchive.md) — A tar Archive.

### Default Implementations

- [ReferenceConvertible Implementations](uttype-swift.struct/referenceconvertible-implementations.md)

## See Also

### Uniform type identifiers

- [UTTagClass](uttagclass.md) — A type that represents tag classes.
- [UTTypeReference](uttypereference.md) — An object that represents a type of data to load, send, or receive.
